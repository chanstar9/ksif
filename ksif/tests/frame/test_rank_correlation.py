# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-16
"""
from unittest import TestCase

from ksif import Portfolio
from ksif.core.columns import *
from ksif.core.frame import RANK_CORRELATION


class TestRankCorrelation(TestCase):

    def test_rank_correlation(self):
        pf = Portfolio()
        rank_ic = pf.rank_correlation(factor=PER, ranked_by=RET_3, rolling=12, show_plot=True, title='PER-RET_3 Rank Correlation')
        self.assertEquals(sorted(rank_ic.columns), sorted([RANK_CORRELATION, 'rolling_12']))
