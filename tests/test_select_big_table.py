import unittest
import numpy as np
import string
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

        self.data = pd.DataFrame( {'Values':range(0,4000000), 
                "Columns":range(0,4000000),
                "Rows":range(0,4000000)}  )

        self.wkfBuilder = bld.WorkflowBuilder()
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( self.data )
        self.wkfBuilder.add_data_step(yAxis={"name":"Values", "type":"double"}, 
                                        columns=[{"name":"Columns", "type":"double"}],
                                        rows=[{"name":"Rows", "type":"double"}])


        
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

 
    def test_select(self) -> None:
        selNames = ['.y']
     
        resDf = self.context.select( selNames )
        
        assert( not resDf is None )
        assert( resDf.shape[0] == 4000000)
        
        np.testing.assert_array_equal(resDf[".y"],  self.data["Values"])

    def test_cselect(self) -> None:
        selNames = ['Columns']
     
        resDf = self.context.cselect( selNames )
        
        assert( not resDf is None )
        assert( resDf.shape[0] == 4000000)
        
        np.testing.assert_array_equal(resDf["Columns"],  self.data["Columns"])

    def test_rselect(self) -> None:
        selNames = ['Rows']
     
        resDf = self.context.rselect( selNames )
        
        assert( not resDf is None )
        assert( resDf.shape[0] == 4000000)
        
        np.testing.assert_array_equal(resDf["Rows"],  self.data["Rows"])



if __name__ == '__main__':
    unittest.main()
