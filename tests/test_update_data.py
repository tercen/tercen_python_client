import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd

from tercen.client.factory import TercenClient
from tercen.client import context as ctx




class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5402/")
        self.session = self.client.userService.connect('test', 'test')
        

    def test_save(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/6c049ac3-ea23-44ec-a236-9b863cf9b6cc
        tercenCtx = ctx.TercenContext( self.client, self.session, "9b611b90f412969d6f617f559f005bc6",
                    "6c049ac3-ea23-44ec-a236-9b863cf9b6cc")

        df = tercenCtx.select(['.y', '.ci', '.ri'])
        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop('.y', axis=1)

        df = tercenCtx.add_namespace(df) 
        tercenCtx.save(df)


if __name__ == '__main__':
    unittest.main()
