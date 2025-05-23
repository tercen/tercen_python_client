import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import polars as pl

import os
import sys
sys.path.append("..")
sys.path.append(".")
from tercen.client import context as ctx
import tercen.util.builder as bld



class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        isLocal = False

        conf = {}
        with open("./tests/env.conf") as f:
            for line in f:
                if len(line.strip()) > 0:
                    (key, val) = line.split(sep="=")
                    conf[str(key)] = str(val).strip()

        self.tol = float(conf["TOLERANCE"])

        if 'TERCEN_PASSWORD' in envs:
            passw = envs['TERCEN_PASSWORD']
        else:
            passw = None

        if 'TERCEN_URI' in envs:
            serviceUri = envs['TERCEN_URI']
        else:
            serviceUri = None
        if 'TERCEN_USERNAME' in envs:
            username = envs['TERCEN_USERNAME']
        else:
            isLocal = True
            username = 'test'
            passw = 'test'
            

            serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])
            




        self.wkfBuilder = bld.WorkflowBuilder(username=username, password=passw, serviceUri=serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')

        name = self.shortDescription()
        if name == "types":
            self.data = pd.DataFrame( {'Values':[0,0,3.4,0,0.3,0], 
                    "Columns":[0,1,0,1,0,1],
                    "Rows":["0","0","1","1","2","2"]} )
            
            self.wkfBuilder.add_table_step( self.data, int_columns=["Columns"] )
            self.wkfBuilder.add_data_step(yAxis={"name":"Values", "type":"double"}, 
                                            columns=[{"name":"Columns", "type":"int32"}],
                                            rows=[{"name":"Rows", "type":"string"}])
        else:
            self.wkfBuilder.add_table_step( './tests/data/hospitals.csv' )
            if name == "simple":
                self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
            elif name == "one_col":
                self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                            columns=[{"name":"Rating.Imaging", "type":"string"}])
            elif name == "x_axis":
                self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                            xAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
            else:
                # TODO Test color projection
                self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                                        columns=[{"name":"Rating.Imaging", "type":"string"}],
                                        rows=[{"name":"Rating.Effectiveness", "type":"string"}],
                                        labels=[{"name":"Facility.Name", "type":"string"}])
        
        
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
        targetYDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       
 
        selNames = ['.y', '.x']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        x = np.sort(resDf[selNames[1]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        np.testing.assert_allclose(y, yt, self.tol)
        np.testing.assert_allclose(x, yt, self.tol)

    def test_select_empty_row(self) -> None:
        '''one_col'''
        targetYDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       
        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        assert(resDf[:,0].dtype == pl.Float64)
        
    def test_select_offset_nr(self) -> None:
        '''types'''
        targetYDf = self.data
       
        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames, offset=3, nr=3 )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf["Values"])[2:5]

        assert( not resDf is None )
        np.testing.assert_allclose(y, yt, self.tol)

    def test_select_types(self) -> None:
        '''types'''
        targetYDf = self.data
       

        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf["Values"])

        assert( not resDf is None )
        np.testing.assert_allclose(y, yt, self.tol)

    def test_select_empty_col_row(self) -> None:
        '''simple'''
        targetYDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
       

        selNames = ['.y', '.ci', '.ri']
     
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        np.testing.assert_allclose(y, yt, self.tol)


    def test_select_col_row(self) -> None:
        targetYDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')
        targetColDf = pl.read_csv('tests/data/Test_Full_Projection_Table_2.csv')
        targetRowDf = pl.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        

        selNames = ['.y', '.ci', '.ri']


        
        resDf = self.context.select( selNames )
        
        y = np.sort(resDf[selNames[0]])
        yt = np.sort(targetYDf[selNames[0]])

        assert( not resDf is None )
        assert(len(np.unique(targetColDf))  == len(np.unique(resDf[".ci"])))
        assert(len(np.unique(targetRowDf))  == len(np.unique(resDf[".ri"])))
        np.testing.assert_allclose(y, yt, self.tol)

    def test_select_one(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        selNames = ['.y']


        targetDf = targetDf[selNames]
        resDf = self.context.select( selNames ) 
        
        stargetDf = targetDf[".y"].sort(in_place=False)
        sresDf = resDf[".y"].sort(in_place=False)

       
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)
        np.testing.assert_allclose(resDf[:,selNames], targetDf[:,selNames], self.tol)

    def test_select_many(self) -> None:
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')

        selNames = ['.y', 'Facility.Name' ]

        targetDf = targetDf[selNames]
        resDf = self.context.select( selNames )
        
        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)
        
        np.testing.assert_allclose(resDf[:,".y"].to_numpy(), targetDf[:,".y"].to_numpy(), self.tol)
        
        for selName in selNames[1:]:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())



    def test_select_all(self) -> None:
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_1.csv')


        selNames = ['']

        resDf = self.context.select( selNames )


        assert( not resDf is None )
        outCols = [n for n in targetDf.columns]
        cnames = [n for n in resDf.columns]

        for cn in cnames:
            assert(cn in outCols)
        


        for selName in cnames:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())
        


    def test_select_all_columns(self):
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        selNames = ['']

        resDf = self.context.cselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())

    def test_select_columns(self):
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_2.csv')

        selNames = ['Rating.Imaging']
        targetDf = targetDf[selNames]
        resDf = self.context.cselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]
        for selName in cnames:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())

    def test_select_all_rows(self):
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        selNames = ['']

        resDf = self.context.rselect( selNames )

        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)


        cnames = [n for n in resDf.columns]

        for selName in cnames:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())

    def test_select_rows(self):
        targetDf = pl.read_csv('tests/data/Test_Full_Projection_Table_3.csv')

        selNames = ['Rating.Effectiveness']
        targetDf = targetDf[selNames]
        resDf = self.context.rselect( selNames )


        assert( not resDf is None )
        assert(resDf.shape == targetDf.shape)

        cnames = [n for n in resDf.columns]

        for selName in cnames:
            np.testing.assert_equal(resDf[:,selName].to_numpy(), targetDf[:,selName].to_numpy())

if __name__ == '__main__':
    unittest.main()
