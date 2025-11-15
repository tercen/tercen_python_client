import base64
import gzip
import hashlib

import pandas as pd
from tercen.client.context import TercenContext
from tercen.model.impl import FileDocument, CSVTask, InitState, Pair, Relation
from tercen.util.helper_functions import dataframe_to_table

import pickle

from tercen.util.io import get_folder_structure


def export_to_project_as_csv(context: TercenContext, df, 
                            rel: Relation, fname: str, projectId: str,
                            user: str, folderId: str = None, timestamp: str = None, exportPrefix: str = "", 
                            workflowId: str = None,
                            meta: list[Pair] = []):
    fname = "{}.csv".format(fname)

    if not timestamp is None:
        if not exportPrefix is None and exportPrefix != "":
            exportPrefix += "_"
        folderPath = get_folder_structure(folderId, context) + "/" + exportPrefix + timestamp
        newFolder = context.context.client.folderService.getOrCreate(projectId, folderPath)
        folderId = newFolder.id


    if folderId is None:
        folderId = ""

    context.log("Exporting {}: Writing temp file".format(fname))

    file = FileDocument()
    file.name = fname.split("/")[-1]
    file.acl.owner = user
    file.projectId = projectId
    file.isDeleted = False
    file.folderId = folderId
    file.metadata.contentType = "application/octet-stream"

    if not workflowId is None:
        file.addMeta("workflow.id", workflowId)

    context.log("Exporting {}: Uploading".format(fname))

    # NOTE: values_as_list=True is required for toJson() - JSON cannot serialize numpy arrays
    fileDoc = context.context.client.fileService.uploadTable(file,
                                                             dataframe_to_table(df, values_as_list=True)[0].toJson())

    task = CSVTask()
    task.state = InitState()

    task.fileDocumentId = fileDoc.id
    task.projectId = projectId
    task.owner = user

    task = context.context.client.taskService.create(task)
    context.context.client.taskService.runTask(task.id)
    taskDone = context.context.client.taskService.waitDone(task.id)

    # Move to correct folder
    sch = context.context.client.tableSchemaService.get(taskDone.schemaId)
    sch.folderId = folderId
    sch.relation = rel

    for m in meta:
        sch.addMeta(m.key, m.value)

    context.context.client.tableSchemaService.update(sch)

    return (sch, df)




def export_df_to_project(context, data, fname,
                                 projectId, folderId, user, compression=1, fileExt="gz",
                                 inplace=True, meta: list[Pair] = [], timestamp = None, exportPrefix=""):

    fname = "{}.{}".format(fname, fileExt)

    if not timestamp is None:
        if not exportPrefix is None and exportPrefix != "":
            exportPrefix += "_"
        folderPath = get_folder_structure(folderId, context) + "/" + exportPrefix + timestamp
        newFolder = context.context.client.folderService.getOrCreate(projectId, folderPath)
        folderId = newFolder.id


    context.log("Exporting {}: Writing temp file".format(fname))
    with gzip.open(fname, 'wb', compresslevel=compression) as f:
        pickle.dump(data, f)

    del data
    data = []

    file = FileDocument()
    file.name = fname.split("/")[-1]
    file.acl.owner = user
    file.projectId = projectId
    file.isDeleted = False
    file.folderId = folderId
    file.metadata.contentEncoding = "gzip"

    for m in meta:
        file.addMeta(m.key, m.value)

    # with open(fname, 'rb') as f:
        # bytes_data = f.read()

    context.log("Exporting {}: Uploading".format(fname))
    file = context.client.fileService.uploadFromFile(file, fname)

    #FIXME This should not be necessary, there is an error elsewhere
    if( file.isDeleted == True ):
        file.isDeleted = False
        context.client.fileService.update(file)


    if inplace == True:
        return (file, data )
    else:
        return (file, None)


def text_to_markdown_df(filename, txt):

    mimetype = "text/markdown"
    txt = txt.replace("[", "**")\
                .replace("]", "**")\
                .replace("\n", "\n\n")

    txtBytes = txt.encode("utf-8")
    checksum = hashlib.md5(txtBytes).hexdigest()

    output_str = [ base64.b64encode(txtBytes) ]


    outs = output_str[0].decode('utf-8')
    txtDf = pd.DataFrame({
        "filename":[filename],
        "mimetype":[mimetype],
        "checksum":[checksum],
        ".content":[outs]
    })

    return txtDf