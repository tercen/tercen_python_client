import numpy as np
import pandas as pd
import json, zlib

from io import BytesIO
import tempfile, string, random

import pytson as ptson

from tercen.model.base import Table, Column

def __pandas_to_table__(df) -> Table:
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

def pandas_to_bytes(df):
    nDigits = 10
    fName = tempfile.gettempdir().join('/')
    fName.join(random.choices(string.ascii_uppercase + string.digits, k=nDigits))

    tbl = __pandas_to_table__( df )
    
    # zlib.compress( str.encode( json.dumps(tbl.toJson())) )
    tsonObj = ptson.encodeTSON(tbl.toJson() )
    tblBytes = tsonObj.getvalue()

    return tblBytes

def bytes_to_pandas( tableBytes ) -> pd.DataFrame:
    dwnTbl = Table()
    

    # s = BytesIO(zlib.decompress(tableBytes))
    s = BytesIO(tableBytes)
    dwnJson = ptson.decodeTSON(s)
    dwnTbl.fromJson(dwnJson)

    # From table to pandas
    dwnDf = pd.DataFrame()
    for i in range(0, len(dwnTbl.columns)):
        col = dwnTbl.columns[i]
        dwnDf.insert(i, col.name, col.values)

    return dwnDf