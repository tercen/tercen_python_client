import tercen.model.base
import json
from tercen.http.HttpClientService import HttpClientService, URI, encodeTSON, decodeTSON, MultiPart, MultiPartMixTransformer


class IssueMessageServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/issue_message")

    def getServiceName(self):
        return "IssueMessage"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.IssueMessageBase(m)
        else:
            return tercen.model.base.IssueMessage(m)

    def findByIssueAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByIssueAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)


class WorkerServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/worker")

    def getServiceName(self):
        return "Task"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.TaskBase(m)
        else:
            return tercen.model.base.Task(m)

    def exec(self, task):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "exec")
            params = {}
            params["task"] = task.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def setPriority(self, priority):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "setPriority")
            params = {}
            params["priority"] = priority
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def setStatus(self, status):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "setStatus")
            params = {}
            params["status"] = status
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def setHeartBeat(self, heartBeat):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "setHeartBeat")
            params = {}
            params["heartBeat"] = heartBeat
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getState(self, all):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "getState")
            params = {}
            params["all"] = all
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.WorkerBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def updateTaskEnv(self, taskId, env):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "updateTaskEnv")
            params = {}
            params["taskId"] = taskId
            params["env"] = list(map(lambda x: x.toJson(), env))
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getTaskStats(self, taskId):
        answer = None
        try:
            uri = URI.create("api/v1/worker" + "/" + "getTaskStats")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class FileServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/file")

    def getServiceName(self):
        return "FileDocument"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.FileDocumentBase(m)
        else:
            return tercen.model.base.FileDocument(m)

    def findFileByWorkflowIdAndStepId(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findFileByWorkflowIdAndStepId", startKey, endKey, limit, skip, descending, useFactory)

    def findByDataUri(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByDataUri", startKey, endKey, limit, skip, descending, useFactory)

    def upload(self, file, bytes):
        answer = None
        try:
            uri = URI.create("api/v1/file" + "/" + "upload")
            parts = []
            parts.append(MultiPart({"Content-Type": "application/json"},
                         json.JSONEncoder().encode([file.toJson()]).encode("utf-8")))
            parts.append(
                MultiPart({"Content-Type": "application/octet-stream"}, bytes))
            response = self.getHttpClient().multipart(
                self.getServiceUri(uri).toString(), None, parts)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.FileDocumentBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def append(self, file, bytes):
        answer = None
        try:
            uri = URI.create("api/v1/file" + "/" + "append")
            parts = []
            parts.append(MultiPart({"Content-Type": "application/json"},
                         json.JSONEncoder().encode([file.toJson()]).encode("utf-8")))
            parts.append(
                MultiPart({"Content-Type": "application/octet-stream"}, bytes))
            response = self.getHttpClient().multipart(
                self.getServiceUri(uri).toString(), None, parts)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.FileDocumentBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def download(self, fileDocumentId):
        answer = None
        try:
            uri = URI.create("api/v1/file" + "/" + "download")
            params = {}
            params["fileDocumentId"] = fileDocumentId
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer


class GarbageCollectorServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/gc")

    def getServiceName(self):
        return "GarbageObject"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.GarbageObjectBase(m)
        else:
            return tercen.model.base.GarbageObject(m)


class LockServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/lock")

    def getServiceName(self):
        return "Lock"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.LockBase(m)
        else:
            return tercen.model.base.Lock(m)

    def lock(self, name, wait):
        answer = None
        try:
            uri = URI.create("api/v1/lock" + "/" + "lock")
            params = {}
            params["name"] = name
            params["wait"] = wait
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.LockBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def releaseLock(self, lock):
        answer = None
        try:
            uri = URI.create("api/v1/lock" + "/" + "releaseLock")
            params = {}
            params["lock"] = lock.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class IssueServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/issue")

    def getServiceName(self):
        return "Issue"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.IssueBase(m)
        else:
            return tercen.model.base.Issue(m)

    def findByProjectAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByProjectAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)


class SubscriptionPlanServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/subscription")

    def getServiceName(self):
        return "SubscriptionPlan"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.SubscriptionPlanBase(m)
        else:
            return tercen.model.base.SubscriptionPlan(m)

    def findByOwner(self, keys, useFactory=False):
        return self.findKeys("findByOwner", keys, useFactory)

    def findSubscriptionPlanByCheckoutSessionId(self, keys, useFactory=False):
        return self.findKeys("checkoutSessionId", keys, useFactory)

    def getSubscriptionPlans(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" +
                             "/" + "getSubscriptionPlans")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getPlans(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" + "/" + "getPlans")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def createSubscriptionPlan(self, userId, plan, successUrl, cancelUrl):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" + "/" +
                             "createSubscriptionPlan")
            params = {}
            params["userId"] = userId
            params["plan"] = plan
            params["successUrl"] = successUrl
            params["cancelUrl"] = cancelUrl
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.SubscriptionPlanBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def setSubscriptionPlanStatus(self, subscriptionPlanId, status):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" + "/" +
                             "setSubscriptionPlanStatus")
            params = {}
            params["subscriptionPlanId"] = subscriptionPlanId
            params["status"] = status
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def updatePaymentMethod(self, subscriptionPlanId, successUrl, cancelUrl):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" +
                             "/" + "updatePaymentMethod")
            params = {}
            params["subscriptionPlanId"] = subscriptionPlanId
            params["successUrl"] = successUrl
            params["cancelUrl"] = cancelUrl
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.SubscriptionPlanBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def setUpdatePaymentMethodStatus(self, subscriptionPlanId, status):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" + "/" +
                             "setUpdatePaymentMethodStatus")
            params = {}
            params["subscriptionPlanId"] = subscriptionPlanId
            params["status"] = status
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def cancelSubscription(self, subscriptionPlanId):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" +
                             "/" + "cancelSubscription")
            params = {}
            params["subscriptionPlanId"] = subscriptionPlanId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def upgradeSubscription(self, subscriptionPlanId, plan):
        answer = None
        try:
            uri = URI.create("api/v1/subscription" +
                             "/" + "upgradeSubscription")
            params = {}
            params["subscriptionPlanId"] = subscriptionPlanId
            params["plan"] = plan
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class PersistentServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/po")

    def getServiceName(self):
        return "PersistentObject"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.PersistentObjectBase(m)
        else:
            return tercen.model.base.PersistentObject(m)

    def findDeleted(self, keys, useFactory=False):
        return self.findKeys("findDeleted", keys, useFactory)

    def findByKind(self, keys, useFactory=False):
        return self.findKeys("findByKind", keys, useFactory)

    def summary(self, teamOrProjectId):
        answer = None
        try:
            uri = URI.create("api/v1/po" + "/" + "summary")
            params = {}
            params["teamOrProjectId"] = teamOrProjectId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.SummaryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def getDependentObjects(self, id):
        answer = None
        try:
            uri = URI.create("api/v1/po" + "/" + "getDependentObjects")
            params = {}
            params["id"] = id
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getDependentObjectIds(self, id):
        answer = None
        try:
            uri = URI.create("api/v1/po" + "/" + "getDependentObjectIds")
            params = {}
            params["id"] = id
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes())
        except BaseException as e:
            self.onError(e)
        return answer


class ActivityServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/activity")

    def getServiceName(self):
        return "Activity"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.ActivityBase(m)
        else:
            return tercen.model.base.Activity(m)

    def findByUserAndDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByUserAndDate", startKey, endKey, limit, skip, descending, useFactory)

    def findByTeamAndDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByTeamAndDate", startKey, endKey, limit, skip, descending, useFactory)

    def findByProjectAndDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByProjectAndDate", startKey, endKey, limit, skip, descending, useFactory)

    def getPublicActivityCount(self, kind, limit):
        answer = None
        try:
            uri = URI.create("api/v1/activity" + "/" +
                             "getPublicActivityCount")
            params = {}
            params["kind"] = kind
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class FolderServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/folder")

    def getServiceName(self):
        return "FolderDocument"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.FolderDocumentBase(m)
        else:
            return tercen.model.base.FolderDocument(m)

    def findFolderByParentFolderAndName(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findFolderByParentFolderAndName", startKey, endKey, limit, skip, descending, useFactory)

    def getOrCreate(self, projectId, path):
        answer = None
        try:
            uri = URI.create("api/v1/folder" + "/" + "getOrCreate")
            params = {}
            params["projectId"] = projectId
            params["path"] = path
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.FolderDocumentBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def getExternalStorageFolders(self, projectId, volume, path):
        answer = None
        try:
            uri = URI.create("api/v1/folder" + "/" +
                             "getExternalStorageFolders")
            params = {}
            params["projectId"] = projectId
            params["volume"] = volume
            params["path"] = path
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class TableSchemaServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/schema")

    def getServiceName(self):
        return "Schema"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.SchemaBase(m)
        else:
            return tercen.model.base.Schema(m)

    def findByQueryHash(self, keys, useFactory=False):
        return self.findKeys("findByQueryHash", keys, useFactory)

    def findSchemaByDataDirectory(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findSchemaByDataDirectory", startKey, endKey, limit, skip, descending, useFactory)

    def select(self, tableId, cnames, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/schema" + "/" + "select")
            params = {}
            params["tableId"] = tableId
            params["cnames"] = cnames
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.TableBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def selectPairwise(self, tableId, cnames, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/schema" + "/" + "selectPairwise")
            params = {}
            params["tableId"] = tableId
            params["cnames"] = cnames
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.TableBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def selectStream(self, tableId, cnames, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/schema" + "/" + "selectStream")
            params = {}
            params["tableId"] = tableId
            params["cnames"] = cnames
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer

    def selectCSV(self, tableId, cnames, offset, limit, separator, quote, encoding):
        answer = None
        try:
            uri = URI.create("api/v1/schema" + "/" + "selectCSV")
            params = {}
            params["tableId"] = tableId
            params["cnames"] = cnames
            params["offset"] = offset
            params["limit"] = limit
            params["separator"] = separator
            params["quote"] = quote
            params["encoding"] = encoding
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer


class TaskServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/task")

    def getServiceName(self):
        return "Task"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.TaskBase(m)
        else:
            return tercen.model.base.Task(m)

    def findByHash(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByHash", startKey, endKey, limit, skip, descending, useFactory)

    def findGCTaskByLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findGCTaskByLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def runTask(self, taskId):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "runTask")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def cancelTask(self, taskId):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "cancelTask")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

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
                answer = tercen.model.base.TaskBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def updateWorker(self, worker):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "updateWorker")
            params = {}
            params["worker"] = worker.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def taskDurationByTeam(self, teamId, year, month):
        answer = 0.0
        try:
            uri = URI.create("api/v1/task" + "/" + "taskDurationByTeam")
            params = {}
            params["teamId"] = teamId
            params["year"] = year
            params["month"] = month
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def getWorkers(self, names):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "getWorkers")
            params = {}
            params["names"] = names
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getTasks(self, names):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "getTasks")
            params = {}
            params["names"] = names
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def setTaskEnvironment(self, taskId, environment):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "setTaskEnvironment")
            params = {}
            params["taskId"] = taskId
            params["environment"] = list(
                map(lambda x: x.toJson(), environment))
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def collectTaskStats(self, taskId):
        answer = None
        try:
            uri = URI.create("api/v1/task" + "/" + "collectTaskStats")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class UserSecretServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/userSecret")

    def getServiceName(self):
        return "UserSecret"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.UserSecretBase(m)
        else:
            return tercen.model.base.UserSecret(m)

    def findSecretByUserId(self, keys, useFactory=False):
        return self.findKeys("secret", keys, useFactory)


class PatchRecordServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/pr")

    def getServiceName(self):
        return "PatchRecords"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.PatchRecordsBase(m)
        else:
            return tercen.model.base.PatchRecords(m)

    def findByChannelId(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByChannelId", startKey, endKey, limit, skip, descending, useFactory)


class EventServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/evt")

    def getServiceName(self):
        return "Event"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.EventBase(m)
        else:
            return tercen.model.base.Event(m)

    def sendChannel(self, channel, evt):
        answer = None
        try:
            uri = URI.create("api/v1/evt" + "/" + "sendChannel")
            params = {}
            params["channel"] = channel
            params["evt"] = evt.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def taskListenerCount(self, taskId):
        answer = 0
        try:
            uri = URI.create("api/v1/evt" + "/" + "taskListenerCount")
            params = {}
            params["taskId"] = taskId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer


class WorkflowServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/workflow")

    def getServiceName(self):
        return "Workflow"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.WorkflowBase(m)
        else:
            return tercen.model.base.Workflow(m)

    def getCubeQuery(self, workflowId, stepId):
        answer = None
        try:
            uri = URI.create("api/v1/workflow" + "/" + "getCubeQuery")
            params = {}
            params["workflowId"] = workflowId
            params["stepId"] = stepId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.CubeQueryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def copyApp(self, workflowId, projectId):
        answer = None
        try:
            uri = URI.create("api/v1/workflow" + "/" + "copyApp")
            params = {}
            params["workflowId"] = workflowId
            params["projectId"] = projectId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.WorkflowBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer


class UserServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/user")

    def getServiceName(self):
        return "User"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.UserBase(m)
        else:
            return tercen.model.base.User(m)

    def findTeamMembers(self, keys, useFactory=False):
        return self.findKeys("teamMembers", keys, useFactory)

    def findUserByCreatedDateAndName(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findUserByCreatedDateAndName", startKey, endKey, limit, skip, descending, useFactory)

    def findUserByEmail(self, keys, useFactory=False):
        return self.findKeys("userByEmail", keys, useFactory)

    def getSamlMessage(self, type):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "getSamlMessage")
            params = {}
            params["type"] = type
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def cookieConsent(self, dummy):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "cookieConsent")
            params = {}
            params["dummy"] = dummy
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def connect(self, usernameOrEmail, password):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "connect")
            params = {}
            params["usernameOrEmail"] = usernameOrEmail
            params["password"] = password
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.UserSessionBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def connect2(self, domain, usernameOrEmail, password):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "connect2")
            params = {}
            params["domain"] = domain
            params["usernameOrEmail"] = usernameOrEmail
            params["password"] = password
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.UserSessionBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def createUser(self, user, password):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "createUser")
            params = {}
            params["user"] = user.toJson()
            params["password"] = password
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.UserBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def hasUserName(self, username):
        answer = True
        try:
            uri = URI.create("api/v1/user" + "/" + "hasUserName")
            params = {}
            params["username"] = username
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def updatePassword(self, userId, password):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "updatePassword")
            params = {}
            params["userId"] = userId
            params["password"] = password
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def updateBillingInfo(self, userId, billingInfo):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "updateBillingInfo")
            params = {}
            params["userId"] = userId
            params["billingInfo"] = billingInfo.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.BillingInfoBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def viesInfo(self, country_code, vatNumber):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "viesInfo")
            params = {}
            params["country_code"] = country_code
            params["vatNumber"] = vatNumber
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ViesInfoBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def summary(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "summary")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.SummaryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def resourceSummary(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "resourceSummary")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ResourceSummaryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def profiles(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "profiles")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ProfilesBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def createToken(self, userId, validityInSeconds):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "createToken")
            params = {}
            params["userId"] = userId
            params["validityInSeconds"] = validityInSeconds
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def isTokenValid(self, token):
        answer = True
        try:
            uri = URI.create("api/v1/user" + "/" + "isTokenValid")
            params = {}
            params["token"] = token
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def setTeamPrivilege(self, username, principal, privilege):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "setTeamPrivilege")
            params = {}
            params["username"] = username
            params["principal"] = principal.toJson()
            params["privilege"] = privilege.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer

    def getServerVersion(self, module):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "getServerVersion")
            params = {}
            params["module"] = module
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.VersionBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def getClientConfig(self, keys):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "getClientConfig")
            params = {}
            params["keys"] = keys
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getInvited(self, email):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "getInvited")
            params = {}
            params["email"] = email
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def sendValidationMail(self, email):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "sendValidationMail")
            params = {}
            params["email"] = email
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def sendResetPasswordEmail(self, email):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "sendResetPasswordEmail")
            params = {}
            params["email"] = email
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def changeUserPassword(self, token, password):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "changeUserPassword")
            params = {}
            params["token"] = token
            params["password"] = password
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def validateUser(self, token):
        answer = None
        try:
            uri = URI.create("api/v1/user" + "/" + "validateUser")
            params = {}
            params["token"] = token
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def canCreatePrivateProject(self, teamOrUserId):
        answer = True
        try:
            uri = URI.create("api/v1/user" + "/" + "canCreatePrivateProject")
            params = {}
            params["teamOrUserId"] = teamOrUserId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = decodeTSON(response.body().bytes()).get(0)
        except BaseException as e:
            self.onError(e)
        return answer


class ProjectDocumentServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/pd")

    def getServiceName(self):
        return "ProjectDocument"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.ProjectDocumentBase(m)
        else:
            return tercen.model.base.ProjectDocument(m)

    def findProjectObjectsByLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findProjectObjectsByLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findProjectObjectsByFolderAndName(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findProjectObjectsByFolderAndName", startKey, endKey, limit, skip, descending, useFactory)

    def findFileByLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findFileByLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findSchemaByLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findSchemaByLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findSchemaByOwnerAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findSchemaByOwnerAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findFileByOwnerAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findFileByOwnerAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def getParentFolders(self, documentId):
        answer = None
        try:
            uri = URI.create("api/v1/pd" + "/" + "getParentFolders")
            params = {}
            params["documentId"] = documentId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def cloneProjectDocument(self, documentId, projectId):
        answer = None
        try:
            uri = URI.create("api/v1/pd" + "/" + "cloneProjectDocument")
            params = {}
            params["documentId"] = documentId
            params["projectId"] = projectId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ProjectDocumentBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer


class CranLibraryServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/rlib")

    def getServiceName(self):
        return "RLibrary"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.RLibraryBase(m)
        else:
            return tercen.model.base.RLibrary(m)

    def findByOwnerNameVersion(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByOwnerNameVersion", startKey, endKey, limit, skip, descending, useFactory)

    def packagesGz(self, repoName):
        answer = None
        try:
            uri = URI.create("api/v1/rlib" + "/" + "packagesGz")
            params = {}
            params["repoName"] = repoName
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer

    def packagesRds(self, repoName):
        answer = None
        try:
            uri = URI.create("api/v1/rlib" + "/" + "packagesRds")
            params = {}
            params["repoName"] = repoName
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer

    def packages(self, repoName):
        answer = None
        try:
            uri = URI.create("api/v1/rlib" + "/" + "packages")
            params = {}
            params["repoName"] = repoName
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer

    def archive(self, repoName, package, filename):
        answer = None
        try:
            uri = URI.create("api/v1/rlib" + "/" + "archive")
            params = {}
            params["repoName"] = repoName
            params["package"] = package
            params["filename"] = filename
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer

    def package(self, repoName, package):
        answer = None
        try:
            uri = URI.create("api/v1/rlib" + "/" + "package")
            params = {}
            params["repoName"] = repoName
            params["package"] = package
            geturi = self.getServiceUri(uri).replaceQueryParameters(
                {"params": json.JSONEncoder().encode(params)})
            response = self.getHttpClient().get(geturi.toString(), None)
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = response.body().bytes()
        except BaseException as e:
            self.onError(e)
        return answer


class TeamServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/team")

    def getServiceName(self):
        return "Team"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.TeamBase(m)
        else:
            return tercen.model.base.Team(m)

    def findTeamByOwner(self, keys, useFactory=False):
        return self.findKeys("teamByOwner", keys, useFactory)

    def profiles(self, teamId):
        answer = None
        try:
            uri = URI.create("api/v1/team" + "/" + "profiles")
            params = {}
            params["teamId"] = teamId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ProfilesBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def resourceSummary(self, teamId):
        answer = None
        try:
            uri = URI.create("api/v1/team" + "/" + "resourceSummary")
            params = {}
            params["teamId"] = teamId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ResourceSummaryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def transferOwnership(self, teamIds, newOwner):
        answer = None
        try:
            uri = URI.create("api/v1/team" + "/" + "transferOwnership")
            params = {}
            params["teamIds"] = teamIds
            params["newOwner"] = newOwner
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class ProjectServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/project")

    def getServiceName(self):
        return "Project"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.ProjectBase(m)
        else:
            return tercen.model.base.Project(m)

    def findByIsPublicAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByIsPublicAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findByTeamAndIsPublicAndLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findByTeamAndIsPublicAndLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def profiles(self, projectId):
        answer = None
        try:
            uri = URI.create("api/v1/project" + "/" + "profiles")
            params = {}
            params["projectId"] = projectId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ProfilesBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def resourceSummary(self, projectId):
        answer = None
        try:
            uri = URI.create("api/v1/project" + "/" + "resourceSummary")
            params = {}
            params["projectId"] = projectId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ResourceSummaryBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def explore(self, category, start, limit):
        answer = None
        try:
            uri = URI.create("api/v1/project" + "/" + "explore")
            params = {}
            params["category"] = category
            params["start"] = start
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def recentProjects(self, userId):
        answer = None
        try:
            uri = URI.create("api/v1/project" + "/" + "recentProjects")
            params = {}
            params["userId"] = userId
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def cloneProject(self, projectId, project):
        answer = None
        try:
            uri = URI.create("api/v1/project" + "/" + "cloneProject")
            params = {}
            params["projectId"] = projectId
            params["project"] = project.toJson()
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.ProjectBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer


class DocumentServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/d")

    def getServiceName(self):
        return "Document"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.DocumentBase(m)
        else:
            return tercen.model.base.Document(m)

    def findWorkflowByTagOwnerCreatedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findWorkflowByTagOwnerCreatedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findProjectByOwnersAndName(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findProjectByOwnersAndName", startKey, endKey, limit, skip, descending, useFactory)

    def findProjectByOwnersAndCreatedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findProjectByOwnersAndCreatedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findOperatorByOwnerLastModifiedDate(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findOperatorByOwnerLastModifiedDate", startKey, endKey, limit, skip, descending, useFactory)

    def findOperatorByUrlAndVersion(self, startKey, endKey, limit=200, skip=0, descending=True, useFactory=False):
        return self.findStartKeys("findOperatorByUrlAndVersion", startKey, endKey, limit, skip, descending, useFactory)

    def search(self, query, limit, useFactory, bookmark):
        answer = None
        try:
            uri = URI.create("api/v1/d" + "/" + "search")
            params = {}
            params["query"] = query
            params["limit"] = limit
            params["useFactory"] = useFactory
            params["bookmark"] = bookmark
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = tercen.model.base.SearchResultBase.createFromJson(
                    decodeTSON(response.body().bytes()))
        except BaseException as e:
            self.onError(e)
        return answer

    def getTercenOperatorLibrary(self, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/d" + "/" + "getTercenOperatorLibrary")
            params = {}
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getTercenWorkflowLibrary(self, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/d" + "/" + "getTercenWorkflowLibrary")
            params = {}
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer

    def getTercenAppLibrary(self, offset, limit):
        answer = None
        try:
            uri = URI.create("api/v1/d" + "/" + "getTercenAppLibrary")
            params = {}
            params["offset"] = offset
            params["limit"] = limit
            response = self.getHttpClient().post(
                self.getServiceUri(uri).toString(), None, encodeTSON(params))
            if response.code() != 200:
                self.onResponseError(response)
            else:
                answer = None
        except BaseException as e:
            self.onError(e)
        return answer


class OperatorServiceBase (HttpClientService):
    def getBaseUri(self):
        return URI.create("api/v1/operator")

    def getServiceName(self):
        return "Operator"

    def toJson(self, object):
        return object.toJson()

    def fromJson(self, m, useFactory=True):
        if m is None:
            return None
        if useFactory:
            return tercen.model.base.OperatorBase(m)
        else:
            return tercen.model.base.Operator(m)
