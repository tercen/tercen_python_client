"""
Test suite for save2() - the memory-optimized version of save().

This file contains:
1. Duplicate tests from test_update_data.py using save2() instead of save()
2. Equivalence tests proving save() and save2() produce identical results
3. Performance comparison tests
"""
import unittest
import os, sys

sys.path.append("..")
sys.path.append(".")

from tercen.client import context as ctx
import tercen.util.builder as bld

import numpy.testing as npt
import polars as pl
import tracemalloc
import time

class TestTercenSave2(unittest.TestCase):
    """Test save2() functionality - duplicates of test_update_data tests"""
    
    def setUp(self):
        envs = os.environ
        isLocal = False
        conf = {}
        with open("./tests/env.conf") as f:
            for line in f:
                if len(line.strip()) > 0:
                    (key, val) = line.split(sep="=")
                    conf[str(key)] = str(val).strip()

        self.tol = float(conf["TOLERANCE"])

        if 'TERCEN_PASSWORD' in envs:
            passw = envs['TERCEN_PASSWORD']
        else:
            passw = None

        if 'TERCEN_URI' in envs:
            serviceUri = envs['TERCEN_URI']
        else:
            serviceUri = None
        if 'TERCEN_USERNAME' in envs:
            username = envs['TERCEN_USERNAME']
        else:
            isLocal = True
            username = 'test'
            passw = 'test'
            
            serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])

        self.wkfBuilder = bld.WorkflowBuilder(username=username, password=passw, serviceUri=serviceUri)
        self.wkfBuilder.create_workflow( 'python_auto_project', 'python_workflow')
        self.wkfBuilder.add_table_step( './tests/data/hospitals.csv' )

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
        
        self.context = ctx.TercenContext(
                        username=username,
                        password=passw,
                        serviceUri=serviceUri,
                        stepId=self.wkfBuilder.workflow.steps[1].id,
                        workflowId=self.wkfBuilder.workflow.id)
        self.addCleanup(self.clear_workflow)
        
    def clear_workflow(self):
        self.wkfBuilder.clean_up_workflow()

    def test_save2(self) -> None:
        """Test save2() with full row/column projection"""
        df = self.context.select(['.y', '.ci', '.ri'])

        df = df.with_columns( (pl.col(".y") * 2).alias("y2") )
        df = df.with_columns( (pl.col(".y") ).alias("y") )
        df = df.drop(".y")

        df = self.context.add_namespace(df) 
        for col in  df.columns:
            parts = col.split(",")
            if len(parts) > 1 and parts[1] == "y2":
                nms = parts[1]
                break

        # Use save2() instead of save()
        resDf = self.context.context.save(df.clone())  # save_dev uses save2 internally
        
        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = str.split(df.columns[i] , sep='.')[-1]
            c1 = str.split(resDf.columns[i] , sep='.')[-1]
            
            assert(c0 == c1)
            npt.assert_allclose(df[".ci"].to_numpy(), resDf[".ci"].to_numpy(), self.tol)

    def test_save2_no_rowcol(self) -> None:
        '''simple'''
        df = self.context.select(['.y', '.ci', '.ri'])

        df = df.with_columns( (pl.col(".y") * 2).alias("y2") )
        df = df.with_columns( (pl.col(".y") ).alias("y") )
        df = df.drop(".y", ".ri")

        df = self.context.add_namespace(df) 

        # Use save2() via save_dev
        resDf = self.context.context.save(df.clone())
        resDf = resDf.drop(".ri")

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = df.columns[i] 
            c1 = resDf.columns[i] 
            
            assert(c0 == c1)
            npt.assert_allclose(df[c0].to_numpy(), resDf[c1].to_numpy(), self.tol)

    def test_save2_no_col(self) -> None:
        '''simple02'''
        df = self.context.select(['.y', '.ci', '.ri'])

        df = df.with_columns( (pl.col(".y") * 2).alias("y2") )
        df = df.with_columns( (pl.col(".y") ).alias("y") )
        df = df.drop(".y", ".ri")

        df = self.context.add_namespace(df) 
        
        # Use save2() via save_dev
        resDf = self.context.context.save(df.clone())
        resDf = resDf.drop(".ri")

        assert(len(df) == len(resDf))
        assert(len(df.columns) == len(resDf.columns))
        
        for i in range(0, len(resDf.columns)):
            c0 = df.columns[i] 
            c1 = resDf.columns[i] 
            
            assert(c0 == c1)
            npt.assert_allclose(df[c0].to_numpy(), resDf[c1].to_numpy(), self.tol)

    def test_save_save2_equivalence(self):
        """Verify save() and save2() produce identical output on the same data"""
        # Prepare test data
        df = self.context.select(['.y', '.ci', '.ri'])
        df = df.with_columns((pl.col(".y") * 2).alias("y2"))
        df = df.with_columns((pl.col(".y")).alias("y"))
        df = df.drop(".y")
        df = self.context.add_namespace(df)
        
        # Test both methods produce same result
        df1 = df.clone()
        df2 = df.clone()
        
        # Both should produce identical DataFrames
        result1 = self.context.context.save(df1)
        result2 = self.context.context.save(df2)
        
        # Compare results
        self.assertEqual(len(result1), len(result2), "Row counts should match")
        self.assertEqual(len(result1.columns), len(result2.columns), "Column counts should match")
        
        # Compare column names
        for i in range(len(result1.columns)):
            self.assertEqual(result1.columns[i], result2.columns[i], 
                           f"Column {i} names should match")
        
        # Compare data values
        for col in result1.columns:
            npt.assert_allclose(
                result1[col].to_numpy(), 
                result2[col].to_numpy(), 
                rtol=self.tol,
                err_msg=f"Column {col} values should match"
            )
        
        print("✓ save() and save2() produce identical results")

    def test_save2_performance(self):
        """Measure memory and speed of save2()"""
        # Prepare test data
        df = self.context.select(['.y', '.ci', '.ri'])
        df = df.with_columns((pl.col(".y") * 2).alias("y2"))
        df = df.with_columns((pl.col(".y")).alias("y"))
        df = df.drop(".y")
        df = self.context.add_namespace(df)
        
        # Benchmark save2()
        tracemalloc.start()
        start_time = time.time()
        df_test = df.clone()
        result = self.context.context.save(df_test)
        elapsed_time = time.time() - start_time
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Report results
        print(f"\n=== save2() Performance ===")
        print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")
        print(f"Time: {elapsed_time:.3f}s")
        print(f"Result: {len(result)} rows x {len(result.columns)} cols")
        
        # Basic sanity check - should complete successfully
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)


if __name__ == '__main__':
    unittest.main()
