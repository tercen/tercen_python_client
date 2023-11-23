import unittest, os
from tercen.client.factory import TercenClient


import pandas as pd
import numpy as np
import tercen.util.helper_functions as utl
from tercen.model.impl import Project, FileDocument, CSVTask, InitState, \
            FileDocument, Project, ImportGitDatasetTask

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
        project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = project.id
        bytes_data = "hello\n\nhello\n\n42".encode("utf_8")
        file = self.client.fileService.upload(file, bytes_data)
        data = self.client.fileService.download(file.id)
        assert data.read() == bytes_data
        self.client.teamService.delete(project.id, project.rev)



    def test_upload_download_large_file(self):
        df = pd.read_csv('./tests/data/hospitals.csv')
        # df = pd.read_csv('./tests/data/scRNAseq_large_by25_no0.csv')
        bytes_data = utl.dataframe_to_bytes(df)


        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        project = self.client.projectService.create(project)
        file = FileDocument()
        file.name = "hello.txt"
        file.acl.owner = 'test'
        file.projectId = project.id 

        

        # bytes_data = "hello\n\nhello\n\n42".encode("utf_8")
        file = self.client.fileService.upload(file, bytes_data)
        data = self.client.fileService.download(file.id)
        assert data.read() == bytes_data
        self.client.teamService.delete(project.id, project.rev)


    def test_upload_file_as_table(self): 
        table = utl.dataframe_to_table(self.data)[0]

        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        project = self.client.projectService.create(project)
        
        file = FileDocument()
        file.name = "test_file_table.csv"
        file.acl.owner = 'test'
        file.projectId = project.id
        # bytes_data = encodeTSON(doc.toJson()).getvalue()
        file = self.client.fileService.uploadTable(file, table.toJson())

        task = CSVTask()
        task.state = InitState()
        task.fileDocumentId = file.id
        task.projectId = project.id
        task.owner = project.acl.owner

        task = self.client.taskService.create( task )
        self.client.taskService.runTask(task.id)
        csvTask = self.client.taskService.waitDone(task.id)

        self.client.fileService.delete(file.id, file.rev)
        self.client.teamService.delete(project.id, project.rev)

    def test_upload_file_from_library(self): 
        dsLib = self.client.documentService.getTercenDatasetLibrary(0, 100)

        
        fileDoc = None
        for l in dsLib:
            if l.name == "Crabs Data.csv":
                fileDoc = l
                break

        assert(not fileDoc is None)


        project = Project()
        project.name = 'python_project_file'
        project.acl.owner = 'test'
        project = self.client.projectService.create(project)

        gt = ''
        if "GITHUB_TOKEN" in os.environ:
            gt = os.environ["GITHUB_TOKEN"]
        


        gitTask = ImportGitDatasetTask()
        gitTask.state = InitState()
        gitTask.gitToken = gt
        gitTask.projectId = project.id
        gitTask.url = fileDoc.url
        gitTask.version = fileDoc.version
        gitTask.owner = project.acl.owner

        gitTask = self.client.taskService.create( gitTask )
        self.client.taskService.runTask(gitTask.id)
        gitTask = self.client.taskService.waitDone(gitTask.id)


        
        sch = self.client.tableSchemaService.get(gitTask.schemaId)
        assert(not sch is None)


        self.client.fileService.delete(sch.id, sch.rev)
        self.client.teamService.delete(project.id, project.rev)




if __name__ == '__main__':
    unittest.main()
