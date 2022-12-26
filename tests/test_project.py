import unittest
from tercen.client.factory import TercenClient
from tercen.model.base import Project


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5400/")
        self.client.userService.connect('test', 'test')

    def test_create_project(self):
        obj = Project()
        obj.name = 'python_project'
        obj.acl.owner = 'test'
        obj = self.client.projectService.create(obj)
        self.client.teamService.delete(obj.id, obj.rev)

    def test_update_project(self):
        obj = Project()
        obj.name = 'python_project'
        obj.acl.owner = 'test'
        obj = self.client.projectService.create(obj)
        obj.name = 'python_project2'
        self.client.projectService.update(obj)
        obj2 = self.client.projectService.get(obj.id)
        self.assertEqual(obj2.name, obj.name)
        self.client.teamService.delete(obj.id, obj.rev)

    def test_find_project(self):
        obj = Project()
        obj.name = 'python_project_find'
        obj.acl.owner = 'test'
        obj = self.client.projectService.create(obj)
        start_key = [obj.acl.owner, False, "2035"]
        end_key = [obj.acl.owner, False, ""]
        projects = self.client.projectService.findByTeamAndIsPublicAndLastModifiedDate(start_key, end_key)
        pp = [p for p in projects if p.id == obj.id]
        self.assertEqual(len(pp), 1)
        self.assertEqual(pp[0].name, obj.name)
        self.client.projectService.delete(obj.id, obj.rev)
        projects = self.client.projectService.findByTeamAndIsPublicAndLastModifiedDate(start_key, end_key)
        pp = [p for p in projects if p.id == obj.id]
        self.assertEqual(len(pp), 0)


if __name__ == '__main__':
    unittest.main()
