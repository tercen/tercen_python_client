import unittest
import os 
import sys
sys.path.append('./')

from tercen.client import context as ctx
import tercen.util.builder as bld
import tercen.util.helper_functions as utl
import pandas as pd

import numpy.testing as npt


if __name__ == '__main__':
    print( "Running Workflow tests")

    isLocal = True
    username = 'test'
    passw = 'test'
    conf = {}
    with open("./tests/env.conf") as f:
        for line in f:
            if len(line.strip()) > 0:
                (key, val) = line.split(sep="=")
                conf[str(key)] = str(val).strip()

    serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])

    # FIXME Not working with integer factors. 
    df = pd.DataFrame(data={"colFactor":["1", "1", "2", "2"],
                    "rowFactor":["R1", "R2", "R1", "R2"],
                    "measurement":[12, 0.7, -4, 33]})
    
    # df = df.astype({'colFactor':'int'})

    wkfBuilder = bld.WorkflowBuilder(username=username, password=passw, serviceUri=serviceUri)
    
    
    # print(wkfBuilder.client.documentService.getTercenOperatorLibrary(0,10))
    wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')

    wkfBuilder.add_table_step( df )
    # wkfBuilder.add_data_step(yAxis={"name":"measurement", "type":"double"}, linkTo="tableStep")
    wkfBuilder.add_data_step(name="DataStep1",
                            yAxis={"name":"measurement", "type":"double", "step":"tableStep"}, 
                            columns=[{"name":"colFactor", "type":"string", "step":"tableStep"}],
                             linkTo="tableStep",
                             operator={"name":"Mean", "version":"1.2.0", "url":"https://github.com/tercen/mean_operator"})
    
    wkfBuilder.add_data_step(name="DataStep2",
                            yAxis={"name":"ds0.mean", "type":"double", "step":"DataStep1"}, 
                            columns=[{"name":"colFactor", "type":"string", "step":"tableStep"}],
                             linkTo="DataStep1",
                             operator=None)

    
    wkfBuilder.clean_up_workflow()
