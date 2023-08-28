import unittest
import numpy as np

import numpy.testing as npt
import pandas as pd
import polars as pl


import os

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

        self.nRows = 100000

        self.data = pd.DataFrame( {'Values':range(0,self.nRows), 
                "Columns":range(0,self.nRows),
                "Rows":range(0,self.nRows)}  )

        self.wkfBuilder = bld.WorkflowBuilder(username=username, password=passw, serviceUri=serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( self.data )
        self.wkfBuilder.add_data_step(yAxis={"name":"Values", "type":"double"}, 
                                        columns=[{"name":"Columns", "type":"double"}],
                                        rows=[{"name":"Rows", "type":"double"}])


        
        self.context = ctx.TercenContext(
                        username=username,
                        password=passw,
                        serviceUri=serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[1].id,
                        workflowId=self.wkfBuilder.workflow.id)

        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

 
    def test_select(self) -> None:
        selNames = ['.y']
     
        resDf = self.context.select( selNames  )

        assert( not resDf is None )
        assert(resDf.__class__ == pl.dataframe.frame.DataFrame)
        assert( resDf.shape[0] == self.nRows)
        
        assert(resDf[".y"].dtype == pl.Float64)

        np.testing.assert_allclose(resDf[".y"],  self.data["Values"], self.tol)

    def test_select_pandas(self) -> None:
        selNames = ['.y']
     
        resDf = self.context.select( selNames , df_lib="pandas" )
        
        

        assert( not resDf is None )
        assert(resDf.__class__ == pd.core.frame.DataFrame)
        assert( resDf.shape[0] == self.nRows)

        assert(resDf[".y"].dtype == np.float64)

        np.testing.assert_allclose(resDf[".y"],  self.data["Values"], self.tol)



    def test_select_stream(self) -> None:
        selNames = ['.y']

        resDf = self.context.select_stream( selNames )
        
        
        assert( not resDf is None )
        assert( resDf.shape[0] == self.nRows) 
        
        np.testing.assert_allclose(resDf[".y"],  self.data["Values"], self.tol)



if __name__ == '__main__':
    unittest.main()
