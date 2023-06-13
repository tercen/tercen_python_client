import unittest
from tercen.client.factory import TercenClient
from tercen.model.base import FileDocument, Project

import pandas as pd
import tercen.util.helper_functions as utl

class TestFileService(unittest.TestCase):

    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5400/")
        self.client.userService.connect('test', 'test')

    
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


    # 97mb 
    # @memunit.assert_mb
    def test_upload_download_large_file(self):
        df = pd.read_csv('./tests/data/hospitals.csv')
        # df = pd.read_csv('./tests/data/scRNAseq_large_by25_no0.csv')
        bytes_data = utl.pandas_to_bytes(df)


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
