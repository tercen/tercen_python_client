import tercen.client.base


class IssueMessageService(tercen.client.base.IssueMessageServiceBase):
    def __init__(self):
        super().__init__()


class WorkerService(tercen.client.base.WorkerServiceBase):
    def __init__(self):
        super().__init__()


class FileService(tercen.client.base.FileServiceBase):
    def __init__(self):
        super().__init__()


class GarbageCollectorService(tercen.client.base.GarbageCollectorServiceBase):
    def __init__(self):
        super().__init__()


class LockService(tercen.client.base.LockServiceBase):
    def __init__(self):
        super().__init__()


class IssueService(tercen.client.base.IssueServiceBase):
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


class TaskService(tercen.client.base.TaskServiceBase):
    def __init__(self):
        super().__init__()


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
