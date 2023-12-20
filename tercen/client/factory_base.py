import tercen.client.impl
from tercen.http.HttpClientService import HttpClientService, HttpClient, URI, encodeTSON, decodeTSON


class TercenClientBase:
    def __init__(self):
        self.httpClient = HttpClient()
        self.tercenURI = URI.create("https://tercen.com/")
        self.workerService = tercen.client.impl.WorkerService()
        self.workerService.tercenClient = self
        self.fileService = tercen.client.impl.FileService()
        self.fileService.tercenClient = self
        self.garbageCollectorService = tercen.client.impl.GarbageCollectorService()
        self.garbageCollectorService.tercenClient = self
        self.lockService = tercen.client.impl.LockService()
        self.lockService.tercenClient = self
        self.subscriptionPlanService = tercen.client.impl.SubscriptionPlanService()
        self.subscriptionPlanService.tercenClient = self
        self.persistentService = tercen.client.impl.PersistentService()
        self.persistentService.tercenClient = self
        self.activityService = tercen.client.impl.ActivityService()
        self.activityService.tercenClient = self
        self.folderService = tercen.client.impl.FolderService()
        self.folderService.tercenClient = self
        self.tableSchemaService = tercen.client.impl.TableSchemaService()
        self.tableSchemaService.tercenClient = self
        self.taskService = tercen.client.impl.TaskService()
        self.taskService.tercenClient = self
        self.userSecretService = tercen.client.impl.UserSecretService()
        self.userSecretService.tercenClient = self
        self.patchRecordService = tercen.client.impl.PatchRecordService()
        self.patchRecordService.tercenClient = self
        self.eventService = tercen.client.impl.EventService()
        self.eventService.tercenClient = self
        self.workflowService = tercen.client.impl.WorkflowService()
        self.workflowService.tercenClient = self
        self.userService = tercen.client.impl.UserService()
        self.userService.tercenClient = self
        self.projectDocumentService = tercen.client.impl.ProjectDocumentService()
        self.projectDocumentService.tercenClient = self
        self.cranLibraryService = tercen.client.impl.CranLibraryService()
        self.cranLibraryService.tercenClient = self
        self.teamService = tercen.client.impl.TeamService()
        self.teamService.tercenClient = self
        self.projectService = tercen.client.impl.ProjectService()
        self.projectService.tercenClient = self
        self.documentService = tercen.client.impl.DocumentService()
        self.documentService.tercenClient = self
        self.operatorService = tercen.client.impl.OperatorService()
        self.operatorService.tercenClient = self
