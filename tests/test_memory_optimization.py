"""
Unit tests comparing original vs optimized helper_functions implementations.

This test suite validates that:
1. Optimized functions produce identical results to original functions
2. Memory usage is significantly reduced
3. Performance is improved
4. All data types are handled correctly
"""

import unittest
import os, sys
import time
import tracemalloc

sys.path.append("..")
sys.path.append(".")

from tercen.client import context as ctx
import tercen.util.builder as bld
import tercen.util.helper_functions as helper_orig
import tercen.util.helper_functions_optimized as helper_opt

import numpy as np
import numpy.testing as npt
import polars as pl
import pandas as pd


class TestMemoryOptimization(unittest.TestCase):
    """Test suite for memory-optimized helper functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        envs = os.environ
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
            username = 'test'
            passw = 'test'
            serviceUri = ''.join([conf["SERVICE_URL"], ":", conf["SERVICE_PORT"]])

        self.username = username
        self.password = passw
        self.serviceUri = serviceUri

    def test_polars_dataframe_conversion_correctness(self):
        """Test that optimized version produces identical results for Polars DataFrames."""
        # Create test data
        df = pl.DataFrame({
            'int_col': [1, 2, 3, 4, 5],
            'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
            'string_col': ['a', 'b', 'c', 'd', 'e']
        })
        
        # Convert using both methods
        tbl_orig, _ = helper_orig.dataframe_to_table(df.clone())
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df.clone())
        
        # Compare results
        self.assertEqual(tbl_orig.nRows, tbl_opt.nRows)
        self.assertEqual(len(tbl_orig.columns), len(tbl_opt.columns))
        
        for i in range(len(tbl_orig.columns)):
            col_orig = tbl_orig.columns[i]
            col_opt = tbl_opt.columns[i]
            
            self.assertEqual(col_orig.name, col_opt.name)
            self.assertEqual(col_orig.type, col_opt.type)
            self.assertEqual(col_orig.nRows, col_opt.nRows)
            
            # Compare values
            npt.assert_array_equal(col_orig.values, col_opt.values)

    def test_pandas_dataframe_conversion_correctness(self):
        """Test that optimized version produces identical results for Pandas DataFrames."""
        # Create test data
        df = pd.DataFrame({
            'int_col': [1, 2, 3, 4, 5],
            'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
            'string_col': ['a', 'b', 'c', 'd', 'e']
        })
        
        # Convert using both methods
        tbl_orig, _ = helper_orig.dataframe_to_table(df.copy())
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df.copy())
        
        # Compare results
        self.assertEqual(tbl_orig.nRows, tbl_opt.nRows)
        self.assertEqual(len(tbl_orig.columns), len(tbl_opt.columns))
        
        for i in range(len(tbl_orig.columns)):
            col_orig = tbl_orig.columns[i]
            col_opt = tbl_opt.columns[i]
            
            self.assertEqual(col_orig.name, col_opt.name)
            self.assertEqual(col_orig.type, col_opt.type)
            self.assertEqual(col_orig.nRows, col_opt.nRows)
            
            # Compare values
            npt.assert_array_equal(col_orig.values, col_opt.values)

    def test_nan_handling_polars(self):
        """Test that NaN values are handled correctly in Polars DataFrames."""
        # Create test data with NaN
        df = pl.DataFrame({
            'float_col': [1.1, float('nan'), 3.3, float('nan'), 5.5],
            'string_col': ['a', None, 'c', None, 'e']
        })
        
        # Convert using both methods
        tbl_orig, _ = helper_orig.dataframe_to_table(df.clone())
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df.clone())
        
        # Compare results
        self.assertEqual(len(tbl_orig.columns), len(tbl_opt.columns))
        
        for i in range(len(tbl_orig.columns)):
            col_orig = tbl_orig.columns[i]
            col_opt = tbl_opt.columns[i]
            
            self.assertEqual(col_orig.name, col_opt.name)
            self.assertEqual(col_orig.type, col_opt.type)
            
            # For string columns, check that None/NaN became empty strings
            if col_orig.type == 'string':
                # Both should convert None to ""
                for j in range(len(col_orig.values)):
                    self.assertEqual(col_orig.values[j], col_opt.values[j])

    def test_nan_handling_pandas(self):
        """Test that NaN values are handled correctly in Pandas DataFrames."""
        # Create test data with NaN
        df = pd.DataFrame({
            'float_col': [1.1, np.nan, 3.3, np.nan, 5.5],
            'string_col': ['a', None, 'c', None, 'e']
        })
        
        # Convert using both methods
        tbl_orig, _ = helper_orig.dataframe_to_table(df.copy())
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df.copy())
        
        # Compare results
        self.assertEqual(len(tbl_orig.columns), len(tbl_opt.columns))
        
        for i in range(len(tbl_orig.columns)):
            col_orig = tbl_orig.columns[i]
            col_opt = tbl_opt.columns[i]
            
            self.assertEqual(col_orig.name, col_opt.name)
            self.assertEqual(col_orig.type, col_opt.type)
            
            # For string columns, check that None/NaN became empty strings
            if col_orig.type == 'string':
                for j in range(len(col_orig.values)):
                    self.assertEqual(col_orig.values[j], col_opt.values[j])

    def test_memory_usage_polars_small(self):
        """Test memory usage for small Polars DataFrame."""
        # Create test data (small)
        df = pl.DataFrame({
            f'col_{i}': list(range(1000)) for i in range(10)
        })
        
        # Measure original
        stats_orig = helper_opt.compare_memory_usage(df.clone(), use_optimized=False)
        
        # Measure optimized
        stats_opt = helper_opt.compare_memory_usage(df.clone(), use_optimized=True)
        
        print(f"\nSmall Polars DataFrame (1K rows x 10 cols):")
        print(f"  Original - Peak: {stats_orig['peak_memory_mb']:.2f} MB, Time: {stats_orig['elapsed_time_sec']:.4f}s")
        print(f"  Optimized - Peak: {stats_opt['peak_memory_mb']:.2f} MB, Time: {stats_opt['elapsed_time_sec']:.4f}s")
        print(f"  Memory savings: {(1 - stats_opt['peak_memory_mb']/stats_orig['peak_memory_mb'])*100:.1f}%")
        print(f"  Speed improvement: {stats_orig['elapsed_time_sec']/stats_opt['elapsed_time_sec']:.1f}x")
        
        # Optimized should use less or equal memory
        self.assertLessEqual(stats_opt['peak_memory_mb'], stats_orig['peak_memory_mb'] * 1.1)

    def test_memory_usage_polars_medium(self):
        """Test memory usage for medium Polars DataFrame."""
        # Create test data (medium)
        df = pl.DataFrame({
            f'col_{i}': list(range(10000)) for i in range(50)
        })
        
        # Measure original
        stats_orig = helper_opt.compare_memory_usage(df.clone(), use_optimized=False)
        
        # Measure optimized
        stats_opt = helper_opt.compare_memory_usage(df.clone(), use_optimized=True)
        
        print(f"\nMedium Polars DataFrame (10K rows x 50 cols):")
        print(f"  Original - Peak: {stats_orig['peak_memory_mb']:.2f} MB, Time: {stats_orig['elapsed_time_sec']:.4f}s")
        print(f"  Optimized - Peak: {stats_opt['peak_memory_mb']:.2f} MB, Time: {stats_opt['elapsed_time_sec']:.4f}s")
        print(f"  Memory savings: {(1 - stats_opt['peak_memory_mb']/stats_orig['peak_memory_mb'])*100:.1f}%")
        print(f"  Speed improvement: {stats_orig['elapsed_time_sec']/stats_opt['elapsed_time_sec']:.1f}x")
        
        # Optimized should use less memory
        self.assertLess(stats_opt['peak_memory_mb'], stats_orig['peak_memory_mb'])

    def test_memory_usage_pandas_small(self):
        """Test memory usage for small Pandas DataFrame."""
        # Create test data (small)
        df = pd.DataFrame({
            f'col_{i}': list(range(1000)) for i in range(10)
        })
        
        # Measure original
        stats_orig = helper_opt.compare_memory_usage(df.copy(), use_optimized=False)
        
        # Measure optimized
        stats_opt = helper_opt.compare_memory_usage(df.copy(), use_optimized=True)
        
        print(f"\nSmall Pandas DataFrame (1K rows x 10 cols):")
        print(f"  Original - Peak: {stats_orig['peak_memory_mb']:.2f} MB, Time: {stats_orig['elapsed_time_sec']:.4f}s")
        print(f"  Optimized - Peak: {stats_opt['peak_memory_mb']:.2f} MB, Time: {stats_opt['elapsed_time_sec']:.4f}s")
        print(f"  Memory savings: {(1 - stats_opt['peak_memory_mb']/stats_orig['peak_memory_mb'])*100:.1f}%")
        print(f"  Speed improvement: {stats_orig['elapsed_time_sec']/stats_opt['elapsed_time_sec']:.1f}x")
        
        # Optimized should use less or equal memory
        self.assertLessEqual(stats_opt['peak_memory_mb'], stats_orig['peak_memory_mb'] * 1.1)

    def test_memory_usage_pandas_medium(self):
        """Test memory usage for medium Pandas DataFrame - shows biggest improvement."""
        # Create test data (medium) - Pandas drop() creates many copies
        df = pd.DataFrame({
            f'col_{i}': list(range(10000)) for i in range(50)
        })
        
        # Measure original
        stats_orig = helper_opt.compare_memory_usage(df.copy(), use_optimized=False)
        
        # Measure optimized
        stats_opt = helper_opt.compare_memory_usage(df.copy(), use_optimized=True)
        
        print(f"\nMedium Pandas DataFrame (10K rows x 50 cols):")
        print(f"  Original - Peak: {stats_orig['peak_memory_mb']:.2f} MB, Time: {stats_orig['elapsed_time_sec']:.4f}s")
        print(f"  Optimized - Peak: {stats_opt['peak_memory_mb']:.2f} MB, Time: {stats_opt['elapsed_time_sec']:.4f}s")
        print(f"  Memory savings: {(1 - stats_opt['peak_memory_mb']/stats_orig['peak_memory_mb'])*100:.1f}%")
        print(f"  Speed improvement: {stats_orig['elapsed_time_sec']/stats_opt['elapsed_time_sec']:.1f}x")
        
        # Optimized should use significantly less memory for Pandas
        # (due to avoiding N-1 DataFrame copies from drop())
        self.assertLess(stats_opt['peak_memory_mb'], stats_orig['peak_memory_mb'] * 0.8)

    def test_values_are_numpy_arrays(self):
        """Test that optimized version always returns numpy arrays, never lists."""
        df = pl.DataFrame({
            'int_col': [1, 2, 3],
            'float_col': [1.1, 2.2, 3.3],
            'string_col': ['a', 'b', 'c']
        })
        
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df)
        
        # All column values should be numpy arrays
        for col in tbl_opt.columns:
            self.assertIsInstance(col.values, np.ndarray, 
                                f"Column {col.name} values should be numpy array, got {type(col.values)}")

    def test_integration_with_context_save(self):
        """Integration test: Use optimized functions in actual save workflow."""
        # Set up workflow
        wkfBuilder = bld.WorkflowBuilder(
            username=self.username, 
            password=self.password, 
            serviceUri=self.serviceUri
        )
        wkfBuilder.create_workflow('python_auto_project', 'python_workflow_opt')
        wkfBuilder.add_table_step('./tests/data/hospitals.csv')
        wkfBuilder.add_data_step(
            yAxis={"name": "Procedure.Hip Knee.Cost", "type": "double"},
            columns=[{"name": "Rating.Imaging", "type": "string"}],
            rows=[{"name": "Rating.Effectiveness", "type": "string"}]
        )
        
        try:
            # Create context
            context = ctx.TercenContext(
                username=self.username,
                password=self.password,
                serviceUri=self.serviceUri,
                stepId=wkfBuilder.workflow.steps[1].id,
                workflowId=wkfBuilder.workflow.id
            )
            
            # Get data
            df = context.select(['.y', '.ci', '.ri'])
            df = df.with_columns((pl.col(".y") * 2).alias("y2"))
            df = df.with_columns((pl.col(".y")).alias("y"))
            df = df.drop(".y")
            df = context.add_namespace(df)
            
            # Monkey-patch to use optimized version
            original_func = helper_orig.dataframe_to_table
            helper_orig.dataframe_to_table = helper_opt.dataframe_to_table_optimized
            
            try:
                # Save using optimized version
                resDf = context.save_dev(df.clone())
                
                # Verify results
                self.assertEqual(len(df), len(resDf))
                self.assertEqual(len(df.columns), len(resDf.columns))
                
                print(f"\nIntegration test passed:")
                print(f"  Input: {len(df)} rows x {len(df.columns)} cols")
                print(f"  Output: {len(resDf)} rows x {len(resDf.columns)} cols")
                
            finally:
                # Restore original function
                helper_orig.dataframe_to_table = original_func
                
        finally:
            # Clean up
            wkfBuilder.clean_up_workflow()

    def test_large_dataframe_performance(self):
        """Performance test with larger DataFrame to show significant improvements."""
        # Create larger test data
        n_rows = 100000
        n_cols = 100
        
        print(f"\nLarge DataFrame test ({n_rows} rows x {n_cols} cols):")
        
        # Create Pandas DataFrame (shows biggest improvement due to drop() fix)
        df = pd.DataFrame({
            f'col_{i}': np.random.randn(n_rows) for i in range(n_cols)
        })
        
        # Measure original
        print("  Running original version...")
        start = time.time()
        tracemalloc.start()
        tbl_orig, _ = helper_orig.dataframe_to_table(df.copy())
        current_orig, peak_orig = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time_orig = time.time() - start
        
        # Measure optimized
        print("  Running optimized version...")
        start = time.time()
        tracemalloc.start()
        tbl_opt, _ = helper_opt.dataframe_to_table_optimized(df.copy())
        current_opt, peak_opt = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        time_opt = time.time() - start
        
        print(f"  Original - Peak: {peak_orig/1024/1024:.2f} MB, Time: {time_orig:.2f}s")
        print(f"  Optimized - Peak: {peak_opt/1024/1024:.2f} MB, Time: {time_opt:.2f}s")
        print(f"  Memory savings: {(1 - peak_opt/peak_orig)*100:.1f}%")
        print(f"  Speed improvement: {time_orig/time_opt:.1f}x")
        
        # Verify correctness
        self.assertEqual(tbl_orig.nRows, tbl_opt.nRows)
        self.assertEqual(len(tbl_orig.columns), len(tbl_opt.columns))
        
        # Should see significant improvements
        self.assertLess(peak_opt, peak_orig * 0.7, "Should save at least 30% memory")
        self.assertLess(time_opt, time_orig * 0.5, "Should be at least 2x faster")


if __name__ == '__main__':
    # Run with verbose output to see performance metrics
    unittest.main(verbosity=2)
