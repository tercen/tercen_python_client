import pandas as pd
import multiprocessing

from tercen.model.base import OperatorResult, FileDocument, ComputationTask, InitState, RunComputationTask, FailedState
from tercen.util import helper_functions as utl
from tercen.http.HttpClientService import encodeTSON




class TercenContext:
    # FIXME client should be obtained from elsewhere
    def __init__(self, client, session, workflowId, stepId, authToken = None, taskId = None):
        self.client = client
        self.workflowId = workflowId
        self.session = session

        self.cubeQuery = client.workflowService.getCubeQuery(workflowId, stepId)

        self.schema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )[0]
        self.cschema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )[0]
        self.rschema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )[0]

        self.names = [col.name for col in self.schema.columns] 
        self.cnames = [col.name for col in self.cschema.columns] 
        self.rnames = [col.name for col in self.rschema.columns] 

        axisQueries = self.cubeQuery.axisQueries

        self.colors = [c.name for q in axisQueries for c in q.colors]
        self.labels = [l.name for q in axisQueries for l in q.labels]
        self.errors = [l.name for q in axisQueries for l in q.errors]
        self.chartType = [q.chartType for q in axisQueries ]
        self.pointSizes = [q.pointSize for q in axisQueries ]

        
        self.yAxis = utl.unique_and_nonempty( [q.yAxis.name for q in axisQueries])
        self.xAxis = utl.unique_and_nonempty( [q.xAxis.name for q in axisQueries])


        self.hasXAxis = any([ col.name == ".x" for col in self.schema.columns ])
        self.hasNumericXAxis = any([ col.name == ".x" and col.type == "double" for col in self.schema.columns ])

        self.isPairwise = len(set(self.cnames).intersection( set(self.rnames) )) > 0

        if not taskId is None:
            self.task = self.client.taskService.get( taskId )
        else:
            self.task = None

        self.namespace = self.cubeQuery.operatorSettings.namespace

    def select(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.schema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.schema.columns, where) ]

        if( self.isPairwise ):
            res = self.client.tableSchemaService.selectPairwise(  self.schema.id, names, offset, nr)
        else:
            res = self.client.tableSchemaService.select(  self.schema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def cselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.cschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.cschema.columns, where) ]

        res = self.client.tableSchemaService.select(  self.cschema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def rselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.rschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.rschema.columns, where) ]

        res = self.client.tableSchemaService.select(  self.rschema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def available_cores(self) -> int:
        return multiprocessing.cpu_count()

    def add_namespace( self, df ) -> pd.DataFrame:
        colnames = df.columns

        def addPrefix(x, ns):
            if not str.startswith(x, "."):
                return ''.join((ns, '.', x))
            else:
                return x
        df.columns = [ addPrefix(c, self.namespace) for c in colnames ]

        return df
    def save( self, df ) -> None:
        if issubclass(df.__class__, OperatorResult):
            result = df
        else:
            result = OperatorResult()

            if isinstance(df, list):
                result.tables = [ utl.pandas_to_table(t) for t in df ]
            else:
                result.tables = [utl.pandas_to_table(df)]
        
        
        resultBytes = encodeTSON( result.toJson() ) 

        fileDoc = FileDocument()
        fileDoc.name = 'result'
        workflow = self.client.workflowService.get( self.workflowId )
        fileDoc.projectId = workflow.projectId
        fileDoc.acl.owner = workflow.acl.owner
        fileDoc.metadata.contentType = 'application/octet-stream'

        fileDoc = self.client.fileService.upload( fileDoc, resultBytes )

        task = None 
        if task is None:
            print("task is null, create a task")
            if self.session.serverVersion is None:
                task = ComputationTask()
            else:
                task = RunComputationTask()

            task.state = InitState()
            task.owner = workflow.acl.owner
            task.projectId = workflow.projectId
            task.query = self.cubeQuery
            task.fileResultId = fileDoc.id
            task = self.client.taskService.create(task)
        else:
            task.fileResultId = fileDoc.id
            rev = self.client.taskService.update(task)
            task.rev = rev

        self.client.taskService.runTask( task.id )
        task = self.client.taskService.waitDone( task.id )

        if issubclass(task.state.__class__, FailedState):
            raise task.state.reason

        

