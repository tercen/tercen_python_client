import unittest, os
from tercen.client.factory import TercenClient
from tercen.model.impl import Team


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

    def test_get_user(self):
        user = self.client.userService.get('test')
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'test')
        # print(user.email)

    def test_find_user(self):
        users = self.client.userService.findUserByEmail(["test@tercen.com"])
        self.assertIsNotNone(users)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].email, "test@tercen.com")

    def test_create_team(self):
        team = Team()
        team.isDeleted = False
        team.name = 'python_team7'
        team.acl.owner = 'test'
        created_team = self.client.teamService.create(team)
        self.assertIsNotNone(created_team)
        self.assertEqual(created_team.name, team.name)
        self.client.teamService.delete(created_team.id, created_team.rev)


if __name__ == '__main__':
    unittest.main()
