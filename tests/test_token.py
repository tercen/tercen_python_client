import unittest, os
from tercen.client.factory import TercenClient

import jwt
import time


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
    
    def test_create_token(self):
        token = self.client.userService.createToken(userId="admin", validityInSeconds=2)
        token_json = jwt.decode( token ,  algorithms=["HS256"], options={"verify_signature": False})

        assert(token_json is dict)
        assert(token_json['data'] != None)
        assert(token_json['data']['u'] == 'admin')

    def test_validate_token(self):
        token = self.client.userService.createToken(userId="admin", validityInSeconds=2)
        token_json = jwt.decode( token ,  algorithms=["HS256"], options={"verify_signature": False})

        test01 = self.client.userService.isTokenValid( token=token)
        assert(test01 == True)

        time.sleep(3)        

        test02 = self.client.userService.isTokenValid( token=token)
        assert(test02 == False)





if __name__ == '__main__':
    unittest.main()
