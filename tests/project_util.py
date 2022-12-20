import os
import sys
sys.path.insert(0, os.path.abspath('/home/thiago/Tercen/repos/tercen_python_client'))

import pandas as pd



from tercen.client.factory import TercenClient
from tercen.model.base import *


import uuid, random, string
import tercen.util.helper_functions as utl
import tercen.util.builder as bld

        
wkfBuilder = bld.WorkflowBuilder()
wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
wkfBuilder.add_table_step( './tests/data/hospitals.csv' )
# wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
#                         columns=[{"name":"Rating.Timeliness", "type":"string"},
#                         {"name":"Facility.State", "type":"string"}])

wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                        xAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                        columns=[{"name":"Rating.Timeliness", "type":"string"},
                        {"name":"Facility.State", "type":"string"}],
                        rows=[{"name":"Rating.Timeliness", "type":"string"},
                        {"name":"Facility.State", "type":"string"}],
                        labels=[{"name":"Facility.State", "type":"string"}],
                        colors=[{"name":"Rating.Mortality", "type":"string"}])


#prevStep:int, columns:list=None, rows:list=None,
#                labels:list=None, errors:list=None, colors:list=None,
#                yAxis:dict=None, xAxis:dict=None

# wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                        # columns=[{"name":"Rating.Timeliness", "type":"string"}])

# wkfBuilder.clean_up_workflow()











# # client = TercenClient("http://127.0.0.1:5402/")
# # session = client.userService.connect('test', 'test')

# # projects = client.projectService.findByIsPublicAndLastModifiedDate('2000', None)
# # for p in projects:
# #     print(p.name)






# steps = []
# tableStep = TableStep()
# tableStep.id = uuid.uuid4().__str__()
# tableStep.name = 'hospitals.csv'

# tableStep.inputs = []

# outPort = OutputPort()
# outPort.linkType = 'relation'
# outPort.name = 'data'
# outPort.id = ''.join( [tableStep.id, '-o-0'] )

# tableStep.outputs = [outPort]

# tableStepModel = TableStepModel()


# rel_id = csvTask.schemaId
# renameRel = RenameRelation()
# renameRel.inNames = ['Facility.Name', 'Facility.City', 'Facility.State', 'Facility.Type', 'Rating.Overall', 'Rating.Mortality', 'Rating.Safety', 'Rating.Readmission', 'Rating.Experience', 'Rating.Effectiveness', 'Rating.Timeliness', 'Rating.Imaging', 'Procedure.Heart Attack.Cost', 'Procedure.Heart Attack.Quality', 'Procedure.Heart Attack.Value', 'Procedure.Heart Failure.Cost', 'Procedure.Heart Failure.Quality', 'Procedure.Heart Failure.Value', 'Procedure.Pneumonia.Cost', 'Procedure.Pneumonia.Quality', 'Procedure.Pneumonia.Value', 'Procedure.Hip Knee.Cost', 'Procedure.Hip Knee.Quality', 'Procedure.Hip Knee.Value', ''.join([rel_id, '._rids']), ''.join([rel_id, '.tlbId']) ]
# renameRel.outNames = ['Facility.Name', 'Facility.City', 'Facility.State', 'Facility.Type', 'Rating.Overall', 'Rating.Mortality', 'Rating.Safety', 'Rating.Readmission', 'Rating.Experience', 'Rating.Effectiveness', 'Rating.Timeliness', 'Rating.Imaging', 'Procedure.Heart Attack.Cost', 'Procedure.Heart Attack.Quality', 'Procedure.Heart Attack.Value', 'Procedure.Heart Failure.Cost', 'Procedure.Heart Failure.Quality', 'Procedure.Heart Failure.Value', 'Procedure.Pneumonia.Cost', 'Procedure.Pneumonia.Quality', 'Procedure.Pneumonia.Value', 'Procedure.Hip Knee.Cost', 'Procedure.Hip Knee.Quality', 'Procedure.Hip Knee.Value', 'rowId', 'tableId']
# renameRel.id = 'rename_' + rel_id

# simpleRel = SimpleRelation()
# simpleRel.id = rel_id

# renameRel.relation = simpleRel


# tableStepModel.relation = renameRel # or simpleRel
# tableStep.model = tableStepModel

# stepSt = StepState()
# stepSt.taskState = DoneState()
# tableStep.state = stepSt



# steps.append( tableStep )
# wkf.steps = steps
# wkf.projectId = proj.id
# wkf.acl.owner = proj.acl.owner
# wkf.name = 'auto_context_test'

# wkfCreated = client.workflowService.create(wkf)

# # Cube query task for the dataStep
# csvSchema = client.tableSchemaService.get(csvTask.schemaId)

# # utl.table_to_pandas(client.tableSchemaService.select(csvTask.schemaId, ['Procedure.Hip Knee.Value'], 0, 4772))
# #csvSchema.columns[0].toJson()
# cbTask = RunComputationTask()

# cpuSharePair = Pair()
# cpuSharePair.key = 'cpu-shares'
# cpuSharePair.value = '128'

# cpuPair = Pair()
# cpuPair.key = 'cpu'
# cpuPair.value = '1'

# ramPair = Pair()
# ramPair.key = 'ram'
# ramPair.value = '101088360'
# cbTask.environment = [cpuSharePair, cpuPair, ramPair]

# cbQuery = CubeQuery()
# cbQuery.relation = utl.as_relation(csvSchema)

# col = Factor()
# col.name = 'Rating.Imaging'
# col.type = 'string'
# cbQuery.colColumns = [col]


# col = Factor()
# col.name = 'Rating.Effectiveness'
# col.type = 'string'
# cbQuery.rowColumns = [col]

# clr = Factor()
# clr.name = 'Facility.Type'
# clr.type = 'string'



# lbl = Factor()
# lbl.name = 'Facility.Name'
# lbl.type = 'string'
# cbQuery.rowColumns = [col]






# axisQuery = CubeAxisQuery()
# axisQuery.yAxis.name = 'Procedure.Hip Knee.Cost'
# axisQuery.yAxis.type = 'double'
# axisQuery.labels = [lbl]
# axisQuery.colors = [clr]
# cbQuery.axisQueries = [axisQuery]


# cbTask.query = CubeQuery()
# cbTask.schemaIds = [csvSchema.id]
# cbTask.projectId = proj.id
# cbTask.owner = proj.acl.owner

# cbTask.state = InitState()
# # cbTask.toJson()
# cbTask2 = client.taskService.create( cbTask )
# # cbTask2.toJson()
# client.taskService.runTask(cbTask2.id)
# cbTaskRan = client.taskService.waitDone(cbTask2.id)

# # cbTaskRan.toJson()



# #client.tableSchemaService.get(cbTaskRan.schemaIds[3]).toJson()


# dataStep = DataStep()
# dataStep.name = 'OperatorStep'
# dataStep.id = uuid.uuid4().__str__()

# # compRelation = Relation()
# # compRelation.id = '' #cbTaskRan.computedRelation.id
# # dataStep.computedRelation = compRelation

# # Port ID -> Step id + -i-N & -o-N (N: 0-n, the connection index). These are used in the link property of the workflow.
# inPort = InputPort()
# inPort.linkType = 'relation'
# inPort.name = 'data'
# inPort.id = ''.join( [dataStep.id, '-i-0'] ) #'2ca54ff5-5b7f-44e9-870b-48facabc41ae-i-0' 


# outPort = OutputPort()
# outPort.linkType = 'relation'
# outPort.name = 'data'
# outPort.id =  ''.join( [dataStep.id, '-o-0'] )

# stpState = StepState()
# stpState.taskId = ''
# stpState.taskState = InitState()

# dataStep.state = stpState

# model = Crosstab()
# model.taskId = cbTaskRan.id # Same as xyAxis, but where does it come from?


# axisList = XYAxisList()
# xyAxis = XYAxis()
# chartPoint = ChartPoint()
# chartPoint.pointSize = 4
# xyAxis.chart = chartPoint
# xyAxis.taskId = cbTaskRan.id


# yAxis = Axis()
# fac = Factor()
# fac.name = 'Procedure.Hip Knee.Cost'
# fac.type = 'double'
# gFac = GraphicalFactor()
# gFac.factor = fac

# rec = Rectangle()
# ext = Point()
# ext.x = 0
# ext.y = 0
# tl = Point()
# tl.x = 0
# tl.y = 0
# rec.extent = ext
# rec.topLeft = tl
# gFac.rectangle = rec

# yAxis.graphicalFactor = gFac

# axSet = AxisSettings()
# axSet.properties = []
# axSet.propertyValues = []
# yAxis.axisSettings = axSet

# ae = Point()
# ae.x = 80
# ae.y = 30
# yAxis.axisExtent = ae


# xAxis = Axis()
# fac = Factor()
# fac.name = ''
# fac.type = 'string'
# gFac = GraphicalFactor()
# gFac.factor = fac
# xAxis.graphicalFactor = gFac
# xAxis.axisExtent = ae


# xAxis.axisSettings = axSet


# clrs = Colors()
# cFac = Factor()
# cFac.name = 'Facility.Type'
# cFac.type = 'string'
# clrs.factors = [cFac]

# palette = CategoryPalette()
# palette.backcolor = 0
# palette.colorList = ColorList()
# palette.properties = []

# clrs.palette = palette

# lbls = Labels()
# lFac = Factor()
# lFac.name = 'Facility.Name'
# lFac.type = 'string'
# lbls.factors = [lFac]

# xyAxis.yAxis = yAxis
# xyAxis.xAxis = xAxis
# xyAxis.colors = clrs
# xyAxis.labels = lbls



# axisList.xyAxis = [xyAxis]

# fltrs = Filters()
# fltrs.removeNaN = True

# model.axis = axisList
# model.filters = fltrs


# columnTbl = CrosstabTable()
# columnTbl.cellSize = 162.25
# columnTbl.offset = 0

# fac = Factor()
# fac.name = 'Rating.Imaging'
# fac.type = 'string'
# gFac = GraphicalFactor()
# gFac.factor = fac

# rec = Rectangle()
# ext = Point()
# ext.x = 0
# ext.y = 30
# tl = Point()
# tl.x = 0
# tl.y = 0
# rec.extent = ext
# rec.topLeft = tl
# gFac.rectangle = rec

# columnTbl.graphicalFactors = [gFac]
# columnTbl.nRows = 4 # FIXME Needs to be programmaticaly obtained

# rowTbl = CrosstabTable()
# rowTbl.cellSize = 140
# rowTbl.offset = 0

# fac = Factor()
# fac.name = 'Rating.Effectiveness'
# fac.type = 'string'
# gFac = GraphicalFactor()
# gFac.factor = fac

# rec = Rectangle()
# ext = Point()
# ext.x = 80
# ext.y = 0
# tl = Point()
# tl.x = 0
# tl.y = 0
# rec.extent = ext
# rec.topLeft = tl
# gFac.rectangle = rec

# rowTbl.graphicalFactors = [gFac]
# rowTbl.nRows = 4 # FIXME Needs to be programmaticaly obtained

# model.columnTable = columnTbl
# model.rowTable = rowTbl

# dataStep.model = model
# dataStep.inputs = [inPort]
# dataStep.outputs = [outPort]

# dataStep.model.operatorSettings.namespace = 'ds1'


# if len(wkfCreated.steps) == 3:
#     wkfCreated.steps.pop()

# wkfCreated.steps.append(dataStep)


# link01 = Link()
# link01.inputId = dataStep.inputs[0].id
# link01.outputId = tableStep.outputs[0].id

# wkfCreated.links = [link01]

# client.workflowService.update(wkfCreated)


# client = TercenClient("http://127.0.0.1:5402/")
# session = client.userService.connect('test', 'test')

# w = client.workflowService.get('f064b90b6e615d70a448fae4880213f6')
# ds = w.steps[1]
# ds.toJson()