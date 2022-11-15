import pandas as pd
import zlib

from io import BytesIO
import tempfile, string, random

import pytson as ptson
import uuid
from tercen.model.base import Table, Column, InMemoryRelation, Relation, SchemaBase, SimpleRelation

def pandas_to_table(df) -> Table:
    tbl = Table()
    tbl.nRows = int(  df.shape[0] )
    tbl.columns = []

    colnames = df.columns.values.tolist()
    dtypes = df.dtypes
    for i in range(0, len(colnames)):
        column = Column()
        column.name = colnames[i]
        values = df.loc[:,colnames[i]].values.tolist()
        

        # FIXME Not handling categorical (factor) and  boolean yet (dtype == bool)
        if( dtypes[i] == "object" and isinstance(values[0], str) ):
            column.type = 'string'
        elif( dtypes[i] == "float64"):
            column.type = 'double'
        elif( dtypes[i] == "int64"):
            column.type = 'int32'
        else:
            raise "Bad column type"
        
        column.values = values

        tbl.columns.append( column )

    return tbl

def table_to_pandas(tbl) -> pd.DataFrame:
    df = pd.DataFrame()

    for c in tbl.columns:
        df[c.name] = c.values

    return df

def pandas_to_bytes(df):
    nDigits = 10
    fName = tempfile.gettempdir().join('/')
    fName.join(random.choices(string.ascii_uppercase + string.digits, k=nDigits))

    tbl = pandas_to_table( df )
    
    # zlib.compress( str.encode( json.dumps(tbl.toJson())) )
    tsonObj = ptson.encodeTSON( tbl.toJson() ) 
    tblBytes = zlib.compress(tsonObj.getvalue())

    return tblBytes


def bytes_to_pandas( tableBytes ) -> pd.DataFrame:
    dwnTbl = Table()
    

    s = BytesIO(zlib.decompress(tableBytes))
    dwnTson = ptson.decodeTSON(s)

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

    rel.id = uuid.uuid4()
    tbl.properties.name = rel.id
    rel.inMemoryTable = tbl

    return rel

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