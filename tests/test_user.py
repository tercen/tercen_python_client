import unittest
from tercen.client.factory import TercenClient
from tercen.model.base import Team


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5400/")
        self.client.userService.connect('test', 'test')

    def test_get_user(self):
        user = self.client.userService.get('test')
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'test')

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
