import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd

import os

from tercen.client import context as ctx




class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        if 'TERCEN_USERNAME' in envs:
            username = envs['TERCEN_USERNAME']
        else:
            username = None

        if 'TERCEN_PASSWORD' in envs:
            passw = envs['TERCEN_PASSWORD']
        else:
            passw = None

        if 'TERCEN_URI' in envs:
            serviceUri = envs['TERCEN_URI']
        else:
            serviceUri = None

        if username is None: # Running locally
            self.context = ctx.TercenContext(
                            stepId="2ca54ff5-5b7f-44e9-870b-48facabc41ae",
                            workflowId="9b611b90f412969d6f617f559f005bc6")
        else: # Running from Github Actions
            self.context = ctx.TercenContext(
                            username=username,
                            password=passw,
                            serviceUri=serviceUri,
                            stepId="2ca54ff5-5b7f-44e9-870b-48facabc41ae",
                            workflowId="9b611b90f412969d6f617f559f005bc6")

    def test_connect_token(self) -> None:
        # token = self.context.context.client.userService.createToken('test', 30)

        token = self.context.context.session.token.token

        newCtx = ctx.TercenContext(
                            authToken= token, 
                            stepId="2ca54ff5-5b7f-44e9-870b-48facabc41ae",
                            workflowId="9b611b90f412969d6f617f559f005bc6")

        assert(not newCtx is None)
        assert(isinstance( newCtx, ctx.TercenContext ) )
    



if __name__ == '__main__':
    unittest.main()
