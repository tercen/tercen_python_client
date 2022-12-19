import os
import sys
# sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('/home/thiago/Tercen/repos/tercen_python_client'))


import pandas as pd

from tercen.client.factory import TercenClient
from tercen.model.base import *


import uuid, random, string
import tercen.util.helper_functions as utl


# TODO Add support for multiple links between steps
class WorkflowBuilder():
    def __init__(self, username='test', password='test', serviceUri="http://127.0.0.1:5402/"):
        self.client = TercenClient(serviceUri)
        self.session = self.client.userService.connect(     username, password)

        self.user = username

        self.steps = []
        self.schemas = []
        self.namespaceCount = 0


    def __randomString(self, nChar=6):
        letters = string.ascii_uppercase
        return ''.join(random.choice(letters) for i in range(nChar)) 

    def create_workflow(self, projectName=None, workflowName = None):
        if projectName is None:
            projectName = ''.joint(['python_project_', self.__randomString(4)])

        if workflowName is None:
            workflowName = ''.joint(['python_workflow_', self.__randomString(4)])

        projects = self.client.projectService.findByIsPublicAndLastModifiedDate('2000', None)

        self.proj = None
        for p in projects:
            if p.name == projectName:
                self.proj = p
                break

        if self.proj is None:
            # Create project
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

        if self.workflow is None:
            self.workflow = Workflow()
            self.workflow.steps = []
            self.workflow.projectId = self.proj.id
            self.workflow.acl.owner = self.proj.acl.owner
            self.workflow.name = workflowName

            self.workflow = self.client.workflowService.create(self.workflow)



    def add_table_step(self, data) -> int:
        if data is None:
            raise "data parameter is empty"
        if isinstance( data, str ):
            df = pd.read_csv(os.path.abspath(data))
        elif isinstance( data, pd.DataFrame ):
            df = data
        else:
            raise "data must either be a file path or a pandas DataFrame"

        # Converts everything to float
        # By default, if a number is not x.x, pandas converts it to int, which might not be desirable
        # However, it might be necessary to alter this behavior
        colNames = list(df)

        for n in colNames:
            if isinstance( df[n].values.tolist()[0], int):
                df = df.astype({n: float})

        dfBytes = utl.pandas_to_bytes(df)

        fileDoc = FileDocument()
        fileDoc.name = "data.csv"
        fileDoc.projectId = self.proj.id
        fileDoc.acl.owner = self.proj.acl.owner
        fileDoc.metadata.contentEncoding = "gzip"

        self.fileDoc = self.client.fileService.upload(fileDoc, dfBytes)

        task = CSVTask()
        task.state = InitState()
        task.fileDocumentId = self.fileDoc.id
        task.projectId = self.proj.id
        task.owner = self.proj.acl.owner

        task = self.client.taskService.create( task )
        self.client.taskService.runTask(task.id)
        self.csvTask = self.client.taskService.waitDone(task.id)

        csvSchema = self.client.tableSchemaService.get(self.csvTask.schemaId)
        self.schemas.append(csvSchema)

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

        self.workflow.steps.append( tableStep )



        self.client.workflowService.update(self.workflow)

        tableTask = CubeQueryTask()
        tableTask.query = CubeQuery()
        tableTask.schemaIds = [csvSchema.id]
        tableTask.projectId = self.proj.id
        tableTask.owner = self.proj.acl.owner

        tableTask.state = InitState()
        tableTask = self.client.taskService.create( tableTask )
        self.client.taskService.runTask(tableTask.id)

        self.tableStepTask = self.client.taskService.waitDone(tableTask.id)

        # Return the index of the step
        return len(self.workflow.steps)-1


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


    def __get_row_number(self, names, yAxisName, schema) -> int:
        colIdx = []
        df = pd.DataFrame()
        for i, c in enumerate(schema.columns):
            if c.name in names:
                res = self.context.client.tableSchemaService.select(  schema.id, c.name, 0, schema.columns[i].nRows)
                df2 = pd.DataFrame()

                for c in res.columns:
                    df2[c.name] = c.values



        if len(colIdx) == 0:
            raise "Columns not found"


        

        
        return 0

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
            gFac.factor = fac
            ctTbl.graphicalFactors = [gFac]
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


        # TODO Does it need to be set?
        # ctTbl.nRows = 4 # FIXME Needs to be programmaticaly obtained
        return ctTbl

    def __run_cube_query_task(self, crosstabModel, prevStep:int):
        # FIXME Change to cubequery task, possibly
        cbTask = RunComputationTask()
        xyAxis = crosstabModel.axis.xyAxis[0]

        cbQuery = CubeQuery()
        # FIXME This should be obtained from previous step

        schema = self.schemas[prevStep]
        cbQuery.relation = utl.as_relation(schema)

        axisQuery = CubeAxisQuery()

        colTbl = crosstabModel.columnTable

        colFacs = []
        for gf in colTbl.graphicalFactors:
            colFacs.append(gf.factor)
        
        cbQuery.colColumns = colFacs

        # TODO create and run cubequery task. This ID will be added to the model!!
        # xyAxis.yAxis = yAx
        # xyAxis.xAxis = xAx
        # xyAxis.colors = clrs
        yAx = xyAxis.yAxis.graphicalFactor.factor
        xAx = xyAxis.xAxis.graphicalFactor.factor

        if yAx.name != '':
            axisQuery.yAxis.name = yAx.name
            axisQuery.yAxis.type = yAx.type
        
        cbQuery.axisQueries = [axisQuery]

        cbTask.query = CubeQuery() #cbQuery
        cbTask.schemaIds = [schema.id]
        cbTask.projectId = self.proj.id
        cbTask.owner = self.proj.acl.owner

        cbTask.state = InitState()
        cbTask = self.client.taskService.create( cbTask )
        self.client.taskService.runTask(cbTask.id)
        self.cbTask = self.client.taskService.waitDone(cbTask.id)
        

    def __add_crosstab_model(self, prevStep:int, columns:list=None, rows:list=None,
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
        

        #TODO Add names and types
        # olumns:list=None, rows:list=None,
        #         labels:list=None, errors:list=None, colors:
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

        cbTaskId = self.__run_cube_query_task(model, prevStep)

        model.taskId = cbTaskId
        model.axis.xyAxis[0].taskId = cbTaskId

        return model


    def clean_up_workflow(self):
        self.client.workflowService.delete(self.workflow.id, self.workflow.rev)
        self.client.fileService.delete(self.fileDoc.id, self.fileDoc.rev)
        self.client.projectService.delete(self.proj.id, self.proj.rev)


    def add_data_step(self, name=None, columns:list=None, rows:list=None,
                labels:list=None, errors:list=None, colors:list=None,
                yAxis:dict=None, xAxis:dict=None, linkTo:int=None) -> None:
        if linkTo is None:
            linkTo = len(self.workflow.steps)-1
        else:
            linkTo = linkTo - 1


        if yAxis is None:
            raise 'y-axis is mandatory'

        if name is None:
            stepName = ''.join(['Data_Step_', self.__randomString(2)])

        dataStep = DataStep()
        dataStep.name = 'OperatorStep'
        dataStep.id = uuid.uuid4().__str__()

        dataStep.outputs = [self.__create_port( dataStep.id, type='out')]
        dataStep.inputs = [self.__create_port( dataStep.id, type='in')]

        stpState = StepState()
        stpState.taskState = InitState()

        dataStep.state = stpState
        dataStep.model = self.__add_crosstab_model(yAxis=yAxis, xAxis=xAxis,
                            columns=columns, rows=rows, labels=labels, errors=errors,
                             colors=colors, prevStep=linkTo)


        self.__run_cube_query_task(dataStep.model, prevStep=linkTo)

        dataStep.model.operatorSettings.namespace = ''.join(['ds', str(self.namespaceCount)]) 
        self.namespaceCount = self.namespaceCount + 1
        



        link = Link()
        # FIXME Only considering the first input and output here
        # A better solution might be to create the output for each step here, as needed
        link.inputId = dataStep.inputs[0].id
        link.outputId = self.workflow.steps[linkTo].outputs[0].id

        self.workflow.steps.append( dataStep )
        self.workflow.links.append(link)

        self.client.workflowService.update(self.workflow)
