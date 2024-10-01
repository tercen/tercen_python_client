from tercen.model.impl import \
      InMemoryRelation, FileDocument, \
        CompositeRelation, SimpleRelation,\
        CSVTask, InitState

import tercen.util.helper_functions as utl

import os, tempfile, string, random, base64, hashlib, pickle, gzip, time, sys
import pandas as pd

from http.client import IncompleteRead


def block_stdout():
    sys.stdout = open(os.devnull, 'w')

def enable_stdout():
    sys.stdout = sys.__stdout__

def filter_by_type(vec, type):
    outVec = []
    for o in vec:
        if isinstance(o, type):
            outVec.append(o)

    return outVec

def get_inmemory_relations(relation):
    relations = []

    if isinstance(relation, CompositeRelation):
        rels = get_inmemory_relations(relation.mainRelation)
        [relations.append(r) for r in rels]

        for jo in relation.joinOperators:
            rels = get_inmemory_relations(jo.rightRelation)
            [relations.append(r) for r in rels]

    elif isinstance(relation, InMemoryRelation):
        relations.append(relation)
    elif not isinstance(relation, SimpleRelation):
        rels = get_inmemory_relations(relation.relation)
        [relations.append(r) for r in rels]

    return relations

def get(vec, idxVec):
    newVec = []
    [newVec.append(vec[i]) for i in idxVec]
    return newVec

def where(vec):
    return [i for i, x in enumerate(vec) if x]

def get_document_id(queryRelation, aliasId, colName):
    inMemRels = get_inmemory_relations(queryRelation)

    for rel in inMemRels:
        tbl = rel.inMemoryTable
        
        documentIds = get(tbl.columns, where([c.name == ".documentId" for c in tbl.columns ]))
        # documentAliasIds = get(tbl.columns, where([c.name == "documentId" for c in tbl.columns ]))
        documentAliasIds = get(tbl.columns, where([c.name == colName for c in tbl.columns ]))

        if not documentIds is None and not documentAliasIds is None:
            idx = where([id == aliasId for id in documentAliasIds[0].values ])
            if not idx is None and len(idx) > 0:
                return documentIds[0].values[idx[0]]

    return None

def get_gcs_filepaths(path):
    paths = []
    fs = os.listdir(path)

    for f in os.listdir(path):
        if os.path.isdir(path + "/" + f):
            newPaths = get_gcs_filepaths(path + "/" + f)
            [paths.append(p) for p in newPaths]
        elif f.endswith(".gcs"):
            paths.append(path + "/" + f)

    return paths

def read_in_chunks(file_object, chunk_size=1024 * 1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def filter_by_base_folder(context, objList, baseFolder):
    filteredList = []
    for obj in objList:
        objBaseFolder = get_folder_structure(obj.folderId, context).split("/")[0]
        if objBaseFolder == baseFolder:
            filteredList.append(obj)

    return filteredList
    
def get_data(context, fileDoc):
    maxTries = 10
    downloadTry = 1
    downloadSuccessful = False

    data = None
    while(downloadTry < maxTries):
        try:
            print("Downloading {} [Try {}]".format(fileDoc.name, downloadTry))
            resp = context.context.client.fileService.download(fileDoc.id)


            with gzip.open(resp, 'rb') as gFile:
                data = gFile.read()
                downloadSuccessful = True
                break
        except IncompleteRead:
            print("Download failed. Trying again in 5 seconds.")
            downloadTry += 1
            time.sleep(5)


    if not downloadSuccessful or data is None:
        raise RuntimeError("Failed to download or extract {}".format(fileDoc.name))

    return pickle.loads(data)

def get_folder_structure(folderId, context):
    folderName = ''
    if folderId != '':
        folder = context.context.client.folderService.get(folderId)
        parentName = get_folder_structure(folder.folderId, context) 

        if parentName != "/":
            folderName += parentName + folder.name + "/"
        else:
            folderName += folder.name + "/"
    
    return folderName

def get_filenames_with_folder(fileDocumentList, context ):
    filenames = []
    for fd in fileDocumentList:
        filenames.append(get_folder_structure(fd.folderId, context) + fd.name)

    return filenames



def get_files_document_by_extension(fileDocumentList, ext):
    fileDocuments = []

    for fd in fileDocumentList:
        if fd.name.endswith(ext):
            fileDocuments.append(fd)

    return fileDocuments


def get_file_document_by_name(fileDocumentList, name):
    fileDocument = None

    for fd in fileDocumentList:
        if fd.name == name:
            fileDocument = fd
            break

    return fileDocument


def find_in_dataframe(cols, value):
        
    colNames = cols.columns
    for col in colNames:
        if value in cols.select(col).to_numpy():
            return True
        
    return False


def get_filedoc_by_fullname(fileDocs, fullNameList, context):
    outFileDocs = []
    
    if not isinstance(fullNameList, list):
        fullNameList = [fullNameList]

    for fd in fileDocs:
        fdName = get_folder_structure(fd.folderId, context) + fd.name
        if fdName in fullNameList:
            outFileDocs.append(fd)
        

    if len(outFileDocs) == 1:
        outFileDocs = outFileDocs[0]

    return outFileDocs


def download_filedocs(fileDocs, context, ext="" ):
    savedFilePaths = []
    baseDir = tempfile.gettempdir() + \
              '/' +\
              ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    
    if not os.path.exists(baseDir):
        os.mkdir(baseDir)

    if not isinstance(fileDocs, list):
        fileDocs = [fileDocs]
    for fd in fileDocs:
        fname = baseDir + '/' + \
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) + \
                ext
        resp = context.context.client.fileService.download(fd.id)
        #touch
        f = open(fname, "wb")
        f.close()

        with open(fname, "ab") as file:
            for chunk in read_in_chunks(resp):
                file.write(chunk)

        savedFilePaths.append(fname)

    return savedFilePaths

def text_to_markdown_df(filename, txt):

    mimetype = "text/markdown"
    txt = txt.replace("[", "**")\
                .replace("]", "**")\
                .replace("\n", "\n\n")

    txtBytes = txt.encode("utf-8")

    output_str = [base64.b64encode(txtBytes)]

    outs = output_str[0].decode('utf-8')
    txtDf = pd.DataFrame({
        "filename":[filename],
        "mimetype":[mimetype],
        ".content":[outs]
    })

    return txtDf


def export_to_project_as_csv(context, df, fname, projectId, folderId, user, timestamp=None ):
    fname = "{}.csv".format(fname)

    if not timestamp is None:
        folderPath = get_folder_structure(folderId, context) + "/" + timestamp
        newFolder = context.context.client.folderService.getOrCreate(projectId, folderPath)
        folderId = newFolder.id

    context.log("Exporting {}: Writing temp file".format(fname))


    file = FileDocument()
    file.name = fname.split("/")[-1]
    file.acl.owner = user 
    file.projectId = projectId
    
    file.folderId = folderId
    file.metadata.contentEncoding = "application/octet-stream"

    context.log("Exporting {}: Uploading".format(fname))
    fileDoc = context.context.client.fileService.uploadTable(file, \
                                                              utl.dataframe_to_table(df, values_as_list=True)[0].toJson())
    
    task = CSVTask()
    task.state = InitState()
    
    task.fileDocumentId =  fileDoc.id
    task.projectId = projectId
    task.owner = user

    task = context.context.client.taskService.create( task )
    context.context.client.taskService.runTask(task.id)
    taskDone = context.context.client.taskService.waitDone(task.id)

    # Move to correct folder
    sch = context.context.client.tableSchemaService.get(taskDone.schemaId)
    sch.folderId = folderId
    context.context.client.tableSchemaService.update(sch)

    return df

def export_to_project(context, data, fname, projectId, folderId, user, timestamp=None, compression=1, fileExt="gz"):
    fname = "{}.{}".format(fname, fileExt)

    if not timestamp is None:
        folderPath = get_folder_structure(folderId, context) + "/" + timestamp
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
    
    file.folderId = folderId
    file.metadata.contentEncoding = "gzip"

    context.log("Exporting {}: Uploading".format(fname))
    context.context.client.fileService.uploadFromFile(file, fname)
    

    return data


def append_img_to_df(df, imagePath, pltCi=0):
    if df is None:
        df = utl.image_file_to_df(imagePath)
        df.insert(0, ".ri", int(pltCi))
    else:
        tmpDf = utl.image_file_to_df(imagePath)
        tmpDf.insert(0, ".ri", int(pltCi))
        df = pd.concat([df, tmpDf])
    return df


def pickle_file_to_df(file_path):
    filename = os.path.basename(file_path)
    mimetype = "application/octet-stream"

    output_str = []

    with open(file_path, mode="rb") as f:
        fc = f.read()
        output_str.append([base64.b64encode(fc)])


    o = output_str[0][0]

    outs = o.decode('utf-8')
    pklDf = pd.DataFrame({
        "filename":[filename],
        "mimetype":[mimetype],
        ".content":[outs]
    })

    return pklDf


def string_to_df(txt, filename):
    import hashlib, base64
    mimetype = "text/markdown"

    txtBytes = txt.encode("utf-8")

    output_str = [ base64.b64encode(txtBytes) ]
    outs = output_str[0].decode('utf-8')
    txtDf = pd.DataFrame({
        "filename":[filename],
        "mimetype":[mimetype],
        ".content":[outs],
    })

    return txtDf

