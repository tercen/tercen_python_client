import pandas as pd
import multiprocessing, sys

import random, string
from tercen.model.base import OperatorResult, FileDocument, ComputationTask, InitState 
from tercen.model.base import RunComputationTask, FailedState, Pair, TaskLogEvent, TaskProgressEvent, SimpleRelation, Relation
from tercen.model.base import JoinOperator, InMemoryRelation, CompositeRelation, WhereRelation, RenameRelation, UnionRelation
from tercen.client.factory import TercenClient
from tercen.util import helper_functions as utl
from tercen.http.HttpClientService import encodeTSON


class TercenContext:
    def __init__(self, workflowId = None, stepId = None, username = 'test', password = 'test',
     authToken = None, taskId = None, serviceUri = "http://127.0.0.1:5400/"):
        
        args = self.parse_args()

        
        if not args["taskId"] is None:
            taskId = args["taskId"]

        if not args["token"] is None:
            authToken = args["token"]

        if not args["serviceUri"] is None:
            serviceUri = args["serviceUri"]


        
        if taskId == None:
            self.context = OperatorContextDev(workflowId=workflowId,
                    stepId=stepId, authToken=authToken, username=username, password=password,
                    serviceUri=serviceUri)
        else:
            self.context = OperatorContext( authToken=authToken,
                    username=username, password=password, taskId=taskId, serviceUri=serviceUri )

    
    

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
    
    def save( self, df ) -> None:
        self.context.save(df)

    def save_dev( self, df ) -> pd.DataFrame:
        return self.context.save(df)


    def save_relation_dev(self, object) -> None:
        result = self.__save_relation(object)
        return self.save_dev(result)

    def save_relation( self, object ) -> None:
        result = self.__save_relation(object)
        self.save(result)
        

    def __save_relation( self, object ) -> Relation:
        self.tables = []
        if issubclass(object.__class__, JoinOperator):
            joins = [object]
        elif issubclass(object.__class__, list):
            check = [issubclass(o.__class__, JoinOperator) for o in object ]
            if not all( check):
                raise 'ctx.save_relation -- a list of JoinOperator is required'
            joins = object
        else:
            raise 'ctx.save_relation -- a single or list of JoinOperator is required'

        self.tables = []
        
        for i in range(0,len(joins)):
            joins[i].rightRelation = self.__convert_inmemory_relation(joins[i].rightRelation)
            
        result = OperatorResult()
        result.tables = self.tables
        result.joinOperators = joins

        return(result)


    def __inmemory_to_simple_relation(self, inmemory) -> SimpleRelation:
        relation = SimpleRelation()
        relation.id = inmemory.inMemoryTable.properties.name
        self.tables.append(inmemory.inMemoryTable)
        return relation


    def __convert_inmemory_relation(self, relation):
        if issubclass(relation.__class__, SimpleRelation):
            return relation
        elif issubclass(relation.__class__, InMemoryRelation):
            # implement inmemory to simple
            return(self.__inmemory_to_simple_relation(relation))
        elif issubclass(relation.__class__, CompositeRelation):
            rel = relation.mainRelation
            if issubclass(rel.__class__, InMemoryRelation):
                relation.mainRelation = self.__inmemory_to_simple_relation(rel)
            else:
                self.__convert_inmemory_relation(rel)

            for jop in relation.joinOperators:
                rel = jop.rightRelation

                if issubclass(rel.__class__, InMemoryRelation):
                    jop.rightRelation = self.__inmemory_to_simple_relation(rel)
                else:
                    self.__convert_inmemory_relation(rel)
        elif issubclass(relation.__class__, WhereRelation) or issubclass(relation.__class__, RenameRelation):
            rel = relation.relation
            if issubclass(relation.__class__, InMemoryRelation):
                relation.relation = self.__inmemory_to_simple_relation(rel)
            else:
                self.__convert_inmemory_relation(rel)
        elif  issubclass(relation.__class__, UnionRelation):
            relation.relations = []
            for r in relation.relations:
                if issubclass(relation.__class__, InMemoryRelation):
                    relation.relations.append( self.__inmemory_to_simple_relation(r) )
                else:
                    self.__convert_inmemory_relation(r)
                    relation.relations.append(r)
        else:
            raise 'convert.inmemory.relation -- not impl'

        return relation

 


    def select(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.schema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.schema.columns, where) ]

        df = pd.DataFrame()

        if self.context.schema.nRows <= 1600000:
            if( self.context.isPairwise ):
                res = self.context.client.tableSchemaService.selectPairwise(  self.context.schema.id, names, offset, nr)
            else:
                res = self.context.client.tableSchemaService.select(  self.context.schema.id, names, offset, nr)
            

            for c in res.columns:
                df[c.name] = c.values
        else:
            offset = 0
            nr = 1500000
            chunkSize = nr
            hasMoreChunks = True

            while hasMoreChunks:
                if (offset + nr) > self.context.schema.nRows:
                    hasMoreChunks = False

                    nr = self.context.schema.nRows - offset 

                if( self.context.isPairwise ):
                    res = self.context.client.tableSchemaService.selectPairwise(  self.context.schema.id, names, offset, nr)
                else:
                    res = self.context.client.tableSchemaService.select(  self.context.schema.id, names, offset, nr)

                chunkDf = pd.DataFrame()
                for c in res.columns:
                    chunkDf[c.name] = c.values

                if offset == 0:
                    df = chunkDf
                else:
                    df = pd.concat([df, chunkDf], ignore_index=True)
                
                offset = offset + chunkSize 




        return df

    def cselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.cschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.cschema.columns, where) ]

        df = pd.DataFrame()

        if self.context.cschema.nRows <= 1600000:
            res = self.context.client.tableSchemaService.select(  self.context.cschema.id, names, offset, nr)

            for c in res.columns:
                df[c.name] = c.values
        else:
            offset = 0
            nr = 1500000
            chunkSize = nr
            hasMoreChunks = True

            while hasMoreChunks:
                if (offset + nr) > self.context.cschema.nRows:
                    hasMoreChunks = False

                    nr = self.context.cschema.nRows - offset 

                res = self.context.client.tableSchemaService.select(  self.context.cschema.id, names, offset, nr)

                chunkDf = pd.DataFrame()
                for c in res.columns:
                    chunkDf[c.name] = c.values

                if offset == 0:
                    df = chunkDf
                else:
                    df = pd.concat([df, chunkDf], ignore_index=True)
                
                offset = offset + chunkSize 

        
        return df

    def rselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.context.rschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.context.rschema.columns, where) ]

        df = pd.DataFrame()

        if self.context.rschema.nRows <= 1600000:
            res = self.context.client.tableSchemaService.select(  self.context.rschema.id, names, offset, nr)

            for c in res.columns:
                df[c.name] = c.values
        else:
            offset = 0
            nr = 1500000
            chunkSize = nr
            hasMoreChunks = True

            while hasMoreChunks:
                if (offset + nr) > self.context.rschema.nRows:
                    hasMoreChunks = False

                    nr = self.context.rschema.nRows - offset 

                res = self.context.client.tableSchemaService.select(  self.context.rschema.id, names, offset, nr)

                chunkDf = pd.DataFrame()
                for c in res.columns:
                    chunkDf[c.name] = c.values

                if offset == 0:
                    df = chunkDf
                else:
                    df = pd.concat([df, chunkDf], ignore_index=True)
                
                offset = offset + chunkSize

        
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
            self.client.httpClient.authorization = authToken


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

    def save(self, df ) -> Relation:
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
            self.client.fileService.upload(fileDoc, resultBytes)

        return None

        

class OperatorContextDev(TercenContext):
    def __init__(self, workflowId = None, stepId = None, authToken = None, username = None, password = None,
                         serviceUri  = None):
        self.client = TercenClient(serviceUri)
        if authToken is None:
            self.session = self.client.userService.connect(username, password)
            self.client.userService.tercenClient.token = self.session.token.token
            
        else:
            self.client.userService.tercenClient.token = authToken
            self.client.httpClient.authorization = authToken

        self.workflowId = workflowId
        #TODO FIXME Check why the cubequery here and the one retrieved from the task are different
        # self.cubeQuery = self.client.workflowService.getCubeQuery(workflowId, stepId)
        wkf = self.client.workflowService.get(workflowId)
        
        stp = None
        for s in wkf.steps:
            if s.id == stepId:
                stp = s
                break

        if stp is None:
            raise "Step not found"
        task = self.client.taskService.get(stp.model.taskId)
        self.cubeQuery  = task.query

        self.schema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )
        self.cschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )
        self.rschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )

        hasCSchema = False
        hasRSchema = False

        if len(self.schema) > 0:
            self.schema = self.schema[0]
        if len(self.cschema) > 0:
            self.cschema = self.cschema[0]
            hasCSchema = True
        if len(self.rschema) > 0:
            self.rschema = self.rschema[0]
            hasRSchema = True

        # self.schema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )[0]
        # self.cschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )[0]
        # self.rschema = self.client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )[0]

        self.names = [col.name for col in self.schema.columns] 
        if hasCSchema:
            self.cnames = [col.name for col in self.cschema.columns] 
        else:
            self.cnames = []

        if hasRSchema:
            self.rnames = [col.name for col in self.rschema.columns] 
        else:
            self.rnames = []

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

        self.isPairwise = self.cnames != [''] and self.rnames != [''] and len(set(self.cnames).intersection( set(self.rnames) )) > 0

        self.task = None

        self.namespace = self.cubeQuery.operatorSettings.namespace

        if self.namespace == '':
            letters = string.ascii_uppercase
            self.namespace = 'ds_' + ''.join(random.choice(letters) for i in range(2)) 
            



    def __select(self, schema, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in schema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( schema.columns, where) ]

        if( self.isPairwise ):
            res = self.client.tableSchemaService.selectPairwise(  schema.id, names, offset, nr)
        else:
            res = self.client.tableSchemaService.select(  schema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        return df

    # For development testing, returns the resulting table
    def save( self, df ) -> pd.DataFrame:
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

        #ts = self.client.tableSchemaService.get(task.computedRelation.joinOperators[0].rightRelation.relation.mainRelation.id)
        cr = task.computedRelation
        if cr.joinOperators[0].rightRelation.__class__ == SimpleRelation:
            ts = self.client.tableSchemaService.get(cr.joinOperators[0].rightRelation.id)

        else:
            ts = self.client.tableSchemaService.get(task.computedRelation.joinOperators[0].rightRelation.relation.mainRelation.id)

        
        dff = self.__select(ts, '')
        cols = dff.columns
        if not ".ci" in cols:
            dff.insert(0, '.ci', 0)
        if not ".ri" in cols:
            dff.insert(1, '.ri', 0)

        return dff
