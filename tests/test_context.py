import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import tempfile, string, random, os, sys
import zlib

import json
import pytson as ptson
import tercen.util.helper_functions as utl
from tercen.client.factory import TercenClient
from tercen.model.base import Project, FileDocument, CSVTask, InitState, DoneState, CubeAxisQuery, CubeQuery, Factor

from tercen.client import context as ctx




class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5402/")
        self.client.userService.connect('test', 'test')

        

        

    def test_select_one(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        tercenCtx = ctx.TercenContext( self.client, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['.y']

        targetDf = targetDf[selNames]
        resDf = tercenCtx.select( selNames )
        
      
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)
        np.testing.assert_array_equal(resDf.loc[:,selNames], targetDf.loc[:,selNames])

    def test_select_many(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        tercenCtx = ctx.TercenContext( self.client, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['.y', 'Facility.Type', 'Facility.Name' ]

        targetDf = targetDf[selNames]
        resDf = tercenCtx.select( selNames )
        
      
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        for selName in selNames:
            np.testing.assert_array_equal(resDf.loc[:,selNames], targetDf.loc[:,selNames])
        


    def test_select_column(self):
        assert(False)

    def test_select_row(self):
        assert(False)



if __name__ == '__main__':
    unittest.main()
