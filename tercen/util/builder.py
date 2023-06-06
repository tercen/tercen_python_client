import os
import sys
sys.path.insert(0, os.path.abspath('../'))

import pandas as pd

from tercen.client.factory import TercenClient
from tercen.model.base import *

import numpy as np

import uuid, random, string
import tercen.util.helper_functions as utl


# TODO Add support for multiple links between steps
# TODO Only supports TableStep -> DataStep Workflows (no multiple steps)
# TODO Does not support installing and running operators
class WorkflowBuilder():
    def __init__(self, username='test', password='test', serviceUri="http://127.0.0.1:5400/"):
        self.client = TercenClient(serviceUri)
        self.session = self.client.userService.connect(     username, password)

        self.user = username

        self.steps = {}
        self.schemas = {}
        self.cbQueries = {}
        self.namespaceCount = 0


    def __randomString(self, nChar=6):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(nChar)) 

    def create_workflow(self, projectName=None, workflowName = None):
        if projectName is None:
            projectName = ''.joint(['python_project_', self.__randomString(4)])

        if workflowName is None:
            workflowName = ''.joint(['python_workflow_', self.__randomString(4)])

        start_key = ["test", False, "2035"]
        end_key = ["test", False, ""]
        projects = self.client.projectService.findByTeamAndIsPublicAndLastModifiedDate(start_key, end_key)

        self.proj = None
        for p in projects:
            if p.name == projectName:
                self.proj = p
                break

        
        if not self.proj is None:
            self.client.projectService.delete(self.proj.id, self.proj.rev)

        proj = Project()
        
        proj.name = 'python_auto_project'
        proj.acl.owner = self.user
        self.proj = self.client.projectService.create(proj)


        self.workflow = None
        wkfObjs = self.client.persistentService.findByKind(['Workflow'], useFactory=True)
        for w in wkfObjs:
            wkf = self.client.workflowService.get(w.id)
            
            if self.proj.id == wkf.projectId and wkf.name == workflowName:
                self.workflow = wkf
                break

        if not self.workflow is None:
            self.client.workflowService.delete(self.workflow.id, self.workflow.rev)

        self.workflow = Workflow()
        self.workflow.steps = []
        self.workflow.projectId = self.proj.id
        self.workflow.acl.owner = self.proj.acl.owner
        self.workflow.name = workflowName

        self.workflow = self.client.workflowService.create(self.workflow)


    # By default, if a number is not x.x, pandas converts it to int, which might not be desirable
    # Thus, int columns need to be manually specified through the int_columns parameter
    def add_table_step(self, data, int_columns=None):
        if data is None:
            raise "data parameter is empty"
        if isinstance( data, str ):
            df = pd.read_csv(os.path.abspath(data))
        elif isinstance( data, pd.DataFrame ):
            df = data
        else:
            raise "data must either be a file path or a pandas DataFrame"

       
        # However, it might be necessary to alter this behavior
        colNames = list(df)

        for n in colNames:
            if (not int_columns is None) and  n in int_columns:
                df = df.astype({n: np.int32})
            elif isinstance( df[n].values.tolist()[0], int):
                df = df.astype({n: np.double})


        fileDoc = FileDocument()
        fileDoc.name = "data.csv"
        fileDoc.projectId = self.proj.id
        fileDoc.acl.owner = self.proj.acl.owner
        fileDoc.metadata.contentEncoding = "application/octet-stream"

        self.fileDoc = self.client.fileService.uploadTable(fileDoc, utl.pandas_to_table(df, values_as_list=True).toJson() )

        task = CSVTask()
        task.state = InitState()
        
        task.fileDocumentId =  self.fileDoc.id
        task.projectId = self.proj.id
        task.owner = self.proj.acl.owner

        task = self.client.taskService.create( task )
        self.client.taskService.runTask(task.id)
        self.csvTask = self.client.taskService.waitDone(task.id)

        csvSchema = self.client.tableSchemaService.get(self.csvTask.schemaId)
        self.schemas["tableStep"]  = csvSchema

        tableStep = TableStep()
        
        rec = Rectangle()
        ext = Point()
        ext.x = 0
        ext.y = 0
        tl = Point()
        tl.x = 0
        tl.y = 0
        rec.extent = ext
        rec.topLeft = tl
        tableStep.rectangle = rec
        tableStep.id = uuid.uuid4().__str__()
        tableStep.name = 'data.csv'

        tableStep.inputs = []
        tableStep.outputs = [self.__create_port( tableStep.id, type='out')]

        tableStepModel = TableStepModel()


        rel_id = self.csvTask.schemaId
        renameRel = RenameRelation()

        inNames = colNames.copy()
        inNames.append(''.join([rel_id, '._rids']))
        inNames.append(''.join([rel_id, '.tlbId']))

        outNames = colNames.copy()
        outNames.append('rowId')
        outNames.append('tableId')

        renameRel.inNames = inNames
        renameRel.outNames = outNames
        renameRel.id = 'rename_' + rel_id

        simpleRel = SimpleRelation()
        simpleRel.id = rel_id

        renameRel.relation = simpleRel

        tableStepModel.relation = renameRel 
        tableStep.model = tableStepModel

        stepSt = StepState()
        stepSt.taskState = DoneState() # Marks the little square on the step green, though it might not be necessary
        tableStep.state = stepSt

        nSteps = len(self.workflow.steps)
        self.workflow.steps.append(tableStep)
        # self.workflow.steps[nSteps]  =  tableStep 


        self.steps["tableStep"] = tableStep
        self.client.workflowService.update(self.workflow)


        tableTask = CubeQueryTask()
        tableTask.query = CubeQuery()
        tableTask.schemaIds = [csvSchema.id]
        tableTask.projectId = self.proj.id
        tableTask.owner = self.proj.acl.owner

        tableTask.state = InitState()
        tableTask = self.client.taskService.create( tableTask )
        
        # self.client.taskService.runTask(tableTask.id)
        self.tableStepTask = tableTask
        # self.tableStepTask = self.client.taskService.waitDone(tableTask.id)

        # Return the index of the step
        # Return name of the step
        # return "tableStep" #len(self.workflow.steps)-1


    def add_data_step(self, name=None, columns:list=None, rows:list=None,
                labels:list=None, errors:list=None, colors:list=None,
                yAxis:dict=None, xAxis:dict=None, linkTo:str=None, 
                operator:dict=None) -> None:
        if linkTo is None:
            linkTo = 'tableStep'

        if yAxis is None:
            raise 'y-axis is mandatory'

        if name is None:
            name = ''.join(['Data_Step_', self.__randomString(2)])

        dataStep = DataStep()
        dataStep.name = name
        dataStep.id = uuid.uuid4().__str__()

        dataStep.outputs = [self.__create_port( dataStep.id, type='out')]
        dataStep.inputs = [self.__create_port( dataStep.id, type='in')]

        stpState = StepState()
        stpState.taskState = InitState()

        dataStep.state = stpState
        dataStep.model = self.__add_crosstab_model(stepName=name, yAxis=yAxis, xAxis=xAxis,
                            columns=columns, rows=rows, labels=labels, errors=errors,
                             colors=colors, prevStep=linkTo)


        dataStep.model.operatorSettings.namespace = ''.join(['ds', str(self.namespaceCount)]) 
        self.namespaceCount = self.namespaceCount + 1

        # Add operator to step
        if not operator is None:
            opKeys = list(operator.keys())
            if not (np.any([k == 'name' for k in opKeys]) and np.any([k == 'version' for k in opKeys]) and np.any([k == 'url' for k in opKeys])):
                raise Exception("Operator parameter must be a dict with name, version and url")
                
            opObj = self.get_operator(opName=operator["name"], opGit=operator["url"], opVersion=operator["version"])

            dataStep.model.operatorSettings.operatorRef.operatorId = opObj.id
            # dataStep.model.operatorSettings.operatorRef.operatorKind = opObj.__class__
            dataStep.model.operatorSettings.operatorRef.operatorName = opObj.name
            dataStep.model.operatorSettings.operatorRef.operatorVersion = opObj.version

        

        link = Link()
        # FIXME Only considering the first input and output here
        # A better solution might be to create the output for each step here, as needed
        link.inputId = dataStep.inputs[0].id

        stpId = self.steps[linkTo].id
        matchList = ([s.id == stpId for s in self.workflow.steps])
        
        linkIdx = [i for i, x in enumerate(matchList) if x]
        linkIdx = linkIdx[0]
        
        link.outputId = self.workflow.steps[linkIdx].outputs[0].id

        self.workflow.steps.append( dataStep )
        self.workflow.links.append(link)

        self.client.workflowService.update(self.workflow)

        self.steps[name] = dataStep

        if not operator is None:
            task = self.run_computation_task(dataStepName=name, prevStep=linkTo)
            self.cbQueries[name] = task.query
            self.schemas[name] = task.computedRelation




    def __install_operator(self, opGit, opName, opVersion, gitToken) -> None:

        # Retrieve list of available operators and try to install the desired one
        opList = self.client.documentService.getTercenOperatorLibrary(0,10)
        if opList is None:
            opList = []

        matchList = [p.name ==  opName for p in  opList]
        opIdx = [i for i, x in enumerate(matchList) if x]

        # Operator not found, must install it
        if (not np.any(matchList)) or (len(opIdx) == 0):
            print(''.join( ('Operator ', opGit, '@', opVersion, ' not installed. Going to install.'    ) ))
            installTask = CreateGitOperatorTask()
            installTask.state = InitState()
            installTask.url.uri = opGit
            installTask.version = opVersion
            installTask.isDeleted = False
            installTask.testRequired = False
            # installTask.gitToken = gitToken
            installTask.owner = self.user

            installTask = self.client.taskService.create(installTask)
            self.client.taskService.runTask(installTask.id)
            installTask = self.client.taskService.waitDone(installTask.id)
            print('Operator installed succesfully')
            return self.client.operatorService.get(installTask.operatorId)
        else:
            print(''.join( ('Operator ', opGit, '@', opVersion, ' is installed.'    ) ))
            return opList[opIdx]


    def get_operator(self, opName, opGit, opVersion, gitToken=''):
        # Check if operator is installed 
        installedOps = self.client.documentService.findOperatorByOwnerLastModifiedDate(self.user, '')

        isInstalled = True
        opId = ''.join((opName, '@', opVersion))
        matchList = [''.join((p.name, '@', p.version)) == opId  for p in  installedOps]
        if not np.any(matchList):
            isInstalled = False
        else:
            opIdx = [i for i, x in enumerate(matchList) if x]
            if len(opIdx) == 0:
                isInstalled = False

        if not isInstalled:
            operator = self.__install_operator(opName=opName, opVersion=opVersion, opGit=opGit, gitToken='')
        else:
            operator = installedOps[opIdx[0]]
        
        return operator


    def __create_graphical_factor(self, facName: str, facType: str) -> GraphicalFactor:
        # ax = Axis()
        fac = Factor()
        fac.name = facName
        fac.type = facType

        gFac = GraphicalFactor()

        gFac.factor = fac
        #TODO These Graphical properties might not be needed, TEST!
        rec = Rectangle()
        ext = Point()
        ext.x = 0
        ext.y = 0
        tl = Point()
        tl.x = 0
        tl.y = 0
        rec.extent = ext
        rec.topLeft = tl
        gFac.rectangle = rec

        return gFac

    def __create_port(self, stepId, type='in') -> Port:
        if type == 'in':
            port = InputPort()
            t = '-i'
        else:
            port = OutputPort()
            t = '-o'
        port.linkType = 'relation'
        port.name = 'data'

        stepId = ''.join([stepId, t])

        if not hasattr(self, 'linkMap'):
            self.linkMap = {}

        if not stepId in self.linkMap:
            newLink =  ''.join( [stepId, '-0'] ) 
            self.linkMap[stepId] = 1
        else:
            nLinks = self.linkMap[stepId]
            newLink =  ''.join( [stepId, '-', nLinks] ) 
            nLinks += 1

            updMap = {stepId:nLinks}

            self.linkMap.update(updMap)


    
        port.id = newLink
        return port



    def __create_empty_graph_fac(self, x=80, y=30) -> GraphicalFactor:
        gFac = GraphicalFactor()

        rec = Rectangle()
        ext = Point()
        ext.x = x
        ext.y = y
        tl = Point()
        tl.x = 0
        tl.y = 0
        rec.extent = ext
        rec.topLeft = tl
        gFac.rectangle = rec
        
        return gFac

    def __add_row_col_projection(self, cols:list=None, schema:SchemaBase=None):
        ctTbl = CrosstabTable()
        ctTbl.cellSize = 140
        ctTbl.offset = 0

        
        if cols is None or len(cols) == 0:
            # fac.name = 'Rating.Effectiveness'
            fac = Factor()
            fac.name = ''
            fac.type = 'string'
            gFac = self.__create_empty_graph_fac()
            # gFac.factor = fac
            # ctTbl.graphicalFactors = [gFac]
        else:
            gFacVec = []

            for i,d in enumerate(cols):
                fac = Factor()
                fac.name = d["name"]
                fac.type = d["type"]

                gFac = self.__create_empty_graph_fac()
                gFac.factor = fac

                gFacVec.append(gFac)

            ctTbl.graphicalFactors = gFacVec


        return ctTbl

    def __factors_from_graphical(self, graphicalFactors:list) -> list:
        facs = []
        for gFac in graphicalFactors:
            facs.append(gFac.factor)
        return facs
    
    def run_computation_task(self, dataStepName, prevStep:str):
                     # TASK Definition
        
        dataStep = self.steps[dataStepName]
        crosstabModel = dataStep.model
        cbTask = RunComputationTask()
        xyAxis = crosstabModel.axis.xyAxis[0]

        cbQuery = CubeQuery()

        schema = self.schemas[prevStep]
        cbQuery.relation = utl.as_relation(schema)

        axisQuery = CubeAxisQuery()

        colTbl = crosstabModel.columnTable

        colFacs = []
        for gf in colTbl.graphicalFactors:
            colFacs.append(gf.factor)
        
        cbQuery.colColumns = colFacs

        yAx = xyAxis.yAxis.graphicalFactor.factor
        xAx = xyAxis.xAxis.graphicalFactor.factor

        if yAx.name != '':
            axisQuery.yAxis.name = yAx.name
            axisQuery.yAxis.type = yAx.type

        if not xAx is None and xAx.name != '':
            axisQuery.xAxis.name = xAx.name
            axisQuery.xAxis.type = xAx.type
        
        axisQuery.labels = xyAxis.labels.factors
        axisQuery.colors = xyAxis.colors.factors
        axisQuery.errors = xyAxis.errors.factors
        
        cbQuery.axisQueries = [axisQuery]
        # Factor list
      
        cbQuery.colColumns = self.__factors_from_graphical(crosstabModel.columnTable.graphicalFactors)
        cbQuery.rowColumns = self.__factors_from_graphical(crosstabModel.rowTable.graphicalFactors)

        cbQuery.operatorSettings = crosstabModel.operatorSettings

        cbTask.query = cbQuery
        cbTask.schemaIds = [schema.id]
        cbTask.projectId = self.proj.id
        cbTask.owner = self.proj.acl.owner

        cbTask.state = InitState()
        cbTask = self.client.taskService.create( cbTask )
        self.client.taskService.runTask(cbTask.id)
        cbTask = self.client.taskService.waitDone(cbTask.id)
        

        return cbTask
        
    
    def __run_cube_query_task(self, crosstabModel, prevStep:str):
        # FIXME Change to cubequery task, possibly
        cbTask = CubeQueryTask() #RunComputationTask()
        xyAxis = crosstabModel.axis.xyAxis[0]

        cbQuery = CubeQuery()

        schema = self.schemas[prevStep]
        cbQuery.relation = utl.as_relation(schema)

        axisQuery = CubeAxisQuery()

        colTbl = crosstabModel.columnTable

        colFacs = []
        for gf in colTbl.graphicalFactors:
            colFacs.append(gf.factor)
        
        cbQuery.colColumns = colFacs

        yAx = xyAxis.yAxis.graphicalFactor.factor
        xAx = xyAxis.xAxis.graphicalFactor.factor

        if yAx.name != '':
            axisQuery.yAxis.name = yAx.name
            axisQuery.yAxis.type = yAx.type

        if not xAx is None and xAx.name != '':
            axisQuery.xAxis.name = xAx.name
            axisQuery.xAxis.type = xAx.type
        
        axisQuery.labels = xyAxis.labels.factors
        axisQuery.colors = xyAxis.colors.factors
        axisQuery.errors = xyAxis.errors.factors
        
        cbQuery.axisQueries = [axisQuery]
        # Factor list
      
        cbQuery.colColumns = self.__factors_from_graphical(crosstabModel.columnTable.graphicalFactors)
        cbQuery.rowColumns = self.__factors_from_graphical(crosstabModel.rowTable.graphicalFactors)

        cbTask.query = cbQuery
        cbTask.schemaIds = [schema.id]
        cbTask.projectId = self.proj.id
        cbTask.owner = self.proj.acl.owner

        cbTask.state = InitState()
        cbTask = self.client.taskService.create( cbTask )
        self.client.taskService.runTask(cbTask.id)
        cbTask = self.client.taskService.waitDone(cbTask.id)
        
        
        return cbTask
        

    def __add_crosstab_model(self, stepName:str, prevStep:str, columns:list=None, rows:list=None,
                labels:list=None, errors:list=None, colors:list=None,
                yAxis:dict=None, xAxis:dict=None ) -> Crosstab:
        model = Crosstab()
        # model.taskId =  ''#self.tableStepTask.id 

        axisList = XYAxisList()
        xyAxis = XYAxis()
        # TODO Check if needed
        chartPoint = ChartPoint()
        chartPoint.pointSize = 4
        xyAxis.chart = chartPoint
        # xyAxis.taskId = '' #model.taskId

        yAx = Axis()
        yAx.graphicalFactor = self.__create_graphical_factor(yAxis["name"], yAxis["type"])

        xAx = Axis()
        if xAxis is None:
            xAx.graphicalFactor = self.__create_graphical_factor("", "string")
        else:    
            xAx.graphicalFactor = self.__create_graphical_factor(xAxis["name"], xAxis["type"])

        axSet = AxisSettings()
        axSet.properties = []
        axSet.propertyValues = []
        
        ae = Point()
        ae.x = 80
        ae.y = 30

        yAx.axisSettings = axSet
        yAx.axisExtent = ae

        xAx.axisSettings = axSet
        xAx.axisExtent = ae


        xyAxis.yAxis = yAx
        xyAxis.xAxis = xAx
        
        model.columnTable = self.__add_row_col_projection(columns, schema=self.schemas[prevStep])
        model.rowTable = self.__add_row_col_projection(rows, schema=self.schemas[prevStep])
        axisList.xyAxis = [xyAxis]

        # ADDING Label factos
        if not labels is None and len(labels) > 0:
            lbls = Labels()
            lblFacs = []
            for l in labels:
                fac = Factor()
                fac.name = l["name"]
                fac.type = l["type"]
                lblFacs.append(fac)
            
            lbls.factors = lblFacs
            xyAxis.labels = lbls

        # ADDING Color factors
        clrs = Colors()

        palette = CategoryPalette()
        palette.backcolor = 0
        palette.colorList = ColorList()
        palette.properties = []

        clrs.palette = palette


        
        if not colors is None and len(colors) > 0:
            clFacs = []
            for c in colors:
                f = Factor()
                f.name = c["name"]
                f.type = c["type"]
                clFacs.append(f)
            clrs.factors = clFacs

            
        xyAxis.colors = clrs

        # ADDING Error factors
        if not errors is None and len(errors) > 0:
            err = Errors()
            
            eFacs = []
            for e in errors:
                f = Factor()
                f.name = e["name"]
                f.type = e["type"]
                eFacs.append(e)
            err.factors = eFacs

            xyAxis.errors = err
            

        # TODO Add support to filters
        fltrs = Filters()
        fltrs.removeNaN = True
        
        
        model.axis = axisList
        model.filters = fltrs

        # TODO get the cubequery from this function and store it elsewhere, so it is easier to run
        cbTask = self.__run_cube_query_task(model, prevStep)
        cbTaskId = cbTask.id

        self.cbQueries[stepName] = cbTask.query

        model.taskId = cbTaskId 
        model.axis.xyAxis[0].taskId = cbTaskId

        return model


    def clean_up_workflow(self):
        self.client.workflowService.delete(self.workflow.id, self.workflow.rev)
        self.client.fileService.delete(self.fileDoc.id, self.fileDoc.rev)
        self.client.projectService.delete(self.proj.id, self.proj.rev)


