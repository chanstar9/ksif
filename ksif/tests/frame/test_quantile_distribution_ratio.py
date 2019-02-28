# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-16
"""
from unittest import TestCase

from ksif import *


class TestQuantileDistributionRatio(TestCase):

    def test_quantile_distribution_ratio(self):
        pf = Portfolio(start_date='2017-01-01')

        # When chunk_num is less than or equal to 1, raise an assertion error.
        with self.assertRaises(AssertionError):
            pf.quantile_distribution_ratio(factor=MKTCAP, chunk_num=1)
        with self.assertRaises(AssertionError):
            pf.quantile_distribution_ratio(factor=MKTCAP, chunk_num=-1)

        # All true parameters with a title.
        # The length of the result data frame is equal to original unique DATE minus one.
        date_num = len(pf[DATE].unique())
        result_data = pf.quantile_distribution_ratio(factor=MKTCAP, cumulative=True, weighted=True, only_positive=True,
                                                     show_plot=True, show_bar_chart=True, title='title')
        self.assertEqual(date_num - 1, len(result_data))

        # All true parameters with a title.
        # The length of the result data frame is equal to original unique DATE minus one.
        date_num = len(pf[DATE].unique())
        result_data = pf.quantile_distribution_ratio(factor=MKTCAP, cumulative=False, weighted=False,
                                                     only_positive=False, show_plot=False, show_bar_chart=False)
        self.assertEqual(date_num - 1, len(result_data))
