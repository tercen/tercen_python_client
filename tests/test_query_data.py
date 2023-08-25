import unittest, os
import numpy as np
import numpy.testing as npt
import pandas as pd
import tempfile, string, random, os, sys
import zlib

import json
import pytson as ptson
import tercen.util.helper_functions as utl
from tercen.client.factory import TercenClient
from tercen.model.base import Project, FileDocument, CSVTask, InitState, DoneState, CubeAxisQuery, CubeQuery, Factor





class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        isLocal = False

        with open("./tests/env.conf") as f:
            for line in f:
                if len(line.strip()) > 0:
                    (key, val) = line.split(sep="=")
                    conf[str(key)] = str(val).strip()

        self.tol = conf["TOLERANCE"]

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
            conf = {}

            serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])

        self.data = self.create_data()

        # Create project
        # Note: unit test for project creation is run elsewhere (test_project)
        obj = Project()
        obj.name = 'python_project'
        obj.acl.owner = 'test'
        self.project = self.client.projectService.create(obj)


        self.addCleanup(self.clear_project_files)
        
    def clear_csv_task(self):
        self.client.taskService.delete(self.csvTask.id, self.csvTask.rev)

    def clear_project_files(self):
        if( hasattr(self, 'fileDoc')):
            self.client.fileService.delete(self.fileDoc.id, self.fileDoc.rev)

        # self.client.projectService.delete(self.workflow.id, self.workflow.rev)
        self.client.projectService.delete(self.project.id, self.project.rev)
        

    def create_data(self):
        numVars = 3
        numObs = 15
        numReplicates = 1

        totalVals   = numVars * numObs * numReplicates
        varVals    = ['var{}'.format( v+1 ) for v in range(0,numVars) for v1 in range(0, numObs) for v2 in range(0, numReplicates)]
        obsVals    = ['obs{}'.format( v+1 ) for v1 in range(0,numVars) for v in range(0, numObs)  for v2 in range(0, numReplicates)]

        data = pd.DataFrame( data={
            "Observation": obsVals,
            "Variable": varVals,
            "Measurement": np.random.rand( totalVals)
        } )

        return data

    def upload_file_doc(self, df):
        dfBytes = utl.dataframe_to_bytes(df)

        fileDoc = FileDocument()
        fileDoc.name = "input_datatable"
        fileDoc.projectId = self.project.id
        fileDoc.acl.owner = self.project.acl.owner
        fileDoc.metadata.contentEncoding = "application/octet-stream"

        fileDoc = self.client.fileService.upload(fileDoc, dfBytes)

        return fileDoc

    def create_csv_task(self, df) -> CSVTask:
        self.fileDoc = self.upload_file_doc(df)
        
        task = CSVTask()
        task.state = InitState()
        task.fileDocumentId = self.fileDoc.id
        task.projectId = self.project.id
        task.owner = self.project.acl.owner

        task = self.client.taskService.create( task )
        self.client.taskService.runTask(task.id)
        csvTask = self.client.taskService.waitDone(task.id)

        return csvTask

    

    def test_transfer_file_document(self) -> None:
        df = self.create_data()

        #FIX Pandas
        self.fileDoc = self.upload_file_doc(df)
        

        dwnFileDoc = self.client.fileService.get( self.fileDoc.id )
        

        fileDownloaded = self.client.fileService.download( self.fileDoc.id )
        dwnDf = utl.bytes_to_dataframe(fileDownloaded.read(), df_engine="pandas")

        assert(  dwnFileDoc.id == self.fileDoc.id )
        npt.assert_allclose( df.iloc[:,0], dwnDf.iloc[:,0], self.tol )
        npt.assert_allclose( df.iloc[:,1], dwnDf.iloc[:,1], self.tol )
        npt.assert_allclose( df.iloc[:,2], dwnDf.iloc[:,2], self.tol )
        
  
    def test_csv_task(self) -> None:
        self.addCleanup(self.clear_csv_task)

        df = self.create_data()
        self.csvTask = self.create_csv_task(df)

        assert( isinstance( self.csvTask.state, DoneState ))
        assert( self.csvTask.duration > 0 )
        assert( not self.csvTask.schemaId is None )
        


if __name__ == '__main__':
    unittest.main()
