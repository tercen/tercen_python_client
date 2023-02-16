import unittest
from tercen.client.factory import TercenClient
from tercen.model.base import FileDocument, Project


class TestFileService(unittest.TestCase):

    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5402/")
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


if __name__ == '__main__':
    unittest.main()
