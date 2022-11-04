import numpy as np
import pandas as pd
import json, zlib

from tercen.model.base import Table, Column

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

def table_bytes_to_pandas( tableBytes ) -> pd.DataFrame:
    dwnTbl = Table()
    dwnJson = json.loads(zlib.decompress(tableBytes).decode())
    dwnTbl.fromJson(dwnJson)

    # From table to pandas
    dwnDf = pd.DataFrame()
    for i in range(0, len(dwnTbl.columns)):
        col = dwnTbl.columns[i]
        dwnDf.insert(i, col.name, col.values)

    return dwnDf