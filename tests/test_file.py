import unittest, os
import sys
sys.path.append("..")
sys.path.append(".")
from tercen.client.factory import TercenClient

import pandas as pd
import numpy as np
import numpy.testing as npt
import tercen.util.helper_functions as utl
from tercen.model.impl import Project, FileDocument, CSVTask, InitState, \
            FileDocument, Project, ImportGitDatasetTask

from tercen.util.helper_functions import download_to_file, get_temp_filepath

class TestFileService(unittest.TestCase):
    
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
        self.client = TercenClient(self.serviceUri)
        self.client.userService.connect(self.username, self.passw)
        self.data = self.create_data()
        self.project = Project()
        self.file = FileDocument()

    def tearDown(self):
        # if( self.file.id != ""):
            # self.client.fileService.delete(self.file.id, self.file.rev)
        if( self.project.id != ""):
            self.client.projectService.delete(self.project.id, self.project.rev)
        

        return super().tearDown()

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

        return(data)

    def test_upload_download_file(self):
        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        self.project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = self.project.id
        bytes_data = "hello\n\nhello\n\n42".encode("utf_8")
        self.file = self.client.fileService.upload(file, bytes_data)
        data = self.client.fileService.download(self.file.id)
        assert data.read() == bytes_data
        # self.client.teamService.delete(project.id, project.rev)
        
        
    def test_download_to_file(self):
        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        self.project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = self.project.id
        bytes_data = "hello\n\nhello\n\n42".encode("utf_8")
        self.file = self.client.fileService.upload(file, bytes_data)
        fpath = get_temp_filepath(ext='txt', workflowId=None)
        download_to_file(self.client, self.file, fpath, maxTries=10, interval=5)
        # data = self.client.fileService.download(file.id)
        with open(fpath, "rb") as f:
            data = f.read()
        assert data == bytes_data
        # self.client.teamService.delete(project.id, project.rev)


    def test_upload_download_large_file(self):
        df = pd.read_csv('./tests/data/hospitals.csv')
        # df = pd.read_csv('./tests/data/scRNAseq_large_by25_no0.csv')
        bytes_data = utl.dataframe_to_bytes(df)


        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        self.project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = self.project.id 

        

        # bytes_data = "hello\n\nhello\n\n42".encode("utf_8")
        self.file = self.client.fileService.upload(file, bytes_data)
        data = self.client.fileService.download(self.file.id)
        assert data.read() == bytes_data
        # self.client.teamService.delete(project.id, project.rev)


    def test_upload_from_file(self):
        df = pd.read_csv('./tests/data/hospitals.csv')
        #bytes_data = utl.dataframe_to_bytes(df)
        import tempfile

        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        self.project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = self.project.id 

        self.file = self.client.fileService.uploadFromFile(file, './tests/data/hospitals.csv')
        data = self.client.fileService.download(self.file.id)
        tmpFile = tempfile.gettempdir() + "/tempfile"
        with open(tmpFile, "wb") as f:
            f.write(data.read())
            
        dfOut = pd.read_csv(tmpFile)
        
        for colIn, colOut in zip(df, dfOut):
            assert(colIn == colOut)
            if isinstance(df[colIn][0], str):
                for valIn, valOut in zip(df[colIn], dfOut[colOut]):
                    if isinstance(valIn, str) or isinstance(valOut, str):
                        assert(valIn == valOut)
            else:
                npt.assert_array_almost_equal(df[colIn],dfOut[colOut])
            

        
        # assert data.read() == bytes_data
        # self.client.teamService.delete(project.id, project.rev)
        



    def test_upload_file_as_table(self): 
        table = utl.dataframe_to_table(self.data)[0]

        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        self.project = self.client.projectService.create(project)
        
        file = FileDocument()
        file.name = "test_file_table.csv"
        file.acl.owner = 'test'
        file.projectId = self.project.id
        # bytes_data = encodeTSON(doc.toJson()).getvalue()
        self.file = self.client.fileService.uploadTable(file, table.toJson())

        task = CSVTask()
        task.state = InitState()
        task.fileDocumentId = self.file.id
        task.projectId = self.project.id
        task.owner = self.project.acl.owner

        task = self.client.taskService.create( task )
        self.client.taskService.runTask(task.id)
        self.client.taskService.waitDone(task.id)

        # self.client.fileService.delete(file.id, file.rev)
        # self.client.teamService.delete(project.id, project.rev)






if __name__ == '__main__':
    unittest.main()
