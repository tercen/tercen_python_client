import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd

from tercen.client.factory import TercenClient
from tercen.client import context as ctx




class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5402/")
        self.session = self.client.userService.connect('test', 'test')
        

        

        

    def test_select_one(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
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

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['.y', 'Facility.Type', 'Facility.Name' ]

        targetDf = targetDf[selNames]
        resDf = tercenCtx.select( selNames )
        
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        for selName in selNames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_all(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['']

        targetDf = targetDf.drop(".cri", axis=1) # int64
        resDf = tercenCtx.select( selNames )
        
      
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])
        


    def test_select_all_columns(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['']

        resDf = tercenCtx.cselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_columns(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['Rating.Imaging']
        targetDf = targetDf[selNames]
        resDf = tercenCtx.cselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_all_rows(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['']

        resDf = tercenCtx.rselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

    def test_select_rows(self):
        targetDf = pd.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        selNames = ['Rating.Effectiveness']
        targetDf = targetDf[selNames]
        resDf = tercenCtx.rselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_array_equal(resDf.loc[:,selName], targetDf.loc[:,selName])

if __name__ == '__main__':
    unittest.main()
