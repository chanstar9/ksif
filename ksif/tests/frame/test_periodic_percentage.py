# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 8. 24.
"""
from unittest import TestCase

import numpy as np

from ksif import Portfolio
from ksif.core.columns import PER


class TestPeriodicPercentage(TestCase):

    def test_periodic_percentage(self):
        pf = Portfolio()
        pf = pf.loc[~np.isnan(pf[PER]), :]

        selected_companies = pf.periodic_percentage(min_percentage=0.0, max_percentage=0.5, factor=PER)

        # The number of selected companies times 4 is almost equal to all companies.
        self.assertAlmostEqual(len(selected_companies) / len(pf), 0.5, delta=0.001)

        # The average PER of selected companies is bigger than the average PER of all companies.
        self.assertTrue(np.average(selected_companies[PER]) > np.average(pf[PER]))
