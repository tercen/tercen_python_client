import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import polars as pl
import json

import tercen.util.helper_functions as utl

class TestTercen(unittest.TestCase):

    def setUp(self):
        numVars = 3
        numObs = 15
        numReplicates = 1

        totalVals   = numVars * numObs * numReplicates
        varVals    = [str('var{}'.format( v+1 )) for v in range(0,numVars) for v1 in range(0, numObs) for v2 in range(0, numReplicates)]
        obsVals    = [str('obs{}'.format( v+1 )) for v1 in range(0,numVars) for v in range(0, numObs)  for v2 in range(0, numReplicates)]
        
        varIVals    = [v+1 for v in range(0,numVars) for v1 in range(0, numObs) for v2 in range(0, numReplicates)]
        obsIVals    = [v+1 for v1 in range(0,numVars) for v in range(0, numObs)  for v2 in range(0, numReplicates)]

        self.df = pd.DataFrame( data={
            "Observation": obsVals,
            "Variable": varVals,
            "Measurement": np.random.rand( totalVals)
        } )

        self.df_cr = pd.DataFrame( data={
            ".ci": obsIVals,
            ".ri": varIVals,
            "Measurement": np.random.rand( totalVals)
        } )

        self.df2 = pl.DataFrame( data={
            "Observation": obsVals,
            "Variable": varVals,
            "Measurement": np.random.rand( totalVals)
        } )


    def test_pandas_to_table(self):
        tbl = utl.dataframe_to_table( self.df )[0]

        assert(len(tbl.columns) == 3)
        assert(tbl.nRows == 45)
        assert(tbl.columns[0].name == "Observation")
        assert(tbl.columns[1].name == "Variable")
        assert(tbl.columns[2].name == "Measurement")
        npt.assert_array_equal( tbl.columns[0].values, self.df.iloc[:,0] )
        npt.assert_array_equal( tbl.columns[1].values, self.df.iloc[:,1] )
        npt.assert_array_equal( tbl.columns[2].values, self.df.iloc[:,2] )

    def test_tson_to_pandas(self):
        tbl = utl.dataframe_to_table( self.df_cr )[0]
        df = utl.tson_to_pandas(tbl.toJson())
        
        colnames = list(df)
        dtypes = df.dtypes

        assert(df.shape[1] == 3)
        assert(df.shape[0] == 45)

        assert(colnames[0] == ".ci")
        assert(colnames[1] == ".ri")
        assert(colnames[2] == "Measurement")

        assert(dtypes[0] == np.int32)
        assert(dtypes[1] == np.int32)
        assert(dtypes[2] == np.double)

        npt.assert_array_equal( df.iloc[:,0], self.df_cr.iloc[:,0] )
        npt.assert_array_equal( df.iloc[:,1], self.df_cr.iloc[:,1] )
        npt.assert_array_equal( df.iloc[:,2], self.df_cr.iloc[:,2] )

    def test_tson_to_polars(self):
        tbl = utl.dataframe_to_table( self.df_cr )[0]
        df = utl.tson_to_polars(tbl.toJson())

        colnames = df.columns
        dtypes = [ str.lower(str(dt)) for dt in  df.dtypes]
        for i in range(0, len(dtypes)):
            if dtypes[i] == 'utf8':
                dtypes[i] = 'object'


        assert(df.shape[1] == 3)
        assert(df.shape[0] == 45)

        assert(colnames[0] == ".ci")
        assert(colnames[1] == ".ri")
        assert(colnames[2] == "Measurement")

        assert(dtypes[0] == 'int32')
        assert(dtypes[1] == 'int32')
        assert(dtypes[2] == 'float64')

        # Rounding errors from polars and pandas types
        npt.assert_array_almost_equal( df[:,0], self.df_cr.iloc[:,0], 0.00001 )
        npt.assert_array_almost_equal( df[:,1], self.df_cr.iloc[:,1], 0.00001 )
        npt.assert_array_almost_equal( df[:,2], self.df_cr.iloc[:,2], 0.00001 )

    def test_polars_to_table(self):
        tbl = utl.dataframe_to_table( self.df2.clone()  )[0]

        assert(len(tbl.columns) == 3)
        assert(tbl.nRows == 45)
        assert(tbl.columns[0].name == "Observation")
        assert(tbl.columns[1].name == "Variable")
        assert(tbl.columns[2].name == "Measurement")
        npt.assert_array_equal( tbl.columns[0].values, self.df2[:,0] )
        npt.assert_array_equal( tbl.columns[1].values, self.df2[:,1] )
        npt.assert_array_equal( tbl.columns[2].values, self.df2[:,2] )


    def test_table_bytes_to_pandas(self):

        dfBytes = utl.dataframe_to_bytes(self.df)

        dfDecoded = utl.bytes_to_pandas(dfBytes)

        
        assert(len(dfDecoded) == 45)
        
        cnames = list(dfDecoded.columns.values)
        assert(len(cnames) == 3)
        assert(cnames[0] == "Observation")
        assert(cnames[1] == "Variable")
        assert(cnames[2] == "Measurement")

        npt.assert_array_equal( dfDecoded.iloc[:,0], self.df.iloc[:,0] )
        npt.assert_array_equal( dfDecoded.iloc[:,1], self.df.iloc[:,1] )
        npt.assert_array_equal( dfDecoded.iloc[:,2], self.df.iloc[:,2] )
        


    def test_table_bytes_to_polars(self):

        dfBytes = utl.dataframe_to_bytes(self.df2, clone=True)

        dfDecoded = utl.bytes_to_pandas(dfBytes)

        
        assert(len(dfDecoded) == 45)
        
        cnames = list(dfDecoded.columns.values)
        assert(len(cnames) == 3)
        assert(cnames[0] == "Observation")
        assert(cnames[1] == "Variable")
        assert(cnames[2] == "Measurement")

        npt.assert_array_equal( dfDecoded.iloc[:,0], self.df2[:,0] )
        npt.assert_array_equal( dfDecoded.iloc[:,1], self.df2[:,1] )
        npt.assert_array_equal( dfDecoded.iloc[:,2], self.df2[:,2] )
        


if __name__ == '__main__':
    unittest.main()
