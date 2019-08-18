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


def disparity(close_p: Series, price_ma: Series):
    return close_p / price_ma * 100


def gap_rise(close_p: Series, open_p: Series):
    return ((open_p > close_p.shift(1)) & (close_p > close_p.shift(1))).to_frame()


def golden_cross(price_ma20: Series, price_ma60: Series):
    df = price_ma20 > price_ma60
    pre_position = df.shift(1)
    pre_position.fillna(method='bfill')
    cross = (df != pre_position)
    return cross.to_frame()


# technical indicator
def big_bull_candle(open, high, low, close, volume):
    if volume.shift(-1) * 2 < volume:
        return 1
    else:
        return 0


def accumulation_candle(open, close, volume):
    return (volume.shift(1) * 2 < volume) & ((close - open) / open <= 0.08) & (0 <= (close - open) / open)
