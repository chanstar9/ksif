# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-14
"""
from unittest import TestCase

from ksif import Portfolio
from ksif.core.columns import *


class TestShowPlot(TestCase):

    def test_show_plot(self):
        pf = Portfolio()
        pf = pf.loc[pf[DATE] >= '2011-05-31', :]

        pf.show_plot()

        pf.show_plot(cumulative=False, weighted=True, title='title', show_benchmark=False)
