# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-14
"""
from unittest import TestCase

import pandas as pd
import numpy as np
from datetime import datetime

from ksif import *


class TestOutcome(TestCase):

    def test_show_plot(self):
        pf = Portfolio()

        outcome = pf.outcome(show_plot=True)
        for value in outcome.values():
            self.assertFalse(pd.isna(value))

    def test_long_only_weighted(self):
        pf = Portfolio()

        outcome = pf.outcome(weighted=MKTCAP)
        for value in outcome.values():
            self.assertFalse(pd.isna(value))

    def test_long_short_weighted(self):
        pf = Portfolio()
        pf['weight'] = np.where(pf[PER] > 0, 1, -1)

        outcome = pf.outcome(weighted='weight')
        for value in outcome.values():
            self.assertFalse(pd.isna(value))

    def test_no_short_period(self):
        pf = Portfolio()
        pf['weight'] = np.where(pf[PER] > 0, 1, -1)
        pf.loc[pf[DATE] == datetime(2019, 1, 31), 'weight'] = 1

        outcome = pf.outcome(weighted='weight')
        for value in outcome.values():
            self.assertFalse(pd.isna(value))
