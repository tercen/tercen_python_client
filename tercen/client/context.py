import pandas as pd
import multiprocessing, sys

from tercen.model.base import OperatorResult, FileDocument, ComputationTask, InitState 
from tercen.model.base import RunComputationTask, FailedState, Pair, TaskLogEvent, TaskProgressEvent
from tercen.client.factory import TercenClient
from tercen.util import helper_functions as utl
from tercen.http.HttpClientService import encodeTSON


class TercenContext:
    def __init__(self, workflowId = None, stepId = None, username = 'test', password = 'test',
     authToken = None, taskId = None, serviceUri = "http://127.0.0.1:5402/"):
        
        args = self.parse_args()

        
        if not args["taskId"] is None:
            taskId = args["taskId"]

        if not args["token"] is None:
            authToken = args["token"]

        if not args["serviceUri"] is None:
            serviceUri = args["serviceUri"]

        if taskId == None:
            self.context = OperatorContextDev(workflowId, stepId, 
                        authToken, username, password, serviceUri)
        else:
            self.context = OperatorContext( authToken, username, password, taskId , serviceUri  )
        

    def parse_args(self) -> dict:
        taskId = None
        serviceUri = None
        token = None

        args = sys.argv
        nArgs = len(args)
        
        for i in range(1, nArgs):
            arg = args[i]
            
            if str.startswith(arg, '--'):
                #argParts = str.split(arg, ' ')
                argName = str.removeprefix(arg, '--')

                if argName == 'taskId':
                    taskId = args[i+1]
                
                if argName == 'serviceUri':
                    serviceUri = args[i+1]
                
                if argName == 'token':
                    token = args[i+1]

        return {'taskId':taskId, 
                'serviceUri':serviceUri, 
                'token':token}

    def select(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.schema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.schema.columns, where) ]

        if( self.context.isPairwise ):
            res = self.context.client.tableSchemaService.selectPairwise(  self.context.schema.id, names, offset, nr)
        else:
            res = self.context.client.tableSchemaService.select(  self.context.schema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        return df

    def cselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.cschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.cschema.columns, where) ]

        res = self.context.client.tableSchemaService.select(  self.context.cschema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def rselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.rschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.rschema.columns, where) ]

        res = self.context.client.tableSchemaService.select(  self.context.rschema.id, names, offset, nr)

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

        df.columns = [ addPrefix(c, self.context.namespace) for c in colnames ]

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
        workflow = self.context.client.workflowService.get( self.context.workflowId )
        fileDoc.projectId = workflow.projectId
        fileDoc.acl.owner = workflow.acl.owner
        fileDoc.metadata.contentType = 'application/octet-stream'

        fileDoc = self.context.client.fileService.upload( fileDoc, resultBytes )

        task = None 
        if task is None:
            print("task is null, create a task")
            if self.context.session.serverVersion is None:
                task = ComputationTask()
            else:
                task = RunComputationTask()

            task.state = InitState()
            task.owner = workflow.acl.owner
            task.projectId = workflow.projectId
            task.query = self.context.cubeQuery
            task.fileResultId = fileDoc.id
            task = self.context.client.taskService.create(task)
        else:
            task.fileResultId = fileDoc.id
            rev = self.context.client.taskService.update(task)
            task.rev = rev

        self.context.client.taskService.runTask( task.id )
        task = self.context.client.taskService.waitDone( task.id )

        if issubclass(task.state.__class__, FailedState):
            raise task.state.reason

    def request_resources(self, nCpus = None, ram=None, ramPerCpu=None) -> list:
        newEnv = []

        if not nCpus is None:
            newPair = Pair()
            newPair.key = 'cpu'
            newPair.value = str(nCpus)

            newEnv.append( newPair)

        if not ram is None:
            newPair = Pair()
            newPair.key = 'ram'
            newPair.value = str(ram)

            newEnv.append( newPair)

        if not ramPerCpu is None:
            newPair = Pair()
            newPair.key = 'ram_per_cpu'
            newPair.value = str(ramPerCpu)

            newEnv.append( newPair)

        if not self.context.taskId is None:
            newEnv = self.context.client.workerService.updateTaskEnv( self.context.taskId, newEnv )

        return newEnv

    def log(self, message) -> None:
        task = self.context.task

        if not task is None:
            evt = TaskLogEvent()
            evt.message = message
            evt.taskId = task.id

            self.context.client.eventService.sendChannel( task.channelId, evt )

    def progress( self, message, actual, total):
        task = self.context.task

        if not task is None:
            evt = TaskProgressEvent()
            evt.message = message
            evt.taskId = task.id
            evt.actual = actual
            evt.total = total

            self.context.client.eventService.sendChannel( task.channelId, evt )


class OperatorContext(TercenContext):
    def __init__(self, authToken, username, password, serviceUri, taskId):
        self.client = TercenClient(serviceUri)
        # self$userService$client$token = self$session$token$token
        if authToken is None:
            self.session = self.client.userService.connect(username, password)
            self.client.userService.tercenClient.token = self.session.token.token
        else:
            self.client.userService.tercenClient.token = authToken

        self.client.userService.client.token = self.session.token.token

        self.task = self.client.taskService.get( taskId )


        self.cubeQuery = self.task.query


        self.schema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )[0]
        self.cschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )[0]
        self.rschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )[0]

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

        

        self.namespace = self.cubeQuery.operatorSettings.namespace

    def save(self, df ) -> None:
        if issubclass(df.__class__, OperatorResult):
            result = df
        else:
            result = OperatorResult()

            if isinstance(df, list):
                result.tables = [ utl.pandas_to_table(t) for t in df ]
            else:
                result.tables = [utl.pandas_to_table(df)]
        
        
        resultBytes = encodeTSON( result.toJson() ) 



        if( len(self.task.fileResultId) == 0 ):
            #Webapp scenario
            fileDoc = FileDocument()
            fileDoc.name = 'result'

            fileDoc.projectId = self.context.task.projectId
            fileDoc.acl.owner = self.context.task.acl.owner
            fileDoc.metadata.contentType = 'application/octet-stream'

            fileDoc = self.context.client.fileService.upload( fileDoc, resultBytes )

            self.task.fileResultId = fileDoc.id
            self.task.rev = self.client.taskService.update(self.task)
            self.task = self.client.taskService.waitDone(self.task.id)

            if issubclass(self.task.state, FailedState):
                raise self.task.state.reason

        else:
            fileDoc = self.client.fileService.get(self.task.fileResultId)
            self.client.fileService.upload(fileDoc, bytes)

        

class OperatorContextDev(TercenContext):
    def __init__(self, workflowId = None, stepId = None, authToken = None, username = None, password = None,
                         serviceUri  = None):
        self.client = TercenClient(serviceUri)
        if authToken is None:
            self.session = self.client.userService.connect(username, password)
            self.client.userService.tercenClient.token = self.session.token.token
        else:
            self.client.userService.tercenClient.token = authToken

        self.workflowId = workflowId

        self.cubeQuery = self.client.workflowService.getCubeQuery(workflowId, stepId)

        self.schema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )[0]
        self.cschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )[0]
        self.rschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )[0]

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

        self.task = None

        self.namespace = self.cubeQuery.operatorSettings.namespace
