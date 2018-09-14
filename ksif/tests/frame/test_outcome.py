# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-14
"""
from unittest import TestCase

import pandas as pd

from ksif import Portfolio


class TestOutcome(TestCase):

    def test_outcome(self):
        pf = Portfolio()

        outcome = pf.outcome()
        for value in outcome.values():
            self.assertFalse(pd.isna(value))
