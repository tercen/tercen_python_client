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
