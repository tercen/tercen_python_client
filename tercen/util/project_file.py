from tercen.client.context import TercenContext
from tercen.model.impl import \
      InMemoryRelation, FileDocument, \
        CompositeRelation, SimpleRelation,\
        CSVTask, InitState

import tercen.util.helper_functions as utl

import os, tempfile, string, random, base64, hashlib, pickle, gzip, time, sys
import pandas as pd

from http.client import IncompleteRead

def get_folder_structure(folderId: str, context: TercenContext) -> str:  
    folderName = ''
    if folderId != '':
        folder = context.context.client.folderService.get(folderId)
        parentName = get_folder_structure(folder.folderId, context) 

        if parentName != "/":
            folderName += parentName + folder.name + "/"
        else:
            folderName += folder.name + "/"
    
    return folderName

def get_data(context: TercenContext, fileDoc: FileDocument, maxTries: int = 10):
    downloadTry = 1
    downloadSuccessful = False

    data = None
    while(downloadTry < maxTries):
        try:
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
        raise RuntimeError("kumo_utils.tercen_utils.get_data: Failed to download or extract {}".format(fileDoc.name))

    return pickle.loads(data)


def read_in_chunks(file_object, chunk_size=1024 * 1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

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

