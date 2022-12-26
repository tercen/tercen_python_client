import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd

import os

from tercen.client import context as ctx
import tercen.util.builder as bld



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


        self.wkfBuilder = bld.WorkflowBuilder()
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( './tests/data/hospitals.csv' )

        name = self.shortDescription()
        if name == "simple":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
        elif name == "one_col":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                        columns=[{"name":"Rating.Imaging", "type":"string"}])
        elif name == "x_axis":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                        xAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
        else:
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                                    columns=[{"name":"Rating.Imaging", "type":"string"}],
                                    rows=[{"name":"Rating.Effectiveness", "type":"string"}],
                                    labels=[{"name":"Facility.Name", "type":"string"}],
                                    colors=[{"name":"Facility.Type", "type":"string"}])
        
        
        if username is None: # Running locally
            self.context = ctx.TercenContext(
                            stepId=self.wkfBuilder.workflow.steps[1].id,
                            workflowId=self.wkfBuilder.workflow.id,
                            serviceUri = "http://127.0.0.1:5400/")
        else: # Running from Github Actions
            self.context = ctx.TercenContext(
                            username=username,
                            password=passw,
                            serviceUri=serviceUri,
                            stepId=self.wkfBuilder.workflow.steps[1].id,
                            workflowId=self.wkfBuilder.workflow.id)

        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

 
    def test_select_x(self) -> None:
        '''x_axis'''
        targetYDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       
 
        selNames = ['.y', '.x']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        x = np.sort(resDf[selNames[1]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        np.testing.assert_array_equal(y, yt)
        np.testing.assert_array_equal(x, yt)

    def test_select_empty_row(self) -> None:
        '''one_col'''
        targetYDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       

        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        np.testing.assert_array_equal(y, yt)


    def test_select_empty_col_row(self) -> None:
        '''simple'''
        targetYDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       

        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        np.testing.assert_array_equal(y, yt)


    def test_select_col_row(self) -> None:
        targetYDf = pd.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
        targetColDf = pd.read_csv('tests/data/Test_Full_Projection_Table_2.csv')
        targetRowDf = pd.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        

        selNames = ['.y', '.ci', '.ri']


        
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        assert(len(np.unique(targetColDf))  == len(np.unique(resDf[".ci"])))
        assert(len(np.unique(targetRowDf))  == len(np.unique(resDf[".ri"])))
        np.testing.assert_array_equal(y, yt)

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
