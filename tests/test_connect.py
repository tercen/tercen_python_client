import unittest
from tercen.client.factory import TercenClient
import time

class TestTercen(unittest.TestCase):
    def test_connect(self):
        fails = 0

        while fails < 60:
            try:
                client = TercenClient("http://127.0.0.1:5402/")
                session = client.userService.connect('test', 'test')
                break
            except:
                fails = fails + 1
                time.sleep(5)

        
        self.assertIsNotNone(session)


if __name__ == '__main__':
    unittest.main()
