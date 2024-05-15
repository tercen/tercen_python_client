import unittest, os
import sys
sys.path.append("..")
sys.path.append(".")
from tercen.client.factory import TercenClient
from tercen.model.impl import Project

class TestUserService(unittest.TestCase):

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

    def test_create_project(self):
        self.client.fileService.__class__
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
        #obj.isPublic = False
        obj.isDeleted = False
        obj = self.client.projectService.create(obj)
        start_key = [obj.acl.owner, True, "9999"]
        end_key = [obj.acl.owner, True, ""]
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
