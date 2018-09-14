# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018-09-14
"""
from unittest import TestCase

import pandas as pd

from ksif.util.checker import not_empty
from ksif.errors import EmptyResultException


class TestChecker(TestCase):

    def test_not_empty(self):
        @not_empty
        def test_empty_dataframe():
            return pd.DataFrame()

        # test_empty_dataframe should raise a EmptyResultException.
        with self.assertRaises(EmptyResultException):
            test_empty_dataframe()

        @not_empty
        def test_empty_series():
            return pd.Series()

        # test_empty_series should raise a EmptyResultException.
        with self.assertRaises(EmptyResultException):
            test_empty_series()

        @not_empty
        def test_none():
            return None

        # test_none should raise nothing.
        test_none()
