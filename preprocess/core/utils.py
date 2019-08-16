# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 22.
"""
import datetime

import numpy as np
from pandas import Series


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


def zero_to_nan(series: Series) -> Series:
    return series.apply(lambda x: np.where(x == 0, np.nan, x))

def disparity(adj_close_p: Series, price_ma: Series):
    return adj_close_p/price_ma*100

def gap_rise(adj_close_p: Series,adj_open_p: Series):
    return (adj_close_p>adj_open_p.shift(1)).to_frame()

def golden_cross(price_ma20:Series, price_ma60:Series):
    df = price_ma20 > price_ma60
    pre_position= df.shift(1)
    pre_position.fillna(method='bfill')
    cross=(df!=pre_position)
    return cross.to_frame()