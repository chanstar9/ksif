# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 7. 6.
"""
import pandas as pd
from pandas import DataFrame
import numpy as np
from copy import copy

from core.columns import *
from core.utils import zero_to_nan

YEAR = 'year'
MONTH_DAY = 'month_day'

EV = 'ev'
AVG_EQUITY = 'avg_equity'
AVG_ASSET = 'avg_asset'


def process_companies(unprocessed_companies: DataFrame) -> DataFrame:
    """

    :param unprocessed_companies: (DataFrame)

    :return processed_companies: (DataFrame)
    """
    # Calculate fiscal quarters of daily data.
    daily_companies = unprocessed_companies.loc[:, DAILY_DATA]
    daily_companies[MONTH_DAY] = daily_companies[DATE].dt.month * 100 + daily_companies[DATE].dt.day
    daily_companies[YEAR] = daily_companies[DATE].dt.year
    daily_companies[FISCAL_QUARTER] = 0
    daily_companies.loc[
        (daily_companies[MONTH_DAY] >= 402) & (daily_companies[MONTH_DAY] < 515), FISCAL_QUARTER
    ] = daily_companies[YEAR] * 10 + 4
    daily_companies.loc[
        (daily_companies[MONTH_DAY] >= 515) & (daily_companies[MONTH_DAY] < 814), FISCAL_QUARTER
    ] = daily_companies[YEAR] * 10 + 1
    daily_companies.loc[
        (daily_companies[MONTH_DAY] >= 814) & (daily_companies[MONTH_DAY] < 1114), FISCAL_QUARTER
    ] = daily_companies[YEAR] * 10 + 2
    daily_companies.loc[
        (daily_companies[MONTH_DAY] < 402) | (daily_companies[MONTH_DAY] >= 1114), FISCAL_QUARTER
    ] = daily_companies[YEAR] * 10 + 3
    daily_companies.loc[(daily_companies[MONTH_DAY] < 515), FISCAL_QUARTER] += -10

    # market capital = $ of common stocks * # of common stocks + $ of preferred stocks + # of preferred stocks
    daily_companies[MKTCAP] = daily_companies[ENDP] * (daily_companies[OUTCST] + daily_companies[CS_TOBEPUB]) + \
                              daily_companies[ENDP_PS] * (daily_companies[OUTPST] + daily_companies[PS_TOBEPUB])
    # market capital of common stocks = $ of common stocks * # of common stocks
    daily_companies[MKTCAP_CS] = daily_companies[ENDP] * (daily_companies[OUTCST] + daily_companies[CS_TOBEPUB])

    # Calculate fiscal quarters of quarterly data.
    quarterly_companies = unprocessed_companies.loc[
        unprocessed_companies.date.dt.month.isin([3, 6, 9, 12]), QUARTERLY_DATA
    ]
    quarterly_companies[FISCAL_QUARTER] = quarterly_companies[DATE].dt.year * 10 + (
            quarterly_companies[DATE].dt.month / 3)
    quarterly_companies = quarterly_companies.drop(columns=[DATE])

    quarterly_companies['sales12'] = quarterly_companies.groupby(CODE)[SALES].rolling(4).sum().reset_index(0, drop=True)
    quarterly_companies['gp12'] = quarterly_companies.groupby(CODE)[GP].rolling(4).sum().reset_index(0, drop=True)
    quarterly_companies['op12'] = quarterly_companies.groupby(CODE)[EBIT].rolling(4).sum().reset_index(0, drop=True)
    quarterly_companies['ni12'] = quarterly_companies.groupby(CODE)[NI_OWNER].rolling(4).sum().reset_index(0, drop=True)
    quarterly_companies['cfo12'] = quarterly_companies.groupby(CODE)[CFO].rolling(4).sum().reset_index(0, drop=True)
    quarterly_companies['ebitda12'] = quarterly_companies.groupby(CODE)[EBITDA].rolling(4).sum().reset_index(0,
                                                                                                             drop=True)
    quarterly_companies['ebt12'] = (
            quarterly_companies.groupby(CODE)[NI].rolling(4).sum().reset_index(0, drop=True) +
            quarterly_companies.groupby(
                CODE)[TAX].rolling(4).sum().reset_index(0, drop=True))

    quarterly_companies['nopat12'] = (
            quarterly_companies['op12'] - quarterly_companies.groupby(CODE)[TAX].rolling(4).sum().reset_index(0,
                                                                                                              drop=True))

    quarterly_companies[AVG_ASSET] = quarterly_companies.groupby(CODE)[ASSETS].rolling(4).mean().reset_index(0,
                                                                                                             drop=True)
    quarterly_companies[AVG_EQUITY] = quarterly_companies.groupby(CODE)[ASSETS].rolling(4).mean().reset_index(0,
                                                                                                              drop=True)

    quarterly_companies[S_A] = quarterly_companies['sales12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[GP_A] = quarterly_companies['gp12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[OP_A] = quarterly_companies['op12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[CF_A] = quarterly_companies['cfo12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[ROA] = quarterly_companies['ni12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[ROE] = quarterly_companies['ni12'] / zero_to_nan(quarterly_companies[AVG_EQUITY])
    quarterly_companies[QROA] = quarterly_companies[NI_OWNER] / zero_to_nan(quarterly_companies.groupby(CODE)[
        ASSETS].rolling(2).mean().reset_index(0, drop=True))
    quarterly_companies[QROE] = quarterly_companies[NI_OWNER] / zero_to_nan(quarterly_companies.groupby(CODE)[
        EQUITY].rolling(2).mean().reset_index(0, drop=True))
    quarterly_companies[EBT_E] = quarterly_companies['ebt12'] / zero_to_nan(quarterly_companies.groupby(CODE)[EQUITY].rolling(
        4).mean().reset_index(0, drop=True))
    quarterly_companies[ROIC] = quarterly_companies.nopat12 / zero_to_nan(
            quarterly_companies[TANG_ASSET] + quarterly_companies[INV] + quarterly_companies[AR] - quarterly_companies[
        ALLOWANCE_AR_] - quarterly_companies[AP])

    quarterly_companies[GP_S] = quarterly_companies['gp12'] / zero_to_nan(quarterly_companies['sales12'])

    quarterly_companies[LIQ_RATIO] = quarterly_companies[CUR_ASSETS] / zero_to_nan(quarterly_companies[CUR_LIAB])
    quarterly_companies[DEBT_RATIO] = quarterly_companies[LIAB] / zero_to_nan(quarterly_companies[EQUITY])

    quarterly_companies[SALESQOQ] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[SALES] - x[SALES].shift(1)) / zero_to_nan(np.abs(x[SALES].shift(1)))).reset_index(drop=True)
    quarterly_companies[GPQOQ] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[GP] - x[GP].shift(1)) / zero_to_nan(np.abs(x[GP].shift(1)))).reset_index(drop=True)
    quarterly_companies[OPQOQ] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[EBIT] - x[EBIT].shift(1)) / zero_to_nan(np.abs(x[EBIT].shift(1)))).reset_index(drop=True)

    quarterly_companies[ROAQOQ] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[ROA] - x[ROA].shift(1)) / zero_to_nan(np.abs(x[ROA].shift(1)))).reset_index(drop=True)
    quarterly_companies[ROAYOY] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[ROA] - x[ROA].shift(4)) / zero_to_nan(np.abs(x[ROA].shift(4)))).reset_index(drop=True)
    quarterly_companies[GP_SYOY] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[GP_S] - x[GP_S].shift(4)) / zero_to_nan(np.abs(x[GP_S].shift(4)))).reset_index(drop=True)
    quarterly_companies[GP_AYOY] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[GP_A] - x[GP_A].shift(4)) / zero_to_nan(np.abs(x[GP_A].shift(4)))).reset_index(drop=True)

    quarterly_companies = quarterly_companies.groupby(CODE).ffill()

    # Merge daily data and quarterly data.
    available_companies = pd.merge(daily_companies, quarterly_companies, how='left', on=[CODE, FISCAL_QUARTER])
    available_companies[PER] = available_companies[MKTCAP] / zero_to_nan(available_companies.ni12) / 1000
    available_companies[PBR] = available_companies[MKTCAP] / zero_to_nan(available_companies[EQUITY]) / 1000
    available_companies[PCR] = available_companies[MKTCAP] / zero_to_nan(available_companies.cfo12) / 1000
    available_companies[PSR] = available_companies[MKTCAP] / zero_to_nan(available_companies.sales12) / 1000
    available_companies[PGPR] = available_companies[MKTCAP] / zero_to_nan(available_companies.gp12) / 1000
    available_companies[POPR] = available_companies[MKTCAP] / zero_to_nan(available_companies.op12) / 1000

    available_companies[EV] = available_companies[MKTCAP] + available_companies[FIN_LIAB] - available_companies[CASH]
    available_companies[EV_EBITDA] = available_companies[EV] / zero_to_nan(available_companies.ebitda12) / 1000
    available_companies[EBIT_EV] = available_companies.op12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(drop=True)
    available_companies[CF_EV] = available_companies.cfo12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(drop=True)
    available_companies[S_EV] = available_companies.sales12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(drop=True)

    available_companies[E_P] = 1 / zero_to_nan(available_companies[PER]).reset_index(drop=True)
    available_companies[B_P] = 1 / zero_to_nan(available_companies[PBR]).reset_index(drop=True)
    available_companies[C_P] = 1 / zero_to_nan(available_companies[PCR]).reset_index(drop=True)
    available_companies[S_P] = 1 / zero_to_nan(available_companies[PSR]).reset_index(drop=True)
    available_companies[GP_P] = 1 / zero_to_nan(available_companies[PGPR]).reset_index(drop=True)
    available_companies[OP_P] = 1 / zero_to_nan(available_companies[POPR]).reset_index(drop=True)

    available_companies[RET_1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJP].shift(-1) - x[ADJP]) / zero_to_nan(x[ADJP])).reset_index(drop=True)
    available_companies[MOM12_1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJP].shift(1) - x[ADJP].shift(12)) / zero_to_nan(x[ADJP].shift(12))).reset_index(drop=True)
    available_companies[MOM6] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJP] - x[ADJP].shift(6)) / zero_to_nan(x[ADJP].shift(6))).reset_index(drop=True)
    available_companies[MOM3] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJP] - x[ADJP].shift(3)) / zero_to_nan(x[ADJP].shift(3))).reset_index(drop=True)
    available_companies[MOM1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJP] - x[ADJP].shift(1)) / zero_to_nan(x[ADJP].shift(1))).reset_index(drop=True)

    # Select result columns
    processed_companies = copy(available_companies[COMPANY_RESULT_COLUMNS])

    # 2001년 5월 31일 이후 데이터만 남기기
    processed_companies = processed_companies.loc[processed_companies[DATE] >= '2001-05-31', :]

    return processed_companies


def process_benchmarks(unprocessed_benchmarks: DataFrame) -> DataFrame:
    """
    Calculate 1 month return of benchmarks.

    :param unprocessed_benchmarks: (DataFrame)
        code        | (String)
        date        | (Datetime)
        price_index | (float)

    :return processed_benchmarks: (DataFrame)
        code        | (String)
        date        | (Datetime)
        ret_1       | (float)
    """
    unprocessed_benchmarks[RET_1] = unprocessed_benchmarks.groupby(CODE).apply(
        lambda x: (x[PRICE_INDEX].shift(-1) - x[PRICE_INDEX]) / x[PRICE_INDEX]
    ).reset_index(level=0)[PRICE_INDEX]
    unprocessed_benchmarks = unprocessed_benchmarks[BENCHMARK_RESULT_COLUMNS]

    # 2001년 5월 31일 이후 데이터만 남기기
    processed_benchmarks = unprocessed_benchmarks.loc[unprocessed_benchmarks[DATE] >= '2001-05-31', :]

    return processed_benchmarks
