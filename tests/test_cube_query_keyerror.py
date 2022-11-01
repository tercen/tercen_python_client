import unittest
from tercen.client.factory import TercenClient


class TestTercen(unittest.TestCase):
    def test_cube_query_keyerror(self):
        client = TercenClient("http://127.0.0.1:5400/")
        session = client.userService.connect('test', 'test')
        self.assertIsNotNone(session)
        # # 6721f92779641b0e2f8a6d152c007e46/ds/0422e789-fcaf-4ef4-b446-76a68a77120c
        # cubeQuery = client.workflowService.getCubeQuery(
        #     workflowId="6721f92779641b0e2f8a6d152c007e46",
        #     stepId="0422e789-fcaf-4ef4-b446-76a68a77120c"
        # )
        # print(cubeQuery)



if __name__ == '__main__':
    unittest.main()
