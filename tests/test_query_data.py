import unittest
import numpy as np
import pandas as pd
from tercen.client.factory import TercenClient


class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://172.42.0.42:5400/")
        self.client.userService.connect('test', 'test')

        self.data = self.create_data()

    def create_data(self):
        num_vars = 3
        num_obs = 2
        num_replicates = 2

        total_vals   = num_vars * num_obs * num_replicates
        
        var_vals    = ['var{}'.format( v+1 ) for v in range(0,num_vars)]
        obs_vals    = ['obs{}'.format( v+1 ) for v in range(0,num_obs) for v1 in range(0, num_vars)]

        # data <- data.frame(Observation = obs_vals, 
        #                     Variable = var_vals, 
        #                     Measurement = runif(total_vals, meas_min_val, meas_max_val))

        return 1

    def test_select(self):
        assert(False)

    def test_select_column(self):
        assert(False)

    def test_select_row(self):
        assert(False)



if __name__ == '__main__':
    unittest.main()
