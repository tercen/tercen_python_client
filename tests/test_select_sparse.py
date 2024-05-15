import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import scipy.sparse as ssp

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



        self.data = pd.DataFrame( {'Values':[0,0,3.4,0,0.3,0], 
                "Columns":[0,1,0,1,0,1],
                "Rows":[0,0,1,1,2,2]}  )


        self.wkfBuilder = bld.WorkflowBuilder(username=username, password=passw, serviceUri=serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( self.data, int_columns=["Columns", "Rows"] )
        self.wkfBuilder.add_data_step(yAxis={"name":"Values", "type":"double"}, 
                                        columns=[{"name":"Columns", "type":"int32"}],
                                        rows=[{"name":"Rows", "type":"int32"}])


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
        resDf = self.context.select_sparse( )
        
 
        assert( not resDf is None )
        assert(resDf.__class__ == ssp._csr.csr_matrix)

        assert( resDf.shape == (6,3) )

        # NOTE sparse matrix support only a single dtype per matrix!
        assert( resDf[:,0].toarray().flatten().dtype == np.float64 )
        assert( resDf[:,1].toarray().flatten().dtype == np.float64 )
        assert( resDf[:,2].toarray().flatten().dtype == np.float64 )
        
        np.testing.assert_allclose(resDf[:,0].toarray().flatten(),  self.data["Values"].values, self.tol)
        np.testing.assert_allclose(resDf[:,1].toarray().flatten(),  self.data["Columns"].values, self.tol)
        np.testing.assert_allclose(resDf[:,2].toarray().flatten(),  self.data["Rows"].values, self.tol)
      
        


    def test_select_wide(self) -> None:
        resDf = self.context.select_sparse( wide=True  )
        
        assert( not resDf is None )
        assert( resDf.todense().shape == (3,2) )
        
        np.testing.assert_allclose(resDf.toarray()[:,0],  self.data["Values"][self.data["Columns"].values==0], self.tol)
        np.testing.assert_allclose(resDf.toarray()[:,1],  self.data["Values"][self.data["Columns"].values==1], self.tol)


if __name__ == '__main__':
    unittest.main()
