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
    return adj_close_p / price_ma * 100


def gap_rise(adj_close_p: Series, adj_open_p: Series):
    return (adj_close_p > zero_to_nan(adj_open_p.shift(1))).to_frame()


def rise_divergence(morning_star: Series, obv: Series):
    signal = Series(np.where(morning_star == 1)[0])
    pre_signal = Series(np.where(morning_star == 1)[0]).shift(1)
    pre_signal = pre_signal.fillna(method='bfill')
    rise = (obv[signal].reset_index(drop=True) > obv[pre_signal].reset_index(drop=True))
    # 이번 morning star시점의 obv가 직전에 발생한 morning star시점의 obv보다 높다면 rise_divergence다
    morning_star[rise[rise == True].index] += 1
    morning_star[morning_star != 2] = 0
    morning_star[morning_star == 2] = 1
    return morning_star


def double_bottom(three_inside_up: Series, time_period):
    # ss파일 기준 three_inside_up이 더 자주 발생하여 일단 이걸로 쌍바닥 찾음.
    # time_period 안에 three_inside_up이 두번 발생하면 쌍바닥으로 정의.
    signal = Series(np.where(three_inside_up == 1)[0])
    interval = signal.diff()
    interval[interval <= time_period] = 1
    interval[interval > time_period] = 0
    ind = interval * signal
    ind = ind.dropna()
    ind = ind[ind != 0]
    ind = ind.reindex(index=ind.values)
    three_inside_up[ind.index] += 1
    return three_inside_up


def golden_cross(price_ma20: Series, price_ma60: Series):
    df = price_ma20 > price_ma60
    pre_position = df.shift(1)
    pre_position = pre_position.fillna(method='bfill')
    cross = (df != pre_position) * 1
    return cross.to_frame()
