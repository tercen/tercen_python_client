import unittest
from tercen.client.factory import TercenClient


class TestTercen(unittest.TestCase):
    def test_connect(self):
        
        client = TercenClient("http://127.0.0.1:5402/")
        session = client.userService.connect('test', 'test')
        self.assertIsNotNone(session)


if __name__ == '__main__':
    unittest.main()
