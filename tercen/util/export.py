import gzip
from tercen.model.impl import FileDocument, CSVTask, InitState
from tercen.util.helper_functions import dataframe_to_table

import pickle

def export_to_project_as_csv(context, df, fname, projectId, folderId, user, workflowFolder=True ):
    fname = "{}.csv".format(fname)


    context.log("Exporting {}: Writing temp file".format(fname))


    file = FileDocument()
    file.name = fname.split("/")[-1]
    file.acl.owner = user 
    file.projectId = projectId
    
    file.folderId = folderId
    file.metadata.contentEncoding = "application/octet-stream"

    context.log("Exporting {}: Uploading".format(fname))
    fileDoc = context.context.client.fileService.uploadTable(file, \
                                dataframe_to_table(df, values_as_list=True)[0].toJson())
    


    task = CSVTask()
    task.state = InitState()
    
    task.fileDocumentId =  fileDoc.id
    task.projectId = projectId
    task.owner = user

    task = context.client.taskService.create( task )
    context.client.taskService.runTask(task.id)
    taskDone = context.client.taskService.waitDone(task.id)

    if workflowFolder == True:
        # Move to correct folder
        sch = context.client.tableSchemaService.get(taskDone.schemaId)
        sch.folderId = folderId
        context.client.tableSchemaService.update(sch)

    return df

def export_obj_pickle_to_project(context, data, fname, \
        projectId, folderId, user, compression=1, fileExt="gz",\
        inplace=True):
    
    fname = "{}.{}".format(fname, fileExt)


    context.log("Exporting {}: Writing temp file".format(fname))
    with gzip.open(fname, 'wb', compresslevel=compression) as f:
        pickle.dump(data, f)
    
    del data
    data = []

    file = FileDocument()
    file.name = fname.split("/")[-1]
    file.acl.owner = user 
    file.projectId = projectId
    
    file.folderId = folderId
    file.metadata.contentEncoding = "gzip"

    with open(fname, 'rb') as f:
            bytes_data =  f.read()

    context.log("Exporting {}: Uploading".format(fname))
    context.client.fileService.uploadFromFile(file, bytes_data)
    
    if inplace == True:
        return data
    else:
        return None

