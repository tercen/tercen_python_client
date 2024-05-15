import tercen.client.base
import tercen.model.base
import tercen.model.impl
import json
from tercen.http.HttpClientService import decodeTSON, URI, MultiPart, encodeTSON



class WorkerService(tercen.client.base.WorkerServiceBase):
    def __init__(self):
        super().__init__()


class FileService(tercen.client.base.FileServiceBase):
    def __init__(self):
        super().__init__()


    # Pass the iterator to post and build from there...
    def uploadTable(self, file, tableJson):
        answer = None
        try:
            uri = URI.create("api/v1/file" + "/" + "upload")
            parts = []
            parts.append(MultiPart({"Content-Type": "application/json"},
                                   json.JSONEncoder().encode([file.toJson()]).encode("utf-8")))
            parts.append(
                MultiPart({"Content-Type": "application/octet-stream"}, tableJson))
            # parts.append(
            # MultiPart({"Content-Type": "application/octet-stream"},
            #    json.JSONEncoder().encode([tableJson]).encode("utf-8") ))

            response = self.getHttpClient().multipart(
                self.getServiceUri(uri).toString(), None, parts)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.impl.FileDocument.createFromJson(
                    decodeTSON(response))
        except BaseException as e:
            self.onError(e)
        return answer

    def uploadFromFile(self, file, filePath):
        import os
        if not os.path.exists(filePath) or not os.path.isfile(filePath):
            raise ValueError("Last argument must be a path to an existing file")
        
        answer = None
        try:
            uri = URI.create("api/v1/file" + "/" + "upload")
            parts = []
            parts.append(MultiPart({"Content-Type": "application/json"},
                         json.JSONEncoder().encode([file.toJson()]).encode("utf-8")))
            parts.append(
                MultiPart({"Content-Type": "application/octet-stream"}, filePath))
            
            response = self.getHttpClient().multipart(
                self.getServiceUri(uri).toString(), None, parts)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.FileDocumentBase.createFromJson(
                    decodeTSON(response))
        except BaseException as e:
            self.onError(e)
        return answer


class GarbageCollectorService(tercen.client.base.GarbageCollectorServiceBase):
    def __init__(self):
        super().__init__()


class LockService(tercen.client.base.LockServiceBase):
    def __init__(self):
        super().__init__()


class SubscriptionPlanService(tercen.client.base.SubscriptionPlanServiceBase):
    def __init__(self):
        super().__init__()


class PersistentService(tercen.client.base.PersistentServiceBase):
    def __init__(self):
        super().__init__()


class ActivityService(tercen.client.base.ActivityServiceBase):
    def __init__(self):
        super().__init__()


class FolderService(tercen.client.base.FolderServiceBase):
    def __init__(self):
        super().__init__()


class TableSchemaService(tercen.client.base.TableSchemaServiceBase):
    def __init__(self):
        super().__init__()


    # def findByQueryHash(self, keys):
    #     return [self.get(keys[0])]


    def selectStream(self, tableId, cnames, offset, limit):
        response = None
        try:
            params = {}
            params["tableId"] = tableId
            params["cnames"] = cnames

            if (offset is None or offset == 0) and\
                 (limit is None or  limit == -1):
                uri = URI.create("api/v1/schema" + "/" + "selectStream")
                params["offset"] = offset
                params["limit"] = limit
            else:
                uri = URI.create("api/v1/schema" + "/" + "select")
                params["offset"] = int(offset)
                if limit is None:
                    params["limit"] = limit
                else:
                    params["limit"] = int(limit)
            
            
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            # else:
            #     answer = response
        except BaseException as e:
            self.onError(e)
        return response

    # def select(self, tableId, cnames, offset, limit):
    #     answer = None
    #     try:
    #         tbl_bytes = super().selectStream(tableId, cnames, offset, limit)
    #         answer = tercen.model.base.TableBase.createFromJson(decodeTSON(tbl_bytes))
    #     except BaseException as e:
    #         self.onError(e)
    #     return answer


class TaskService(tercen.client.base.TaskServiceBase):
    def __init__(self):
        super().__init__()

    def subclassHierarchy( self, baseClass ):
        classes = [baseClass]

        sc = baseClass.__subclasses__()

        if sc == None or len(sc) == 0:
            return classes
        else:
            for cls in sc:
                subClasses = self.subclassHierarchy(cls)

                for cc in subClasses:
                    classes.append( cc )

            return classes


    def specificClassFromJsonTask( self, m):
        className = m['kind']
        subclasses = self.subclassHierarchy( tercen.model.base.TaskBase )

        klass = None
        for cl in subclasses:
            if cl.__name__ == className:
                klass = cl
                break
        newObj = klass(m)

        return newObj

    def waitDone(self, taskId):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "waitDone")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                # answer = tercen.model.base.TaskBase.createFromJson(
                #     decodeTSON(response))
                # respTson = decodeTSON(response)

                # answer1 = tercen.model.base.TaskBase.createFromJson(respTson)

                # answer = self.specificClassFromJsonTask(decodeTSON(response))
                answer = self.fromJson(decodeTSON(response))


        except BaseException as e:
            self.onError(e)
        return answer


class UserSecretService(tercen.client.base.UserSecretServiceBase):
    def __init__(self):
        super().__init__()


class PatchRecordService(tercen.client.base.PatchRecordServiceBase):
    def __init__(self):
        super().__init__()


class EventService(tercen.client.base.EventServiceBase):
    def __init__(self):
        super().__init__()


class WorkflowService(tercen.client.base.WorkflowServiceBase):
    def __init__(self):
        super().__init__()


class UserService(tercen.client.base.UserServiceBase):
    def __init__(self):
        super().__init__()

    def connect(self, usernameOrEmail, password):
        return self.connect2("", usernameOrEmail, password)

    def connect2(self, domain, usernameOrEmail, password):
        session = super().connect2(domain, usernameOrEmail, password)
        self.tercenClient.httpClient.authorization = session.token.token
        return session


class ProjectDocumentService(tercen.client.base.ProjectDocumentServiceBase):
    def __init__(self):
        super().__init__()


class CranLibraryService(tercen.client.base.CranLibraryServiceBase):
    def __init__(self):
        super().__init__()


class TeamService(tercen.client.base.TeamServiceBase):
    def __init__(self):
        super().__init__()


class ProjectService(tercen.client.base.ProjectServiceBase):
    def __init__(self):
        super().__init__()


class DocumentService(tercen.client.base.DocumentServiceBase):
    def __init__(self):
        super().__init__()


class OperatorService(tercen.client.base.OperatorServiceBase):
    def __init__(self):
        super().__init__()
