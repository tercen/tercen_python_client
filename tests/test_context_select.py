import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd

import os

from tercen.client.factory import TercenClient
from tercen.client import context as ctx




class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        if 'TERCEN_USERNAME' in envs:
            username = envs['TERCEN_USERNAME']
        else:
            username = None

        if 'TERCEN_PASSWORD' in envs:
            passw = envs['TERCEN_PASSWORD']
        else:
            passw = None

        if 'TERCEN_URI' in envs:
            serviceUri = envs['TERCEN_URI']
        else:
            serviceUri = None

        if username is None: # Running locally
            self.context = ctx.TercenContext(
                            stepId="2ca54ff5-5b7f-44e9-870b-48facabc41ae",
                            workflowId="9b611b90f412969d6f617f559f005bc6")
        else: # Running from Github Actions
            self.context = ctx.TercenContext(
                            username=username,
                            password=passw,
                            serviceUri=serviceUri,
                            stepId="2ca54ff5-5b7f-44e9-870b-48facabc41ae",
                            workflowId="9b611b90f412969d6f617f559f005bc6")

    def test_select_one(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        selNames = ['.y']


        targetDf = targetDf[selNames]
        resDf = self.context.select( selNames )
        
      
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)
        np.testing.assert_array_equal(resDf.loc[:,selNames], targetDf.loc[:,selNames])

    def test_select_many(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        selNames = ['.y', 'Facility.Type', 'Facility.Name' ]

        targetDf = targetDf[selNames]
        resDf = self.context.select( selNames )
        
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        for selName in selNames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_all(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        selNames = ['']

        targetDf = targetDf.drop(".cri", axis=1) # int64
        resDf = self.context.select( selNames )
        
      
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])
        


    def test_select_all_columns(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        selNames = ['']

        resDf = self.context.cselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_columns(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        selNames = ['Rating.Imaging']
        targetDf = targetDf[selNames]
        resDf = self.context.cselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_all_rows(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        selNames = ['']

        resDf = self.context.rselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_rows(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        selNames = ['Rating.Effectiveness']
        targetDf = targetDf[selNames]
        resDf = self.context.rselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

if __name__ == '__main__':
    unittest.main()
