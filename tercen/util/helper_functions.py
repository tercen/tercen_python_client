import pandas as pd
import polars as pl
import numpy as np
import polars.datatypes.classes as plc

from io import BytesIO
import tempfile, string, random

import pytson as ptson

import uuid, os, hashlib, base64
from tercen.model.base import Table, Column, InMemoryRelation, Relation, SchemaBase, SimpleRelation
from tercen.model.base import CompositeRelation, JoinOperator, ColumnPair

# import tercen.util.pytmp as ptmp



def dataframe_to_table(df, values_as_list=False) -> Table:

    df_lib = "polars"
    if df.__class__ == pd.DataFrame:
        df_lib = "pandas"

    tbl = Table()
    tbl.nRows = int(  df.shape[0] )
    tbl.columns = []

    
    if df_lib == "polars":
        colnames = df.columns
        dtypes = [ str.lower(str(dt)) for dt in  df.dtypes]
        for i in range(0, len(dtypes)):
            if dtypes[i] == 'utf8':
                dtypes[i] = 'object'

        
    else:
        colnames = list(df)
        dtypes = df.dtypes

    
    for i in range(0, len(colnames)):
        column = Column()
        column.name = colnames[i]
        if df_lib == "polars":
            values = df.drop_in_place( colnames[i]).to_numpy()
        else:
            values = df.loc[:,colnames[i]].values
            df = df.drop(colnames[i], axis=1)
        

        # FIXME Not handling categorical (factor) and  boolean yet (dtype == bool)
        if( dtypes[i] == "object" and isinstance(values[0], str) ):
            column.type = 'string'
        elif( dtypes[i] == "float64" or dtypes[i] == "float32"):
            column.type = 'double'
        elif( dtypes[i] == "int64" or dtypes[i] == "int32"):
            column.type = 'int32'
        else:
            raise "Bad column type"
        if values_as_list == True:
            column.values = values.tolist()
        else:
            column.values = values
        column.nRows = tbl.nRows
        
        tbl.columns.append( column )

    # df is returned so we are changing the input df
    return (tbl, df)


def tson_to_polars(tson:dict) -> pl.DataFrame:
    df = None
    
    for col in tson.pop("columns"):
        ctype = col.pop("type")
        cname = col.pop("name")
        vals = col.pop("values")
        dtype = pl.Int32
        if ctype == "double":
            dtype = pl.Float64
        if ctype == "string":
            dtype = pl.Utf8
        if ctype == "object":
            dtype = pl.Object
        if df is None:
            df = pl.DataFrame({
                cname:vals}, schema={cname:dtype})
        else:
            df = pl.concat([df,pl.DataFrame({
                cname:vals}, schema={cname:dtype})], how="horizontal")

    return df

def tson_to_pandas(tson:dict) -> pl.DataFrame:
    df = None
    for col in tson.pop("columns"):
        ctype = col.pop("type")
        dtype = np.int32
        if ctype == "double":
            dtype = np.double
        if ctype == "object" or ctype == "string":
            dtype = object
        if df is None:
            df = pd.DataFrame({
                col.pop("name"):col.pop("values")}, dtype=dtype)
        else:
            df = pd.concat([df,pd.DataFrame({
                col.pop("name"):col.pop("values")},dtype=dtype)], axis=1)

    # PRevents int columns, like .ci and .ri to be coded as indices of the dataframe
    #df.reset_index(inplace=True)
    return df



class TercenBytes():
    def __init__(self, data):
        self.chunkSize = 16 * 1024
        self.c0 = -1 #self.data[0:self.chunkSize]
        self.cf = -1
        self.data = data


    def __next__(self):
        if self.c0 == -1:
            self.c0 = 0 
            self.cf = self.chunkSize
        else:
            self.c0 = self.c0 + self.chunkSize 
            self.cf = self.cf + self.chunkSize 

        if self.cf > len(self.data):
            self.cf = len(self.data)

        if self.c0 < self.cf and self.c0 < len(self.data):
            return  self.data[self.c0:self.cf]

        else:
            raise StopIteration

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration


# @TODO adjust for polars, or deprecate
def dataframe_to_bytes(df, clone=False):
    nDigits = 10
    fName = tempfile.gettempdir().join('/')
    fName.join(random.choices(string.ascii_uppercase + string.digits, k=nDigits))

    if clone == True and df.__class__  == pl.DataFrame:
        tbl = dataframe_to_table( df.clone() )[0]
    else:
        tbl = dataframe_to_table( df )[0]

    tsonObj = ptson.encodeTSON( tbl.toJson() ) 


    return tsonObj.getvalue()


# @TODO adjust for polars, or deprecate
def bytes_to_pandas( tableBytes ) -> pd.DataFrame:
    dwnTbl = Table()
    
    buf = BytesIO()
    buf.write(tableBytes)
    buf.seek(0)
    dwnTson = ptson.decodeTSON(buf)

    dwnTbl.fromJson(dwnTson)

    # From table to pandas
    dwnDf = pd.DataFrame()
    for i in range(0, len(dwnTbl.columns)):
        col = dwnTbl.columns[i]
        dwnDf.insert(i, col.name, col.values)

    return dwnDf

def bytes_to_dataframe( tableBytes, df_engine="polars" ) -> pd.DataFrame:
    dwnTbl = Table()
    
    buf = BytesIO()
    buf.write(tableBytes)
    buf.seek(0)
    dwnTson = ptson.decodeTSON(buf)

    dwnTbl.fromJson(dwnTson)

    if df_engine == "pandas":
                # From table to pandas
        dwnDf = pd.DataFrame()
        for i in range(0, len(dwnTbl.columns)):
            col = dwnTbl.columns[i]
            dwnDf.insert(i, col.name, col.values)
    else:
        # From table to polars
        dwnDf = pl.DataFrame()
        for i in range(0, len(dwnTbl.columns)):
            col = dwnTbl.columns[i]
            dwnDf = dwnDf.with_column( pl.col(col.values).alias(col.name))


    return dwnDf


def as_relation(obj) -> Relation:
    if issubclass(obj.__class__, Relation):
        return obj

    if isinstance(obj, pd.DataFrame) or isinstance(obj, pl.DataFrame) or isinstance(obj, pl.LazyFrame):
        tbl = dataframe_to_table(obj)[0]
    elif issubclass(obj.__class__, Table):
        tbl = obj
    elif issubclass(obj.__class__, SchemaBase):
        rel = SimpleRelation()
        rel.id = obj.id
        return rel
    else:
        raise ValueError("as_relation -- pandas data.frame or tercen::Table is required")

    rel = InMemoryRelation()

    rel.id = uuid.uuid4().__str__()
    tbl.properties.name = rel.id
    rel.inMemoryTable = tbl

    return rel


def left_join_relation( left, right, lby, rby) -> Relation:
    if lby.__class__ == str:
        lby = [lby]

    if rby.__class__ == str:
        rby = [rby]

    compositeRelation = as_composite_relation(left)
    if compositeRelation.joinOperators == None or len(compositeRelation.joinOperators) == 0:
        compositeRelation.joinOperators  = [ as_join_operator(right, lby, rby) ]
    else:
        compositeRelation.joinOperators.append( as_join_operator(right, lby, rby) )

    return compositeRelation

def as_composite_relation( object) -> Relation:
    relation = as_relation(object)
    if issubclass(relation.__class__, CompositeRelation):
        composite = relation
    elif issubclass(relation.__class__, Relation):
        composite = CompositeRelation()
        composite.id = uuid.uuid4().__str__()
        composite.mainRelation = relation
    else:
        raise "as_composite_relation -- a Relation is required"
    
    return composite


def as_join_operator( object, lby, rby ) -> JoinOperator:
    relation = as_relation(object)
    join = JoinOperator()
    join.rightRelation = relation
    join.leftPair = mk_pair(lby, rby)
    return join

def mk_pair(lColumns, rColumns) -> ColumnPair:
    pair = ColumnPair()
    pair.lColumns = list( lColumns )
    pair.rColumns = list( rColumns )
    return pair



def logical_index( logicalList ) -> list:
    return [ i for i, x in enumerate(logicalList) if x ]

def get_from_idx_list( l, idx ) -> list:
    return [l[i] for i in idx]

def unique_and_nonempty( strList) -> list:
    res = []
    # Get unique values
    uniqueList = list(set(strList))

    for el in uniqueList:
        if len(el) > 0:
            res.append(el)

    return res


def image_file_to_df(file_path):
    filename = os.path.basename(file_path)
    ftype = os.path.splitext(file_path)[1]

    if ftype == '.png':
        mimetype = "image/png"
    elif ftype == '.svg':
        mimetype = "image/svg+xml"
    elif ftype == '.pdf':
        mimetype = "image/pdf"
    else:
        mimetype = 'unknown'

    checksum = hashlib.md5(open(file_path,'rb').read()).hexdigest()

    output_str = []

    for fpath in file_path:
        with open(file_path, mode="rb") as f:
            fc = f.read()
            output_str.append([base64.b64encode(fc)])


    o = output_str[0][0]

    outs = o.decode('utf-8')
    imgDf = pd.DataFrame({
        "filename":[filename],
        "mimetype":[mimetype],
        "checksum":[checksum],
        ".content":[outs]
    })

    return imgDf

def get_temp_filepath(ext=''):
    
    if ext != '' and str.find(ext, '.') < 0: 
        ext = ''.join([".", ext])

    letters = string.ascii_letters
    fname = ''.join(random.choice(letters) for i in range(32))
    file_path = ''.join((tempfile.gettempdir(), '/', fname,
            ext))
    
    return file_path


def flatten(l):
    ll = []

    for i in l:
        if isinstance(i, list):
            items = flatten(i)
            for k in items:
                ll.append(k)
        else:
            ll.append(i)
      
    return ll