import pandas as pd
import zlib

from io import BytesIO
import tempfile, string, random

import pytson as ptson
import uuid
from tercen.model.base import Table, Column, InMemoryRelation, Relation, SchemaBase, SimpleRelation
from tercen.model.base import CompositeRelation, JoinOperator, ColumnPair

# import tercen.util.pytmp as ptmp



def pandas_to_table(df, values_as_list=False) -> Table:
    tbl = Table()
    tbl.nRows = int(  df.shape[0] )
    tbl.columns = []

    colnames = list(df)
    dtypes = df.dtypes
    for i in range(0, len(colnames)):
        column = Column()
        column.name = colnames[i]
        values = df.loc[:,colnames[i]].values
        

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

    return tbl

def table_to_pandas(tbl) -> pd.DataFrame:
    df = pd.DataFrame()

    for c in tbl.columns:
        df[c.name] = c.values

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


def pandas_to_bytes(df):
    nDigits = 10
    fName = tempfile.gettempdir().join('/')
    fName.join(random.choices(string.ascii_uppercase + string.digits, k=nDigits))

    tbl = pandas_to_table( df )

    tsonObj = ptson.encodeTSON( tbl.toJson() ) 
    #tblBytes = zlib.compress(tsonObj.getvalue())

    return tsonObj.getvalue()


def bytes_to_pandas( tableBytes ) -> pd.DataFrame:
    dwnTbl = Table()
    

    # s = BytesIO(zlib.decompress(tableBytes))
    # FIXME
    # Check if this is still necessary
    # If not, remove
    # If yes, avoid creating the buffer here.
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


def as_relation(obj) -> Relation:
    if issubclass(obj.__class__, Relation):
        return obj

    if isinstance(obj, pd.DataFrame):
        tbl = pandas_to_table(obj)
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