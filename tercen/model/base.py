import tercen.model.vocabulary as Vocabulary
from tercen.base.BaseObject import BaseObject


class SciObjectBase(BaseObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.SciObject_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.SciObject_CLASS:
            return SciObject(m)
        if kind == Vocabulary.EnumeratedProperty_CLASS:
            return EnumeratedProperty(m)
        if kind == Vocabulary.FactorsProperty_CLASS:
            return FactorsProperty(m)
        if kind == Vocabulary.FormulaProperty_CLASS:
            return FormulaProperty(m)
        if kind == Vocabulary.DoubleProperty_CLASS:
            return DoubleProperty(m)
        if kind == Vocabulary.StringProperty_CLASS:
            return StringProperty(m)
        if kind == Vocabulary.BooleanProperty_CLASS:
            return BooleanProperty(m)
        if kind == Vocabulary.AnnotationOperatorModel_CLASS:
            return AnnotationOperatorModel(m)
        if kind == Vocabulary.NamedFilter_CLASS:
            return NamedFilter(m)
        if kind == Vocabulary.Filter_CLASS:
            return Filter(m)
        if kind == Vocabulary.FilterExpr_CLASS:
            return FilterExpr(m)
        if kind == Vocabulary.RunningState_CLASS:
            return RunningState(m)
        if kind == Vocabulary.RunningDependentState_CLASS:
            return RunningDependentState(m)
        if kind == Vocabulary.FailedState_CLASS:
            return FailedState(m)
        if kind == Vocabulary.CanceledState_CLASS:
            return CanceledState(m)
        if kind == Vocabulary.DoneState_CLASS:
            return DoneState(m)
        if kind == Vocabulary.InitState_CLASS:
            return InitState(m)
        if kind == Vocabulary.PendingState_CLASS:
            return PendingState(m)
        if kind == Vocabulary.StorageProfile_CLASS:
            return StorageProfile(m)
        if kind == Vocabulary.RunProfile_CLASS:
            return RunProfile(m)
        if kind == Vocabulary.CpuTimeProfile_CLASS:
            return CpuTimeProfile(m)
        if kind == Vocabulary.TableProfile_CLASS:
            return TableProfile(m)
        if kind == Vocabulary.ApiCallProfile_CLASS:
            return ApiCallProfile(m)
        if kind == Vocabulary.TableRelation_CLASS:
            return TableRelation(m)
        if kind == Vocabulary.ReferenceRelation_CLASS:
            return ReferenceRelation(m)
        if kind == Vocabulary.WhereRelation_CLASS:
            return WhereRelation(m)
        if kind == Vocabulary.DistinctRelation_CLASS:
            return DistinctRelation(m)
        if kind == Vocabulary.InMemoryRelation_CLASS:
            return InMemoryRelation(m)
        if kind == Vocabulary.RenameRelation_CLASS:
            return RenameRelation(m)
        if kind == Vocabulary.UnionRelation_CLASS:
            return UnionRelation(m)
        if kind == Vocabulary.SimpleRelation_CLASS:
            return SimpleRelation(m)
        if kind == Vocabulary.GatherRelation_CLASS:
            return GatherRelation(m)
        if kind == Vocabulary.CompositeRelation_CLASS:
            return CompositeRelation(m)
        if kind == Vocabulary.GroupByRelation_CLASS:
            return GroupByRelation(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        if kind == Vocabulary.RelationStep_CLASS:
            return RelationStep(m)
        if kind == Vocabulary.ExportStep_CLASS:
            return ExportStep(m)
        if kind == Vocabulary.ModelStep_CLASS:
            return ModelStep(m)
        if kind == Vocabulary.ViewStep_CLASS:
            return ViewStep(m)
        if kind == Vocabulary.InputPort_CLASS:
            return InputPort(m)
        if kind == Vocabulary.OutputPort_CLASS:
            return OutputPort(m)
        if kind == Vocabulary.GarbageTasks_CLASS:
            return GarbageTasks(m)
        if kind == Vocabulary.GarbageTasks2_CLASS:
            return GarbageTasks2(m)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        if kind == Vocabulary.User_CLASS:
            return User(m)
        if kind == Vocabulary.RLibrary_CLASS:
            return RLibrary(m)
        if kind == Vocabulary.Operator_CLASS:
            return Operator(m)
        if kind == Vocabulary.WorkerEndpoint_CLASS:
            return WorkerEndpoint(m)
        if kind == Vocabulary.ProjectDocument_CLASS:
            return ProjectDocument(m)
        if kind == Vocabulary.Project_CLASS:
            return Project(m)
        if kind == Vocabulary.SubscriptionPlan_CLASS:
            return SubscriptionPlan(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        if kind == Vocabulary.ProjectTask_CLASS:
            return ProjectTask(m)
        if kind == Vocabulary.GlTask_CLASS:
            return GlTask(m)
        if kind == Vocabulary.CreateGitOperatorTask_CLASS:
            return CreateGitOperatorTask(m)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        if kind == Vocabulary.PatchRecords_CLASS:
            return PatchRecords(m)
        if kind == Vocabulary.TaskEvent_CLASS:
            return TaskEvent(m)
        if kind == Vocabulary.GenericEvent_CLASS:
            return GenericEvent(m)
        if kind == Vocabulary.GarbageObject_CLASS:
            return GarbageObject(m)
        if kind == Vocabulary.Activity_CLASS:
            return Activity(m)
        if kind == Vocabulary.Document_CLASS:
            return Document(m)
        if kind == Vocabulary.Lock_CLASS:
            return Lock(m)
        if kind == Vocabulary.Task_CLASS:
            return Task(m)
        if kind == Vocabulary.Event_CLASS:
            return Event(m)
        if kind == Vocabulary.UserSecret_CLASS:
            return UserSecret(m)
        if kind == Vocabulary.Column_CLASS:
            return Column(m)
        if kind == Vocabulary.StartProcess_CLASS:
            return StartProcess(m)
        if kind == Vocabulary.Relation_CLASS:
            return Relation(m)
        if kind == Vocabulary.Step_CLASS:
            return Step(m)
        if kind == Vocabulary.Port_CLASS:
            return Port(m)
        if kind == Vocabulary.PersistentObject_CLASS:
            return PersistentObject(m)
        if kind == Vocabulary.Link_CLASS:
            return Link(m)
        if kind == Vocabulary.ColumnSchema_CLASS:
            return ColumnSchema(m)
        if kind == Vocabulary.CSVFileMetadata_CLASS:
            return CSVFileMetadata(m)
        if kind == Vocabulary.JetPalette_CLASS:
            return JetPalette(m)
        if kind == Vocabulary.RampPalette_CLASS:
            return RampPalette(m)
        if kind == Vocabulary.CategoryPalette_CLASS:
            return CategoryPalette(m)
        if kind == Vocabulary.DoubleColorElement_CLASS:
            return DoubleColorElement(m)
        if kind == Vocabulary.StringColorElement_CLASS:
            return StringColorElement(m)
        if kind == Vocabulary.TableStepModel_CLASS:
            return TableStepModel(m)
        if kind == Vocabulary.Crosstab_CLASS:
            return Crosstab(m)
        if kind == Vocabulary.JoinStepModel_CLASS:
            return JoinStepModel(m)
        if kind == Vocabulary.WizardStepModel_CLASS:
            return WizardStepModel(m)
        if kind == Vocabulary.MeltStepModel_CLASS:
            return MeltStepModel(m)
        if kind == Vocabulary.ExportModel_CLASS:
            return ExportModel(m)
        if kind == Vocabulary.Attribute_CLASS:
            return Attribute(m)
        if kind == Vocabulary.MappingFactor_CLASS:
            return MappingFactor(m)
        if kind == Vocabulary.ChartLine_CLASS:
            return ChartLine(m)
        if kind == Vocabulary.ChartPoint_CLASS:
            return ChartPoint(m)
        if kind == Vocabulary.ChartHeatmap_CLASS:
            return ChartHeatmap(m)
        if kind == Vocabulary.ChartBar_CLASS:
            return ChartBar(m)
        if kind == Vocabulary.ChartSize_CLASS:
            return ChartSize(m)
        if kind == Vocabulary.Rectangle_CLASS:
            return Rectangle(m)
        if kind == Vocabulary.ResourceSummary_CLASS:
            return ResourceSummary(m)
        if kind == Vocabulary.BillingInfo_CLASS:
            return BillingInfo(m)
        if kind == Vocabulary.Property_CLASS:
            return Property(m)
        if kind == Vocabulary.Version_CLASS:
            return Version(m)
        if kind == Vocabulary.Filters_CLASS:
            return Filters(m)
        if kind == Vocabulary.CubeQuery_CLASS:
            return CubeQuery(m)
        if kind == Vocabulary.UserSession_CLASS:
            return UserSession(m)
        if kind == Vocabulary.Table_CLASS:
            return Table(m)
        if kind == Vocabulary.Acl_CLASS:
            return Acl(m)
        if kind == Vocabulary.TaskSummary_CLASS:
            return TaskSummary(m)
        if kind == Vocabulary.Token_CLASS:
            return Token(m)
        if kind == Vocabulary.JoinOperator_CLASS:
            return JoinOperator(m)
        if kind == Vocabulary.OperatorModel_CLASS:
            return OperatorModel(m)
        if kind == Vocabulary.CrosstabTable_CLASS:
            return CrosstabTable(m)
        if kind == Vocabulary.XYAxisList_CLASS:
            return XYAxisList(m)
        if kind == Vocabulary.FilterTopExpr_CLASS:
            return FilterTopExpr(m)
        if kind == Vocabulary.PatchRecord_CLASS:
            return PatchRecord(m)
        if kind == Vocabulary.State_CLASS:
            return State(m)
        if kind == Vocabulary.ColumnSchemaMetaData_CLASS:
            return ColumnSchemaMetaData(m)
        if kind == Vocabulary.Privilege_CLASS:
            return Privilege(m)
        if kind == Vocabulary.ViesInfo_CLASS:
            return ViesInfo(m)
        if kind == Vocabulary.RDescription_CLASS:
            return RDescription(m)
        if kind == Vocabulary.Profile_CLASS:
            return Profile(m)
        if kind == Vocabulary.Date_CLASS:
            return Date(m)
        if kind == Vocabulary.StepState_CLASS:
            return StepState(m)
        if kind == Vocabulary.OperatorResult_CLASS:
            return OperatorResult(m)
        if kind == Vocabulary.Address_CLASS:
            return Address(m)
        if kind == Vocabulary.XYAxis_CLASS:
            return XYAxis(m)
        if kind == Vocabulary.IdObject_CLASS:
            return IdObject(m)
        if kind == Vocabulary.Principal_CLASS:
            return Principal(m)
        if kind == Vocabulary.Url_CLASS:
            return Url(m)
        if kind == Vocabulary.RProxy_CLASS:
            return RProxy(m)
        if kind == Vocabulary.Pair_CLASS:
            return Pair(m)
        if kind == Vocabulary.FileMetadata_CLASS:
            return FileMetadata(m)
        if kind == Vocabulary.AxisSettings_CLASS:
            return AxisSettings(m)
        if kind == Vocabulary.Worker_CLASS:
            return Worker(m)
        if kind == Vocabulary.Ace_CLASS:
            return Ace(m)
        if kind == Vocabulary.Labels_CLASS:
            return Labels(m)
        if kind == Vocabulary.OperatorSettings_CLASS:
            return OperatorSettings(m)
        if kind == Vocabulary.TableSummary_CLASS:
            return TableSummary(m)
        if kind == Vocabulary.Point_CLASS:
            return Point(m)
        if kind == Vocabulary.Summary_CLASS:
            return Summary(m)
        if kind == Vocabulary.Errors_CLASS:
            return Errors(m)
        if kind == Vocabulary.Palette_CLASS:
            return Palette(m)
        if kind == Vocabulary.GraphicalFactor_CLASS:
            return GraphicalFactor(m)
        if kind == Vocabulary.ColorList_CLASS:
            return ColorList(m)
        if kind == Vocabulary.SearchResult_CLASS:
            return SearchResult(m)
        if kind == Vocabulary.PreProcessor_CLASS:
            return PreProcessor(m)
        if kind == Vocabulary.AnnotationModel_CLASS:
            return AnnotationModel(m)
        if kind == Vocabulary.ColorElement_CLASS:
            return ColorElement(m)
        if kind == Vocabulary.Properties_CLASS:
            return Properties(m)
        if kind == Vocabulary.PropertyValue_CLASS:
            return PropertyValue(m)
        if kind == Vocabulary.AclContext_CLASS:
            return AclContext(m)
        if kind == Vocabulary.OperatorUnitTest_CLASS:
            return OperatorUnitTest(m)
        if kind == Vocabulary.StepModel_CLASS:
            return StepModel(m)
        if kind == Vocabulary.Profiles_CLASS:
            return Profiles(m)
        if kind == Vocabulary.OperatorRef_CLASS:
            return OperatorRef(m)
        if kind == Vocabulary.Factor_CLASS:
            return Factor(m)
        if kind == Vocabulary.ColumnPair_CLASS:
            return ColumnPair(m)
        if kind == Vocabulary.TaxId_CLASS:
            return TaxId(m)
        if kind == Vocabulary.Plan_CLASS:
            return Plan(m)
        if kind == Vocabulary.CSVParserParam_CLASS:
            return CSVParserParam(m)
        if kind == Vocabulary.AppDesign_CLASS:
            return AppDesign(m)
        if kind == Vocabulary.Axis_CLASS:
            return Axis(m)
        if kind == Vocabulary.Colors_CLASS:
            return Colors(m)
        if kind == Vocabulary.TableProperties_CLASS:
            return TableProperties(m)
        if kind == Vocabulary.Chart_CLASS:
            return Chart(m)
        raise ValueError("bad kind : " + kind +
                         " for class SciObject in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.SciObject_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.SciObject_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class SciObject(SciObjectBase):
    def __init__(self, m=None):
        super().__init__(m)


class IdObjectBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.id = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.IdObject_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.id = m[Vocabulary.id_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.IdObject_CLASS:
            return IdObject(m)
        if kind == Vocabulary.TableRelation_CLASS:
            return TableRelation(m)
        if kind == Vocabulary.ReferenceRelation_CLASS:
            return ReferenceRelation(m)
        if kind == Vocabulary.WhereRelation_CLASS:
            return WhereRelation(m)
        if kind == Vocabulary.DistinctRelation_CLASS:
            return DistinctRelation(m)
        if kind == Vocabulary.InMemoryRelation_CLASS:
            return InMemoryRelation(m)
        if kind == Vocabulary.RenameRelation_CLASS:
            return RenameRelation(m)
        if kind == Vocabulary.UnionRelation_CLASS:
            return UnionRelation(m)
        if kind == Vocabulary.SimpleRelation_CLASS:
            return SimpleRelation(m)
        if kind == Vocabulary.GatherRelation_CLASS:
            return GatherRelation(m)
        if kind == Vocabulary.CompositeRelation_CLASS:
            return CompositeRelation(m)
        if kind == Vocabulary.GroupByRelation_CLASS:
            return GroupByRelation(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        if kind == Vocabulary.RelationStep_CLASS:
            return RelationStep(m)
        if kind == Vocabulary.ExportStep_CLASS:
            return ExportStep(m)
        if kind == Vocabulary.ModelStep_CLASS:
            return ModelStep(m)
        if kind == Vocabulary.ViewStep_CLASS:
            return ViewStep(m)
        if kind == Vocabulary.InputPort_CLASS:
            return InputPort(m)
        if kind == Vocabulary.OutputPort_CLASS:
            return OutputPort(m)
        if kind == Vocabulary.GarbageTasks_CLASS:
            return GarbageTasks(m)
        if kind == Vocabulary.GarbageTasks2_CLASS:
            return GarbageTasks2(m)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        if kind == Vocabulary.User_CLASS:
            return User(m)
        if kind == Vocabulary.RLibrary_CLASS:
            return RLibrary(m)
        if kind == Vocabulary.Operator_CLASS:
            return Operator(m)
        if kind == Vocabulary.WorkerEndpoint_CLASS:
            return WorkerEndpoint(m)
        if kind == Vocabulary.ProjectDocument_CLASS:
            return ProjectDocument(m)
        if kind == Vocabulary.Project_CLASS:
            return Project(m)
        if kind == Vocabulary.SubscriptionPlan_CLASS:
            return SubscriptionPlan(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        if kind == Vocabulary.ProjectTask_CLASS:
            return ProjectTask(m)
        if kind == Vocabulary.GlTask_CLASS:
            return GlTask(m)
        if kind == Vocabulary.CreateGitOperatorTask_CLASS:
            return CreateGitOperatorTask(m)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        if kind == Vocabulary.PatchRecords_CLASS:
            return PatchRecords(m)
        if kind == Vocabulary.TaskEvent_CLASS:
            return TaskEvent(m)
        if kind == Vocabulary.GenericEvent_CLASS:
            return GenericEvent(m)
        if kind == Vocabulary.GarbageObject_CLASS:
            return GarbageObject(m)
        if kind == Vocabulary.Activity_CLASS:
            return Activity(m)
        if kind == Vocabulary.Document_CLASS:
            return Document(m)
        if kind == Vocabulary.Lock_CLASS:
            return Lock(m)
        if kind == Vocabulary.Task_CLASS:
            return Task(m)
        if kind == Vocabulary.Event_CLASS:
            return Event(m)
        if kind == Vocabulary.UserSecret_CLASS:
            return UserSecret(m)
        if kind == Vocabulary.Column_CLASS:
            return Column(m)
        if kind == Vocabulary.StartProcess_CLASS:
            return StartProcess(m)
        if kind == Vocabulary.Relation_CLASS:
            return Relation(m)
        if kind == Vocabulary.Step_CLASS:
            return Step(m)
        if kind == Vocabulary.Port_CLASS:
            return Port(m)
        if kind == Vocabulary.PersistentObject_CLASS:
            return PersistentObject(m)
        if kind == Vocabulary.Link_CLASS:
            return Link(m)
        if kind == Vocabulary.ColumnSchema_CLASS:
            return ColumnSchema(m)
        raise ValueError("bad kind : " + kind +
                         " for class IdObject in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.IdObject_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.IdObject_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.id_DP] = self.id
        return m


class IdObject(IdObjectBase):
    def __init__(self, m=None):
        super().__init__(m)


class PersistentObjectBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isDeleted = True
            self.rev = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PersistentObject_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.isDeleted = m[Vocabulary.isDeleted_DP]
        self.rev = m[Vocabulary.rev_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PersistentObject_CLASS:
            return PersistentObject(m)
        if kind == Vocabulary.GarbageTasks_CLASS:
            return GarbageTasks(m)
        if kind == Vocabulary.GarbageTasks2_CLASS:
            return GarbageTasks2(m)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        if kind == Vocabulary.User_CLASS:
            return User(m)
        if kind == Vocabulary.RLibrary_CLASS:
            return RLibrary(m)
        if kind == Vocabulary.Operator_CLASS:
            return Operator(m)
        if kind == Vocabulary.WorkerEndpoint_CLASS:
            return WorkerEndpoint(m)
        if kind == Vocabulary.ProjectDocument_CLASS:
            return ProjectDocument(m)
        if kind == Vocabulary.Project_CLASS:
            return Project(m)
        if kind == Vocabulary.SubscriptionPlan_CLASS:
            return SubscriptionPlan(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        if kind == Vocabulary.ProjectTask_CLASS:
            return ProjectTask(m)
        if kind == Vocabulary.GlTask_CLASS:
            return GlTask(m)
        if kind == Vocabulary.CreateGitOperatorTask_CLASS:
            return CreateGitOperatorTask(m)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        if kind == Vocabulary.PatchRecords_CLASS:
            return PatchRecords(m)
        if kind == Vocabulary.TaskEvent_CLASS:
            return TaskEvent(m)
        if kind == Vocabulary.GenericEvent_CLASS:
            return GenericEvent(m)
        if kind == Vocabulary.GarbageObject_CLASS:
            return GarbageObject(m)
        if kind == Vocabulary.Activity_CLASS:
            return Activity(m)
        if kind == Vocabulary.Document_CLASS:
            return Document(m)
        if kind == Vocabulary.Lock_CLASS:
            return Lock(m)
        if kind == Vocabulary.Task_CLASS:
            return Task(m)
        if kind == Vocabulary.Event_CLASS:
            return Event(m)
        if kind == Vocabulary.UserSecret_CLASS:
            return UserSecret(m)
        raise ValueError("bad kind : " + kind +
                         " for class PersistentObject in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PersistentObject_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PersistentObject_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.isDeleted_DP] = self.isDeleted
        m[Vocabulary.rev_DP] = self.rev
        return m


class PersistentObject(PersistentObjectBase):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isDeleted = False
        else:
            self.fromJson(m)


class DocumentBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.description = ""
            self.name = ""
            self.createdBy = ""
            self.tags = list()
            self.version = ""
            self.authors = list()
            self.isPublic = True
            self.acl = Acl()
            self.createdDate = Date()
            self.lastModifiedDate = Date()
            self.urls = list()
            self.meta = list()
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Document_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.description = m[Vocabulary.description_DP]
        self.name = m[Vocabulary.name_DP]
        self.createdBy = m[Vocabulary.createdBy_DP]
        if m.get(Vocabulary.tags_DP) is None:
            self.tags = list()
        else:
            self.tags = m[Vocabulary.tags_DP]
        self.version = m[Vocabulary.version_DP]
        if m.get(Vocabulary.authors_DP) is None:
            self.authors = list()
        else:
            self.authors = m[Vocabulary.authors_DP]
        self.isPublic = m[Vocabulary.isPublic_DP]
        if m.get(Vocabulary.acl_OP) is None:
            self.acl = Acl()
        else:
            self.acl = AclBase.createFromJson(m.get(Vocabulary.acl_OP))
        if m.get(Vocabulary.createdDate_OP) is None:
            self.createdDate = Date()
        else:
            self.createdDate = DateBase.createFromJson(
                m.get(Vocabulary.createdDate_OP))
        if m.get(Vocabulary.lastModifiedDate_OP) is None:
            self.lastModifiedDate = Date()
        else:
            self.lastModifiedDate = DateBase.createFromJson(
                m.get(Vocabulary.lastModifiedDate_OP))
        if m.get(Vocabulary.urls_OP) is None:
            self.urls = list()
        else:
            self.urls = list()
            for o in m.get(Vocabulary.urls_OP):
                self.urls.append(UrlBase.createFromJson(o))
        if m.get(Vocabulary.meta_OP) is None:
            self.meta = list()
        else:
            self.meta = list()
            for o in m.get(Vocabulary.meta_OP):
                self.meta.append(PairBase.createFromJson(o))
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Document_CLASS:
            return Document(m)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        if kind == Vocabulary.User_CLASS:
            return User(m)
        if kind == Vocabulary.RLibrary_CLASS:
            return RLibrary(m)
        if kind == Vocabulary.Operator_CLASS:
            return Operator(m)
        if kind == Vocabulary.WorkerEndpoint_CLASS:
            return WorkerEndpoint(m)
        if kind == Vocabulary.ProjectDocument_CLASS:
            return ProjectDocument(m)
        if kind == Vocabulary.Project_CLASS:
            return Project(m)
        if kind == Vocabulary.SubscriptionPlan_CLASS:
            return SubscriptionPlan(m)
        raise ValueError("bad kind : " + kind +
                         " for class Document in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Document_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Document_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.description_DP] = self.description
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.createdBy_DP] = self.createdBy
        m[Vocabulary.acl_OP] = self.acl if self.acl is None else self.acl.toJson()
        m[Vocabulary.createdDate_OP] = self.createdDate if self.createdDate is None else self.createdDate.toJson()
        m[Vocabulary.lastModifiedDate_OP] = self.lastModifiedDate if self.lastModifiedDate is None else self.lastModifiedDate.toJson()
        m[Vocabulary.urls_OP] = list(map(lambda x: x.toJson(), self.urls))
        m[Vocabulary.tags_DP] = self.tags
        m[Vocabulary.meta_OP] = list(map(lambda x: x.toJson(), self.meta))
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        m[Vocabulary.version_DP] = self.version
        m[Vocabulary.authors_DP] = self.authors
        m[Vocabulary.isPublic_DP] = self.isPublic
        return m


class Document(DocumentBase):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isPublic = False
        else:
            self.fromJson(m)


class UserBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.email = ""
            self.isValidated = True
            self.domain = ""
            self.roles = list()
            self.invitedByUsername = ""
            self.invitationCounts = 0
            self.maxInvitation = 0
            self.teamAcl = Acl()
            self.billingInfo = BillingInfo()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.User_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.email = m[Vocabulary.email_DP]
        self.isValidated = m[Vocabulary.isValidated_DP]
        self.domain = m[Vocabulary.domain_DP]
        if m.get(Vocabulary.roles_DP) is None:
            self.roles = list()
        else:
            self.roles = m[Vocabulary.roles_DP]
        self.invitedByUsername = m[Vocabulary.invitedByUsername_DP]
        self.invitationCounts = m[Vocabulary.invitationCounts_DP]
        self.maxInvitation = m[Vocabulary.maxInvitation_DP]
        if m.get(Vocabulary.teamAcl_OP) is None:
            self.teamAcl = Acl()
        else:
            self.teamAcl = AclBase.createFromJson(m.get(Vocabulary.teamAcl_OP))
        if m.get(Vocabulary.billingInfo_OP) is None:
            self.billingInfo = BillingInfo()
        else:
            self.billingInfo = BillingInfoBase.createFromJson(
                m.get(Vocabulary.billingInfo_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.User_CLASS:
            return User(m)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        raise ValueError("bad kind : " + kind +
                         " for class User in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.User_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.User_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.email_DP] = self.email
        m[Vocabulary.isValidated_DP] = self.isValidated
        m[Vocabulary.domain_DP] = self.domain
        m[Vocabulary.roles_DP] = self.roles
        m[Vocabulary.teamAcl_OP] = self.teamAcl if self.teamAcl is None else self.teamAcl.toJson()
        m[Vocabulary.invitedByUsername_DP] = self.invitedByUsername
        m[Vocabulary.invitationCounts_DP] = self.invitationCounts
        m[Vocabulary.maxInvitation_DP] = self.maxInvitation
        m[Vocabulary.billingInfo_OP] = self.billingInfo if self.billingInfo is None else self.billingInfo.toJson()
        return m


class User(UserBase):
    def __init__(self, m=None):
        super().__init__(m)


class TeamBase(User):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Team_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Team_CLASS:
            return Team(m)
        raise ValueError("bad kind : " + kind +
                         " for class Team in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Team_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Team_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class Team(TeamBase):
    def __init__(self, m=None):
        super().__init__(m)


class PropertyBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.description = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Property_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.description = m[Vocabulary.description_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Property_CLASS:
            return Property(m)
        if kind == Vocabulary.EnumeratedProperty_CLASS:
            return EnumeratedProperty(m)
        if kind == Vocabulary.FactorsProperty_CLASS:
            return FactorsProperty(m)
        if kind == Vocabulary.FormulaProperty_CLASS:
            return FormulaProperty(m)
        if kind == Vocabulary.DoubleProperty_CLASS:
            return DoubleProperty(m)
        if kind == Vocabulary.StringProperty_CLASS:
            return StringProperty(m)
        if kind == Vocabulary.BooleanProperty_CLASS:
            return BooleanProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class Property in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Property_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Property_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.description_DP] = self.description
        return m


class Property(PropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class DoublePropertyBase(Property):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.defaultValue = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DoubleProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.defaultValue = m[Vocabulary.defaultValue_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DoubleProperty_CLASS:
            return DoubleProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class DoubleProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DoubleProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DoubleProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.defaultValue_DP] = self.defaultValue
        return m


class DoubleProperty(DoublePropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class RectangleBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.extent = Point()
            self.topLeft = Point()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Rectangle_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.extent_OP) is None:
            self.extent = Point()
        else:
            self.extent = PointBase.createFromJson(m.get(Vocabulary.extent_OP))
        if m.get(Vocabulary.topLeft_OP) is None:
            self.topLeft = Point()
        else:
            self.topLeft = PointBase.createFromJson(
                m.get(Vocabulary.topLeft_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Rectangle_CLASS:
            return Rectangle(m)
        raise ValueError("bad kind : " + kind +
                         " for class Rectangle in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Rectangle_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Rectangle_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.extent_OP] = self.extent if self.extent is None else self.extent.toJson()
        m[Vocabulary.topLeft_OP] = self.topLeft if self.topLeft is None else self.topLeft.toJson()
        return m


class Rectangle(RectangleBase):
    def __init__(self, m=None):
        super().__init__(m)


class StateBase(SciObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.State_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.State_CLASS:
            return State(m)
        if kind == Vocabulary.RunningState_CLASS:
            return RunningState(m)
        if kind == Vocabulary.RunningDependentState_CLASS:
            return RunningDependentState(m)
        if kind == Vocabulary.FailedState_CLASS:
            return FailedState(m)
        if kind == Vocabulary.CanceledState_CLASS:
            return CanceledState(m)
        if kind == Vocabulary.DoneState_CLASS:
            return DoneState(m)
        if kind == Vocabulary.InitState_CLASS:
            return InitState(m)
        if kind == Vocabulary.PendingState_CLASS:
            return PendingState(m)
        raise ValueError("bad kind : " + kind +
                         " for class State in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.State_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.State_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class State(StateBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunningStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunningState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunningState_CLASS:
            return RunningState(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunningState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunningState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunningState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class RunningState(RunningStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class RelationBase(IdObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Relation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Relation_CLASS:
            return Relation(m)
        if kind == Vocabulary.TableRelation_CLASS:
            return TableRelation(m)
        if kind == Vocabulary.ReferenceRelation_CLASS:
            return ReferenceRelation(m)
        if kind == Vocabulary.WhereRelation_CLASS:
            return WhereRelation(m)
        if kind == Vocabulary.DistinctRelation_CLASS:
            return DistinctRelation(m)
        if kind == Vocabulary.InMemoryRelation_CLASS:
            return InMemoryRelation(m)
        if kind == Vocabulary.RenameRelation_CLASS:
            return RenameRelation(m)
        if kind == Vocabulary.UnionRelation_CLASS:
            return UnionRelation(m)
        if kind == Vocabulary.SimpleRelation_CLASS:
            return SimpleRelation(m)
        if kind == Vocabulary.GatherRelation_CLASS:
            return GatherRelation(m)
        if kind == Vocabulary.CompositeRelation_CLASS:
            return CompositeRelation(m)
        if kind == Vocabulary.GroupByRelation_CLASS:
            return GroupByRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class Relation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Relation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Relation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class Relation(RelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class WhereRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.relation = Relation()
            self.filters = Filters()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.WhereRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = Filters()
        else:
            self.filters = FiltersBase.createFromJson(
                m.get(Vocabulary.filters_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.WhereRelation_CLASS:
            return WhereRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class WhereRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.WhereRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.WhereRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.filters_OP] = self.filters if self.filters is None else self.filters.toJson()
        return m


class WhereRelation(WhereRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class ProfileBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Profile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Profile_CLASS:
            return Profile(m)
        if kind == Vocabulary.StorageProfile_CLASS:
            return StorageProfile(m)
        if kind == Vocabulary.RunProfile_CLASS:
            return RunProfile(m)
        if kind == Vocabulary.CpuTimeProfile_CLASS:
            return CpuTimeProfile(m)
        if kind == Vocabulary.TableProfile_CLASS:
            return TableProfile(m)
        if kind == Vocabulary.ApiCallProfile_CLASS:
            return ApiCallProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class Profile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Profile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Profile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        return m


class Profile(ProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class StorageProfileBase(Profile):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.size = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StorageProfile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.size = m[Vocabulary.size_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StorageProfile_CLASS:
            return StorageProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class StorageProfile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StorageProfile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StorageProfile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.size_DP] = self.size
        return m


class StorageProfile(StorageProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class ResourceSummaryBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.storage = 0.0
            self.usedStorage = 0.0
            self.cpuTime = 0.0
            self.usedCpuTime = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ResourceSummary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.storage = m[Vocabulary.storage_DP]
        self.usedStorage = m[Vocabulary.usedStorage_DP]
        self.cpuTime = m[Vocabulary.cpuTime_DP]
        self.usedCpuTime = m[Vocabulary.usedCpuTime_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ResourceSummary_CLASS:
            return ResourceSummary(m)
        raise ValueError("bad kind : " + kind +
                         " for class ResourceSummary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ResourceSummary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ResourceSummary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.storage_DP] = self.storage
        m[Vocabulary.usedStorage_DP] = self.usedStorage
        m[Vocabulary.cpuTime_DP] = self.cpuTime
        m[Vocabulary.usedCpuTime_DP] = self.usedCpuTime
        return m


class ResourceSummary(ResourceSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)


class BillingInfoBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.firstName = ""
            self.lastName = ""
            self.companyName = ""
            self.taxId = TaxId()
            self.address = Address()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.BillingInfo_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.firstName = m[Vocabulary.firstName_DP]
        self.lastName = m[Vocabulary.lastName_DP]
        self.companyName = m[Vocabulary.companyName_DP]
        if m.get(Vocabulary.taxId_OP) is None:
            self.taxId = TaxId()
        else:
            self.taxId = TaxIdBase.createFromJson(m.get(Vocabulary.taxId_OP))
        if m.get(Vocabulary.address_OP) is None:
            self.address = Address()
        else:
            self.address = AddressBase.createFromJson(
                m.get(Vocabulary.address_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.BillingInfo_CLASS:
            return BillingInfo(m)
        raise ValueError("bad kind : " + kind +
                         " for class BillingInfo in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.BillingInfo_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.BillingInfo_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.firstName_DP] = self.firstName
        m[Vocabulary.lastName_DP] = self.lastName
        m[Vocabulary.companyName_DP] = self.companyName
        m[Vocabulary.taxId_OP] = self.taxId if self.taxId is None else self.taxId.toJson()
        m[Vocabulary.address_OP] = self.address if self.address is None else self.address.toJson()
        return m


class BillingInfo(BillingInfoBase):
    def __init__(self, m=None):
        super().__init__(m)


class EventBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.date = Date()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Event_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.date_OP) is None:
            self.date = Date()
        else:
            self.date = DateBase.createFromJson(m.get(Vocabulary.date_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Event_CLASS:
            return Event(m)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        if kind == Vocabulary.PatchRecords_CLASS:
            return PatchRecords(m)
        if kind == Vocabulary.TaskEvent_CLASS:
            return TaskEvent(m)
        if kind == Vocabulary.GenericEvent_CLASS:
            return GenericEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class Event in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Event_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Event_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.date_OP] = self.date if self.date is None else self.date.toJson()
        return m


class Event(EventBase):
    def __init__(self, m=None):
        super().__init__(m)


class PatchRecordsBase(Event):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.u = ""
            self.cI = ""
            self.oI = ""
            self.oR = ""
            self.oK = ""
            self.s = 0
            self.rs = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PatchRecords_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.u = m[Vocabulary.u_DP]
        self.cI = m[Vocabulary.cI_DP]
        self.oI = m[Vocabulary.oI_DP]
        self.oR = m[Vocabulary.oR_DP]
        self.oK = m[Vocabulary.oK_DP]
        self.s = m[Vocabulary.s_DP]
        if m.get(Vocabulary.rs_OP) is None:
            self.rs = list()
        else:
            self.rs = list()
            for o in m.get(Vocabulary.rs_OP):
                self.rs.append(PatchRecordBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PatchRecords_CLASS:
            return PatchRecords(m)
        raise ValueError("bad kind : " + kind +
                         " for class PatchRecords in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PatchRecords_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PatchRecords_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.u_DP] = self.u
        m[Vocabulary.cI_DP] = self.cI
        m[Vocabulary.oI_DP] = self.oI
        m[Vocabulary.oR_DP] = self.oR
        m[Vocabulary.oK_DP] = self.oK
        m[Vocabulary.s_DP] = self.s
        m[Vocabulary.rs_OP] = list(map(lambda x: x.toJson(), self.rs))
        return m


class PatchRecords(PatchRecordsBase):
    def __init__(self, m=None):
        super().__init__(m)


class GarbageObjectBase(PersistentObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GarbageObject_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GarbageObject_CLASS:
            return GarbageObject(m)
        if kind == Vocabulary.GarbageTasks_CLASS:
            return GarbageTasks(m)
        if kind == Vocabulary.GarbageTasks2_CLASS:
            return GarbageTasks2(m)
        raise ValueError("bad kind : " + kind +
                         " for class GarbageObject in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GarbageObject_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GarbageObject_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class GarbageObject(GarbageObjectBase):
    def __init__(self, m=None):
        super().__init__(m)


class GarbageTasksBase(GarbageObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.workflowId = ""
            self.deletedTaskIds = list()
            self.addedTaskIds = list()
            self.deletedStepIds = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GarbageTasks_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.workflowId = m[Vocabulary.workflowId_DP]
        if m.get(Vocabulary.deletedTaskIds_DP) is None:
            self.deletedTaskIds = list()
        else:
            self.deletedTaskIds = m[Vocabulary.deletedTaskIds_DP]
        if m.get(Vocabulary.addedTaskIds_DP) is None:
            self.addedTaskIds = list()
        else:
            self.addedTaskIds = m[Vocabulary.addedTaskIds_DP]
        if m.get(Vocabulary.deletedStepIds_DP) is None:
            self.deletedStepIds = list()
        else:
            self.deletedStepIds = m[Vocabulary.deletedStepIds_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GarbageTasks_CLASS:
            return GarbageTasks(m)
        raise ValueError("bad kind : " + kind +
                         " for class GarbageTasks in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GarbageTasks_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GarbageTasks_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.workflowId_DP] = self.workflowId
        m[Vocabulary.deletedTaskIds_DP] = self.deletedTaskIds
        m[Vocabulary.addedTaskIds_DP] = self.addedTaskIds
        m[Vocabulary.deletedStepIds_DP] = self.deletedStepIds
        return m


class GarbageTasks(GarbageTasksBase):
    def __init__(self, m=None):
        super().__init__(m)


class VersionBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.major = 0
            self.minor = 0
            self.patch = 0
            self.tag = ""
            self.date = ""
            self.commit = ""
            self.features = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Version_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.major = m[Vocabulary.major_DP]
        self.minor = m[Vocabulary.minor_DP]
        self.patch = m[Vocabulary.patch_DP]
        self.tag = m[Vocabulary.tag_DP]
        self.date = m[Vocabulary.date_DP]
        self.commit = m[Vocabulary.commit_DP]
        if m.get(Vocabulary.features_DP) is None:
            self.features = list()
        else:
            self.features = m[Vocabulary.features_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Version_CLASS:
            return Version(m)
        raise ValueError("bad kind : " + kind +
                         " for class Version in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Version_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Version_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.major_DP] = self.major
        m[Vocabulary.minor_DP] = self.minor
        m[Vocabulary.patch_DP] = self.patch
        m[Vocabulary.tag_DP] = self.tag
        m[Vocabulary.date_DP] = self.date
        m[Vocabulary.commit_DP] = self.commit
        m[Vocabulary.features_DP] = self.features
        return m


class Version(VersionBase):
    def __init__(self, m=None):
        super().__init__(m)


class FiltersBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.removeNaN = True
            self.namedFilters = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Filters_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.removeNaN = m[Vocabulary.removeNaN_DP]
        if m.get(Vocabulary.namedFilters_OP) is None:
            self.namedFilters = list()
        else:
            self.namedFilters = list()
            for o in m.get(Vocabulary.namedFilters_OP):
                self.namedFilters.append(NamedFilterBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Filters_CLASS:
            return Filters(m)
        raise ValueError("bad kind : " + kind +
                         " for class Filters in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Filters_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Filters_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.removeNaN_DP] = self.removeNaN
        m[Vocabulary.namedFilters_OP] = list(
            map(lambda x: x.toJson(), self.namedFilters))
        return m


class Filters(FiltersBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.properties = Properties()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Chart_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = Properties()
        else:
            self.properties = PropertiesBase.createFromJson(
                m.get(Vocabulary.properties_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Chart_CLASS:
            return Chart(m)
        if kind == Vocabulary.ChartLine_CLASS:
            return ChartLine(m)
        if kind == Vocabulary.ChartPoint_CLASS:
            return ChartPoint(m)
        if kind == Vocabulary.ChartHeatmap_CLASS:
            return ChartHeatmap(m)
        if kind == Vocabulary.ChartBar_CLASS:
            return ChartBar(m)
        if kind == Vocabulary.ChartSize_CLASS:
            return ChartSize(m)
        raise ValueError("bad kind : " + kind +
                         " for class Chart in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Chart_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Chart_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.properties_OP] = self.properties if self.properties is None else self.properties.toJson()
        return m


class Chart(ChartBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartHeatmapBase(Chart):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ChartHeatmap_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ChartHeatmap_CLASS:
            return ChartHeatmap(m)
        raise ValueError("bad kind : " + kind +
                         " for class ChartHeatmap in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ChartHeatmap_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ChartHeatmap_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ChartHeatmap(ChartHeatmapBase):
    def __init__(self, m=None):
        super().__init__(m)


class CubeQueryBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.qtHash = ""
            self.columnHash = ""
            self.rowHash = ""
            self.relation = Relation()
            self.colColumns = list()
            self.rowColumns = list()
            self.axisQueries = list()
            self.filters = Filters()
            self.operatorSettings = OperatorSettings()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CubeQuery_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.qtHash = m[Vocabulary.qtHash_DP]
        self.columnHash = m[Vocabulary.columnHash_DP]
        self.rowHash = m[Vocabulary.rowHash_DP]
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))
        if m.get(Vocabulary.colColumns_OP) is None:
            self.colColumns = list()
        else:
            self.colColumns = list()
            for o in m.get(Vocabulary.colColumns_OP):
                self.colColumns.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.rowColumns_OP) is None:
            self.rowColumns = list()
        else:
            self.rowColumns = list()
            for o in m.get(Vocabulary.rowColumns_OP):
                self.rowColumns.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.axisQueries_OP) is None:
            self.axisQueries = list()
        else:
            self.axisQueries = list()
            for o in m.get(Vocabulary.axisQueries_OP):
                self.axisQueries.append(CubeAxisQueryBase.createFromJson(o))
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = Filters()
        else:
            self.filters = FiltersBase.createFromJson(
                m.get(Vocabulary.filters_OP))
        if m.get(Vocabulary.operatorSettings_OP) is None:
            self.operatorSettings = OperatorSettings()
        else:
            self.operatorSettings = OperatorSettingsBase.createFromJson(
                m.get(Vocabulary.operatorSettings_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CubeQuery_CLASS:
            return CubeQuery(m)
        raise ValueError("bad kind : " + kind +
                         " for class CubeQuery in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CubeQuery_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CubeQuery_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.colColumns_OP] = list(
            map(lambda x: x.toJson(), self.colColumns))
        m[Vocabulary.rowColumns_OP] = list(
            map(lambda x: x.toJson(), self.rowColumns))
        m[Vocabulary.axisQueries_OP] = list(
            map(lambda x: x.toJson(), self.axisQueries))
        m[Vocabulary.filters_OP] = self.filters if self.filters is None else self.filters.toJson()
        m[Vocabulary.operatorSettings_OP] = self.operatorSettings if self.operatorSettings is None else self.operatorSettings.toJson()
        m[Vocabulary.qtHash_DP] = self.qtHash
        m[Vocabulary.columnHash_DP] = self.columnHash
        m[Vocabulary.rowHash_DP] = self.rowHash
        return m


class CubeQuery(CubeQueryBase):
    def __init__(self, m=None):
        super().__init__(m)


class RLibraryBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.rDescription = RDescription()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RLibrary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.rDescription_OP) is None:
            self.rDescription = RDescription()
        else:
            self.rDescription = RDescriptionBase.createFromJson(
                m.get(Vocabulary.rDescription_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RLibrary_CLASS:
            return RLibrary(m)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        raise ValueError("bad kind : " + kind +
                         " for class RLibrary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RLibrary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RLibrary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.rDescription_OP] = self.rDescription if self.rDescription is None else self.rDescription.toJson()
        return m


class RLibrary(RLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)


class FilterTopExprBase(SciObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FilterTopExpr_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FilterTopExpr_CLASS:
            return FilterTopExpr(m)
        if kind == Vocabulary.NamedFilter_CLASS:
            return NamedFilter(m)
        if kind == Vocabulary.Filter_CLASS:
            return Filter(m)
        if kind == Vocabulary.FilterExpr_CLASS:
            return FilterExpr(m)
        raise ValueError("bad kind : " + kind +
                         " for class FilterTopExpr in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FilterTopExpr_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FilterTopExpr_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class FilterTopExpr(FilterTopExprBase):
    def __init__(self, m=None):
        super().__init__(m)


class FilterBase(FilterTopExpr):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.logical = ""
            self.isNot = True
            self.filterExprs = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Filter_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.logical = m[Vocabulary.logical_DP]
        self.isNot = m[Vocabulary.not_DP]
        if m.get(Vocabulary.filterExprs_OP) is None:
            self.filterExprs = list()
        else:
            self.filterExprs = list()
            for o in m.get(Vocabulary.filterExprs_OP):
                self.filterExprs.append(FilterTopExprBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Filter_CLASS:
            return Filter(m)
        if kind == Vocabulary.NamedFilter_CLASS:
            return NamedFilter(m)
        raise ValueError("bad kind : " + kind +
                         " for class Filter in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Filter_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Filter_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.logical_DP] = self.logical
        m[Vocabulary.not_DP] = self.isNot
        m[Vocabulary.filterExprs_OP] = list(
            map(lambda x: x.toJson(), self.filterExprs))
        return m


class Filter(FilterBase):
    def __init__(self, m=None):
        super().__init__(m)


class StepBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.groupId = ""
            self.name = ""
            self.inputs = list()
            self.outputs = list()
            self.rectangle = Rectangle()
            self.state = StepState()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Step_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.groupId = m[Vocabulary.groupId_DP]
        self.name = m[Vocabulary.name_DP]
        if m.get(Vocabulary.inputs_OP) is None:
            self.inputs = list()
        else:
            self.inputs = list()
            for o in m.get(Vocabulary.inputs_OP):
                self.inputs.append(InputPortBase.createFromJson(o))
        if m.get(Vocabulary.outputs_OP) is None:
            self.outputs = list()
        else:
            self.outputs = list()
            for o in m.get(Vocabulary.outputs_OP):
                self.outputs.append(OutputPortBase.createFromJson(o))
        if m.get(Vocabulary.rectangle_OP) is None:
            self.rectangle = Rectangle()
        else:
            self.rectangle = RectangleBase.createFromJson(
                m.get(Vocabulary.rectangle_OP))
        if m.get(Vocabulary.state_OP) is None:
            self.state = StepState()
        else:
            self.state = StepStateBase.createFromJson(
                m.get(Vocabulary.state_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Step_CLASS:
            return Step(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        if kind == Vocabulary.RelationStep_CLASS:
            return RelationStep(m)
        if kind == Vocabulary.ExportStep_CLASS:
            return ExportStep(m)
        if kind == Vocabulary.ModelStep_CLASS:
            return ModelStep(m)
        if kind == Vocabulary.ViewStep_CLASS:
            return ViewStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class Step in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Step_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Step_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.groupId_DP] = self.groupId
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.inputs_OP] = list(map(lambda x: x.toJson(), self.inputs))
        m[Vocabulary.outputs_OP] = list(
            map(lambda x: x.toJson(), self.outputs))
        m[Vocabulary.rectangle_OP] = self.rectangle if self.rectangle is None else self.rectangle.toJson()
        m[Vocabulary.state_OP] = self.state if self.state is None else self.state.toJson()
        return m


class Step(StepBase):
    def __init__(self, m=None):
        super().__init__(m)


class ModelStepBase(Step):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ModelStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ModelStep_CLASS:
            return ModelStep(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        if kind == Vocabulary.RelationStep_CLASS:
            return RelationStep(m)
        if kind == Vocabulary.ExportStep_CLASS:
            return ExportStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class ModelStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ModelStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ModelStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ModelStep(ModelStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class RelationStepBase(ModelStep):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RelationStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RelationStep_CLASS:
            return RelationStep(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class RelationStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RelationStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RelationStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class RelationStep(RelationStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class GroupStepBase(RelationStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.appId = ""
            self.appName = ""
            self.version = ""
            self.offset = Point()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GroupStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.appId = m[Vocabulary.appId_DP]
        self.appName = m[Vocabulary.appName_DP]
        self.version = m[Vocabulary.version_DP]
        if m.get(Vocabulary.offset_OP) is None:
            self.offset = Point()
        else:
            self.offset = PointBase.createFromJson(m.get(Vocabulary.offset_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GroupStep_CLASS:
            return GroupStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class GroupStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GroupStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GroupStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.appId_DP] = self.appId
        m[Vocabulary.appName_DP] = self.appName
        m[Vocabulary.version_DP] = self.version
        m[Vocabulary.offset_OP] = self.offset if self.offset is None else self.offset.toJson()
        return m


class GroupStep(GroupStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskEventBase(Event):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.taskId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.taskId = m[Vocabulary.taskId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskEvent_CLASS:
            return TaskEvent(m)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.taskId_DP] = self.taskId
        return m


class TaskEvent(TaskEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskLogEventBase(TaskEvent):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.message = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskLogEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.message = m[Vocabulary.message_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskLogEvent_CLASS:
            return TaskLogEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskLogEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskLogEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskLogEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.message_DP] = self.message
        return m


class TaskLogEvent(TaskLogEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class UserSessionBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.serverVersion = Version()
            self.user = User()
            self.token = Token()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.UserSession_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.serverVersion_OP) is None:
            self.serverVersion = Version()
        else:
            self.serverVersion = VersionBase.createFromJson(
                m.get(Vocabulary.serverVersion_OP))
        if m.get(Vocabulary.user_OP) is None:
            self.user = User()
        else:
            self.user = UserBase.createFromJson(m.get(Vocabulary.user_OP))
        if m.get(Vocabulary.token_OP) is None:
            self.token = Token()
        else:
            self.token = TokenBase.createFromJson(m.get(Vocabulary.token_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.UserSession_CLASS:
            return UserSession(m)
        raise ValueError("bad kind : " + kind +
                         " for class UserSession in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.UserSession_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.UserSession_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.serverVersion_OP] = self.serverVersion if self.serverVersion is None else self.serverVersion.toJson()
        m[Vocabulary.user_OP] = self.user if self.user is None else self.user.toJson()
        m[Vocabulary.token_OP] = self.token if self.token is None else self.token.toJson()
        return m


class UserSession(UserSessionBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.nRows = 0
            self.properties = TableProperties()
            self.columns = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Table_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.nRows = m[Vocabulary.nRows_DP]
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = TableProperties()
        else:
            self.properties = TablePropertiesBase.createFromJson(
                m.get(Vocabulary.properties_OP))
        if m.get(Vocabulary.columns_OP) is None:
            self.columns = list()
        else:
            self.columns = list()
            for o in m.get(Vocabulary.columns_OP):
                self.columns.append(ColumnBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Table_CLASS:
            return Table(m)
        raise ValueError("bad kind : " + kind +
                         " for class Table in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Table_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Table_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.nRows_DP] = self.nRows
        m[Vocabulary.properties_OP] = self.properties if self.properties is None else self.properties.toJson()
        m[Vocabulary.columns_OP] = list(
            map(lambda x: x.toJson(), self.columns))
        return m


class Table(TableBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.longDescription = ""
            self.properties = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Operator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.longDescription = m[Vocabulary.longDescription_DP]
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PropertyBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Operator_CLASS:
            return Operator(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class Operator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Operator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Operator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        m[Vocabulary.longDescription_DP] = self.longDescription
        return m


class Operator(OperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class GitOperatorBase(Operator):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.path = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GitOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.path = m[Vocabulary.path_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GitOperator_CLASS:
            return GitOperator(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class GitOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GitOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GitOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.path_DP] = self.path
        return m


class GitOperator(GitOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class DockerOperatorBase(GitOperator):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.container = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DockerOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.container = m[Vocabulary.container_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DockerOperator_CLASS:
            return DockerOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class DockerOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DockerOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DockerOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.container_DP] = self.container
        return m


class DockerOperator(DockerOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class AclBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.owner = ""
            self.aces = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Acl_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.owner = m[Vocabulary.owner_DP]
        if m.get(Vocabulary.aces_OP) is None:
            self.aces = list()
        else:
            self.aces = list()
            for o in m.get(Vocabulary.aces_OP):
                self.aces.append(AceBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Acl_CLASS:
            return Acl(m)
        raise ValueError("bad kind : " + kind +
                         " for class Acl in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Acl_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Acl_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.owner_DP] = self.owner
        m[Vocabulary.aces_OP] = list(map(lambda x: x.toJson(), self.aces))
        return m


class Acl(AclBase):
    def __init__(self, m=None):
        super().__init__(m)


class CubeAxisQueryBase(BaseObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.pointSize = 0
            self.chartType = ""
            self.yAxis = Factor()
            self.yAxisSettings = AxisSettings()
            self.xAxis = Factor()
            self.xAxisSettings = AxisSettings()
            self.errors = list()
            self.labels = list()
            self.colors = list()
            self.preprocessors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CubeAxisQuery_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.pointSize = m[Vocabulary.pointSize_DP]
        self.chartType = m[Vocabulary.chartType_DP]
        if m.get(Vocabulary.yAxis_OP) is None:
            self.yAxis = Factor()
        else:
            self.yAxis = FactorBase.createFromJson(m.get(Vocabulary.yAxis_OP))
        if m.get(Vocabulary.yAxisSettings_OP) is None:
            self.yAxisSettings = AxisSettings()
        else:
            self.yAxisSettings = AxisSettingsBase.createFromJson(
                m.get(Vocabulary.yAxisSettings_OP))
        if m.get(Vocabulary.xAxis_OP) is None:
            self.xAxis = Factor()
        else:
            self.xAxis = FactorBase.createFromJson(m.get(Vocabulary.xAxis_OP))
        if m.get(Vocabulary.xAxisSettings_OP) is None:
            self.xAxisSettings = AxisSettings()
        else:
            self.xAxisSettings = AxisSettingsBase.createFromJson(
                m.get(Vocabulary.xAxisSettings_OP))
        if m.get(Vocabulary.errors_OP) is None:
            self.errors = list()
        else:
            self.errors = list()
            for o in m.get(Vocabulary.errors_OP):
                self.errors.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.labels_OP) is None:
            self.labels = list()
        else:
            self.labels = list()
            for o in m.get(Vocabulary.labels_OP):
                self.labels.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.colors_OP) is None:
            self.colors = list()
        else:
            self.colors = list()
            for o in m.get(Vocabulary.colors_OP):
                self.colors.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.preprocessors_OP) is None:
            self.preprocessors = list()
        else:
            self.preprocessors = list()
            for o in m.get(Vocabulary.preprocessors_OP):
                self.preprocessors.append(PreProcessorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CubeAxisQuery_CLASS:
            return CubeAxisQuery(m)
        raise ValueError("bad kind : " + kind +
                         " for class CubeAxisQuery in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CubeAxisQuery_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CubeAxisQuery_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.pointSize_DP] = self.pointSize
        m[Vocabulary.chartType_DP] = self.chartType
        m[Vocabulary.yAxis_OP] = self.yAxis if self.yAxis is None else self.yAxis.toJson()
        m[Vocabulary.yAxisSettings_OP] = self.yAxisSettings if self.yAxisSettings is None else self.yAxisSettings.toJson()
        m[Vocabulary.xAxis_OP] = self.xAxis if self.xAxis is None else self.xAxis.toJson()
        m[Vocabulary.xAxisSettings_OP] = self.xAxisSettings if self.xAxisSettings is None else self.xAxisSettings.toJson()
        m[Vocabulary.errors_OP] = list(map(lambda x: x.toJson(), self.errors))
        m[Vocabulary.labels_OP] = list(map(lambda x: x.toJson(), self.labels))
        m[Vocabulary.colors_OP] = list(map(lambda x: x.toJson(), self.colors))
        m[Vocabulary.preprocessors_OP] = list(
            map(lambda x: x.toJson(), self.preprocessors))
        return m


class CubeAxisQuery(CubeAxisQueryBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskSummaryBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.n = 0
            self.duration = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskSummary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.n = m[Vocabulary.n_DP]
        self.duration = m[Vocabulary.duration_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskSummary_CLASS:
            return TaskSummary(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskSummary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskSummary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskSummary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.n_DP] = self.n
        m[Vocabulary.duration_DP] = self.duration
        return m


class TaskSummary(TaskSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunningDependentStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunningDependentState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunningDependentState_CLASS:
            return RunningDependentState(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunningDependentState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunningDependentState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunningDependentState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class RunningDependentState(RunningDependentStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class PaletteBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.backcolor = 0
            self.properties = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Palette_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.backcolor = m[Vocabulary.backcolor_DP]
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PropertyValueBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Palette_CLASS:
            return Palette(m)
        if kind == Vocabulary.JetPalette_CLASS:
            return JetPalette(m)
        if kind == Vocabulary.RampPalette_CLASS:
            return RampPalette(m)
        if kind == Vocabulary.CategoryPalette_CLASS:
            return CategoryPalette(m)
        raise ValueError("bad kind : " + kind +
                         " for class Palette in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Palette_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Palette_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.backcolor_DP] = self.backcolor
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        return m


class Palette(PaletteBase):
    def __init__(self, m=None):
        super().__init__(m)


class RampPaletteBase(Palette):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isUserDefined = True
            self.doubleColorElements = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RampPalette_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.isUserDefined = m[Vocabulary.isUserDefined_DP]
        if m.get(Vocabulary.doubleColorElements_OP) is None:
            self.doubleColorElements = list()
        else:
            self.doubleColorElements = list()
            for o in m.get(Vocabulary.doubleColorElements_OP):
                self.doubleColorElements.append(
                    DoubleColorElementBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RampPalette_CLASS:
            return RampPalette(m)
        if kind == Vocabulary.JetPalette_CLASS:
            return JetPalette(m)
        raise ValueError("bad kind : " + kind +
                         " for class RampPalette in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RampPalette_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RampPalette_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.isUserDefined_DP] = self.isUserDefined
        m[Vocabulary.doubleColorElements_OP] = list(
            map(lambda x: x.toJson(), self.doubleColorElements))
        return m


class RampPalette(RampPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)


class DistinctRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.group = list()
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DistinctRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.group_DP) is None:
            self.group = list()
        else:
            self.group = m[Vocabulary.group_DP]
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DistinctRelation_CLASS:
            return DistinctRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class DistinctRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DistinctRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DistinctRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.group_DP] = self.group
        return m


class DistinctRelation(DistinctRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.duration = 0.0
            self.owner = ""
            self.taskHash = ""
            self.channelId = ""
            self.environment = list()
            self.state = State()
            self.createdDate = Date()
            self.lastModifiedDate = Date()
            self.runDate = Date()
            self.completedDate = Date()
            self.aclContext = AclContext()
            self.meta = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Task_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.duration = m[Vocabulary.duration_DP]
        self.owner = m[Vocabulary.owner_DP]
        self.taskHash = m[Vocabulary.taskHash_DP]
        self.channelId = m[Vocabulary.channelId_DP]
        if m.get(Vocabulary.environment_OP) is None:
            self.environment = list()
        else:
            self.environment = list()
            for o in m.get(Vocabulary.environment_OP):
                self.environment.append(PairBase.createFromJson(o))
        if m.get(Vocabulary.state_OP) is None:
            self.state = State()
        else:
            self.state = StateBase.createFromJson(m.get(Vocabulary.state_OP))
        if m.get(Vocabulary.createdDate_OP) is None:
            self.createdDate = Date()
        else:
            self.createdDate = DateBase.createFromJson(
                m.get(Vocabulary.createdDate_OP))
        if m.get(Vocabulary.lastModifiedDate_OP) is None:
            self.lastModifiedDate = Date()
        else:
            self.lastModifiedDate = DateBase.createFromJson(
                m.get(Vocabulary.lastModifiedDate_OP))
        if m.get(Vocabulary.runDate_OP) is None:
            self.runDate = Date()
        else:
            self.runDate = DateBase.createFromJson(
                m.get(Vocabulary.runDate_OP))
        if m.get(Vocabulary.completedDate_OP) is None:
            self.completedDate = Date()
        else:
            self.completedDate = DateBase.createFromJson(
                m.get(Vocabulary.completedDate_OP))
        if m.get(Vocabulary.aclContext_OP) is None:
            self.aclContext = AclContext()
        else:
            self.aclContext = AclContextBase.createFromJson(
                m.get(Vocabulary.aclContext_OP))
        if m.get(Vocabulary.meta_OP) is None:
            self.meta = list()
        else:
            self.meta = list()
            for o in m.get(Vocabulary.meta_OP):
                self.meta.append(PairBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Task_CLASS:
            return Task(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        if kind == Vocabulary.ProjectTask_CLASS:
            return ProjectTask(m)
        if kind == Vocabulary.GlTask_CLASS:
            return GlTask(m)
        if kind == Vocabulary.CreateGitOperatorTask_CLASS:
            return CreateGitOperatorTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class Task in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Task_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Task_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.environment_OP] = list(
            map(lambda x: x.toJson(), self.environment))
        m[Vocabulary.state_OP] = self.state if self.state is None else self.state.toJson()
        m[Vocabulary.createdDate_OP] = self.createdDate if self.createdDate is None else self.createdDate.toJson()
        m[Vocabulary.lastModifiedDate_OP] = self.lastModifiedDate if self.lastModifiedDate is None else self.lastModifiedDate.toJson()
        m[Vocabulary.runDate_OP] = self.runDate if self.runDate is None else self.runDate.toJson()
        m[Vocabulary.completedDate_OP] = self.completedDate if self.completedDate is None else self.completedDate.toJson()
        m[Vocabulary.duration_DP] = self.duration
        m[Vocabulary.aclContext_OP] = self.aclContext if self.aclContext is None else self.aclContext.toJson()
        m[Vocabulary.owner_DP] = self.owner
        m[Vocabulary.taskHash_DP] = self.taskHash
        m[Vocabulary.channelId_DP] = self.channelId
        m[Vocabulary.meta_OP] = list(map(lambda x: x.toJson(), self.meta))
        return m


class Task(TaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ProjectTaskBase(Task):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.projectId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ProjectTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.projectId = m[Vocabulary.projectId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ProjectTask_CLASS:
            return ProjectTask(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ProjectTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ProjectTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ProjectTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.projectId_DP] = self.projectId
        return m


class ProjectTask(ProjectTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ExportWorkflowTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.workflowId = ""
            self.fileId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ExportWorkflowTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.workflowId = m[Vocabulary.workflowId_DP]
        self.fileId = m[Vocabulary.fileId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ExportWorkflowTask_CLASS:
            return ExportWorkflowTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ExportWorkflowTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ExportWorkflowTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ExportWorkflowTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.workflowId_DP] = self.workflowId
        m[Vocabulary.fileId_DP] = self.fileId
        return m


class ExportWorkflowTask(ExportWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class StartProcessBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.executable = ""
            self.arguments = list()
            self.timeout = 0
            self.pid = 0
            self.script = ""
            self.ulimits = Ulimits()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StartProcess_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.executable = m[Vocabulary.executable_DP]
        if m.get(Vocabulary.arguments_DP) is None:
            self.arguments = list()
        else:
            self.arguments = m[Vocabulary.arguments_DP]
        self.timeout = m[Vocabulary.timeout_DP]
        self.pid = m[Vocabulary.pid_DP]
        self.script = m[Vocabulary.script_DP]
        if m.get(Vocabulary.ulimits_OP) is None:
            self.ulimits = Ulimits()
        else:
            self.ulimits = UlimitsBase.createFromJson(
                m.get(Vocabulary.ulimits_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StartProcess_CLASS:
            return StartProcess(m)
        raise ValueError("bad kind : " + kind +
                         " for class StartProcess in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StartProcess_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StartProcess_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.executable_DP] = self.executable
        m[Vocabulary.arguments_DP] = self.arguments
        m[Vocabulary.ulimits_OP] = self.ulimits if self.ulimits is None else self.ulimits.toJson()
        m[Vocabulary.timeout_DP] = self.timeout
        m[Vocabulary.pid_DP] = self.pid
        m[Vocabulary.script_DP] = self.script
        return m


class StartProcess(StartProcessBase):
    def __init__(self, m=None):
        super().__init__(m)


class TokenBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.userId = ""
            self.token = ""
            self.domain = ""
            self.expiry = Date()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Token_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.userId = m[Vocabulary.userId_DP]
        self.token = m[Vocabulary.token_DP]
        self.domain = m[Vocabulary.domain_DP]
        if m.get(Vocabulary.expiry_OP) is None:
            self.expiry = Date()
        else:
            self.expiry = DateBase.createFromJson(m.get(Vocabulary.expiry_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Token_CLASS:
            return Token(m)
        raise ValueError("bad kind : " + kind +
                         " for class Token in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Token_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Token_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.userId_DP] = self.userId
        m[Vocabulary.expiry_OP] = self.expiry if self.expiry is None else self.expiry.toJson()
        m[Vocabulary.token_DP] = self.token
        m[Vocabulary.domain_DP] = self.domain
        return m


class Token(TokenBase):
    def __init__(self, m=None):
        super().__init__(m)


class ActivityCountBase(BaseObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.objectId = ""
            self.count = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ActivityCount_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.objectId = m[Vocabulary.objectId_DP]
        self.count = m[Vocabulary.count_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ActivityCount_CLASS:
            return ActivityCount(m)
        raise ValueError("bad kind : " + kind +
                         " for class ActivityCount in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ActivityCount_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ActivityCount_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.objectId_DP] = self.objectId
        m[Vocabulary.count_DP] = self.count
        return m


class ActivityCount(ActivityCountBase):
    def __init__(self, m=None):
        super().__init__(m)


class JoinOperatorBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.joinType = ""
            self.leftPair = ColumnPair()
            self.rightRelation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.JoinOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.joinType = m[Vocabulary.joinType_DP]
        if m.get(Vocabulary.leftPair_OP) is None:
            self.leftPair = ColumnPair()
        else:
            self.leftPair = ColumnPairBase.createFromJson(
                m.get(Vocabulary.leftPair_OP))
        if m.get(Vocabulary.rightRelation_OP) is None:
            self.rightRelation = Relation()
        else:
            self.rightRelation = RelationBase.createFromJson(
                m.get(Vocabulary.rightRelation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.JoinOperator_CLASS:
            return JoinOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class JoinOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.JoinOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.JoinOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.joinType_DP] = self.joinType
        m[Vocabulary.leftPair_OP] = self.leftPair if self.leftPair is None else self.leftPair.toJson()
        m[Vocabulary.rightRelation_OP] = self.rightRelation if self.rightRelation is None else self.rightRelation.toJson()
        return m


class JoinOperator(JoinOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorModelBase(SciObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OperatorModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OperatorModel_CLASS:
            return OperatorModel(m)
        if kind == Vocabulary.AnnotationOperatorModel_CLASS:
            return AnnotationOperatorModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class OperatorModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OperatorModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OperatorModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class OperatorModel(OperatorModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class FileMetadataBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.contentType = ""
            self.cacheControl = ""
            self.contentEncoding = ""
            self.contentLanguage = ""
            self.md5Hash = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FileMetadata_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.contentType = m[Vocabulary.contentType_DP]
        self.cacheControl = m[Vocabulary.cacheControl_DP]
        self.contentEncoding = m[Vocabulary.contentEncoding_DP]
        self.contentLanguage = m[Vocabulary.contentLanguage_DP]
        self.md5Hash = m[Vocabulary.md5Hash_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FileMetadata_CLASS:
            return FileMetadata(m)
        if kind == Vocabulary.CSVFileMetadata_CLASS:
            return CSVFileMetadata(m)
        raise ValueError("bad kind : " + kind +
                         " for class FileMetadata in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FileMetadata_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FileMetadata_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.contentType_DP] = self.contentType
        m[Vocabulary.cacheControl_DP] = self.cacheControl
        m[Vocabulary.contentEncoding_DP] = self.contentEncoding
        m[Vocabulary.contentLanguage_DP] = self.contentLanguage
        m[Vocabulary.md5Hash_DP] = self.md5Hash
        return m


class FileMetadata(FileMetadataBase):
    def __init__(self, m=None):
        super().__init__(m)


class CSVFileMetadataBase(FileMetadata):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.separator = ""
            self.quote = ""
            self.headers = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CSVFileMetadata_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.separator = m[Vocabulary.separator_DP]
        self.quote = m[Vocabulary.quote_DP]
        self.headers = m[Vocabulary.headers_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CSVFileMetadata_CLASS:
            return CSVFileMetadata(m)
        raise ValueError("bad kind : " + kind +
                         " for class CSVFileMetadata in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CSVFileMetadata_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CSVFileMetadata_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.separator_DP] = self.separator
        m[Vocabulary.quote_DP] = self.quote
        m[Vocabulary.headers_DP] = self.headers
        return m


class CSVFileMetadata(CSVFileMetadataBase):
    def __init__(self, m=None):
        super().__init__(m)


class StepModelBase(SciObject):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StepModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StepModel_CLASS:
            return StepModel(m)
        if kind == Vocabulary.TableStepModel_CLASS:
            return TableStepModel(m)
        if kind == Vocabulary.Crosstab_CLASS:
            return Crosstab(m)
        if kind == Vocabulary.JoinStepModel_CLASS:
            return JoinStepModel(m)
        if kind == Vocabulary.WizardStepModel_CLASS:
            return WizardStepModel(m)
        if kind == Vocabulary.MeltStepModel_CLASS:
            return MeltStepModel(m)
        if kind == Vocabulary.ExportModel_CLASS:
            return ExportModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class StepModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StepModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StepModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class StepModel(StepModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableStepModelBase(StepModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableStepModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableStepModel_CLASS:
            return TableStepModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableStepModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableStepModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableStepModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        return m


class TableStepModel(TableStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class NamespaceStepBase(RelationStep):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.NamespaceStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.NamespaceStep_CLASS:
            return NamespaceStep(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class NamespaceStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.NamespaceStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.NamespaceStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class NamespaceStep(NamespaceStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class MeltStepBase(NamespaceStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = MeltStepModel()
            self.meltedAttributes = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.MeltStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = MeltStepModel()
        else:
            self.model = MeltStepModelBase.createFromJson(
                m.get(Vocabulary.model_OP))
        if m.get(Vocabulary.meltedAttributes_OP) is None:
            self.meltedAttributes = list()
        else:
            self.meltedAttributes = list()
            for o in m.get(Vocabulary.meltedAttributes_OP):
                self.meltedAttributes.append(AttributeBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.MeltStep_CLASS:
            return MeltStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class MeltStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.MeltStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.MeltStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        m[Vocabulary.meltedAttributes_OP] = list(
            map(lambda x: x.toJson(), self.meltedAttributes))
        return m


class MeltStep(MeltStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class CrosstabTableBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.cellSize = 0.0
            self.offset = 0
            self.nRows = 0
            self.graphicalFactors = list()
            self.rectangleSelections = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CrosstabTable_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.cellSize = m[Vocabulary.cellSize_DP]
        self.offset = m[Vocabulary.offset_DP]
        self.nRows = m[Vocabulary.nRows_DP]
        if m.get(Vocabulary.graphicalFactors_OP) is None:
            self.graphicalFactors = list()
        else:
            self.graphicalFactors = list()
            for o in m.get(Vocabulary.graphicalFactors_OP):
                self.graphicalFactors.append(
                    GraphicalFactorBase.createFromJson(o))
        if m.get(Vocabulary.rectangleSelections_OP) is None:
            self.rectangleSelections = list()
        else:
            self.rectangleSelections = list()
            for o in m.get(Vocabulary.rectangleSelections_OP):
                self.rectangleSelections.append(
                    RectangleBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CrosstabTable_CLASS:
            return CrosstabTable(m)
        raise ValueError("bad kind : " + kind +
                         " for class CrosstabTable in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CrosstabTable_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CrosstabTable_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.cellSize_DP] = self.cellSize
        m[Vocabulary.offset_DP] = self.offset
        m[Vocabulary.graphicalFactors_OP] = list(
            map(lambda x: x.toJson(), self.graphicalFactors))
        m[Vocabulary.rectangleSelections_OP] = list(
            map(lambda x: x.toJson(), self.rectangleSelections))
        m[Vocabulary.nRows_DP] = self.nRows
        return m


class CrosstabTable(CrosstabTableBase):
    def __init__(self, m=None):
        super().__init__(m)


class XYAxisListBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.rectangleSelections = list()
            self.xyAxis = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.XYAxisList_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.rectangleSelections_OP) is None:
            self.rectangleSelections = list()
        else:
            self.rectangleSelections = list()
            for o in m.get(Vocabulary.rectangleSelections_OP):
                self.rectangleSelections.append(
                    RectangleBase.createFromJson(o))
        if m.get(Vocabulary.xyAxis_OP) is None:
            self.xyAxis = list()
        else:
            self.xyAxis = list()
            for o in m.get(Vocabulary.xyAxis_OP):
                self.xyAxis.append(XYAxisBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.XYAxisList_CLASS:
            return XYAxisList(m)
        raise ValueError("bad kind : " + kind +
                         " for class XYAxisList in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.XYAxisList_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.XYAxisList_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.rectangleSelections_OP] = list(
            map(lambda x: x.toJson(), self.rectangleSelections))
        m[Vocabulary.xyAxis_OP] = list(map(lambda x: x.toJson(), self.xyAxis))
        return m


class XYAxisList(XYAxisListBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColorElementBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.color = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ColorElement_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.color = m[Vocabulary.color_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ColorElement_CLASS:
            return ColorElement(m)
        if kind == Vocabulary.DoubleColorElement_CLASS:
            return DoubleColorElement(m)
        if kind == Vocabulary.StringColorElement_CLASS:
            return StringColorElement(m)
        raise ValueError("bad kind : " + kind +
                         " for class ColorElement in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ColorElement_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ColorElement_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.color_DP] = self.color
        return m


class ColorElement(ColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)


class DoubleColorElementBase(ColorElement):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.stringValue = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DoubleColorElement_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.stringValue = m[Vocabulary.stringValue_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DoubleColorElement_CLASS:
            return DoubleColorElement(m)
        raise ValueError("bad kind : " + kind +
                         " for class DoubleColorElement in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DoubleColorElement_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DoubleColorElement_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.stringValue_DP] = self.stringValue
        return m


class DoubleColorElement(DoubleColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskProgressEventBase(TaskEvent):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.message = ""
            self.total = 0
            self.actual = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskProgressEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.message = m[Vocabulary.message_DP]
        self.total = m[Vocabulary.total_DP]
        self.actual = m[Vocabulary.actual_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskProgressEvent_CLASS:
            return TaskProgressEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskProgressEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskProgressEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskProgressEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.message_DP] = self.message
        m[Vocabulary.total_DP] = self.total
        m[Vocabulary.actual_DP] = self.actual
        return m


class TaskProgressEvent(TaskProgressEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class CrosstabBase(StepModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.taskId = ""
            self.axis = XYAxisList()
            self.columnTable = CrosstabTable()
            self.filters = Filters()
            self.operatorSettings = OperatorSettings()
            self.rowTable = CrosstabTable()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Crosstab_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.taskId = m[Vocabulary.taskId_DP]
        if m.get(Vocabulary.axis_OP) is None:
            self.axis = XYAxisList()
        else:
            self.axis = XYAxisListBase.createFromJson(
                m.get(Vocabulary.axis_OP))
        if m.get(Vocabulary.columnTable_OP) is None:
            self.columnTable = CrosstabTable()
        else:
            self.columnTable = CrosstabTableBase.createFromJson(
                m.get(Vocabulary.columnTable_OP))
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = Filters()
        else:
            self.filters = FiltersBase.createFromJson(
                m.get(Vocabulary.filters_OP))
        if m.get(Vocabulary.operatorSettings_OP) is None:
            self.operatorSettings = OperatorSettings()
        else:
            self.operatorSettings = OperatorSettingsBase.createFromJson(
                m.get(Vocabulary.operatorSettings_OP))
        if m.get(Vocabulary.rowTable_OP) is None:
            self.rowTable = CrosstabTable()
        else:
            self.rowTable = CrosstabTableBase.createFromJson(
                m.get(Vocabulary.rowTable_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Crosstab_CLASS:
            return Crosstab(m)
        raise ValueError("bad kind : " + kind +
                         " for class Crosstab in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Crosstab_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Crosstab_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.axis_OP] = self.axis if self.axis is None else self.axis.toJson()
        m[Vocabulary.columnTable_OP] = self.columnTable if self.columnTable is None else self.columnTable.toJson()
        m[Vocabulary.filters_OP] = self.filters if self.filters is None else self.filters.toJson()
        m[Vocabulary.operatorSettings_OP] = self.operatorSettings if self.operatorSettings is None else self.operatorSettings.toJson()
        m[Vocabulary.rowTable_OP] = self.rowTable if self.rowTable is None else self.rowTable.toJson()
        m[Vocabulary.taskId_DP] = self.taskId
        return m


class Crosstab(CrosstabBase):
    def __init__(self, m=None):
        super().__init__(m)


class ProjectDocumentBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.projectId = ""
            self.folderId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ProjectDocument_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.projectId = m[Vocabulary.projectId_DP]
        self.folderId = m[Vocabulary.folderId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ProjectDocument_CLASS:
            return ProjectDocument(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        raise ValueError("bad kind : " + kind +
                         " for class ProjectDocument in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ProjectDocument_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ProjectDocument_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.projectId_DP] = self.projectId
        m[Vocabulary.folderId_DP] = self.folderId
        return m


class ProjectDocument(ProjectDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)


class IssueBase(ProjectDocument):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Issue_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Issue_CLASS:
            return Issue(m)
        raise ValueError("bad kind : " + kind +
                         " for class Issue in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Issue_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Issue_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class Issue(IssueBase):
    def __init__(self, m=None):
        super().__init__(m)


class PatchRecordBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.p = ""
            self.t = ""
            self.d = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PatchRecord_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.p = m[Vocabulary.p_DP]
        self.t = m[Vocabulary.t_DP]
        self.d = m[Vocabulary.d_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PatchRecord_CLASS:
            return PatchRecord(m)
        raise ValueError("bad kind : " + kind +
                         " for class PatchRecord in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PatchRecord_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PatchRecord_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.p_DP] = self.p
        m[Vocabulary.t_DP] = self.t
        m[Vocabulary.d_DP] = self.d
        return m


class PatchRecord(PatchRecordBase):
    def __init__(self, m=None):
        super().__init__(m)


class CubeQueryTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.removeOnGC = True
            self.schemaIds = list()
            self.query = CubeQuery()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CubeQueryTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.removeOnGC = m[Vocabulary.removeOnGC_DP]
        if m.get(Vocabulary.schemaIds_DP) is None:
            self.schemaIds = list()
        else:
            self.schemaIds = m[Vocabulary.schemaIds_DP]
        if m.get(Vocabulary.query_OP) is None:
            self.query = CubeQuery()
        else:
            self.query = CubeQueryBase.createFromJson(
                m.get(Vocabulary.query_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CubeQueryTask_CLASS:
            return CubeQueryTask(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class CubeQueryTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CubeQueryTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CubeQueryTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.query_OP] = self.query if self.query is None else self.query.toJson()
        m[Vocabulary.removeOnGC_DP] = self.removeOnGC
        m[Vocabulary.schemaIds_DP] = self.schemaIds
        return m


class CubeQueryTask(CubeQueryTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ComputationTaskBase(CubeQueryTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.parentTaskId = ""
            self.fileResultId = ""
            self.computedRelation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ComputationTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.parentTaskId = m[Vocabulary.parentTaskId_DP]
        self.fileResultId = m[Vocabulary.fileResultId_DP]
        if m.get(Vocabulary.computedRelation_OP) is None:
            self.computedRelation = Relation()
        else:
            self.computedRelation = RelationBase.createFromJson(
                m.get(Vocabulary.computedRelation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ComputationTask_CLASS:
            return ComputationTask(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ComputationTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ComputationTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ComputationTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.parentTaskId_DP] = self.parentTaskId
        m[Vocabulary.fileResultId_DP] = self.fileResultId
        m[Vocabulary.computedRelation_OP] = self.computedRelation if self.computedRelation is None else self.computedRelation.toJson()
        return m


class ComputationTask(ComputationTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class SaveComputationResultTaskBase(ComputationTask):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.SaveComputationResultTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.SaveComputationResultTask_CLASS:
            return SaveComputationResultTask(m)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class SaveComputationResultTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.SaveComputationResultTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.SaveComputationResultTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class SaveComputationResultTask(SaveComputationResultTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunComputationTaskBase(SaveComputationResultTask):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunComputationTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunComputationTask_CLASS:
            return RunComputationTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunComputationTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunComputationTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunComputationTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class RunComputationTask(RunComputationTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class WorkerEndpointBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.uri = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.WorkerEndpoint_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.uri = m[Vocabulary.uri_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.WorkerEndpoint_CLASS:
            return WorkerEndpoint(m)
        raise ValueError("bad kind : " + kind +
                         " for class WorkerEndpoint in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.WorkerEndpoint_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.WorkerEndpoint_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.uri_DP] = self.uri
        return m


class WorkerEndpoint(WorkerEndpointBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColumnSchemaMetaDataBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.sort = list()
            self.ascending = True
            self.quartiles = list()
            self.properties = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ColumnSchemaMetaData_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.sort_DP) is None:
            self.sort = list()
        else:
            self.sort = m[Vocabulary.sort_DP]
        self.ascending = m[Vocabulary.ascending_DP]
        if m.get(Vocabulary.quartiles_DP) is None:
            self.quartiles = list()
        else:
            self.quartiles = m[Vocabulary.quartiles_DP]
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PairBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ColumnSchemaMetaData_CLASS:
            return ColumnSchemaMetaData(m)
        raise ValueError("bad kind : " + kind +
                         " for class ColumnSchemaMetaData in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ColumnSchemaMetaData_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ColumnSchemaMetaData_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.sort_DP] = self.sort
        m[Vocabulary.ascending_DP] = self.ascending
        m[Vocabulary.quartiles_DP] = self.quartiles
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        return m


class ColumnSchemaMetaData(ColumnSchemaMetaDataBase):
    def __init__(self, m=None):
        super().__init__(m)


class PrivilegeBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.type = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Privilege_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.type = m[Vocabulary.type_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Privilege_CLASS:
            return Privilege(m)
        raise ValueError("bad kind : " + kind +
                         " for class Privilege in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Privilege_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Privilege_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.type_DP] = self.type
        return m


class Privilege(PrivilegeBase):
    def __init__(self, m=None):
        super().__init__(m)


class CSVTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.fileDocumentId = ""
            self.schemaId = ""
            self.valueName = ""
            self.variableName = ""
            self.gatherNames = list()
            self.schema = Schema()
            self.params = CSVParserParam()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CSVTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.fileDocumentId = m[Vocabulary.fileDocumentId_DP]
        self.schemaId = m[Vocabulary.schemaId_DP]
        self.valueName = m[Vocabulary.valueName_DP]
        self.variableName = m[Vocabulary.variableName_DP]
        if m.get(Vocabulary.gatherNames_DP) is None:
            self.gatherNames = list()
        else:
            self.gatherNames = m[Vocabulary.gatherNames_DP]
        if m.get(Vocabulary.schema_OP) is None:
            self.schema = Schema()
        else:
            self.schema = SchemaBase.createFromJson(
                m.get(Vocabulary.schema_OP))
        if m.get(Vocabulary.params_OP) is None:
            self.params = CSVParserParam()
        else:
            self.params = CSVParserParamBase.createFromJson(
                m.get(Vocabulary.params_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CSVTask_CLASS:
            return CSVTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class CSVTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CSVTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CSVTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.fileDocumentId_DP] = self.fileDocumentId
        m[Vocabulary.schemaId_DP] = self.schemaId
        m[Vocabulary.valueName_DP] = self.valueName
        m[Vocabulary.variableName_DP] = self.variableName
        m[Vocabulary.gatherNames_DP] = self.gatherNames
        m[Vocabulary.schema_OP] = self.schema if self.schema is None else self.schema.toJson()
        m[Vocabulary.params_OP] = self.params if self.params is None else self.params.toJson()
        return m


class CSVTask(CSVTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ActivityBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.type = ""
            self.objectKind = ""
            self.teamId = ""
            self.projectId = ""
            self.userId = ""
            self.projectName = ""
            self.isPublic = True
            self.date = Date()
            self.properties = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Activity_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.type = m[Vocabulary.type_DP]
        self.objectKind = m[Vocabulary.objectKind_DP]
        self.teamId = m[Vocabulary.teamId_DP]
        self.projectId = m[Vocabulary.projectId_DP]
        self.userId = m[Vocabulary.userId_DP]
        self.projectName = m[Vocabulary.projectName_DP]
        self.isPublic = m[Vocabulary.isPublic_DP]
        if m.get(Vocabulary.date_OP) is None:
            self.date = Date()
        else:
            self.date = DateBase.createFromJson(m.get(Vocabulary.date_OP))
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PairBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Activity_CLASS:
            return Activity(m)
        raise ValueError("bad kind : " + kind +
                         " for class Activity in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Activity_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Activity_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.objectKind_DP] = self.objectKind
        m[Vocabulary.date_OP] = self.date if self.date is None else self.date.toJson()
        m[Vocabulary.teamId_DP] = self.teamId
        m[Vocabulary.projectId_DP] = self.projectId
        m[Vocabulary.userId_DP] = self.userId
        m[Vocabulary.projectName_DP] = self.projectName
        m[Vocabulary.isPublic_DP] = self.isPublic
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        return m


class Activity(ActivityBase):
    def __init__(self, m=None):
        super().__init__(m)


class ViesInfoBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.countryCode = ""
            self.vatNumber = ""
            self.requestDate = ""
            self.valid = True
            self.name = ""
            self.address = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ViesInfo_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.countryCode = m[Vocabulary.countryCode_DP]
        self.vatNumber = m[Vocabulary.vatNumber_DP]
        self.requestDate = m[Vocabulary.requestDate_DP]
        self.valid = m[Vocabulary.valid_DP]
        self.name = m[Vocabulary.name_DP]
        self.address = m[Vocabulary.address_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ViesInfo_CLASS:
            return ViesInfo(m)
        raise ValueError("bad kind : " + kind +
                         " for class ViesInfo in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ViesInfo_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ViesInfo_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.countryCode_DP] = self.countryCode
        m[Vocabulary.vatNumber_DP] = self.vatNumber
        m[Vocabulary.requestDate_DP] = self.requestDate
        m[Vocabulary.valid_DP] = self.valid
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.address_DP] = self.address
        return m


class ViesInfo(ViesInfoBase):
    def __init__(self, m=None):
        super().__init__(m)


class JoinStepModelBase(StepModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.rightPrefix = ""
            self.leftFactors = list()
            self.rightFactors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.JoinStepModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.rightPrefix = m[Vocabulary.rightPrefix_DP]
        if m.get(Vocabulary.leftFactors_OP) is None:
            self.leftFactors = list()
        else:
            self.leftFactors = list()
            for o in m.get(Vocabulary.leftFactors_OP):
                self.leftFactors.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.rightFactors_OP) is None:
            self.rightFactors = list()
        else:
            self.rightFactors = list()
            for o in m.get(Vocabulary.rightFactors_OP):
                self.rightFactors.append(FactorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.JoinStepModel_CLASS:
            return JoinStepModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class JoinStepModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.JoinStepModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.JoinStepModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.leftFactors_OP] = list(
            map(lambda x: x.toJson(), self.leftFactors))
        m[Vocabulary.rightFactors_OP] = list(
            map(lambda x: x.toJson(), self.rightFactors))
        m[Vocabulary.rightPrefix_DP] = self.rightPrefix
        return m


class JoinStepModel(JoinStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class UlimitsBase(BaseObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.core_file_size = 0
            self.data_seg_size = 0
            self.scheduling_priority = 0
            self.file_size = 0
            self.pending_signals = 0
            self.max_locked_memory = 0
            self.max_memory_size = 0
            self.open_files = 0
            self.pipe_size = 0
            self.message_queues = 0
            self.real_time_priority = 0
            self.stack_size = 0
            self.cpu_time = 0
            self.max_user_processes = 0
            self.virtual_memory = 0
            self.file_locks = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Ulimits_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.core_file_size = m[Vocabulary.core_file_size_DP]
        self.data_seg_size = m[Vocabulary.data_seg_size_DP]
        self.scheduling_priority = m[Vocabulary.scheduling_priority_DP]
        self.file_size = m[Vocabulary.file_size_DP]
        self.pending_signals = m[Vocabulary.pending_signals_DP]
        self.max_locked_memory = m[Vocabulary.max_locked_memory_DP]
        self.max_memory_size = m[Vocabulary.max_memory_size_DP]
        self.open_files = m[Vocabulary.open_files_DP]
        self.pipe_size = m[Vocabulary.pipe_size_DP]
        self.message_queues = m[Vocabulary.message_queues_DP]
        self.real_time_priority = m[Vocabulary.real_time_priority_DP]
        self.stack_size = m[Vocabulary.stack_size_DP]
        self.cpu_time = m[Vocabulary.cpu_time_DP]
        self.max_user_processes = m[Vocabulary.max_user_processes_DP]
        self.virtual_memory = m[Vocabulary.virtual_memory_DP]
        self.file_locks = m[Vocabulary.file_locks_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Ulimits_CLASS:
            return Ulimits(m)
        raise ValueError("bad kind : " + kind +
                         " for class Ulimits in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Ulimits_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Ulimits_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.core_file_size_DP] = self.core_file_size
        m[Vocabulary.data_seg_size_DP] = self.data_seg_size
        m[Vocabulary.scheduling_priority_DP] = self.scheduling_priority
        m[Vocabulary.file_size_DP] = self.file_size
        m[Vocabulary.pending_signals_DP] = self.pending_signals
        m[Vocabulary.max_locked_memory_DP] = self.max_locked_memory
        m[Vocabulary.max_memory_size_DP] = self.max_memory_size
        m[Vocabulary.open_files_DP] = self.open_files
        m[Vocabulary.pipe_size_DP] = self.pipe_size
        m[Vocabulary.message_queues_DP] = self.message_queues
        m[Vocabulary.real_time_priority_DP] = self.real_time_priority
        m[Vocabulary.stack_size_DP] = self.stack_size
        m[Vocabulary.cpu_time_DP] = self.cpu_time
        m[Vocabulary.max_user_processes_DP] = self.max_user_processes
        m[Vocabulary.virtual_memory_DP] = self.virtual_memory
        m[Vocabulary.file_locks_DP] = self.file_locks
        return m


class Ulimits(UlimitsBase):
    def __init__(self, m=None):
        super().__init__(m)


class RDescriptionBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.Package = ""
            self.Version = ""
            self.Depends = ""
            self.Imports = ""
            self.LinkingTo = ""
            self.Suggests = ""
            self.License = ""
            self.MD5sum = ""
            self.NeedsCompilation = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RDescription_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.Package = m[Vocabulary.Package_DP]
        self.Version = m[Vocabulary.Version_DP]
        self.Depends = m[Vocabulary.Depends_DP]
        self.Imports = m[Vocabulary.Imports_DP]
        self.LinkingTo = m[Vocabulary.LinkingTo_DP]
        self.Suggests = m[Vocabulary.Suggests_DP]
        self.License = m[Vocabulary.License_DP]
        self.MD5sum = m[Vocabulary.MD5sum_DP]
        self.NeedsCompilation = m[Vocabulary.NeedsCompilation_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RDescription_CLASS:
            return RDescription(m)
        raise ValueError("bad kind : " + kind +
                         " for class RDescription in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RDescription_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RDescription_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.Package_DP] = self.Package
        m[Vocabulary.Version_DP] = self.Version
        m[Vocabulary.Depends_DP] = self.Depends
        m[Vocabulary.Imports_DP] = self.Imports
        m[Vocabulary.LinkingTo_DP] = self.LinkingTo
        m[Vocabulary.Suggests_DP] = self.Suggests
        m[Vocabulary.License_DP] = self.License
        m[Vocabulary.MD5sum_DP] = self.MD5sum
        m[Vocabulary.NeedsCompilation_DP] = self.NeedsCompilation
        return m


class RDescription(RDescriptionBase):
    def __init__(self, m=None):
        super().__init__(m)


class JetPaletteBase(RampPalette):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.JetPalette_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.JetPalette_CLASS:
            return JetPalette(m)
        raise ValueError("bad kind : " + kind +
                         " for class JetPalette in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.JetPalette_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.JetPalette_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class JetPalette(JetPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)


class SimpleRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.index = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.SimpleRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.index = m[Vocabulary.index_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.SimpleRelation_CLASS:
            return SimpleRelation(m)
        if kind == Vocabulary.TableRelation_CLASS:
            return TableRelation(m)
        if kind == Vocabulary.ReferenceRelation_CLASS:
            return ReferenceRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class SimpleRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.SimpleRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.SimpleRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.index_DP] = self.index
        return m


class SimpleRelation(SimpleRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableRelationBase(SimpleRelation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.nRows = 0
            self.data_dir = ""
            self.meta_data = list()
            self.attributes = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.nRows = m[Vocabulary.nRows_DP]
        self.data_dir = m[Vocabulary.data_dir_DP]
        if m.get(Vocabulary.meta_data_OP) is None:
            self.meta_data = list()
        else:
            self.meta_data = list()
            for o in m.get(Vocabulary.meta_data_OP):
                self.meta_data.append(PairBase.createFromJson(o))
        if m.get(Vocabulary.attributes_OP) is None:
            self.attributes = list()
        else:
            self.attributes = list()
            for o in m.get(Vocabulary.attributes_OP):
                self.attributes.append(AttributeBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableRelation_CLASS:
            return TableRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.meta_data_OP] = list(
            map(lambda x: x.toJson(), self.meta_data))
        m[Vocabulary.nRows_DP] = self.nRows
        m[Vocabulary.data_dir_DP] = self.data_dir
        m[Vocabulary.attributes_OP] = list(
            map(lambda x: x.toJson(), self.attributes))
        return m


class TableRelation(TableRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class DateBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.value = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Date_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.value = m[Vocabulary.value_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Date_CLASS:
            return Date(m)
        raise ValueError("bad kind : " + kind +
                         " for class Date in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Date_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Date_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.value_DP] = self.value
        return m


class Date(DateBase):
    def __init__(self, m=None):
        super().__init__(m)


class StepStateBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.taskId = ""
            self.taskState = State()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StepState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.taskId = m[Vocabulary.taskId_DP]
        if m.get(Vocabulary.taskState_OP) is None:
            self.taskState = State()
        else:
            self.taskState = StateBase.createFromJson(
                m.get(Vocabulary.taskState_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StepState_CLASS:
            return StepState(m)
        raise ValueError("bad kind : " + kind +
                         " for class StepState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StepState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StepState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.taskId_DP] = self.taskId
        m[Vocabulary.taskState_OP] = self.taskState if self.taskState is None else self.taskState.toJson()
        return m


class StepState(StepStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorResultBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.tables = list()
            self.joinOperators = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OperatorResult_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.tables_OP) is None:
            self.tables = list()
        else:
            self.tables = list()
            for o in m.get(Vocabulary.tables_OP):
                self.tables.append(TableBase.createFromJson(o))
        if m.get(Vocabulary.joinOperators_OP) is None:
            self.joinOperators = list()
        else:
            self.joinOperators = list()
            for o in m.get(Vocabulary.joinOperators_OP):
                self.joinOperators.append(JoinOperatorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OperatorResult_CLASS:
            return OperatorResult(m)
        raise ValueError("bad kind : " + kind +
                         " for class OperatorResult in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OperatorResult_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OperatorResult_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.tables_OP] = list(map(lambda x: x.toJson(), self.tables))
        m[Vocabulary.joinOperators_OP] = list(
            map(lambda x: x.toJson(), self.joinOperators))
        return m


class OperatorResult(OperatorResultBase):
    def __init__(self, m=None):
        super().__init__(m)


class RSourceLibraryBase(RLibrary):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.fileId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RSourceLibrary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.fileId = m[Vocabulary.fileId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RSourceLibrary_CLASS:
            return RSourceLibrary(m)
        raise ValueError("bad kind : " + kind +
                         " for class RSourceLibrary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RSourceLibrary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RSourceLibrary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.fileId_DP] = self.fileId
        return m


class RSourceLibrary(RSourceLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)


class FileDocumentBase(ProjectDocument):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.dataUri = ""
            self.size = 0
            self.metadata = FileMetadata()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FileDocument_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.dataUri = m[Vocabulary.dataUri_DP]
        self.size = m[Vocabulary.size_DP]
        if m.get(Vocabulary.metadata_OP) is None:
            self.metadata = FileMetadata()
        else:
            self.metadata = FileMetadataBase.createFromJson(
                m.get(Vocabulary.metadata_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FileDocument_CLASS:
            return FileDocument(m)
        raise ValueError("bad kind : " + kind +
                         " for class FileDocument in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FileDocument_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FileDocument_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.dataUri_DP] = self.dataUri
        m[Vocabulary.metadata_OP] = self.metadata if self.metadata is None else self.metadata.toJson()
        m[Vocabulary.size_DP] = self.size
        return m


class FileDocument(FileDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)


class AddressBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.country = ""
            self.state = ""
            self.city = ""
            self.zipCode = ""
            self.address1 = ""
            self.address2 = ""
            self.phone = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Address_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.country = m[Vocabulary.country_DP]
        self.state = m[Vocabulary.state_DP]
        self.city = m[Vocabulary.city_DP]
        self.zipCode = m[Vocabulary.zipCode_DP]
        self.address1 = m[Vocabulary.address1_DP]
        self.address2 = m[Vocabulary.address2_DP]
        self.phone = m[Vocabulary.phone_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Address_CLASS:
            return Address(m)
        raise ValueError("bad kind : " + kind +
                         " for class Address in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Address_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Address_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.country_DP] = self.country
        m[Vocabulary.state_DP] = self.state
        m[Vocabulary.city_DP] = self.city
        m[Vocabulary.zipCode_DP] = self.zipCode
        m[Vocabulary.address1_DP] = self.address1
        m[Vocabulary.address2_DP] = self.address2
        m[Vocabulary.phone_DP] = self.phone
        return m


class Address(AddressBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskDataEventBase(TaskEvent):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.bytes = None
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskDataEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.bytes = m[Vocabulary.bytes_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskDataEvent_CLASS:
            return TaskDataEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskDataEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskDataEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskDataEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.bytes_DP] = self.bytes
        return m


class TaskDataEvent(TaskDataEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class StringPropertyBase(Property):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.defaultValue = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StringProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.defaultValue = m[Vocabulary.defaultValue_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StringProperty_CLASS:
            return StringProperty(m)
        if kind == Vocabulary.EnumeratedProperty_CLASS:
            return EnumeratedProperty(m)
        if kind == Vocabulary.FactorsProperty_CLASS:
            return FactorsProperty(m)
        if kind == Vocabulary.FormulaProperty_CLASS:
            return FormulaProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class StringProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StringProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StringProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.defaultValue_DP] = self.defaultValue
        return m


class StringProperty(StringPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class XYAxisBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.taskId = ""
            self.chart = Chart()
            self.colors = Colors()
            self.errors = Errors()
            self.labels = Labels()
            self.xAxis = Axis()
            self.yAxis = Axis()
            self.preprocessors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.XYAxis_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.taskId = m[Vocabulary.taskId_DP]
        if m.get(Vocabulary.chart_OP) is None:
            self.chart = Chart()
        else:
            self.chart = ChartBase.createFromJson(m.get(Vocabulary.chart_OP))
        if m.get(Vocabulary.colors_OP) is None:
            self.colors = Colors()
        else:
            self.colors = ColorsBase.createFromJson(
                m.get(Vocabulary.colors_OP))
        if m.get(Vocabulary.errors_OP) is None:
            self.errors = Errors()
        else:
            self.errors = ErrorsBase.createFromJson(
                m.get(Vocabulary.errors_OP))
        if m.get(Vocabulary.labels_OP) is None:
            self.labels = Labels()
        else:
            self.labels = LabelsBase.createFromJson(
                m.get(Vocabulary.labels_OP))
        if m.get(Vocabulary.xAxis_OP) is None:
            self.xAxis = Axis()
        else:
            self.xAxis = AxisBase.createFromJson(m.get(Vocabulary.xAxis_OP))
        if m.get(Vocabulary.yAxis_OP) is None:
            self.yAxis = Axis()
        else:
            self.yAxis = AxisBase.createFromJson(m.get(Vocabulary.yAxis_OP))
        if m.get(Vocabulary.preprocessors_OP) is None:
            self.preprocessors = list()
        else:
            self.preprocessors = list()
            for o in m.get(Vocabulary.preprocessors_OP):
                self.preprocessors.append(PreProcessorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.XYAxis_CLASS:
            return XYAxis(m)
        raise ValueError("bad kind : " + kind +
                         " for class XYAxis in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.XYAxis_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.XYAxis_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.chart_OP] = self.chart if self.chart is None else self.chart.toJson()
        m[Vocabulary.colors_OP] = self.colors if self.colors is None else self.colors.toJson()
        m[Vocabulary.errors_OP] = self.errors if self.errors is None else self.errors.toJson()
        m[Vocabulary.labels_OP] = self.labels if self.labels is None else self.labels.toJson()
        m[Vocabulary.xAxis_OP] = self.xAxis if self.xAxis is None else self.xAxis.toJson()
        m[Vocabulary.yAxis_OP] = self.yAxis if self.yAxis is None else self.yAxis.toJson()
        m[Vocabulary.taskId_DP] = self.taskId
        m[Vocabulary.preprocessors_OP] = list(
            map(lambda x: x.toJson(), self.preprocessors))
        return m


class XYAxis(XYAxisBase):
    def __init__(self, m=None):
        super().__init__(m)


class PrincipalBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.principalId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Principal_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.principalId = m[Vocabulary.principalId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Principal_CLASS:
            return Principal(m)
        raise ValueError("bad kind : " + kind +
                         " for class Principal in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Principal_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Principal_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.principalId_DP] = self.principalId
        return m


class Principal(PrincipalBase):
    def __init__(self, m=None):
        super().__init__(m)


class FactorBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.type = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Factor_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.type = m[Vocabulary.type_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Factor_CLASS:
            return Factor(m)
        if kind == Vocabulary.Attribute_CLASS:
            return Attribute(m)
        if kind == Vocabulary.MappingFactor_CLASS:
            return MappingFactor(m)
        raise ValueError("bad kind : " + kind +
                         " for class Factor in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Factor_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Factor_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.type_DP] = self.type
        return m


class Factor(FactorBase):
    def __init__(self, m=None):
        super().__init__(m)


class AttributeBase(Factor):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.relationId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Attribute_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.relationId = m[Vocabulary.relationId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Attribute_CLASS:
            return Attribute(m)
        raise ValueError("bad kind : " + kind +
                         " for class Attribute in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Attribute_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Attribute_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relationId_DP] = self.relationId
        return m


class Attribute(AttributeBase):
    def __init__(self, m=None):
        super().__init__(m)


class ImportWorkflowTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.fileId = ""
            self.workflowId = ""
            self.gitToken = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ImportWorkflowTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.fileId = m[Vocabulary.fileId_DP]
        self.workflowId = m[Vocabulary.workflowId_DP]
        self.gitToken = m[Vocabulary.gitToken_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ImportWorkflowTask_CLASS:
            return ImportWorkflowTask(m)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ImportWorkflowTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ImportWorkflowTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ImportWorkflowTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.fileId_DP] = self.fileId
        m[Vocabulary.workflowId_DP] = self.workflowId
        m[Vocabulary.gitToken_DP] = self.gitToken
        return m


class ImportWorkflowTask(ImportWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ProjectBase(Document):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Project_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Project_CLASS:
            return Project(m)
        raise ValueError("bad kind : " + kind +
                         " for class Project in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Project_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Project_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class Project(ProjectBase):
    def __init__(self, m=None):
        super().__init__(m)


class UrlBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.uri = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Url_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.uri = m[Vocabulary.uri_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Url_CLASS:
            return Url(m)
        raise ValueError("bad kind : " + kind +
                         " for class Url in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Url_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Url_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.uri_DP] = self.uri
        return m


class Url(UrlBase):
    def __init__(self, m=None):
        super().__init__(m)


class StringColorElementBase(ColorElement):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.stringValue = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.StringColorElement_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.stringValue = m[Vocabulary.stringValue_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.StringColorElement_CLASS:
            return StringColorElement(m)
        raise ValueError("bad kind : " + kind +
                         " for class StringColorElement in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.StringColorElement_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.StringColorElement_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.stringValue_DP] = self.stringValue
        return m


class StringColorElement(StringColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)


class EnumeratedPropertyBase(StringProperty):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.values = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.EnumeratedProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.values_DP) is None:
            self.values = list()
        else:
            self.values = m[Vocabulary.values_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.EnumeratedProperty_CLASS:
            return EnumeratedProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class EnumeratedProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.EnumeratedProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.EnumeratedProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.values_DP] = self.values
        return m


class EnumeratedProperty(EnumeratedPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class TestOperatorTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.operatorId = ""
            self.testRequired = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TestOperatorTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.operatorId = m[Vocabulary.operatorId_DP]
        self.testRequired = m[Vocabulary.testRequired_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TestOperatorTask_CLASS:
            return TestOperatorTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class TestOperatorTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TestOperatorTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TestOperatorTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.operatorId_DP] = self.operatorId
        m[Vocabulary.testRequired_DP] = self.testRequired
        return m


class TestOperatorTask(TestOperatorTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ImportGitWorkflowTaskBase(ImportWorkflowTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.version = ""
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ImportGitWorkflowTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.version = m[Vocabulary.version_DP]
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ImportGitWorkflowTask_CLASS:
            return ImportGitWorkflowTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ImportGitWorkflowTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ImportGitWorkflowTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ImportGitWorkflowTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        m[Vocabulary.version_DP] = self.version
        return m


class ImportGitWorkflowTask(ImportGitWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class ReferenceRelationBase(SimpleRelation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ReferenceRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ReferenceRelation_CLASS:
            return ReferenceRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class ReferenceRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ReferenceRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ReferenceRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        return m


class ReferenceRelation(ReferenceRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class RProxyBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.targetUrl = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RProxy_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.targetUrl = m[Vocabulary.targetUrl_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RProxy_CLASS:
            return RProxy(m)
        raise ValueError("bad kind : " + kind +
                         " for class RProxy in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RProxy_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RProxy_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.targetUrl_DP] = self.targetUrl
        return m


class RProxy(RProxyBase):
    def __init__(self, m=None):
        super().__init__(m)


class PairBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.key = ""
            self.value = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Pair_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.key = m[Vocabulary.key_DP]
        self.value = m[Vocabulary.value_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Pair_CLASS:
            return Pair(m)
        raise ValueError("bad kind : " + kind +
                         " for class Pair in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Pair_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Pair_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.key_DP] = self.key
        m[Vocabulary.value_DP] = self.value
        return m


class Pair(PairBase):
    def __init__(self, m=None):
        super().__init__(m)


class InMemoryRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.inMemoryTable = Table()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.InMemoryRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.inMemoryTable_OP) is None:
            self.inMemoryTable = Table()
        else:
            self.inMemoryTable = TableBase.createFromJson(
                m.get(Vocabulary.inMemoryTable_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.InMemoryRelation_CLASS:
            return InMemoryRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class InMemoryRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.InMemoryRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.InMemoryRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.inMemoryTable_OP] = self.inMemoryTable if self.inMemoryTable is None else self.inMemoryTable.toJson()
        return m


class InMemoryRelation(InMemoryRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunProfileBase(Profile):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.memory = 0
            self.kernelMemory = 0
            self.blkioWeight = 0
            self.pidsLimit = 0
            self.ulimits_nofile = 0
            self.timeout = 0
            self.storageSize = ""
            self.cpusetCpus = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunProfile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.memory = m[Vocabulary.memory_DP]
        self.kernelMemory = m[Vocabulary.kernelMemory_DP]
        self.blkioWeight = m[Vocabulary.blkioWeight_DP]
        self.pidsLimit = m[Vocabulary.pidsLimit_DP]
        self.ulimits_nofile = m[Vocabulary.ulimits_nofile_DP]
        self.timeout = m[Vocabulary.timeout_DP]
        self.storageSize = m[Vocabulary.storageSize_DP]
        self.cpusetCpus = m[Vocabulary.cpusetCpus_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunProfile_CLASS:
            return RunProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunProfile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunProfile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunProfile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.memory_DP] = self.memory
        m[Vocabulary.kernelMemory_DP] = self.kernelMemory
        m[Vocabulary.blkioWeight_DP] = self.blkioWeight
        m[Vocabulary.pidsLimit_DP] = self.pidsLimit
        m[Vocabulary.ulimits_nofile_DP] = self.ulimits_nofile
        m[Vocabulary.timeout_DP] = self.timeout
        m[Vocabulary.storageSize_DP] = self.storageSize
        m[Vocabulary.cpusetCpus_DP] = self.cpusetCpus
        return m


class RunProfile(RunProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class CpuTimeProfileBase(Profile):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.cpuTime = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CpuTimeProfile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.cpuTime = m[Vocabulary.cpuTime_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CpuTimeProfile_CLASS:
            return CpuTimeProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class CpuTimeProfile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CpuTimeProfile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CpuTimeProfile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.cpuTime_DP] = self.cpuTime
        return m


class CpuTimeProfile(CpuTimeProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class AxisSettingsBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.properties = list()
            self.propertyValues = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.AxisSettings_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PropertyBase.createFromJson(o))
        if m.get(Vocabulary.propertyValues_OP) is None:
            self.propertyValues = list()
        else:
            self.propertyValues = list()
            for o in m.get(Vocabulary.propertyValues_OP):
                self.propertyValues.append(PropertyValueBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.AxisSettings_CLASS:
            return AxisSettings(m)
        raise ValueError("bad kind : " + kind +
                         " for class AxisSettings in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.AxisSettings_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.AxisSettings_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        m[Vocabulary.propertyValues_OP] = list(
            map(lambda x: x.toJson(), self.propertyValues))
        return m


class AxisSettings(AxisSettingsBase):
    def __init__(self, m=None):
        super().__init__(m)


class MappingFilterBase(BaseObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.description = ""
            self.isRequired = True
            self.namedFilter = NamedFilter()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.MappingFilter_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.description = m[Vocabulary.description_DP]
        self.isRequired = m[Vocabulary.isRequired_DP]
        if m.get(Vocabulary.namedFilter_OP) is None:
            self.namedFilter = NamedFilter()
        else:
            self.namedFilter = NamedFilterBase.createFromJson(
                m.get(Vocabulary.namedFilter_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.MappingFilter_CLASS:
            return MappingFilter(m)
        raise ValueError("bad kind : " + kind +
                         " for class MappingFilter in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.MappingFilter_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.MappingFilter_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.description_DP] = self.description
        m[Vocabulary.namedFilter_OP] = self.namedFilter if self.namedFilter is None else self.namedFilter.toJson()
        m[Vocabulary.isRequired_DP] = self.isRequired
        return m


class MappingFilter(MappingFilterBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartBarBase(Chart):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ChartBar_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ChartBar_CLASS:
            return ChartBar(m)
        raise ValueError("bad kind : " + kind +
                         " for class ChartBar in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ChartBar_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ChartBar_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ChartBar(ChartBarBase):
    def __init__(self, m=None):
        super().__init__(m)


class FolderDocumentBase(ProjectDocument):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FolderDocument_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FolderDocument_CLASS:
            return FolderDocument(m)
        raise ValueError("bad kind : " + kind +
                         " for class FolderDocument in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FolderDocument_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FolderDocument_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class FolderDocument(FolderDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)


class LockBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Lock_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Lock_CLASS:
            return Lock(m)
        raise ValueError("bad kind : " + kind +
                         " for class Lock in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Lock_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Lock_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        return m


class Lock(LockBase):
    def __init__(self, m=None):
        super().__init__(m)


class WorkerBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.status = ""
            self.name = ""
            self.uri = ""
            self.priority = 0.0
            self.nCPU = 0
            self.nThread = 0
            self.memory = 0.0
            self.nAvailableThread = 0
            self.availableMemory = 0.0
            self.availableTaskTypes = list()
            self.taskIds = list()
            self.lastDateActivity = ""
            self.heartBeat = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Worker_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.status = m[Vocabulary.status_DP]
        self.name = m[Vocabulary.name_DP]
        self.uri = m[Vocabulary.uri_DP]
        self.priority = m[Vocabulary.priority_DP]
        self.nCPU = m[Vocabulary.nCPU_DP]
        self.nThread = m[Vocabulary.nThread_DP]
        self.memory = m[Vocabulary.memory_DP]
        self.nAvailableThread = m[Vocabulary.nAvailableThread_DP]
        self.availableMemory = m[Vocabulary.availableMemory_DP]
        if m.get(Vocabulary.availableTaskTypes_DP) is None:
            self.availableTaskTypes = list()
        else:
            self.availableTaskTypes = m[Vocabulary.availableTaskTypes_DP]
        if m.get(Vocabulary.taskIds_DP) is None:
            self.taskIds = list()
        else:
            self.taskIds = m[Vocabulary.taskIds_DP]
        self.lastDateActivity = m[Vocabulary.lastDateActivity_DP]
        self.heartBeat = m[Vocabulary.heartBeat_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Worker_CLASS:
            return Worker(m)
        raise ValueError("bad kind : " + kind +
                         " for class Worker in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Worker_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Worker_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.status_DP] = self.status
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.uri_DP] = self.uri
        m[Vocabulary.priority_DP] = self.priority
        m[Vocabulary.nCPU_DP] = self.nCPU
        m[Vocabulary.nThread_DP] = self.nThread
        m[Vocabulary.memory_DP] = self.memory
        m[Vocabulary.nAvailableThread_DP] = self.nAvailableThread
        m[Vocabulary.availableMemory_DP] = self.availableMemory
        m[Vocabulary.availableTaskTypes_DP] = self.availableTaskTypes
        m[Vocabulary.taskIds_DP] = self.taskIds
        m[Vocabulary.lastDateActivity_DP] = self.lastDateActivity
        m[Vocabulary.heartBeat_DP] = self.heartBeat
        return m


class Worker(WorkerBase):
    def __init__(self, m=None):
        super().__init__(m)


class ImportGitDatasetTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.version = ""
            self.gitToken = ""
            self.schemaId = ""
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ImportGitDatasetTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.version = m[Vocabulary.version_DP]
        self.gitToken = m[Vocabulary.gitToken_DP]
        self.schemaId = m[Vocabulary.schemaId_DP]
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ImportGitDatasetTask_CLASS:
            return ImportGitDatasetTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ImportGitDatasetTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ImportGitDatasetTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ImportGitDatasetTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        m[Vocabulary.version_DP] = self.version
        m[Vocabulary.gitToken_DP] = self.gitToken
        m[Vocabulary.schemaId_DP] = self.schemaId
        return m


class ImportGitDatasetTask(ImportGitDatasetTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class AceBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.principals = list()
            self.privileges = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Ace_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.principals_OP) is None:
            self.principals = list()
        else:
            self.principals = list()
            for o in m.get(Vocabulary.principals_OP):
                self.principals.append(PrincipalBase.createFromJson(o))
        if m.get(Vocabulary.privileges_OP) is None:
            self.privileges = list()
        else:
            self.privileges = list()
            for o in m.get(Vocabulary.privileges_OP):
                self.privileges.append(PrivilegeBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Ace_CLASS:
            return Ace(m)
        raise ValueError("bad kind : " + kind +
                         " for class Ace in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Ace_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Ace_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.principals_OP] = list(
            map(lambda x: x.toJson(), self.principals))
        m[Vocabulary.privileges_OP] = list(
            map(lambda x: x.toJson(), self.privileges))
        return m


class Ace(AceBase):
    def __init__(self, m=None):
        super().__init__(m)


class InStepBase(RelationStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.groupPortPosition = Point()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.InStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.groupPortPosition_OP) is None:
            self.groupPortPosition = Point()
        else:
            self.groupPortPosition = PointBase.createFromJson(
                m.get(Vocabulary.groupPortPosition_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.InStep_CLASS:
            return InStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class InStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.InStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.InStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.groupPortPosition_OP] = self.groupPortPosition if self.groupPortPosition is None else self.groupPortPosition.toJson()
        return m


class InStep(InStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class LabelsBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.factors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Labels_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(FactorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Labels_CLASS:
            return Labels(m)
        raise ValueError("bad kind : " + kind +
                         " for class Labels in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Labels_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Labels_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        return m


class Labels(LabelsBase):
    def __init__(self, m=None):
        super().__init__(m)


class RenvInstalledLibraryBase(RLibrary):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.path = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RenvInstalledLibrary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.path = m[Vocabulary.path_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RenvInstalledLibrary_CLASS:
            return RenvInstalledLibrary(m)
        raise ValueError("bad kind : " + kind +
                         " for class RenvInstalledLibrary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RenvInstalledLibrary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RenvInstalledLibrary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.path_DP] = self.path
        return m


class RenvInstalledLibrary(RenvInstalledLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorSettingsBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.namespace = ""
            self.operatorRef = OperatorRef()
            self.environment = list()
            self.operatorModel = OperatorModel()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OperatorSettings_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.namespace = m[Vocabulary.namespace_DP]
        if m.get(Vocabulary.operatorRef_OP) is None:
            self.operatorRef = OperatorRef()
        else:
            self.operatorRef = OperatorRefBase.createFromJson(
                m.get(Vocabulary.operatorRef_OP))
        if m.get(Vocabulary.environment_OP) is None:
            self.environment = list()
        else:
            self.environment = list()
            for o in m.get(Vocabulary.environment_OP):
                self.environment.append(PairBase.createFromJson(o))
        if m.get(Vocabulary.operatorModel_OP) is None:
            self.operatorModel = OperatorModel()
        else:
            self.operatorModel = OperatorModelBase.createFromJson(
                m.get(Vocabulary.operatorModel_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OperatorSettings_CLASS:
            return OperatorSettings(m)
        raise ValueError("bad kind : " + kind +
                         " for class OperatorSettings in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OperatorSettings_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OperatorSettings_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.namespace_DP] = self.namespace
        m[Vocabulary.operatorRef_OP] = self.operatorRef if self.operatorRef is None else self.operatorRef.toJson()
        m[Vocabulary.environment_OP] = list(
            map(lambda x: x.toJson(), self.environment))
        m[Vocabulary.operatorModel_OP] = self.operatorModel if self.operatorModel is None else self.operatorModel.toJson()
        return m


class OperatorSettings(OperatorSettingsBase):
    def __init__(self, m=None):
        super().__init__(m)


class SchemaBase(ProjectDocument):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.nRows = 0
            self.dataDirectory = ""
            self.columns = list()
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Schema_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.nRows = m[Vocabulary.nRows_DP]
        self.dataDirectory = m[Vocabulary.dataDirectory_DP]
        if m.get(Vocabulary.columns_OP) is None:
            self.columns = list()
        else:
            self.columns = list()
            for o in m.get(Vocabulary.columns_OP):
                self.columns.append(ColumnSchemaBase.createFromJson(o))
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Schema_CLASS:
            return Schema(m)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        raise ValueError("bad kind : " + kind +
                         " for class Schema in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Schema_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Schema_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.nRows_DP] = self.nRows
        m[Vocabulary.columns_OP] = list(
            map(lambda x: x.toJson(), self.columns))
        m[Vocabulary.dataDirectory_DP] = self.dataDirectory
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        return m


class Schema(SchemaBase):
    def __init__(self, m=None):
        super().__init__(m)


class CubeQueryTableSchemaBase(Schema):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.queryHash = ""
            self.queryTableType = ""
            self.query = CubeQuery()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CubeQueryTableSchema_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.queryHash = m[Vocabulary.queryHash_DP]
        self.queryTableType = m[Vocabulary.queryTableType_DP]
        if m.get(Vocabulary.query_OP) is None:
            self.query = CubeQuery()
        else:
            self.query = CubeQueryBase.createFromJson(
                m.get(Vocabulary.query_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CubeQueryTableSchema_CLASS:
            return CubeQueryTableSchema(m)
        raise ValueError("bad kind : " + kind +
                         " for class CubeQueryTableSchema in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CubeQueryTableSchema_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CubeQueryTableSchema_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.queryHash_DP] = self.queryHash
        m[Vocabulary.queryTableType_DP] = self.queryTableType
        m[Vocabulary.query_OP] = self.query if self.query is None else self.query.toJson()
        return m


class CubeQueryTableSchema(CubeQueryTableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)


class CategoryPaletteBase(Palette):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.colorList = ColorList()
            self.stringColorElements = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CategoryPalette_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.colorList_OP) is None:
            self.colorList = ColorList()
        else:
            self.colorList = ColorListBase.createFromJson(
                m.get(Vocabulary.colorList_OP))
        if m.get(Vocabulary.stringColorElements_OP) is None:
            self.stringColorElements = list()
        else:
            self.stringColorElements = list()
            for o in m.get(Vocabulary.stringColorElements_OP):
                self.stringColorElements.append(
                    StringColorElementBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CategoryPalette_CLASS:
            return CategoryPalette(m)
        raise ValueError("bad kind : " + kind +
                         " for class CategoryPalette in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CategoryPalette_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CategoryPalette_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.colorList_OP] = self.colorList if self.colorList is None else self.colorList.toJson()
        m[Vocabulary.stringColorElements_OP] = list(
            map(lambda x: x.toJson(), self.stringColorElements))
        return m


class CategoryPalette(CategoryPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableSummaryBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.n = 0
            self.size = 0
            self.nr = 0
            self.nc = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableSummary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.n = m[Vocabulary.n_DP]
        self.size = m[Vocabulary.size_DP]
        self.nr = m[Vocabulary.nr_DP]
        self.nc = m[Vocabulary.nc_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableSummary_CLASS:
            return TableSummary(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableSummary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableSummary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableSummary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.n_DP] = self.n
        m[Vocabulary.size_DP] = self.size
        m[Vocabulary.nr_DP] = self.nr
        m[Vocabulary.nc_DP] = self.nc
        return m


class TableSummary(TableSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)


class PointBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.x = 0.0
            self.y = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Point_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.x = m[Vocabulary.x_DP]
        self.y = m[Vocabulary.y_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Point_CLASS:
            return Point(m)
        raise ValueError("bad kind : " + kind +
                         " for class Point in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Point_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Point_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.x_DP] = self.x
        m[Vocabulary.y_DP] = self.y
        return m


class Point(PointBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColumnSchemaBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.type = ""
            self.nRows = 0
            self.size = 0
            self.metaData = ColumnSchemaMetaData()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ColumnSchema_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.type = m[Vocabulary.type_DP]
        self.nRows = m[Vocabulary.nRows_DP]
        self.size = m[Vocabulary.size_DP]
        if m.get(Vocabulary.metaData_OP) is None:
            self.metaData = ColumnSchemaMetaData()
        else:
            self.metaData = ColumnSchemaMetaDataBase.createFromJson(
                m.get(Vocabulary.metaData_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ColumnSchema_CLASS:
            return ColumnSchema(m)
        if kind == Vocabulary.Column_CLASS:
            return Column(m)
        raise ValueError("bad kind : " + kind +
                         " for class ColumnSchema in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ColumnSchema_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ColumnSchema_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.nRows_DP] = self.nRows
        m[Vocabulary.size_DP] = self.size
        m[Vocabulary.metaData_OP] = self.metaData if self.metaData is None else self.metaData.toJson()
        return m


class ColumnSchema(ColumnSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColumnBase(ColumnSchema):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.values = None
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Column_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.values = m[Vocabulary.values_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Column_CLASS:
            return Column(m)
        raise ValueError("bad kind : " + kind +
                         " for class Column in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Column_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Column_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.values_DP] = self.values
        return m


class Column(ColumnBase):
    def __init__(self, m=None):
        super().__init__(m)


class SummaryBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.tableSummary = TableSummary()
            self.computedTableSummary = TableSummary()
            self.queryTableSummary = TableSummary()
            self.taskSummary = TaskSummary()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Summary_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.tableSummary_OP) is None:
            self.tableSummary = TableSummary()
        else:
            self.tableSummary = TableSummaryBase.createFromJson(
                m.get(Vocabulary.tableSummary_OP))
        if m.get(Vocabulary.computedTableSummary_OP) is None:
            self.computedTableSummary = TableSummary()
        else:
            self.computedTableSummary = TableSummaryBase.createFromJson(
                m.get(Vocabulary.computedTableSummary_OP))
        if m.get(Vocabulary.queryTableSummary_OP) is None:
            self.queryTableSummary = TableSummary()
        else:
            self.queryTableSummary = TableSummaryBase.createFromJson(
                m.get(Vocabulary.queryTableSummary_OP))
        if m.get(Vocabulary.taskSummary_OP) is None:
            self.taskSummary = TaskSummary()
        else:
            self.taskSummary = TaskSummaryBase.createFromJson(
                m.get(Vocabulary.taskSummary_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Summary_CLASS:
            return Summary(m)
        raise ValueError("bad kind : " + kind +
                         " for class Summary in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Summary_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Summary_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.tableSummary_OP] = self.tableSummary if self.tableSummary is None else self.tableSummary.toJson()
        m[Vocabulary.computedTableSummary_OP] = self.computedTableSummary if self.computedTableSummary is None else self.computedTableSummary.toJson()
        m[Vocabulary.queryTableSummary_OP] = self.queryTableSummary if self.queryTableSummary is None else self.queryTableSummary.toJson()
        m[Vocabulary.taskSummary_OP] = self.taskSummary if self.taskSummary is None else self.taskSummary.toJson()
        return m


class Summary(SummaryBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaskStateEventBase(TaskEvent):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.state = State()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaskStateEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.state_OP) is None:
            self.state = State()
        else:
            self.state = StateBase.createFromJson(m.get(Vocabulary.state_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaskStateEvent_CLASS:
            return TaskStateEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaskStateEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaskStateEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaskStateEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.state_OP] = self.state if self.state is None else self.state.toJson()
        return m


class TaskStateEvent(TaskStateEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class WebAppOperatorBase(GitOperator):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isViewOnly = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.WebAppOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.isViewOnly = m[Vocabulary.isViewOnly_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.WebAppOperator_CLASS:
            return WebAppOperator(m)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class WebAppOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.WebAppOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.WebAppOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.isViewOnly_DP] = self.isViewOnly
        return m


class WebAppOperator(WebAppOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class ShinyOperatorBase(WebAppOperator):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ShinyOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ShinyOperator_CLASS:
            return ShinyOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class ShinyOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ShinyOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ShinyOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ShinyOperator(ShinyOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class ErrorsBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.factors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Errors_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(FactorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Errors_CLASS:
            return Errors(m)
        raise ValueError("bad kind : " + kind +
                         " for class Errors in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Errors_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Errors_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        return m


class Errors(ErrorsBase):
    def __init__(self, m=None):
        super().__init__(m)


class GlTaskBase(Task):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.glQuery = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GlTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.glQuery = m[Vocabulary.glQuery_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GlTask_CLASS:
            return GlTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class GlTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GlTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GlTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.glQuery_DP] = self.glQuery
        return m


class GlTask(GlTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class FailedStateBase(State):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.error = ""
            self.reason = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FailedState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.error = m[Vocabulary.error_DP]
        self.reason = m[Vocabulary.reason_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FailedState_CLASS:
            return FailedState(m)
        raise ValueError("bad kind : " + kind +
                         " for class FailedState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FailedState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FailedState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.error_DP] = self.error
        m[Vocabulary.reason_DP] = self.reason
        return m


class FailedState(FailedStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class CanceledStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CanceledState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CanceledState_CLASS:
            return CanceledState(m)
        raise ValueError("bad kind : " + kind +
                         " for class CanceledState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CanceledState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CanceledState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class CanceledState(CanceledStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunWorkflowTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.workflowId = ""
            self.workflowRev = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunWorkflowTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.workflowId = m[Vocabulary.workflowId_DP]
        self.workflowRev = m[Vocabulary.workflowRev_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunWorkflowTask_CLASS:
            return RunWorkflowTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunWorkflowTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunWorkflowTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunWorkflowTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.workflowId_DP] = self.workflowId
        m[Vocabulary.workflowRev_DP] = self.workflowRev
        return m


class RunWorkflowTask(RunWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class GraphicalFactorBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.factor = Factor()
            self.rectangle = Rectangle()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GraphicalFactor_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.factor_OP) is None:
            self.factor = Factor()
        else:
            self.factor = FactorBase.createFromJson(
                m.get(Vocabulary.factor_OP))
        if m.get(Vocabulary.rectangle_OP) is None:
            self.rectangle = Rectangle()
        else:
            self.rectangle = RectangleBase.createFromJson(
                m.get(Vocabulary.rectangle_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GraphicalFactor_CLASS:
            return GraphicalFactor(m)
        raise ValueError("bad kind : " + kind +
                         " for class GraphicalFactor in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GraphicalFactor_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GraphicalFactor_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factor_OP] = self.factor if self.factor is None else self.factor.toJson()
        m[Vocabulary.rectangle_OP] = self.rectangle if self.rectangle is None else self.rectangle.toJson()
        return m


class GraphicalFactor(GraphicalFactorBase):
    def __init__(self, m=None):
        super().__init__(m)


class RenameRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.inNames = list()
            self.outNames = list()
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RenameRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.inNames_DP) is None:
            self.inNames = list()
        else:
            self.inNames = m[Vocabulary.inNames_DP]
        if m.get(Vocabulary.outNames_DP) is None:
            self.outNames = list()
        else:
            self.outNames = m[Vocabulary.outNames_DP]
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RenameRelation_CLASS:
            return RenameRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class RenameRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RenameRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RenameRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.inNames_DP] = self.inNames
        m[Vocabulary.outNames_DP] = self.outNames
        return m


class RenameRelation(RenameRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartSizeBase(Chart):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.pointSize = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ChartSize_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.pointSize = m[Vocabulary.pointSize_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ChartSize_CLASS:
            return ChartSize(m)
        if kind == Vocabulary.ChartLine_CLASS:
            return ChartLine(m)
        if kind == Vocabulary.ChartPoint_CLASS:
            return ChartPoint(m)
        raise ValueError("bad kind : " + kind +
                         " for class ChartSize in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ChartSize_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ChartSize_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.pointSize_DP] = self.pointSize
        return m


class ChartSize(ChartSizeBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartLineBase(ChartSize):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ChartLine_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ChartLine_CLASS:
            return ChartLine(m)
        raise ValueError("bad kind : " + kind +
                         " for class ChartLine in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ChartLine_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ChartLine_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ChartLine(ChartLineBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColorListBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ColorList_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ColorList_CLASS:
            return ColorList(m)
        raise ValueError("bad kind : " + kind +
                         " for class ColorList in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ColorList_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ColorList_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        return m


class ColorList(ColorListBase):
    def __init__(self, m=None):
        super().__init__(m)


class CrossTabStepBase(NamespaceStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = Crosstab()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CrossTabStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = Crosstab()
        else:
            self.model = CrosstabBase.createFromJson(
                m.get(Vocabulary.model_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CrossTabStep_CLASS:
            return CrossTabStep(m)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class CrossTabStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CrossTabStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CrossTabStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        return m


class CrossTabStep(CrossTabStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class DataStepBase(CrossTabStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.parentDataStepId = ""
            self.computedRelation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DataStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.parentDataStepId = m[Vocabulary.parentDataStepId_DP]
        if m.get(Vocabulary.computedRelation_OP) is None:
            self.computedRelation = Relation()
        else:
            self.computedRelation = RelationBase.createFromJson(
                m.get(Vocabulary.computedRelation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DataStep_CLASS:
            return DataStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class DataStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DataStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DataStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.computedRelation_OP] = self.computedRelation if self.computedRelation is None else self.computedRelation.toJson()
        m[Vocabulary.parentDataStepId_DP] = self.parentDataStepId
        return m


class DataStep(DataStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class SearchResultBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.total_rows = 0
            self.bookmark = ""
            self.rows = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.SearchResult_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.total_rows = m[Vocabulary.total_rows_DP]
        self.bookmark = m[Vocabulary.bookmark_DP]
        if m.get(Vocabulary.rows_OP) is None:
            self.rows = list()
        else:
            self.rows = list()
            for o in m.get(Vocabulary.rows_OP):
                self.rows.append(PersistentObjectBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.SearchResult_CLASS:
            return SearchResult(m)
        raise ValueError("bad kind : " + kind +
                         " for class SearchResult in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.SearchResult_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.SearchResult_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.total_rows_DP] = self.total_rows
        m[Vocabulary.bookmark_DP] = self.bookmark
        m[Vocabulary.rows_OP] = list(map(lambda x: x.toJson(), self.rows))
        return m


class SearchResult(SearchResultBase):
    def __init__(self, m=None):
        super().__init__(m)


class PreProcessorBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.type = ""
            self.operatorRef = OperatorRef()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PreProcessor_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.type = m[Vocabulary.type_DP]
        if m.get(Vocabulary.operatorRef_OP) is None:
            self.operatorRef = OperatorRef()
        else:
            self.operatorRef = OperatorRefBase.createFromJson(
                m.get(Vocabulary.operatorRef_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PreProcessor_CLASS:
            return PreProcessor(m)
        raise ValueError("bad kind : " + kind +
                         " for class PreProcessor in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PreProcessor_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PreProcessor_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.operatorRef_OP] = self.operatorRef if self.operatorRef is None else self.operatorRef.toJson()
        return m


class PreProcessor(PreProcessorBase):
    def __init__(self, m=None):
        super().__init__(m)


class AnnotationModelBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.taskId = ""
            self.factors = list()
            self.annotationFactors = list()
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.AnnotationModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.taskId = m[Vocabulary.taskId_DP]
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(GraphicalFactorBase.createFromJson(o))
        if m.get(Vocabulary.annotationFactors_OP) is None:
            self.annotationFactors = list()
        else:
            self.annotationFactors = list()
            for o in m.get(Vocabulary.annotationFactors_OP):
                self.annotationFactors.append(
                    GraphicalFactorBase.createFromJson(o))
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.AnnotationModel_CLASS:
            return AnnotationModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class AnnotationModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.AnnotationModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.AnnotationModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.annotationFactors_OP] = list(
            map(lambda x: x.toJson(), self.annotationFactors))
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.taskId_DP] = self.taskId
        return m


class AnnotationModel(AnnotationModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class ROperatorBase(GitOperator):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ROperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ROperator_CLASS:
            return ROperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class ROperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ROperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ROperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ROperator(ROperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class OutStepBase(RelationStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.groupPortPosition = Point()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OutStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.groupPortPosition_OP) is None:
            self.groupPortPosition = Point()
        else:
            self.groupPortPosition = PointBase.createFromJson(
                m.get(Vocabulary.groupPortPosition_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OutStep_CLASS:
            return OutStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class OutStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OutStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OutStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.groupPortPosition_OP] = self.groupPortPosition if self.groupPortPosition is None else self.groupPortPosition.toJson()
        return m


class OutStep(OutStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class PortBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.linkType = ""
            self.name = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Port_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.linkType = m[Vocabulary.linkType_DP]
        self.name = m[Vocabulary.name_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Port_CLASS:
            return Port(m)
        if kind == Vocabulary.InputPort_CLASS:
            return InputPort(m)
        if kind == Vocabulary.OutputPort_CLASS:
            return OutputPort(m)
        raise ValueError("bad kind : " + kind +
                         " for class Port in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Port_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Port_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.linkType_DP] = self.linkType
        m[Vocabulary.name_DP] = self.name
        return m


class Port(PortBase):
    def __init__(self, m=None):
        super().__init__(m)


class InputPortBase(Port):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.InputPort_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.InputPort_CLASS:
            return InputPort(m)
        raise ValueError("bad kind : " + kind +
                         " for class InputPort in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.InputPort_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.InputPort_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class InputPort(InputPortBase):
    def __init__(self, m=None):
        super().__init__(m)


class PropertiesBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.properties = list()
            self.propertyValues = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Properties_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.properties_OP) is None:
            self.properties = list()
        else:
            self.properties = list()
            for o in m.get(Vocabulary.properties_OP):
                self.properties.append(PropertyBase.createFromJson(o))
        if m.get(Vocabulary.propertyValues_OP) is None:
            self.propertyValues = list()
        else:
            self.propertyValues = list()
            for o in m.get(Vocabulary.propertyValues_OP):
                self.propertyValues.append(PropertyValueBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Properties_CLASS:
            return Properties(m)
        raise ValueError("bad kind : " + kind +
                         " for class Properties in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Properties_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Properties_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.properties_OP] = list(
            map(lambda x: x.toJson(), self.properties))
        m[Vocabulary.propertyValues_OP] = list(
            map(lambda x: x.toJson(), self.propertyValues))
        return m


class Properties(PropertiesBase):
    def __init__(self, m=None):
        super().__init__(m)


class PropertyValueBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.value = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PropertyValue_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.value = m[Vocabulary.value_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PropertyValue_CLASS:
            return PropertyValue(m)
        raise ValueError("bad kind : " + kind +
                         " for class PropertyValue in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PropertyValue_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PropertyValue_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.value_DP] = self.value
        return m


class PropertyValue(PropertyValueBase):
    def __init__(self, m=None):
        super().__init__(m)


class DoneStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DoneState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DoneState_CLASS:
            return DoneState(m)
        raise ValueError("bad kind : " + kind +
                         " for class DoneState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DoneState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DoneState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class DoneState(DoneStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class AclContextBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.username = ""
            self.domain = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.AclContext_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.username = m[Vocabulary.username_DP]
        self.domain = m[Vocabulary.domain_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.AclContext_CLASS:
            return AclContext(m)
        raise ValueError("bad kind : " + kind +
                         " for class AclContext in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.AclContext_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.AclContext_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.username_DP] = self.username
        m[Vocabulary.domain_DP] = self.domain
        return m


class AclContext(AclContextBase):
    def __init__(self, m=None):
        super().__init__(m)


class DockerWebAppOperatorBase(WebAppOperator):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.container = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.DockerWebAppOperator_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.container = m[Vocabulary.container_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.DockerWebAppOperator_CLASS:
            return DockerWebAppOperator(m)
        raise ValueError("bad kind : " + kind +
                         " for class DockerWebAppOperator in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.DockerWebAppOperator_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.DockerWebAppOperator_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.container_DP] = self.container
        return m


class DockerWebAppOperator(DockerWebAppOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorUnitTestBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.namespace = ""
            self.inputFileUris = list()
            self.inputDataUri = ""
            self.outputDataUri = list()
            self.columns = list()
            self.rows = list()
            self.colors = list()
            self.labels = list()
            self.yAxis = ""
            self.xAxis = ""
            self.absTol = 0.0
            self.relTol = 0.0
            self.equalityMethod = ""
            self.r2 = 0.0
            self.skipColumns = list()
            self.propertyValues = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OperatorUnitTest_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.namespace = m[Vocabulary.namespace_DP]
        if m.get(Vocabulary.inputFileUris_DP) is None:
            self.inputFileUris = list()
        else:
            self.inputFileUris = m[Vocabulary.inputFileUris_DP]
        self.inputDataUri = m[Vocabulary.inputDataUri_DP]
        if m.get(Vocabulary.outputDataUri_DP) is None:
            self.outputDataUri = list()
        else:
            self.outputDataUri = m[Vocabulary.outputDataUri_DP]
        if m.get(Vocabulary.columns_DP) is None:
            self.columns = list()
        else:
            self.columns = m[Vocabulary.columns_DP]
        if m.get(Vocabulary.rows_DP) is None:
            self.rows = list()
        else:
            self.rows = m[Vocabulary.rows_DP]
        if m.get(Vocabulary.colors_DP) is None:
            self.colors = list()
        else:
            self.colors = m[Vocabulary.colors_DP]
        if m.get(Vocabulary.labels_DP) is None:
            self.labels = list()
        else:
            self.labels = m[Vocabulary.labels_DP]
        self.yAxis = m[Vocabulary.yAxis_DP]
        self.xAxis = m[Vocabulary.xAxis_DP]
        self.absTol = m[Vocabulary.absTol_DP]
        self.relTol = m[Vocabulary.relTol_DP]
        self.equalityMethod = m[Vocabulary.equalityMethod_DP]
        self.r2 = m[Vocabulary.r2_DP]
        if m.get(Vocabulary.skipColumns_DP) is None:
            self.skipColumns = list()
        else:
            self.skipColumns = m[Vocabulary.skipColumns_DP]
        if m.get(Vocabulary.propertyValues_OP) is None:
            self.propertyValues = list()
        else:
            self.propertyValues = list()
            for o in m.get(Vocabulary.propertyValues_OP):
                self.propertyValues.append(PropertyValueBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OperatorUnitTest_CLASS:
            return OperatorUnitTest(m)
        raise ValueError("bad kind : " + kind +
                         " for class OperatorUnitTest in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OperatorUnitTest_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OperatorUnitTest_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.namespace_DP] = self.namespace
        m[Vocabulary.propertyValues_OP] = list(
            map(lambda x: x.toJson(), self.propertyValues))
        m[Vocabulary.inputFileUris_DP] = self.inputFileUris
        m[Vocabulary.inputDataUri_DP] = self.inputDataUri
        m[Vocabulary.outputDataUri_DP] = self.outputDataUri
        m[Vocabulary.columns_DP] = self.columns
        m[Vocabulary.rows_DP] = self.rows
        m[Vocabulary.colors_DP] = self.colors
        m[Vocabulary.labels_DP] = self.labels
        m[Vocabulary.yAxis_DP] = self.yAxis
        m[Vocabulary.xAxis_DP] = self.xAxis
        m[Vocabulary.absTol_DP] = self.absTol
        m[Vocabulary.relTol_DP] = self.relTol
        m[Vocabulary.equalityMethod_DP] = self.equalityMethod
        m[Vocabulary.r2_DP] = self.r2
        m[Vocabulary.skipColumns_DP] = self.skipColumns
        return m


class OperatorUnitTest(OperatorUnitTestBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableStepBase(RelationStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = TableStepModel()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = TableStepModel()
        else:
            self.model = TableStepModelBase.createFromJson(
                m.get(Vocabulary.model_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableStep_CLASS:
            return TableStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        return m


class TableStep(TableStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class RunWebAppTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.operatorId = ""
            self.cubeQueryTaskId = ""
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.RunWebAppTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.operatorId = m[Vocabulary.operatorId_DP]
        self.cubeQueryTaskId = m[Vocabulary.cubeQueryTaskId_DP]
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.RunWebAppTask_CLASS:
            return RunWebAppTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class RunWebAppTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.RunWebAppTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.RunWebAppTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.operatorId_DP] = self.operatorId
        m[Vocabulary.cubeQueryTaskId_DP] = self.cubeQueryTaskId
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        return m


class RunWebAppTask(RunWebAppTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class UnionRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.relations = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.UnionRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.relations_OP) is None:
            self.relations = list()
        else:
            self.relations = list()
            for o in m.get(Vocabulary.relations_OP):
                self.relations.append(RelationBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.UnionRelation_CLASS:
            return UnionRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class UnionRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.UnionRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.UnionRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relations_OP] = list(
            map(lambda x: x.toJson(), self.relations))
        return m


class UnionRelation(UnionRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class ProfilesBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.apiProfile = ApiCallProfile()
            self.tableProfile = TableProfile()
            self.cpuTimeProfile = CpuTimeProfile()
            self.storageProfile = StorageProfile()
            self.runProfile = RunProfile()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Profiles_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.apiProfile_OP) is None:
            self.apiProfile = ApiCallProfile()
        else:
            self.apiProfile = ApiCallProfileBase.createFromJson(
                m.get(Vocabulary.apiProfile_OP))
        if m.get(Vocabulary.tableProfile_OP) is None:
            self.tableProfile = TableProfile()
        else:
            self.tableProfile = TableProfileBase.createFromJson(
                m.get(Vocabulary.tableProfile_OP))
        if m.get(Vocabulary.cpuTimeProfile_OP) is None:
            self.cpuTimeProfile = CpuTimeProfile()
        else:
            self.cpuTimeProfile = CpuTimeProfileBase.createFromJson(
                m.get(Vocabulary.cpuTimeProfile_OP))
        if m.get(Vocabulary.storageProfile_OP) is None:
            self.storageProfile = StorageProfile()
        else:
            self.storageProfile = StorageProfileBase.createFromJson(
                m.get(Vocabulary.storageProfile_OP))
        if m.get(Vocabulary.runProfile_OP) is None:
            self.runProfile = RunProfile()
        else:
            self.runProfile = RunProfileBase.createFromJson(
                m.get(Vocabulary.runProfile_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Profiles_CLASS:
            return Profiles(m)
        raise ValueError("bad kind : " + kind +
                         " for class Profiles in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Profiles_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Profiles_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.apiProfile_OP] = self.apiProfile if self.apiProfile is None else self.apiProfile.toJson()
        m[Vocabulary.tableProfile_OP] = self.tableProfile if self.tableProfile is None else self.tableProfile.toJson()
        m[Vocabulary.cpuTimeProfile_OP] = self.cpuTimeProfile if self.cpuTimeProfile is None else self.cpuTimeProfile.toJson()
        m[Vocabulary.storageProfile_OP] = self.storageProfile if self.storageProfile is None else self.storageProfile.toJson()
        m[Vocabulary.runProfile_OP] = self.runProfile if self.runProfile is None else self.runProfile.toJson()
        return m


class Profiles(ProfilesBase):
    def __init__(self, m=None):
        super().__init__(m)


class FactorsPropertyBase(StringProperty):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FactorsProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FactorsProperty_CLASS:
            return FactorsProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class FactorsProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FactorsProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FactorsProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class FactorsProperty(FactorsPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class OperatorRefBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.version = ""
            self.operatorId = ""
            self.operatorKind = ""
            self.propertyValues = list()
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OperatorRef_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.version = m[Vocabulary.version_DP]
        self.operatorId = m[Vocabulary.operatorId_DP]
        self.operatorKind = m[Vocabulary.operatorKind_DP]
        if m.get(Vocabulary.propertyValues_OP) is None:
            self.propertyValues = list()
        else:
            self.propertyValues = list()
            for o in m.get(Vocabulary.propertyValues_OP):
                self.propertyValues.append(PropertyValueBase.createFromJson(o))
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OperatorRef_CLASS:
            return OperatorRef(m)
        raise ValueError("bad kind : " + kind +
                         " for class OperatorRef in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OperatorRef_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OperatorRef_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.version_DP] = self.version
        m[Vocabulary.operatorId_DP] = self.operatorId
        m[Vocabulary.operatorKind_DP] = self.operatorKind
        m[Vocabulary.propertyValues_OP] = list(
            map(lambda x: x.toJson(), self.propertyValues))
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        return m


class OperatorRef(OperatorRefBase):
    def __init__(self, m=None):
        super().__init__(m)


class JoinStepBase(NamespaceStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = JoinStepModel()
            self.rightAttributes = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.JoinStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = JoinStepModel()
        else:
            self.model = JoinStepModelBase.createFromJson(
                m.get(Vocabulary.model_OP))
        if m.get(Vocabulary.rightAttributes_OP) is None:
            self.rightAttributes = list()
        else:
            self.rightAttributes = list()
            for o in m.get(Vocabulary.rightAttributes_OP):
                self.rightAttributes.append(AttributeBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.JoinStep_CLASS:
            return JoinStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class JoinStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.JoinStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.JoinStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        m[Vocabulary.rightAttributes_OP] = list(
            map(lambda x: x.toJson(), self.rightAttributes))
        return m


class JoinStep(JoinStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class WizardStepBase(NamespaceStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = WizardStepModel()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.WizardStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = WizardStepModel()
        else:
            self.model = WizardStepModelBase.createFromJson(
                m.get(Vocabulary.model_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.WizardStep_CLASS:
            return WizardStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class WizardStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.WizardStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.WizardStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        return m


class WizardStep(WizardStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class WizardStepModelBase(StepModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.namespace = ""
            self.description = ""
            self.appDesignType = ""
            self.factors = list()
            self.filters = list()
            self.steps = list()
            self.defaultFactors = list()
            self.defaultFilters = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.WizardStepModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.namespace = m[Vocabulary.namespace_DP]
        self.description = m[Vocabulary.description_DP]
        self.appDesignType = m[Vocabulary.appDesignType_DP]
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(MappingFactorBase.createFromJson(o))
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = list()
        else:
            self.filters = list()
            for o in m.get(Vocabulary.filters_OP):
                self.filters.append(MappingFilterBase.createFromJson(o))
        if m.get(Vocabulary.steps_OP) is None:
            self.steps = list()
        else:
            self.steps = list()
            for o in m.get(Vocabulary.steps_OP):
                self.steps.append(StepBase.createFromJson(o))
        if m.get(Vocabulary.defaultFactors_OP) is None:
            self.defaultFactors = list()
        else:
            self.defaultFactors = list()
            for o in m.get(Vocabulary.defaultFactors_OP):
                self.defaultFactors.append(MappingFactorBase.createFromJson(o))
        if m.get(Vocabulary.defaultFilters_OP) is None:
            self.defaultFilters = list()
        else:
            self.defaultFilters = list()
            for o in m.get(Vocabulary.defaultFilters_OP):
                self.defaultFilters.append(MappingFilterBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.WizardStepModel_CLASS:
            return WizardStepModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class WizardStepModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.WizardStepModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.WizardStepModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.namespace_DP] = self.namespace
        m[Vocabulary.description_DP] = self.description
        m[Vocabulary.appDesignType_DP] = self.appDesignType
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.filters_OP] = list(
            map(lambda x: x.toJson(), self.filters))
        m[Vocabulary.steps_OP] = list(map(lambda x: x.toJson(), self.steps))
        m[Vocabulary.defaultFactors_OP] = list(
            map(lambda x: x.toJson(), self.defaultFactors))
        m[Vocabulary.defaultFilters_OP] = list(
            map(lambda x: x.toJson(), self.defaultFilters))
        return m


class WizardStepModel(WizardStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class InitStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.InitState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.InitState_CLASS:
            return InitState(m)
        raise ValueError("bad kind : " + kind +
                         " for class InitState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.InitState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.InitState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class InitState(InitStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class PendingStateBase(State):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.PendingState_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.PendingState_CLASS:
            return PendingState(m)
        raise ValueError("bad kind : " + kind +
                         " for class PendingState in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.PendingState_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.PendingState_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class PendingState(PendingStateBase):
    def __init__(self, m=None):
        super().__init__(m)


class ChartPointBase(ChartSize):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ChartPoint_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ChartPoint_CLASS:
            return ChartPoint(m)
        raise ValueError("bad kind : " + kind +
                         " for class ChartPoint in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ChartPoint_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ChartPoint_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ChartPoint(ChartPointBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColumnPairBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.lColumns = list()
            self.rColumns = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ColumnPair_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.lColumns_DP) is None:
            self.lColumns = list()
        else:
            self.lColumns = m[Vocabulary.lColumns_DP]
        if m.get(Vocabulary.rColumns_DP) is None:
            self.rColumns = list()
        else:
            self.rColumns = m[Vocabulary.rColumns_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ColumnPair_CLASS:
            return ColumnPair(m)
        raise ValueError("bad kind : " + kind +
                         " for class ColumnPair in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ColumnPair_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ColumnPair_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.lColumns_DP] = self.lColumns
        m[Vocabulary.rColumns_DP] = self.rColumns
        return m


class ColumnPair(ColumnPairBase):
    def __init__(self, m=None):
        super().__init__(m)


class CreateGitOperatorTaskBase(Task):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.version = ""
            self.operatorId = ""
            self.gitToken = ""
            self.testRequired = True
            self.url = Url()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CreateGitOperatorTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.version = m[Vocabulary.version_DP]
        self.operatorId = m[Vocabulary.operatorId_DP]
        self.gitToken = m[Vocabulary.gitToken_DP]
        self.testRequired = m[Vocabulary.testRequired_DP]
        if m.get(Vocabulary.url_OP) is None:
            self.url = Url()
        else:
            self.url = UrlBase.createFromJson(m.get(Vocabulary.url_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CreateGitOperatorTask_CLASS:
            return CreateGitOperatorTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class CreateGitOperatorTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CreateGitOperatorTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CreateGitOperatorTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.url_OP] = self.url if self.url is None else self.url.toJson()
        m[Vocabulary.version_DP] = self.version
        m[Vocabulary.operatorId_DP] = self.operatorId
        m[Vocabulary.gitToken_DP] = self.gitToken
        m[Vocabulary.testRequired_DP] = self.testRequired
        return m


class CreateGitOperatorTask(CreateGitOperatorTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class TaxIdBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.type = ""
            self.value = ""
            self.isValid = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TaxId_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.type = m[Vocabulary.type_DP]
        self.value = m[Vocabulary.value_DP]
        self.isValid = m[Vocabulary.isValid_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TaxId_CLASS:
            return TaxId(m)
        raise ValueError("bad kind : " + kind +
                         " for class TaxId in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TaxId_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TaxId_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.value_DP] = self.value
        m[Vocabulary.isValid_DP] = self.isValid
        return m


class TaxId(TaxIdBase):
    def __init__(self, m=None):
        super().__init__(m)


class IssueMessageBase(ProjectDocument):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.issueId = ""
            self.body = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.IssueMessage_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.issueId = m[Vocabulary.issueId_DP]
        self.body = m[Vocabulary.body_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.IssueMessage_CLASS:
            return IssueMessage(m)
        raise ValueError("bad kind : " + kind +
                         " for class IssueMessage in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.IssueMessage_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.IssueMessage_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.issueId_DP] = self.issueId
        m[Vocabulary.body_DP] = self.body
        return m


class IssueMessage(IssueMessageBase):
    def __init__(self, m=None):
        super().__init__(m)


class FilterExprBase(FilterTopExpr):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.filterOp = ""
            self.stringValue = ""
            self.factor = Factor()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FilterExpr_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.filterOp = m[Vocabulary.filterOp_DP]
        self.stringValue = m[Vocabulary.stringValue_DP]
        if m.get(Vocabulary.factor_OP) is None:
            self.factor = Factor()
        else:
            self.factor = FactorBase.createFromJson(
                m.get(Vocabulary.factor_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FilterExpr_CLASS:
            return FilterExpr(m)
        raise ValueError("bad kind : " + kind +
                         " for class FilterExpr in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FilterExpr_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FilterExpr_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.filterOp_DP] = self.filterOp
        m[Vocabulary.stringValue_DP] = self.stringValue
        m[Vocabulary.factor_OP] = self.factor if self.factor is None else self.factor.toJson()
        return m


class FilterExpr(FilterExprBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableSchemaBase(Schema):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableSchema_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableSchema_CLASS:
            return TableSchema(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableSchema in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableSchema_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableSchema_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class TableSchema(TableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)


class PlanBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.displayName = ""
            self.paymentProviderPlanId = ""
            self.descriptions = list()
            self.price = 0.0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Plan_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        self.displayName = m[Vocabulary.displayName_DP]
        self.paymentProviderPlanId = m[Vocabulary.paymentProviderPlanId_DP]
        if m.get(Vocabulary.descriptions_DP) is None:
            self.descriptions = list()
        else:
            self.descriptions = m[Vocabulary.descriptions_DP]
        self.price = m[Vocabulary.price_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Plan_CLASS:
            return Plan(m)
        raise ValueError("bad kind : " + kind +
                         " for class Plan in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Plan_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Plan_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.displayName_DP] = self.displayName
        m[Vocabulary.paymentProviderPlanId_DP] = self.paymentProviderPlanId
        m[Vocabulary.descriptions_DP] = self.descriptions
        m[Vocabulary.price_DP] = self.price
        return m


class Plan(PlanBase):
    def __init__(self, m=None):
        super().__init__(m)


class CSVParserParamBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.separator = ""
            self.encoding = ""
            self.quote = ""
            self.hasHeaders = True
            self.allowMalformed = True
            self.comment = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CSVParserParam_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.separator = m[Vocabulary.separator_DP]
        self.encoding = m[Vocabulary.encoding_DP]
        self.quote = m[Vocabulary.quote_DP]
        self.hasHeaders = m[Vocabulary.hasHeaders_DP]
        self.allowMalformed = m[Vocabulary.allowMalformed_DP]
        self.comment = m[Vocabulary.comment_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CSVParserParam_CLASS:
            return CSVParserParam(m)
        raise ValueError("bad kind : " + kind +
                         " for class CSVParserParam in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CSVParserParam_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CSVParserParam_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.separator_DP] = self.separator
        m[Vocabulary.encoding_DP] = self.encoding
        m[Vocabulary.quote_DP] = self.quote
        m[Vocabulary.hasHeaders_DP] = self.hasHeaders
        m[Vocabulary.allowMalformed_DP] = self.allowMalformed
        m[Vocabulary.comment_DP] = self.comment
        return m


class CSVParserParam(CSVParserParamBase):
    def __init__(self, m=None):
        super().__init__(m)


class ExportTableTaskBase(ProjectTask):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.exportName = ""
            self.schemaIds = list()
            self.exportType = ""
            self.exportToId = ""
            self.exportId = ""
            self.namespaces = list()
            self.exportedSchemaIds = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ExportTableTask_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.exportName = m[Vocabulary.exportName_DP]
        if m.get(Vocabulary.schemaIds_DP) is None:
            self.schemaIds = list()
        else:
            self.schemaIds = m[Vocabulary.schemaIds_DP]
        self.exportType = m[Vocabulary.exportType_DP]
        self.exportToId = m[Vocabulary.exportToId_DP]
        self.exportId = m[Vocabulary.exportId_DP]
        if m.get(Vocabulary.namespaces_DP) is None:
            self.namespaces = list()
        else:
            self.namespaces = m[Vocabulary.namespaces_DP]
        if m.get(Vocabulary.exportedSchemaIds_DP) is None:
            self.exportedSchemaIds = list()
        else:
            self.exportedSchemaIds = m[Vocabulary.exportedSchemaIds_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ExportTableTask_CLASS:
            return ExportTableTask(m)
        raise ValueError("bad kind : " + kind +
                         " for class ExportTableTask in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ExportTableTask_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ExportTableTask_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.exportName_DP] = self.exportName
        m[Vocabulary.schemaIds_DP] = self.schemaIds
        m[Vocabulary.exportType_DP] = self.exportType
        m[Vocabulary.exportToId_DP] = self.exportToId
        m[Vocabulary.exportId_DP] = self.exportId
        m[Vocabulary.namespaces_DP] = self.namespaces
        m[Vocabulary.exportedSchemaIds_DP] = self.exportedSchemaIds
        return m


class ExportTableTask(ExportTableTaskBase):
    def __init__(self, m=None):
        super().__init__(m)


class GenericEventBase(Event):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.type = ""
            self.content = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GenericEvent_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.type = m[Vocabulary.type_DP]
        self.content = m[Vocabulary.content_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GenericEvent_CLASS:
            return GenericEvent(m)
        raise ValueError("bad kind : " + kind +
                         " for class GenericEvent in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GenericEvent_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GenericEvent_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.content_DP] = self.content
        return m


class GenericEvent(GenericEventBase):
    def __init__(self, m=None):
        super().__init__(m)


class OutputPortBase(Port):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.OutputPort_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.OutputPort_CLASS:
            return OutputPort(m)
        raise ValueError("bad kind : " + kind +
                         " for class OutputPort in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.OutputPort_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.OutputPort_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class OutputPort(OutputPortBase):
    def __init__(self, m=None):
        super().__init__(m)


class LinkBase(IdObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.inputId = ""
            self.outputId = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Link_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.inputId = m[Vocabulary.inputId_DP]
        self.outputId = m[Vocabulary.outputId_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Link_CLASS:
            return Link(m)
        raise ValueError("bad kind : " + kind +
                         " for class Link in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Link_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Link_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.inputId_DP] = self.inputId
        m[Vocabulary.outputId_DP] = self.outputId
        return m


class Link(LinkBase):
    def __init__(self, m=None):
        super().__init__(m)


class AppDesignBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.namespace = ""
            self.description = ""
            self.name = ""
            self.type = ""
            self.factors = list()
            self.filters = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.AppDesign_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.namespace = m[Vocabulary.namespace_DP]
        self.description = m[Vocabulary.description_DP]
        self.name = m[Vocabulary.name_DP]
        self.type = m[Vocabulary.type_DP]
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(MappingFactorBase.createFromJson(o))
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = list()
        else:
            self.filters = list()
            for o in m.get(Vocabulary.filters_OP):
                self.filters.append(MappingFilterBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.AppDesign_CLASS:
            return AppDesign(m)
        raise ValueError("bad kind : " + kind +
                         " for class AppDesign in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.AppDesign_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.AppDesign_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.namespace_DP] = self.namespace
        m[Vocabulary.description_DP] = self.description
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.type_DP] = self.type
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.filters_OP] = list(
            map(lambda x: x.toJson(), self.filters))
        return m


class AppDesign(AppDesignBase):
    def __init__(self, m=None):
        super().__init__(m)


class GarbageTasks2Base(GarbageObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.date = ""
            self.workflowId = ""
            self.deletedTaskIds = list()
            self.addedTaskIds = list()
            self.deletedStepIds = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GarbageTasks2_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.date = m[Vocabulary.date_DP]
        self.workflowId = m[Vocabulary.workflowId_DP]
        if m.get(Vocabulary.deletedTaskIds_DP) is None:
            self.deletedTaskIds = list()
        else:
            self.deletedTaskIds = m[Vocabulary.deletedTaskIds_DP]
        if m.get(Vocabulary.addedTaskIds_DP) is None:
            self.addedTaskIds = list()
        else:
            self.addedTaskIds = m[Vocabulary.addedTaskIds_DP]
        if m.get(Vocabulary.deletedStepIds_DP) is None:
            self.deletedStepIds = list()
        else:
            self.deletedStepIds = m[Vocabulary.deletedStepIds_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GarbageTasks2_CLASS:
            return GarbageTasks2(m)
        raise ValueError("bad kind : " + kind +
                         " for class GarbageTasks2 in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GarbageTasks2_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GarbageTasks2_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.date_DP] = self.date
        m[Vocabulary.workflowId_DP] = self.workflowId
        m[Vocabulary.deletedTaskIds_DP] = self.deletedTaskIds
        m[Vocabulary.addedTaskIds_DP] = self.addedTaskIds
        m[Vocabulary.deletedStepIds_DP] = self.deletedStepIds
        return m


class GarbageTasks2(GarbageTasks2Base):
    def __init__(self, m=None):
        super().__init__(m)


class WorkflowBase(ProjectDocument):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.links = list()
            self.steps = list()
            self.offset = Point()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Workflow_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.links_OP) is None:
            self.links = list()
        else:
            self.links = list()
            for o in m.get(Vocabulary.links_OP):
                self.links.append(LinkBase.createFromJson(o))
        if m.get(Vocabulary.steps_OP) is None:
            self.steps = list()
        else:
            self.steps = list()
            for o in m.get(Vocabulary.steps_OP):
                self.steps.append(StepBase.createFromJson(o))
        if m.get(Vocabulary.offset_OP) is None:
            self.offset = Point()
        else:
            self.offset = PointBase.createFromJson(m.get(Vocabulary.offset_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Workflow_CLASS:
            return Workflow(m)
        raise ValueError("bad kind : " + kind +
                         " for class Workflow in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Workflow_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Workflow_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.links_OP] = list(map(lambda x: x.toJson(), self.links))
        m[Vocabulary.steps_OP] = list(map(lambda x: x.toJson(), self.steps))
        m[Vocabulary.offset_OP] = self.offset if self.offset is None else self.offset.toJson()
        return m


class Workflow(WorkflowBase):
    def __init__(self, m=None):
        super().__init__(m)


class NamedFilterBase(Filter):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.NamedFilter_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.NamedFilter_CLASS:
            return NamedFilter(m)
        raise ValueError("bad kind : " + kind +
                         " for class NamedFilter in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.NamedFilter_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.NamedFilter_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        return m


class NamedFilter(NamedFilterBase):
    def __init__(self, m=None):
        super().__init__(m)


class TableProfileBase(Profile):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.nRows = 0
            self.nCols = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableProfile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.nRows = m[Vocabulary.nRows_DP]
        self.nCols = m[Vocabulary.nCols_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableProfile_CLASS:
            return TableProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableProfile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableProfile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableProfile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.nRows_DP] = self.nRows
        m[Vocabulary.nCols_DP] = self.nCols
        return m


class TableProfile(TableProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class MeltStepModelBase(StepModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.namespace = ""
            self.selectionPattern = ""
            self.factorType = ""
            self.factors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.MeltStepModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.namespace = m[Vocabulary.namespace_DP]
        self.selectionPattern = m[Vocabulary.selectionPattern_DP]
        self.factorType = m[Vocabulary.factorType_DP]
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(FactorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.MeltStepModel_CLASS:
            return MeltStepModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class MeltStepModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.MeltStepModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.MeltStepModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.namespace_DP] = self.namespace
        m[Vocabulary.selectionPattern_DP] = self.selectionPattern
        m[Vocabulary.factorType_DP] = self.factorType
        return m


class MeltStepModel(MeltStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class ExportModelBase(StepModel):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ExportModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ExportModel_CLASS:
            return ExportModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class ExportModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ExportModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ExportModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ExportModel(ExportModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class AnnotationOperatorModelBase(OperatorModel):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.filters = Filters()
            self.annotationModels = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.AnnotationOperatorModel_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.filters_OP) is None:
            self.filters = Filters()
        else:
            self.filters = FiltersBase.createFromJson(
                m.get(Vocabulary.filters_OP))
        if m.get(Vocabulary.annotationModels_OP) is None:
            self.annotationModels = list()
        else:
            self.annotationModels = list()
            for o in m.get(Vocabulary.annotationModels_OP):
                self.annotationModels.append(
                    AnnotationModelBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.AnnotationOperatorModel_CLASS:
            return AnnotationOperatorModel(m)
        raise ValueError("bad kind : " + kind +
                         " for class AnnotationOperatorModel in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.AnnotationOperatorModel_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.AnnotationOperatorModel_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.filters_OP] = self.filters if self.filters is None else self.filters.toJson()
        m[Vocabulary.annotationModels_OP] = list(
            map(lambda x: x.toJson(), self.annotationModels))
        return m


class AnnotationOperatorModel(AnnotationOperatorModelBase):
    def __init__(self, m=None):
        super().__init__(m)


class AxisBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.axisExtent = Point()
            self.axisSettings = AxisSettings()
            self.graphicalFactor = GraphicalFactor()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Axis_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.axisExtent_OP) is None:
            self.axisExtent = Point()
        else:
            self.axisExtent = PointBase.createFromJson(
                m.get(Vocabulary.axisExtent_OP))
        if m.get(Vocabulary.axisSettings_OP) is None:
            self.axisSettings = AxisSettings()
        else:
            self.axisSettings = AxisSettingsBase.createFromJson(
                m.get(Vocabulary.axisSettings_OP))
        if m.get(Vocabulary.graphicalFactor_OP) is None:
            self.graphicalFactor = GraphicalFactor()
        else:
            self.graphicalFactor = GraphicalFactorBase.createFromJson(
                m.get(Vocabulary.graphicalFactor_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Axis_CLASS:
            return Axis(m)
        raise ValueError("bad kind : " + kind +
                         " for class Axis in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Axis_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Axis_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.axisExtent_OP] = self.axisExtent if self.axisExtent is None else self.axisExtent.toJson()
        m[Vocabulary.axisSettings_OP] = self.axisSettings if self.axisSettings is None else self.axisSettings.toJson()
        m[Vocabulary.graphicalFactor_OP] = self.graphicalFactor if self.graphicalFactor is None else self.graphicalFactor.toJson()
        return m


class Axis(AxisBase):
    def __init__(self, m=None):
        super().__init__(m)


class BooleanPropertyBase(Property):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.defaultValue = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.BooleanProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.defaultValue = m[Vocabulary.defaultValue_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.BooleanProperty_CLASS:
            return BooleanProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class BooleanProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.BooleanProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.BooleanProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.defaultValue_DP] = self.defaultValue
        return m


class BooleanProperty(BooleanPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class GatherRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.names = list()
            self.valueName = ""
            self.variableName = ""
            self.valueType = ""
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GatherRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.names_DP) is None:
            self.names = list()
        else:
            self.names = m[Vocabulary.names_DP]
        self.valueName = m[Vocabulary.valueName_DP]
        self.variableName = m[Vocabulary.variableName_DP]
        self.valueType = m[Vocabulary.valueType_DP]
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GatherRelation_CLASS:
            return GatherRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class GatherRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GatherRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GatherRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.names_DP] = self.names
        m[Vocabulary.valueName_DP] = self.valueName
        m[Vocabulary.variableName_DP] = self.variableName
        m[Vocabulary.valueType_DP] = self.valueType
        return m


class GatherRelation(GatherRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class ExportStepBase(ModelStep):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.model = ExportModel()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ExportStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.model_OP) is None:
            self.model = ExportModel()
        else:
            self.model = ExportModelBase.createFromJson(
                m.get(Vocabulary.model_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ExportStep_CLASS:
            return ExportStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class ExportStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ExportStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ExportStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.model_OP] = self.model if self.model is None else self.model.toJson()
        return m


class ExportStep(ExportStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class ViewStepBase(Step):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ViewStep_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ViewStep_CLASS:
            return ViewStep(m)
        raise ValueError("bad kind : " + kind +
                         " for class ViewStep in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ViewStep_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ViewStep_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class ViewStep(ViewStepBase):
    def __init__(self, m=None):
        super().__init__(m)


class ApiCallProfileBase(Profile):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.nCalls = 0
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ApiCallProfile_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.nCalls = m[Vocabulary.nCalls_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ApiCallProfile_CLASS:
            return ApiCallProfile(m)
        raise ValueError("bad kind : " + kind +
                         " for class ApiCallProfile in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ApiCallProfile_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ApiCallProfile_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.nCalls_DP] = self.nCalls
        return m


class ApiCallProfile(ApiCallProfileBase):
    def __init__(self, m=None):
        super().__init__(m)


class ColorsBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.factors = list()
            self.palette = Palette()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.Colors_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(FactorBase.createFromJson(o))
        if m.get(Vocabulary.palette_OP) is None:
            self.palette = Palette()
        else:
            self.palette = PaletteBase.createFromJson(
                m.get(Vocabulary.palette_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.Colors_CLASS:
            return Colors(m)
        raise ValueError("bad kind : " + kind +
                         " for class Colors in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.Colors_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.Colors_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.palette_OP] = self.palette if self.palette is None else self.palette.toJson()
        return m


class Colors(ColorsBase):
    def __init__(self, m=None):
        super().__init__(m)


class CompositeRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.joinOperators = list()
            self.mainRelation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.CompositeRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.joinOperators_OP) is None:
            self.joinOperators = list()
        else:
            self.joinOperators = list()
            for o in m.get(Vocabulary.joinOperators_OP):
                self.joinOperators.append(JoinOperatorBase.createFromJson(o))
        if m.get(Vocabulary.mainRelation_OP) is None:
            self.mainRelation = Relation()
        else:
            self.mainRelation = RelationBase.createFromJson(
                m.get(Vocabulary.mainRelation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.CompositeRelation_CLASS:
            return CompositeRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class CompositeRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.CompositeRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.CompositeRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.joinOperators_OP] = list(
            map(lambda x: x.toJson(), self.joinOperators))
        m[Vocabulary.mainRelation_OP] = self.mainRelation if self.mainRelation is None else self.mainRelation.toJson()
        return m


class CompositeRelation(CompositeRelationBase):
    def __init__(self, m=None):
        super().__init__(m)


class ComputedTableSchemaBase(Schema):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.query = CubeQuery()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.ComputedTableSchema_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.query_OP) is None:
            self.query = CubeQuery()
        else:
            self.query = CubeQueryBase.createFromJson(
                m.get(Vocabulary.query_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.ComputedTableSchema_CLASS:
            return ComputedTableSchema(m)
        raise ValueError("bad kind : " + kind +
                         " for class ComputedTableSchema in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.ComputedTableSchema_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.ComputedTableSchema_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.query_OP] = self.query if self.query is None else self.query.toJson()
        return m


class ComputedTableSchema(ComputedTableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)


class TablePropertiesBase(SciObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.name = ""
            self.sortOrder = list()
            self.ascending = True
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.TableProperties_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.name = m[Vocabulary.name_DP]
        if m.get(Vocabulary.sortOrder_DP) is None:
            self.sortOrder = list()
        else:
            self.sortOrder = m[Vocabulary.sortOrder_DP]
        self.ascending = m[Vocabulary.ascending_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.TableProperties_CLASS:
            return TableProperties(m)
        raise ValueError("bad kind : " + kind +
                         " for class TableProperties in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.TableProperties_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.TableProperties_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.name_DP] = self.name
        m[Vocabulary.sortOrder_DP] = self.sortOrder
        m[Vocabulary.ascending_DP] = self.ascending
        return m


class TableProperties(TablePropertiesBase):
    def __init__(self, m=None):
        super().__init__(m)


class MappingFactorBase(Factor):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.isSingle = True
            self.description = ""
            self.factorName = ""
            self.isRequired = True
            self.factors = list()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.MappingFactor_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.isSingle = m[Vocabulary.isSingle_DP]
        self.description = m[Vocabulary.description_DP]
        self.factorName = m[Vocabulary.factorName_DP]
        self.isRequired = m[Vocabulary.isRequired_DP]
        if m.get(Vocabulary.factors_OP) is None:
            self.factors = list()
        else:
            self.factors = list()
            for o in m.get(Vocabulary.factors_OP):
                self.factors.append(FactorBase.createFromJson(o))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.MappingFactor_CLASS:
            return MappingFactor(m)
        raise ValueError("bad kind : " + kind +
                         " for class MappingFactor in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.MappingFactor_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.MappingFactor_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.isSingle_DP] = self.isSingle
        m[Vocabulary.description_DP] = self.description
        m[Vocabulary.factorName_DP] = self.factorName
        m[Vocabulary.factors_OP] = list(
            map(lambda x: x.toJson(), self.factors))
        m[Vocabulary.isRequired_DP] = self.isRequired
        return m


class MappingFactor(MappingFactorBase):
    def __init__(self, m=None):
        super().__init__(m)


class SubscriptionPlanBase(Document):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.providerKey = ""
            self.paymentProviderPlanId = ""
            self.checkoutSessionId = ""
            self.subscriptionId = ""
            self.status = ""
            self.paymentMethodStatus = ""
            self.ip = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.SubscriptionPlan_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.providerKey = m[Vocabulary.providerKey_DP]
        self.paymentProviderPlanId = m[Vocabulary.paymentProviderPlanId_DP]
        self.checkoutSessionId = m[Vocabulary.checkoutSessionId_DP]
        self.subscriptionId = m[Vocabulary.subscriptionId_DP]
        self.status = m[Vocabulary.status_DP]
        self.paymentMethodStatus = m[Vocabulary.paymentMethodStatus_DP]
        self.ip = m[Vocabulary.ip_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.SubscriptionPlan_CLASS:
            return SubscriptionPlan(m)
        raise ValueError("bad kind : " + kind +
                         " for class SubscriptionPlan in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.SubscriptionPlan_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.SubscriptionPlan_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.providerKey_DP] = self.providerKey
        m[Vocabulary.paymentProviderPlanId_DP] = self.paymentProviderPlanId
        m[Vocabulary.checkoutSessionId_DP] = self.checkoutSessionId
        m[Vocabulary.subscriptionId_DP] = self.subscriptionId
        m[Vocabulary.status_DP] = self.status
        m[Vocabulary.paymentMethodStatus_DP] = self.paymentMethodStatus
        m[Vocabulary.ip_DP] = self.ip
        return m


class SubscriptionPlan(SubscriptionPlanBase):
    def __init__(self, m=None):
        super().__init__(m)


class FormulaPropertyBase(StringProperty):
    def __init__(self, m=None):
        if m is not None:
            self.fromJson(m)

        else:
            super().__init__(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.FormulaProperty_CLASS:
            self.subKind = m.get(Vocabulary.KIND)

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.FormulaProperty_CLASS:
            return FormulaProperty(m)
        raise ValueError("bad kind : " + kind +
                         " for class FormulaProperty in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.FormulaProperty_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.FormulaProperty_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        return m


class FormulaProperty(FormulaPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)


class UserSecretBase(PersistentObject):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.userId = ""
            self.salt = ""
            self.hashPassword = ""
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.UserSecret_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        self.userId = m[Vocabulary.userId_DP]
        self.salt = m[Vocabulary.salt_DP]
        self.hashPassword = m[Vocabulary.hashPassword_DP]

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.UserSecret_CLASS:
            return UserSecret(m)
        raise ValueError("bad kind : " + kind +
                         " for class UserSecret in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.UserSecret_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.UserSecret_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.userId_DP] = self.userId
        m[Vocabulary.salt_DP] = self.salt
        m[Vocabulary.hashPassword_DP] = self.hashPassword
        return m


class UserSecret(UserSecretBase):
    def __init__(self, m=None):
        super().__init__(m)


class GroupByRelationBase(Relation):
    def __init__(self, m=None):
        if m is None:
            super().__init__(m)
            self.group = list()
            self.relation = Relation()
        else:
            self.fromJson(m)

    def fromJson(self, m):
        super().fromJson(m)
        self.subKind = m.get(Vocabulary.SUBKIND)
        if self.subKind is None and m.get(Vocabulary.KIND) != Vocabulary.GroupByRelation_CLASS:
            self.subKind = m.get(Vocabulary.KIND)
        if m.get(Vocabulary.group_DP) is None:
            self.group = list()
        else:
            self.group = m[Vocabulary.group_DP]
        if m.get(Vocabulary.relation_OP) is None:
            self.relation = Relation()
        else:
            self.relation = RelationBase.createFromJson(
                m.get(Vocabulary.relation_OP))

    @classmethod
    def createFromJson(cls, m):
        kind = m.get(Vocabulary.KIND)
        if kind == Vocabulary.GroupByRelation_CLASS:
            return GroupByRelation(m)
        raise ValueError("bad kind : " + kind +
                         " for class GroupByRelation in createFromJson")

    def toJson(self):
        m = super().toJson()
        m[Vocabulary.KIND] = Vocabulary.GroupByRelation_CLASS
        if self.subKind is not None and self.subKind != Vocabulary.GroupByRelation_CLASS:
            m[Vocabulary.SUBKIND] = self.subKind
        else:
            m.pop(Vocabulary.SUBKIND, None)
        m[Vocabulary.relation_OP] = self.relation if self.relation is None else self.relation.toJson()
        m[Vocabulary.group_DP] = self.group
        return m


class GroupByRelation(GroupByRelationBase):
    def __init__(self, m=None):
        super().__init__(m)
