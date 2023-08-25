import unittest, os
from tercen.client.factory import TercenClient
from tercen.model.base import FileDocument, Project

import pandas as pd
import tercen.util.helper_functions as utl

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
        session = self.client.userService.connect(self.username, self.passw)

    
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



if __name__ == '__main__':
    unittest.main()
