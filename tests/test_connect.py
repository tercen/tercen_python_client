import unittest
from tercen.client.factory import TercenClient


class TestTercen(unittest.TestCase):
    def test_connect(self):
        client = TercenClient("http://172.42.0.42:5402/")
        session = client.userService.connect('test', 'test')
        self.assertIsNotNone(session)


if __name__ == '__main__':
    unittest.main()
