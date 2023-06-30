import unittest
import os 

from tercen.client import context as ctx
import tercen.util.builder as bld
import tercen.util.helper_functions as utl
import pandas as pd
import polars as pl
import numpy as np
import numpy.testing as npt

class TestTercen(unittest.TestCase):
    def setUp(self):
        envs = os.environ
        isLocal = False
        if 'TERCEN_PASSWORD' in envs:
            self.passw = envs['TERCEN_PASSWORD']
        else:
            self.passw = None

        if 'TERCEN_URI' in envs:
            self.serviceUri = envs['TERCEN_URI']
        else:
            self.serviceUri = None
        if 'TERCEN_USERNAME' in envs:
            self.username = envs['TERCEN_USERNAME']
        else:
            isLocal = True
            self.username = 'test'
            self.passw = 'test'
            conf = {}
            with open("./tests/env.conf") as f:
                for line in f:
                    if len(line.strip()) > 0:
                        (key, val) = line.split(sep="=")
                        conf[str(key)] = str(val).strip()

            self.serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])



        self.wkfBuilder = bld.WorkflowBuilder(username=self.username, password=self.passw, serviceUri=self.serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( './tests/data/hospitals.csv' )
        # self.wkfBuilder.add_table_step( df )

        name = self.shortDescription()
        if name == "simple":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"})
        elif name == "simple02":
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"},
                                    columns=[{"name":"Rating.Imaging", "type":"string"}])
        else:
            self.wkfBuilder.add_data_step(yAxis={"name":"Procedure.Hip Knee.Cost", "type":"double"}, 
                                    columns=[{"name":"Rating.Imaging", "type":"string"}],
                                    rows=[{"name":"Rating.Effectiveness", "type":"string"}],
                                    labels=[{"name":"Facility.Name", "type":"string"}],
                                    colors=[{"name":"Facility.Type", "type":"string"}])
            # self.wkfBuilder.add_data_step(yAxis={"name":"measurement", "type":"double"}, 
                        # columns=[{"name":"colFactor", "type":"string"}],
                        # rows=[{"name":"rowFactor", "type":"string"}])
        
        self.context = ctx.TercenContext(
                        username=self.username,
                        password=self.passw,
                        serviceUri=self.serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[1].id,
                        workflowId=self.wkfBuilder.workflow.id)
        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

    # 112.5    
    # @memunit.assert_mb
    def test_save(self) -> None:
        '''simple'''
        df = self.context.select(['.y'])

        df = df.with_columns((pl.col(".y") * 2).alias("y2"))
        
        df = self.context.add_namespace(df) 

        
        rdf_smp = utl.as_relation(df.clone())
        jdf_smp = utl.as_join_operator(rdf_smp, [ ], [ ])


        resDf = self.context.save_relation_dev(jdf_smp) 

        if np.any([c == ".ci" for c in resDf.columns]):
            resDf = resDf.drop(".ci")

        if np.any([c == ".ri" for c in resDf.columns]):
            resDf = resDf.drop(".ri")
        # resDf = resDf.drop(columns=[".ci", ".ri"]) # Automatically from save_dev
        # resDf = resDf.drop(".ci", ".ri")

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = str.split(df.columns[i] , sep='.')[-1]
            c1 = str.split(resDf.columns[i] , sep='.')[-1]
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[df.columns[i]].to_numpy(), resDf[resDf.columns[i]].to_numpy())

    def test_save_col(self) -> None:
        df = self.context.select(['.y', '.ci', '.ri'])

        df = df.with_columns((pl.col(".y") * 2).alias("y2"))
        df = df.with_columns((pl.col(".ci") ).alias("i"))
        df = df.with_columns((pl.col(".ri") ).alias("r"))

        df = df.drop(".ci", ".ri", ".y")
        
        df = self.context.add_namespace(df) 

        rdf = utl.as_relation(df.clone())
        crel = self.context.get_crelation()
        rrel = self.context.get_rrelation()

        rids_factor = ''.join((crel.id, "._rids"))

        rdf = utl.left_join_relation(rdf, crel, ".i", rids_factor)
        rdf = utl.left_join_relation(rdf, rrel, ".i", rids_factor)
        jdf = utl.as_join_operator(rdf, utl.flatten([self.context.cnames, self.context.rnames]), 
                                   utl.flatten([self.context.cnames, self.context.rnames]))

        resDf = self.context.save_relation_dev(jdf) 
        
        if np.any([c == ".ci" for c in resDf.columns]):
            resDf = resDf.drop(".ci")

        if np.any([c == ".ri" for c in resDf.columns]):
            resDf = resDf.drop(".ri")


        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = str.split(df.columns[i] , sep='.')[-1]
            c1 = str.split(resDf.columns[i] , sep='.')[-1]
            
            assert(c0 == c1)
            npt.assert_array_almost_equal(df[df.columns[i]].to_numpy(), resDf[resDf.columns[i]].to_numpy())
            
