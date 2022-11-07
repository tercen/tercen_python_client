import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import tempfile, string, random, os, sys

import tercen.util.http_utils as utl
from tercen.model.base import Table, Column



class TestTercen(unittest.TestCase):
    def setUp(self):
        numVars = 3
        numObs = 15
        numReplicates = 1

        totalVals   = numVars * numObs * numReplicates
        varVals    = ['var{}'.format( v+1 ) for v in range(0,numVars) for v1 in range(0, numObs) for v2 in range(0, numReplicates)]
        obsVals    = ['obs{}'.format( v+1 ) for v1 in range(0,numVars) for v in range(0, numObs)  for v2 in range(0, numReplicates)]

        self.df = pd.DataFrame( data={
            "Observation": obsVals,
            "Variable": varVals,
            "Measurement": np.random.rand( totalVals)
        } )


    def test_pandas_to_table(self):
        tbl = utl.pandas_to_table( self.df )

        assert(len(tbl.columns) == 3)
        assert(tbl.nRows == 45)
        assert(tbl.columns[0].name == "Observation")
        assert(tbl.columns[1].name == "Variable")
        assert(tbl.columns[2].name == "Measurement")
        npt.assert_array_equal( tbl.columns[0].values, self.df.iloc[:,0] )
        npt.assert_array_equal( tbl.columns[1].values, self.df.iloc[:,1] )
        npt.assert_array_equal( tbl.columns[2].values, self.df.iloc[:,2] )


    def test_table_bytes_to_pandas(self):

        dfBytes = utl.pandas_to_bytes(self.df)

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
        


        


if __name__ == '__main__':
    unittest.main()
