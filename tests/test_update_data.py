import unittest
import os 

from tercen.client import context as ctx
import tercen.util.builder as bld

import numpy.testing as npt

class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        isLocal = False
        if 'TERCEN_PASSWORD' in envs:
            self.passw = envs['TERCEN_PASSWORD']
        else:
            self.passw = None

        if 'TERCEN_URI' in envs:
            self.serviceUri = envs['TERCEN_URI']
        else:
            self.serviceUri = None
        if 'TERCEN_USERNAME' in envs:
            self.username = envs['TERCEN_USERNAME']
        else:
            isLocal = True
            self.username = 'test'
            self.passw = 'test'
            conf = {}
            with open("./tests/env.conf") as f:
                for line in f:
                    if len(line.strip()) > 0:
                        (key, val) = line.split(sep="=")
                        conf[str(key)] = str(val).strip()

            self.serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])



        self.wkfBuilder = bld.WorkflowBuilder(username=self.username, password=self.passw, serviceUri=self.serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( './tests/data/hospitals.csv' )

        name = self.shortDescription()
        if name == "simple":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
        elif name == "simple02":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                                    columns=[{"name":"Rating.Imaging", "type":"string"}])
        else:
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                                    columns=[{"name":"Rating.Imaging", "type":"string"}],
                                    rows=[{"name":"Rating.Effectiveness", "type":"string"}],
                                    labels=[{"name":"Facility.Name", "type":"string"}],
                                    colors=[{"name":"Facility.Type", "type":"string"}])
        
        self.context = ctx.TercenContext(
                        username=self.username,
                        password=self.passw,
                        serviceUri=self.serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[1].id,
                        workflowId=self.wkfBuilder.workflow.id)
        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

    # 112.5    
    # @memunit.assert_mb
    def test_save(self) -> None:
        df = self.context.select(['.y', '.ci', '.ri'])

        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop('.y', axis=1)

        
        df = self.context.add_namespace(df) 
        for col in  df.columns:
            parts = col.split(",")
            if len(parts) > 1 and parts[1] == "y2":
                nms = parts[1]
                break

        # FIXME
        # 1. Use save
        # 2. Ensure workflow builder accepts a step to be added
        # 3. Use that to get a projection
        # 4. Compare the results
        resDf = self.context.save_dev(df)

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = str.split(df.columns[i] , sep='.')[-1]
            c1 = str.split(resDf.columns[i] , sep='.')[-1]
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[".ci"].values, resDf[".ci"].values)

    def test_save_no_rowcol(self) -> None:
        '''simple'''
        df = self.context.select(['.y', '.ci', '.ri'])
        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop(['.y'], axis=1)

        df = self.context.add_namespace(df) 

        resDf =  self.context.save_dev(df)

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = df.columns[i] 
            c1 = resDf.columns[i] 
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[c0].values, resDf[c1].values)

    def test_save_no_col(self) -> None:
        '''simple02'''
        df = self.context.select(['.y', '.ci', '.ri'])
        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop(['.y'], axis=1)

        df = self.context.add_namespace(df) 
        resDf = self.context.save_dev(df) 
        

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = df.columns[i] 
            c1 = resDf.columns[i] 
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[c0].values, resDf[c1].values)




if __name__ == '__main__':
    unittest.main()
