import unittest

from tercen.client.factory import TercenClient
from tercen.client import context as ctx



# FAILING HERE!
# Run this test and find out what is going on
class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://127.0.0.1:5402/")
        self.session = self.client.userService.connect('test', 'test')
        

    def test_save(self) -> None:
        # http://127.0.0.1:5402/test/w/9b611b90f412969d6f617f559f005bc6/ds/2ca54ff5-5b7f-44e9-870b-48facabc41ae
        
        tercenCtx = ctx.TercenContext( "9b611b90f412969d6f617f559f005bc6",
                    "2ca54ff5-5b7f-44e9-870b-48facabc41ae")

        df = tercenCtx.select(['.y', '.ci', '.ri'])
        df['y2'] = df['.y'] * 2
        df['y'] = df['.y']
        df = df.drop('.y', axis=1)

        df = tercenCtx.add_namespace(df) 
        tercenCtx.save(df)


if __name__ == '__main__':
    unittest.main()
