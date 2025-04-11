import gzip
import pickle
import tercen
from tercen.util.export import export_df_to_project, export_to_project_as_csv
from tercen.util.helper_functions import download_to_file, get_temp_filepath
from tercen.model.impl import Pair, Project, FileDocument, CSVTask, InitState, \
    FileDocument, Project, ImportGitDatasetTask
import tercen.util.helper_functions as utl
import numpy.testing as npt
import numpy as np
import pandas as pd
from tercen.client.factory import TercenClient
import unittest
import os
import sys
sys.path.append("..")
sys.path.append(".")
from tercen.client import context as ctx
import tercen.util.builder as bld

class TestFileService(unittest.TestCase):

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
        self.data = pd.DataFrame( {'Values':[0,0,3.4,0,0.3,0], 
                "Columns":[0,1,0,1,0,1],
                "Rows":["0","0","1","1","2","2"]} )
        
        self.wkfBuilder.add_table_step( self.data, int_columns=["Columns"] )
        self.wkfBuilder.add_data_step(yAxis={"name":"Values", "type":"double"}, 
                                        columns=[{"name":"Columns", "type":"int32"}],
                                        rows=[{"name":"Rows", "type":"string"}])
        # self.project = Project()
        # self.file = FileDocument()
        self.context = ctx.TercenContext(
                username=username,
                password=passw,
                serviceUri=serviceUri,
                stepId=self.wkfBuilder.workflow.steps[1].id,
                workflowId=self.wkfBuilder.workflow.id)

        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()


    def test_export_df(self):
        result = export_df_to_project( self.context, self.data, fname="test_data", projectId=self.wkfBuilder.proj.id, meta=[Pair(m={"key":"key1", "value":"value1"} )],
                             inplace=False, user="test", folderId="" )

        
        assert(isinstance(result[0], FileDocument))   
        
        fileDoc = result[0]
        assert( fileDoc.hasMeta("key1"))
        


if __name__ == '__main__':
    unittest.main()
