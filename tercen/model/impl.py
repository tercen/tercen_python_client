from tercen.model.base import *

class SciObject(SciObjectBase):
    def __init__(self, m=None):
        super().__init__(m)

class IdObject(IdObjectBase):
    def __init__(self, m=None):
        super().__init__(m)

class PersistentObject(PersistentObjectBase):
    def __init__(self, m=None):
        super().__init__(m)

class Document(DocumentBase):
    def __init__(self, m=None):
        super().__init__(m)

class User(UserBase):
    def __init__(self, m=None):
        super().__init__(m)

class Team(TeamBase):
    def __init__(self, m=None):
        super().__init__(m)

class Property(PropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class DoubleProperty(DoublePropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class Rectangle(RectangleBase):
    def __init__(self, m=None):
        super().__init__(m)

class State(StateBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunningState(RunningStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class Relation(RelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class WhereRelation(WhereRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class Profile(ProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class StorageProfile(StorageProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class ResourceSummary(ResourceSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)

class BillingInfo(BillingInfoBase):
    def __init__(self, m=None):
        super().__init__(m)

class Event(EventBase):
    def __init__(self, m=None):
        super().__init__(m)

class PatchRecords(PatchRecordsBase):
    def __init__(self, m=None):
        super().__init__(m)

class GarbageObject(GarbageObjectBase):
    def __init__(self, m=None):
        super().__init__(m)

class GarbageTasks(GarbageTasksBase):
    def __init__(self, m=None):
        super().__init__(m)

class Version(VersionBase):
    def __init__(self, m=None):
        super().__init__(m)

class Filters(FiltersBase):
    def __init__(self, m=None):
        super().__init__(m)

class Chart(ChartBase):
    def __init__(self, m=None):
        super().__init__(m)

class ChartHeatmap(ChartHeatmapBase):
    def __init__(self, m=None):
        super().__init__(m)

class StatisticNode(StatisticNodeBase):
    def __init__(self, m=None):
        super().__init__(m)

class CubeQuery(CubeQueryBase):
    def __init__(self, m=None):
        super().__init__(m)

class RLibrary(RLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)

class FilterTopExpr(FilterTopExprBase):
    def __init__(self, m=None):
        super().__init__(m)

class Filter(FilterBase):
    def __init__(self, m=None):
        super().__init__(m)

class Step(StepBase):
    def __init__(self, m=None):
        super().__init__(m)

class ModelStep(ModelStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class RelationStep(RelationStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class GroupStep(GroupStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskEvent(TaskEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskLogEvent(TaskLogEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class UserSession(UserSessionBase):
    def __init__(self, m=None):
        super().__init__(m)

class Table(TableBase):
    def __init__(self, m=None):
        super().__init__(m)

class Operator(OperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class GitOperator(GitOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class DockerOperator(DockerOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class Acl(AclBase):
    def __init__(self, m=None):
        super().__init__(m)

class CubeAxisQuery(CubeAxisQueryBase):
    def __init__(self, m=None):
        super().__init__(m)

class GateNode(GateNodeBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskSummary(TaskSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)

class Palette(PaletteBase):
    def __init__(self, m=None):
        super().__init__(m)

class RampPalette(RampPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)

class DistinctRelation(DistinctRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunningDependentState(RunningDependentStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class Task(TaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ProjectTask(ProjectTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ExportWorkflowTask(ExportWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class StartProcess(StartProcessBase):
    def __init__(self, m=None):
        super().__init__(m)

class Token(TokenBase):
    def __init__(self, m=None):
        super().__init__(m)

class ActivityCount(ActivityCountBase):
    def __init__(self, m=None):
        super().__init__(m)

class JoinOperator(JoinOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class OperatorModel(OperatorModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class FileMetadata(FileMetadataBase):
    def __init__(self, m=None):
        super().__init__(m)

class CSVFileMetadata(CSVFileMetadataBase):
    def __init__(self, m=None):
        super().__init__(m)

class StepModel(StepModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableStepModel(TableStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class NamespaceStep(NamespaceStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class MeltStep(MeltStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class CrosstabTable(CrosstabTableBase):
    def __init__(self, m=None):
        super().__init__(m)

class XYAxisList(XYAxisListBase):
    def __init__(self, m=None):
        super().__init__(m)

class ColorElement(ColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)

class DoubleColorElement(DoubleColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskProgressEvent(TaskProgressEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class Crosstab(CrosstabBase):
    def __init__(self, m=None):
        super().__init__(m)

class ProjectDocument(ProjectDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)

class Issue(IssueBase):
    def __init__(self, m=None):
        super().__init__(m)

class PatchRecord(PatchRecordBase):
    def __init__(self, m=None):
        super().__init__(m)

class CubeQueryTask(CubeQueryTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ComputationTask(ComputationTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class SaveComputationResultTask(SaveComputationResultTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunComputationTask(RunComputationTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class WorkerEndpoint(WorkerEndpointBase):
    def __init__(self, m=None):
        super().__init__(m)

class ColumnSchemaMetaData(ColumnSchemaMetaDataBase):
    def __init__(self, m=None):
        super().__init__(m)

class Privilege(PrivilegeBase):
    def __init__(self, m=None):
        super().__init__(m)

class CSVTask(CSVTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class Activity(ActivityBase):
    def __init__(self, m=None):
        super().__init__(m)

class ViesInfo(ViesInfoBase):
    def __init__(self, m=None):
        super().__init__(m)

class JoinStepModel(JoinStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class Ulimits(UlimitsBase):
    def __init__(self, m=None):
        super().__init__(m)

class RDescription(RDescriptionBase):
    def __init__(self, m=None):
        super().__init__(m)

class JetPalette(JetPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)

class SimpleRelation(SimpleRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableRelation(TableRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class Date(DateBase):
    def __init__(self, m=None):
        super().__init__(m)

class StepState(StepStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class OperatorResult(OperatorResultBase):
    def __init__(self, m=None):
        super().__init__(m)

class RSourceLibrary(RSourceLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)

class FileDocument(FileDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)

class Address(AddressBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskDataEvent(TaskDataEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class StringProperty(StringPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class XYAxis(XYAxisBase):
    def __init__(self, m=None):
        super().__init__(m)

class Principal(PrincipalBase):
    def __init__(self, m=None):
        super().__init__(m)

class Factor(FactorBase):
    def __init__(self, m=None):
        super().__init__(m)

class Attribute(AttributeBase):
    def __init__(self, m=None):
        super().__init__(m)

class ImportWorkflowTask(ImportWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class Project(ProjectBase):
    def __init__(self, m=None):
        super().__init__(m)

class Url(UrlBase):
    def __init__(self, m=None):
        super().__init__(m)

class StringColorElement(StringColorElementBase):
    def __init__(self, m=None):
        super().__init__(m)

class EnumeratedProperty(EnumeratedPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class TestOperatorTask(TestOperatorTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ImportGitWorkflowTask(ImportGitWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ReferenceRelation(ReferenceRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class RProxy(RProxyBase):
    def __init__(self, m=None):
        super().__init__(m)

class Pair(PairBase):
    def __init__(self, m=None):
        super().__init__(m)

class InMemoryRelation(InMemoryRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunProfile(RunProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class CpuTimeProfile(CpuTimeProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class AxisSettings(AxisSettingsBase):
    def __init__(self, m=None):
        super().__init__(m)

class MappingFilter(MappingFilterBase):
    def __init__(self, m=None):
        super().__init__(m)

class ChartBar(ChartBarBase):
    def __init__(self, m=None):
        super().__init__(m)

class FolderDocument(FolderDocumentBase):
    def __init__(self, m=None):
        super().__init__(m)

class Lock(LockBase):
    def __init__(self, m=None):
        super().__init__(m)

class Worker(WorkerBase):
    def __init__(self, m=None):
        super().__init__(m)

class ImportGitDatasetTask(ImportGitDatasetTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class Ace(AceBase):
    def __init__(self, m=None):
        super().__init__(m)

class InStep(InStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class Labels(LabelsBase):
    def __init__(self, m=None):
        super().__init__(m)

class RenvInstalledLibrary(RenvInstalledLibraryBase):
    def __init__(self, m=None):
        super().__init__(m)

class OperatorSettings(OperatorSettingsBase):
    def __init__(self, m=None):
        super().__init__(m)

class Schema(SchemaBase):
    def __init__(self, m=None):
        super().__init__(m)

class CubeQueryTableSchema(CubeQueryTableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)

class CategoryPalette(CategoryPaletteBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableSummary(TableSummaryBase):
    def __init__(self, m=None):
        super().__init__(m)

class Point(PointBase):
    def __init__(self, m=None):
        super().__init__(m)

class ColumnSchema(ColumnSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)

class Column(ColumnBase):
    def __init__(self, m=None):
        super().__init__(m)

class Summary(SummaryBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaskStateEvent(TaskStateEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class WebAppOperator(WebAppOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class ShinyOperator(ShinyOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class Errors(ErrorsBase):
    def __init__(self, m=None):
        super().__init__(m)

class GlTask(GlTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class FailedState(FailedStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class CanceledState(CanceledStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunWorkflowTask(RunWorkflowTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class GraphicalFactor(GraphicalFactorBase):
    def __init__(self, m=None):
        super().__init__(m)

class RenameRelation(RenameRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class ChartSize(ChartSizeBase):
    def __init__(self, m=None):
        super().__init__(m)

class ChartLine(ChartLineBase):
    def __init__(self, m=None):
        super().__init__(m)

class ColorList(ColorListBase):
    def __init__(self, m=None):
        super().__init__(m)

class CrossTabStep(CrossTabStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class DataStep(DataStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class SearchResult(SearchResultBase):
    def __init__(self, m=None):
        super().__init__(m)

class GateOperatorModel(GateOperatorModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class AnnotationModel(AnnotationModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class ROperator(ROperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class OutStep(OutStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class LibraryTask(LibraryTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class PreProcessor(PreProcessorBase):
    def __init__(self, m=None):
        super().__init__(m)

class Port(PortBase):
    def __init__(self, m=None):
        super().__init__(m)

class InputPort(InputPortBase):
    def __init__(self, m=None):
        super().__init__(m)

class Properties(PropertiesBase):
    def __init__(self, m=None):
        super().__init__(m)

class PropertyValue(PropertyValueBase):
    def __init__(self, m=None):
        super().__init__(m)

class DoneState(DoneStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class AclContext(AclContextBase):
    def __init__(self, m=None):
        super().__init__(m)

class DockerWebAppOperator(DockerWebAppOperatorBase):
    def __init__(self, m=None):
        super().__init__(m)

class OperatorUnitTest(OperatorUnitTestBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableStep(TableStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class RunWebAppTask(RunWebAppTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class UnionRelation(UnionRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class Profiles(ProfilesBase):
    def __init__(self, m=None):
        super().__init__(m)

class FilterExpr(FilterExprBase):
    def __init__(self, m=None):
        super().__init__(m)

class FilterExpr2d(FilterExpr2dBase):
    def __init__(self, m=None):
        super().__init__(m)

class FactorsProperty(FactorsPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class OperatorRef(OperatorRefBase):
    def __init__(self, m=None):
        super().__init__(m)

class JoinStep(JoinStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class WizardStep(WizardStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class WizardStepModel(WizardStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class InitState(InitStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class PendingState(PendingStateBase):
    def __init__(self, m=None):
        super().__init__(m)

class ChartPoint(ChartPointBase):
    def __init__(self, m=None):
        super().__init__(m)

class ColumnPair(ColumnPairBase):
    def __init__(self, m=None):
        super().__init__(m)

class CreateGitOperatorTask(CreateGitOperatorTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class TaxId(TaxIdBase):
    def __init__(self, m=None):
        super().__init__(m)

class IssueMessage(IssueMessageBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableSchema(TableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)

class Plan(PlanBase):
    def __init__(self, m=None):
        super().__init__(m)

class CSVParserParam(CSVParserParamBase):
    def __init__(self, m=None):
        super().__init__(m)

class ExportTableTask(ExportTableTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class GenericEvent(GenericEventBase):
    def __init__(self, m=None):
        super().__init__(m)

class OutputPort(OutputPortBase):
    def __init__(self, m=None):
        super().__init__(m)

class Link(LinkBase):
    def __init__(self, m=None):
        super().__init__(m)

class AppDesign(AppDesignBase):
    def __init__(self, m=None):
        super().__init__(m)

class GarbageTasks2(GarbageTasks2Base):
    def __init__(self, m=None):
        super().__init__(m)

class Workflow(WorkflowBase):
    def __init__(self, m=None):
        super().__init__(m)

class NamedFilter(NamedFilterBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableProfile(TableProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class MeltStepModel(MeltStepModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class ExportModel(ExportModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class AnnotationOperatorModel(AnnotationOperatorModelBase):
    def __init__(self, m=None):
        super().__init__(m)

class Axis(AxisBase):
    def __init__(self, m=None):
        super().__init__(m)

class BooleanProperty(BooleanPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class GatherRelation(GatherRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class ExportStep(ExportStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class ViewStep(ViewStepBase):
    def __init__(self, m=None):
        super().__init__(m)

class ApiCallProfile(ApiCallProfileBase):
    def __init__(self, m=None):
        super().__init__(m)

class Colors(ColorsBase):
    def __init__(self, m=None):
        super().__init__(m)

class CompositeRelation(CompositeRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

class GitProjectTask(GitProjectTaskBase):
    def __init__(self, m=None):
        super().__init__(m)

class ComputedTableSchema(ComputedTableSchemaBase):
    def __init__(self, m=None):
        super().__init__(m)

class TableProperties(TablePropertiesBase):
    def __init__(self, m=None):
        super().__init__(m)

class MappingFactor(MappingFactorBase):
    def __init__(self, m=None):
        super().__init__(m)

class SubscriptionPlan(SubscriptionPlanBase):
    def __init__(self, m=None):
        super().__init__(m)

class FormulaProperty(FormulaPropertyBase):
    def __init__(self, m=None):
        super().__init__(m)

class UserSecret(UserSecretBase):
    def __init__(self, m=None):
        super().__init__(m)

class GroupByRelation(GroupByRelationBase):
    def __init__(self, m=None):
        super().__init__(m)

