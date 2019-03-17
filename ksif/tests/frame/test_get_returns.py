# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-14
"""
from datetime import datetime
from unittest import TestCase

import numpy as np
import pandas as pd

from ksif import *


class TestOutcome(TestCase):

    def test_long_only_weighted(self):
        pf = Portfolio()

        returns = pf.get_returns()
        self.assertFalse(pd.isna(all(returns[PORTFOLIO_RETURN])))

    def test_long_short_weighted(self):
        pf = Portfolio()
        pf['weight'] = np.where(pf[PER] > 0, 1, -1)

        returns = pf.get_returns(weighted='weight')
        self.assertFalse(pd.isna(all(returns[PORTFOLIO_RETURN])))

    def test_no_short_period(self):
        pf = Portfolio()
        pf['weight'] = np.where(pf[PER] > 0, 1, -1)
        pf.loc[pf[DATE] == datetime(2019, 1, 31), 'weight'] = 1

        returns = pf.get_returns(weighted='weight')
        self.assertFalse(pd.isna(all(returns[PORTFOLIO_RETURN])))
