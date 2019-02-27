# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 8. 24.
"""
from unittest import TestCase

from ksif import *


class TestPeriodicStandardize(TestCase):

    def test_periodic_standardize(self):
        pf = Portfolio()

        prefix = 'std_'
        std_per = prefix + PER

        pf = pf.periodic_standardize(factor=PER, prefix=prefix)

        # Periodic means are almost 0.
        pf.groupby(by=DATE)[std_per].mean().apply(lambda x: self.assertAlmostEqual(x, 0))
