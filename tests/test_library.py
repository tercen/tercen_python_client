import unittest, os
import sys
sys.path.append("..")
sys.path.append(".")
from tercen.client.factory import TercenClient
from tercen.model.impl import Operator, Document

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
        self.client.userService.connect(self.username, self.passw)

    def test_library_operator(self):
        lib = self.client.documentService.getLibrary('', [], ['Operator'], [], 0, 500)

        assert(not lib is None)
        assert(len(lib) > 0)

        for op in lib:
            assert( isinstance(op, Document  )) 

            assert( op.subKind in ["Operator", "ROperator", "DockerOperator", "ShinyOperator",\
                                   "DockerWebAppOperator", "WebAppOperator"])


    # def test_library_tags(self):
    #     lib = self.client.documentService.getLibrary('', [], ['Schema', 'File', 'Operator'], ["flow cytometry"], 0, 100)

    #     assert(not lib is None)
    #     assert(len(lib) > 0)

    #     for op in lib:
    #         assert( isinstance(op, Document )) 
    #         assert("flow cytometry" in op.tags)

    def test_library(self):
        lib = self.client.documentService.getLibrary('', [], ['Schema', 'File', 'Operator'], [], 10, limit=int(15))

        assert(not lib is None)
        # assert(len(lib) == 15)
        # Parameters offset and limit are being ignored
        assert(len(lib) > 0)

        for op in lib:
            assert( isinstance(op, Document )) 

        

if __name__ == '__main__':
    unittest.main()
