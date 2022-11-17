import pandas as pd
from itertools import chain

from ..util import helper_functions as utl


class TercenContext:
    # FIXME client should be obtained from elsewhere
    def __init__(self, client, workflowId, stepId):
        self.client = client
        self.cubeQuery = client.workflowService.getCubeQuery(workflowId, stepId)

        self.schema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.qtHash] )[0]
        self.cschema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.columnHash] )[0]
        self.rschema = client.tableSchemaService.findByQueryHash( keys=[self.cubeQuery.rowHash] )[0]

        self.names = [col.name for col in self.schema.columns] 
        self.cnames = [col.name for col in self.cschema.columns] 
        self.rnames = [col.name for col in self.rschema.columns] 

        axisQueries = self.cubeQuery.axisQueries

        self.colors = [c.name for q in axisQueries for c in q.colors]
        self.labels = [l.name for q in axisQueries for l in q.labels]
        self.errors = [l.name for q in axisQueries for l in q.errors]
        self.chartType = [q.chartType for q in axisQueries ]
        self.pointSizes = [q.pointSize for q in axisQueries ]

        
        self.yAxis = utl.unique_and_nonempty( [q.yAxis.name for q in axisQueries])
        self.xAxis = utl.unique_and_nonempty( [q.xAxis.name for q in axisQueries])


        self.hasXAxis = any([ col.name == ".x" for col in self.schema.columns ])
        self.hasNumericXAxis = any([ col.name == ".x" and col.type == "double" for col in self.schema.columns ])

        self.isPairwise = len(set(self.cnames).intersection( set(self.rnames) )) > 0

    def select(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.schema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.schema.columns, where) ]

        if( self.isPairwise ):
            res = self.client.tableSchemaService.selectPairwise(  self.schema.id, names, offset, nr)
        else:
            res = self.client.tableSchemaService.select(  self.schema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def cselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.cschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.cschema.columns, where) ]

        res = self.client.tableSchemaService.select(  self.cschema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

    def rselect(self, names=[], offset=0, nr=None) -> pd.DataFrame:
        if not nr is None and nr < 0:
            nr = None

        if( names is None or len(names) == 0 or (len(names) == 1 and names[0] == '' )):
            where = utl.logical_index([ c.type != 'uint64' and c.type != 'int64' for c in self.rschema.columns ])
            names = [ c.name for c in utl.get_from_idx_list( self.rschema.columns, where) ]

        res = self.client.tableSchemaService.select(  self.rschema.id, names, offset, nr)

        df = pd.DataFrame()

        for c in res.columns:
            df[c.name] = c.values

        
        return df

