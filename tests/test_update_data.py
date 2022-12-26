import unittest
import os 

from tercen.client import context as ctx
import tercen.util.builder as bld

import numpy.testing as npt

# FAILING HERE!
# Run this test and find out what is going on
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
        

    def test_save(self) -> None:
        df = self.context.select(['.y', '.ci', '.ri'])
        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop('.y', axis=1)

        df = self.context.add_namespace(df) 
        resDf = self.context.save_dev(df)

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = str.split(df.columns[i] , sep='.')[-1]
            c1 = str.split(resDf.columns[i] , sep='.')[-1]
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[".ci"].values, resDf[".ci"].values)




if __name__ == '__main__':
    unittest.main()
