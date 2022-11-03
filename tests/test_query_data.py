import unittest
import numpy as np
import pandas as pd
from tercen.client.factory import TercenClient
from tercen.model.base import Project


class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://172.42.0.42:5400/")
        self.client.userService.connect('test', 'test')

        self.data = self.create_data()

        #=================================================
        # Create project
        # Note, unit test for project creation is run elsewhere (test_project)
        obj = Project()
        obj.name = 'python_project'
        obj.acl.owner = 'test'
        self.project = self.client.projectService.create(obj)
        #=================================================


    def tearDown(self) -> None:
        self.client.teamService.delete(self.project.id, self.project.rev)


        return super().tearDown()

    def create_data(self):
        num_vars = 3
        num_obs = 15
        num_replicates = 1

        total_vals   = num_vars * num_obs * num_replicates
        
        var_vals    = ['var{}'.format( v+1 ) for v in range(0,num_vars) for v1 in range(0, num_obs) for v2 in range(0, num_replicates)]
        obs_vals    = ['obs{}'.format( v+1 ) for v1 in range(0,num_vars) for v in range(0, num_obs)  for v2 in range(0, num_replicates)]

        data = pd.DataFrame( data={
            "Observation": obs_vals,
            "Variable": var_vals,
            "Measurement": np.random.rand( total_vals)
        } )

        return data

    def test_create_data_task(self) -> None:
        assert(False)

    def test_select(self):
        assert(False)

    def test_select_column(self):
        assert(False)

    def test_select_row(self):
        assert(False)



if __name__ == '__main__':
    unittest.main()
