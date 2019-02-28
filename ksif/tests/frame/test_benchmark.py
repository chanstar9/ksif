# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 8. 24.
"""
from unittest import TestCase

from ksif import *
from pandas.util.testing import assert_frame_equal


class TestBenchmark(TestCase):

    def test_benchmark(self):
        pf = Portfolio()

        # The return of Portfolio.benchmark should be str.
        self.assertEqual(type(pf.benchmark), str)

    def test_get_benchmark(self):
        pf = Portfolio()

        # The default benchmark is KOSPI.
        benchmark = pf.get_benchmark()
        self.assertEqual(benchmark.columns.tolist(),
                         [BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12])

        # If the benchmark is set, return the benchmark.
        benchmark = pf.get_benchmark(benchmark=KOSDAQ)
        self.assertEqual(benchmark.columns.tolist(),
                         [BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12])

        # If the benchmark is not exist, raise ValueError.
        with self.assertRaises(ValueError):
            pf.get_benchmark(benchmark='There is no such a benchmark.')

    def test_set_benchmark(self):
        pf = Portfolio()

        # If the benchmark is not exist, raise ValueError.
        with self.assertRaises(ValueError):
            pf.set_benchmark(benchmark='There is no such a benchmark.')

        # If the benchmark is exist, change the default benchmark.
        kosdaq_1 = pf.get_benchmark(benchmark=KOSDAQ)
        pf.set_benchmark(benchmark=KOSDAQ)
        kosdaq_2 = pf.get_benchmark()

        assert_frame_equal(kosdaq_1, kosdaq_2)
