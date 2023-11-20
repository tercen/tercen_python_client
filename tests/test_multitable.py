import unittest
import os 

from tercen.client import context as ctx
import tercen.util.builder as bld
import tercen.util.helper_functions as utl
import pandas as pd
import polars as pl
import numpy as np
import numpy.testing as npt

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
        if name == "multitable_singleds":
            self.wkfBuilder.add_table_step( './tests/data/hospitals.csv', name="hospitals_ts" )
            self.wkfBuilder.add_table_step( './tests/data/CrabsData.csv', name="crabs_ts" )
            
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},\
                                          linkTo="hospitals_ts")
        
            self.wkfBuilder.add_data_step(yAxis={"name":"measurement", "type":"double"},\
                                          linkTo="crabs_ts")
            
        if name == "multidatastep":
            self.wkfBuilder.add_table_step( './tests/data/hospitals.csv', name="hospitals_ts" )
            self.wkfBuilder.add_table_step( './tests/data/CrabsData.csv', name="crabs_ts" )

            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},\
                                          linkTo="hospitals_ts")

        
        self.context1 = ctx.TercenContext(
                        username=username,
                        password=passw,
                        serviceUri=serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[2].id,
                        workflowId=self.wkfBuilder.workflow.id)
        
        self.context2 = ctx.TercenContext(
                        username=username,
                        password=passw,
                        serviceUri=serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[3].id,
                        workflowId=self.wkfBuilder.workflow.id)
        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

    def test_multitable_singleds(self) -> None:
        '''multitable_singleds'''

        y1 = self.context1.select([".y"]).to_numpy()
        
        outY1 = pl.read_csv('./tests/data/hospitals.csv').select("Procedure.Hip Knee.Cost").to_numpy()
        outY1 = np.sort(outY1, axis=0)

        assert(len(y1) == len(outY1))
        npt.assert_allclose(y1, outY1, self.tol)

        y2 = self.context2.select([".y"]).to_numpy()

        outY2 = pl.read_csv('./tests/data/CrabsData.csv').select("measurement").to_numpy()
        outY2 = np.sort(outY2, axis=0)

        assert(len(y2) == len(outY2))
        npt.assert_allclose(y2, outY2, self.tol)
