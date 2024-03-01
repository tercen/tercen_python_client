import unittest, os
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
        session = self.client.userService.connect(self.username, self.passw)

    def test_operator_library(self):
        #Parameters are seemingly ignored
        lib = self.client.documentService.getTercenOperatorLibrary(0, 1)

        assert(not lib is None)
        assert(len(lib) > 0)

        for op in lib:
            op.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0]
            if not issubclass(op.__class__, Operator  ):
                print('z')
            assert( issubclass(op.__class__, Operator  )) 

    def test_dataset_library(self):
        #Parameters are seemingly ignored
        lib = self.client.documentService.getLibrary('', [], ['Schema', 'File', 'Operator'], [], 0, 100)

        assert(not lib is None)
        assert(len(lib) > 0)

        for op in lib:
            assert( isinstance(op, Document )) 
        

if __name__ == '__main__':
    unittest.main()
