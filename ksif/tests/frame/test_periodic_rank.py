# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 8. 24.
"""
from unittest import TestCase

from ksif import *


class TestPeriodicRank(TestCase):

    def test_periodic_rank(self):
        pf = Portfolio()
        pf = pf.periodic_rank(min_rank=26, max_rank=50)

        # Periodic sizes are 25.
        pf.groupby(by=DATE).size().apply(lambda x: self.assertEqual(x, 25))
