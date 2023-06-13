import unittest
import os 
import sys
sys.path.append('./')

#FIXME No need for all here
from tercen.model.base import *
from tercen.client import context as ctx
import tercen.util.builder as bld
import tercen.util.helper_functions as utl
import pandas as pd

import numpy.testing as npt

def __factors_from_graphical(graphicalFactors:list) -> list:
    facs = []
    for gFac in graphicalFactors:
        facs.append(gFac.factor)
    return facs

def __create_cube_query_task( crosstabModel, computedRelation, projId, projOwner):
    cbTask = CubeQueryTask() 
    xyAxis = crosstabModel.axis.xyAxis[0]

    cbQuery = CubeQuery()
    cbQuery.relation = computedRelation

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
    
    cbQuery.colColumns = __factors_from_graphical(crosstabModel.columnTable.graphicalFactors)
    # cbQuery.rowColumns = __factors_from_graphical(crosstabModel.rowTable.graphicalFactors)

    cbTask.query = cbQuery
    # cbTask.schemaIds = [schema.id]
    cbTask.projectId = projId
    cbTask.owner = projOwner
    
    return cbTask


def __get_schema_id(computedRelation, client):
    # cr = task.computedRelation
    if computedRelation.joinOperators[0].rightRelation.__class__ == SimpleRelation:
        ts = client.tableSchemaService.get(computedRelation.joinOperators[0].rightRelation.id)

    else:
        ts = client.tableSchemaService.get(computedRelation.joinOperators[0].rightRelation.relation.mainRelation.id)

    return ts.id

if __name__ == '__main__':
    print( "Running Workflow tests")

    isLocal = True
    username = 'test'
    passw = 'test'
    conf = {}

    absPath = os.path.dirname(os.path.abspath(__file__))
    confFilepath = os.path.join(absPath, 'env.conf')
    with open(confFilepath) as f:
        for line in f:
            if len(line.strip()) > 0:
                (key, val) = line.split(sep="=")
                conf[str(key)] = str(val).strip()

    serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])

    #http://127.0.0.1:5402/test/w/be55b66517bf9e5663a68bac18002d65/

    # Unable to create context from a tableStep which has not yet been run
    context = ctx.TercenContext(
                username=username,
                password=passw,
                serviceUri=serviceUri,
                workflowId="be55b66517bf9e5663a68bac18002d65")
    
    stepList = context.context.workflowId
    wkf = context.context.client.workflowService.get(context.context.workflowId)
    stepList = wkf.steps

    tableStep = wkf.steps[0]
    tableStepSchema = context.context.client.tableSchemaService.get(tableStep.model.relation.relation.id)
    step = stepList[1]
    # for step in stepList:
    for i in range(1, len(stepList)):
        step = wkf.steps[i]
        if i > 1:
            ur = UnionRelation()
            schemaIds =[tableStepSchema.id]
            ur.relations = [tableStep.model.relation.relation]
            for j in range(i-1, 0, -1):
                schemaId = __get_schema_id( wkf.steps[j].computedRelation, context.context.client )
                schemaIds.append(schemaId)

                ur.relations.append(wkf.steps[j].computedRelation)
            
            cbTask = __create_cube_query_task(step.model, step.computedRelation, wkf.projectId,  wkf.acl.owner)
            cbTask.state = InitState()
            cbTask.schemaIds = schemaIds
            cbTask.query.relation = ur
            cbTask = context.context.client.taskService.create( cbTask )
            context.context.client.taskService.runTask(cbTask.id)
            cbTask = context.context.client.taskService.waitDone(cbTask.id)
            
            # step.state.taskState = InitState()
            step.state.taskId = cbTask.id
            wkf.steps[i] = step

            context.context.client.workflowService.update(wkf)
        cubeQuery =  context.context.client.workflowService.getCubeQuery(wkf.id, step.id)

        task = RunComputationTask()
        task.query = cubeQuery
        task.state = InitState()
        task.projectId = wkf.projectId
        task.owner = wkf.acl.owner  
        
        task = context.context.client.taskService.create(task) 
        context.context.client.taskService.runTask(task.id)
        task = context.context.client.taskService.waitDone(task.id)

        step.computedRelation = task.computedRelation
        step.state.taskId = task.id
        step.state.taskState = task.state
        # step.state = DoneState()
        wkf.steps[i] = step

        context.context.client.workflowService.update(wkf)



