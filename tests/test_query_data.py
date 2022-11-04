import unittest
import numpy as np
import numpy.testing as npt
import pandas as pd
import tempfile, string, random, os, sys
import zlib

import json
import pytson as ptson
import tercen.util.http_utils as utl
from tercen.client.factory import TercenClient
from tercen.model.base import Project, FileDocument, Table





class TestTercen(unittest.TestCase):
    def setUp(self):
        self.client = TercenClient("http://172.42.0.42:5400/")
        self.client.userService.connect('test', 'test')

        self.data = self.create_data()

        # Create project
        # Note: unit test for project creation is run elsewhere (test_project)
        obj = Project()
        obj.name = 'python_project'
        obj.acl.owner = 'test'
        self.project = self.client.projectService.create(obj)


    def tearDown(self):
        self.client.fileService.delete(self.fileDoc.id, self.fileDoc.rev)
        self.client.teamService.delete(self.project.id, self.project.rev)

    def create_data(self):
        numVars = 3
        numObs = 15
        numReplicates = 1

        totalVals   = numVars * numObs * numReplicates
        varVals    = ['var{}'.format( v+1 ) for v in range(0,numVars) for v1 in range(0, numObs) for v2 in range(0, numReplicates)]
        obsVals    = ['obs{}'.format( v+1 ) for v1 in range(0,numVars) for v in range(0, numObs)  for v2 in range(0, numReplicates)]

        data = pd.DataFrame( data={
            "Observation": obsVals,
            "Variable": varVals,
            "Measurement": np.random.rand( totalVals)
        } )

        return data


    def df_to_bytes(self, df):
        nDigits = 10
        fName = tempfile.gettempdir().join('/')
        fName.join(random.choices(string.ascii_uppercase + string.digits, k=nDigits))

        tbl = utl.pandas_to_table( df )
        tblBytes = zlib.compress( str.encode( json.dumps(tbl.toJson())) )

        return tblBytes

    def test_transfer_file_document(self) -> None:
        df = self.create_data()
        dfBytes = self.df_to_bytes(df)

        self.fileDoc = FileDocument()
        self.fileDoc.name = "input_datatable"
        self.fileDoc.projectId = self.project.id
        self.fileDoc.acl.owner = self.project.acl.owner
        self.fileDoc.metadata.contentEncoding = "gzip"

        self.fileDoc = self.client.fileService.upload(self.fileDoc, dfBytes)

        dwnFileDoc = self.client.fileService.get( self.fileDoc.id )
        

        fileDownloaded = self.client.fileService.download( self.fileDoc.id )
        dwnDf = utl.table_bytes_to_pandas(fileDownloaded)

        assert(  dwnFileDoc.id == self.fileDoc.id )
        npt.assert_array_equal( df.iloc[:,0], dwnDf.iloc[:,0] )
        npt.assert_array_equal( df.iloc[:,1], dwnDf.iloc[:,1] )
        npt.assert_array_equal( df.iloc[:,2], dwnDf.iloc[:,2] )
        
  
    def test_csv_task(self) -> None:
        # TODO Port python equivalent
        # task = CSVTask$new()
        # task$state = InitState$new()
        # task$fileDocumentId = fileDoc$id
        # task$owner = project$acl$owner
        # task$projectId = project$id
        
        # task = client$taskService$create(task)
        # client$taskService$runTask(task$id)
        # task = client$taskService$waitDone(task$id)
        # if (inherits(task$state, 'FailedState')){
        #   stop(task$state$reason)
        # }
        
        
        # table_schema = client$tableSchemaService$get(task$schemaId)
        # client$tableSchemaService$update(table_schema)
        #assert(False)
        assert(False)

    def test_select(self):
        assert(False)

    def test_select_column(self):
        assert(False)

    def test_select_row(self):
        assert(False)



if __name__ == '__main__':
    unittest.main()
