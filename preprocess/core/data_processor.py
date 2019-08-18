# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Chankyu Choi
:Date: 2018. 7. 6.
"""
from copy import copy
from datetime import datetime

import numpy as np
import pandas as pd
import talib as ta
from pandas import DataFrame
from pandas.tseries.offsets import MonthEnd

from preprocess.core.columns import *
from preprocess.core.utils import *

YEAR = 'year'
MONTH_DAY = 'month_day'

EV = 'ev'  # 시장가격
AVG_EQUITY = 'avg_equity'
AVG_ASSET = 'avg_asset'


def process_companies(unprocessed_companies: DataFrame) -> DataFrame:
    """
    :param unprocessed_companies: (DataFrame)
    :return processed_companies: (DataFrame)
    """
    # price and volume adjustment
    unprocessed_companies[ADJ_TRADING_VOLUME] = unprocessed_companies[TRADING_VOLUME] * unprocessed_companies[ADJ_C]
    unprocessed_companies[CONSENSUS_MEAN] = unprocessed_companies[CONSENSUS_MEAN] / unprocessed_companies[ADJ_C]
    unprocessed_companies[DIV_ADJ_C] = unprocessed_companies[ADJ_C] * unprocessed_companies[DIV_ADJ_C]
    unprocessed_companies[DIV_ADJ_C] = unprocessed_companies[::-1].groupby(CODE)[DIV_ADJ_C].apply(lambda x: x.cumprod())
    unprocessed_companies[DIV_ADJ_C] = unprocessed_companies[::-1].groupby(CODE)[DIV_ADJ_C].shift(1)
    unprocessed_companies[DIV_ADJ_C] = unprocessed_companies[DIV_ADJ_C].fillna(1)
    unprocessed_companies[ADJ_OPEN_P] = unprocessed_companies.groupby(CODE).apply(
        lambda x: x[OPEN_P] / x[DIV_ADJ_C]).reset_index(drop=True)
    unprocessed_companies[ADJ_HIGH_P] = unprocessed_companies.groupby(CODE).apply(
        lambda x: x[HIGH_P] / x[DIV_ADJ_C]).reset_index(drop=True)
    unprocessed_companies[ADJ_LOW_P] = unprocessed_companies.groupby(CODE).apply(
        lambda x: x[LOW_P] / x[DIV_ADJ_C]).reset_index(drop=True)
    unprocessed_companies[ADJ_CLOSE_P] = unprocessed_companies.groupby(CODE).apply(
        lambda x: x[CLOSE_P] / x[DIV_ADJ_C]).reset_index(drop=True)

    # market capital = price of common stocks * # of common stocks
    unprocessed_companies.loc[:, MKTCAP] = unprocessed_companies[CLOSE_P] * (
            unprocessed_companies[LISTED_SHARES] + unprocessed_companies[CS_TOBEPUB])

    # outstanding shares = # of common stocks - (# of largest shareholder's stocks + # of major shareholder's stocks)
    unprocessed_companies.loc[:, OS_SHARES] = unprocessed_companies[LISTED_SHARES] - (
            unprocessed_companies[LS_SHARES] + unprocessed_companies[OVER_10_QUARTILE_SHARES] + unprocessed_companies[
        OVER_20_QUARTILE_SHARES])

    # Calculate fiscal quarters of daily data.
    daily_companies = unprocessed_companies.loc[:, DAILY_DATA].reset_index(drop=True)
    daily_companies.loc[:, MONTH_DAY] = daily_companies[DATE].dt.month * 100 + daily_companies[DATE].dt.day
    daily_companies.loc[:, YEAR] = daily_companies[DATE].dt.year
    daily_companies.loc[:, FISCAL_QUARTER] = 0
    daily_companies.loc[(daily_companies[MONTH_DAY] >= 402) & (daily_companies[MONTH_DAY] < 515), FISCAL_QUARTER] = \
        daily_companies[YEAR] * 10 + 4
    daily_companies.loc[(daily_companies[MONTH_DAY] >= 515) & (daily_companies[MONTH_DAY] < 814), FISCAL_QUARTER] = \
        daily_companies[YEAR] * 10 + 1
    daily_companies.loc[(daily_companies[MONTH_DAY] >= 814) & (daily_companies[MONTH_DAY] < 1114), FISCAL_QUARTER] = \
        daily_companies[YEAR] * 10 + 2
    daily_companies.loc[(daily_companies[MONTH_DAY] < 402) | (daily_companies[MONTH_DAY] >= 1114), FISCAL_QUARTER] = \
        daily_companies[YEAR] * 10 + 3
    daily_companies.loc[(daily_companies[MONTH_DAY] < 515), FISCAL_QUARTER] += -10

    # Calculate fiscal quarters of quarterly data.
    quarterly_companies = unprocessed_companies.loc[
        unprocessed_companies.date.dt.month.isin([3, 6, 9, 12]), QUARTERLY_DATA].reset_index(drop=True)
    quarterly_companies[FISCAL_QUARTER] = quarterly_companies[DATE].dt.year * 10 + (
            quarterly_companies[DATE].dt.month / 3)
    quarterly_companies = quarterly_companies.drop(columns=[DATE])

    quarterly_companies['sales12'] = quarterly_companies.groupby(CODE)[SALES].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['gp12'] = quarterly_companies.groupby(CODE)[GP].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['op12'] = quarterly_companies.groupby(CODE)[EBIT].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['ni12'] = quarterly_companies.groupby(CODE)[NI_OWNER].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['cfo12'] = quarterly_companies.groupby(CODE)[CFO].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['ebitda12'] = quarterly_companies.groupby(CODE)[EBITDA].rolling(4).sum().reset_index(drop=True)
    quarterly_companies['ebt12'] = (
            quarterly_companies.groupby(CODE)[NI].rolling(4).sum() +
            quarterly_companies.groupby(CODE)[TAX].rolling(4).sum()
    ).reset_index(drop=True)

    quarterly_companies['noplat12'] = (
            quarterly_companies['op12'] - quarterly_companies.groupby(CODE)[TAX].rolling(4).sum().reset_index(drop=True)
    )

    quarterly_companies[AVG_ASSET] = quarterly_companies.groupby(CODE)[ASSETS].rolling(4).mean().reset_index(drop=True)
    quarterly_companies[AVG_EQUITY] = quarterly_companies.groupby(CODE)[EQUITY].rolling(4).mean().reset_index(drop=True)

    # Profit factors
    quarterly_companies[S_A] = quarterly_companies['sales12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[GP_A] = quarterly_companies['gp12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[OP_A] = quarterly_companies['op12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[CF_A] = quarterly_companies['cfo12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[ROA] = quarterly_companies['ni12'] / zero_to_nan(quarterly_companies[AVG_ASSET])
    quarterly_companies[ROE] = quarterly_companies['ni12'] / zero_to_nan(quarterly_companies[AVG_EQUITY])
    quarterly_companies[QROA] = quarterly_companies[NI_OWNER] / zero_to_nan(
        quarterly_companies.groupby(CODE)[ASSETS].rolling(2).mean()).reset_index(drop=True)
    quarterly_companies[QROE] = quarterly_companies[NI_OWNER] / zero_to_nan(
        quarterly_companies.groupby(CODE)[EQUITY].rolling(2).mean()).reset_index(drop=True)
    quarterly_companies[EBT_E] = quarterly_companies['ebt12'] / zero_to_nan(
        quarterly_companies.groupby(CODE)[EQUITY].rolling(4).mean()).reset_index(drop=True)
    quarterly_companies[ROIC] = quarterly_companies.noplat12 / zero_to_nan(
        quarterly_companies[TANG_ASSET] + quarterly_companies[INV] + quarterly_companies[AR] -
        quarterly_companies[ALLOWANCE_AR_] - quarterly_companies[AP]
    )
    quarterly_companies[DIVP] = quarterly_companies.groupby(CODE)[DIVP].rolling(4).sum().reset_index(drop=True)

    quarterly_companies[GP_S] = quarterly_companies['gp12'] / zero_to_nan(quarterly_companies['sales12'])

    # Growth factors
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
    quarterly_companies[ASSETSYOY] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[ASSETS] - x[ASSETS].shift(4)) / zero_to_nan(np.abs(x[ASSETS].shift(4)))).reset_index(drop=True)
    quarterly_companies[ASSETSQOQ] = quarterly_companies.groupby(CODE).apply(
        lambda x: (x[ASSETS] - x[ASSETS].shift(1)) / zero_to_nan(np.abs(x[ASSETS].shift(1)))).reset_index(drop=True)

    # Safety factors
    quarterly_companies[LIQ_RATIO] = quarterly_companies[CUR_ASSETS] / zero_to_nan(quarterly_companies[CUR_LIAB])
    quarterly_companies[DEBT_RATIO] = quarterly_companies[LIAB] / zero_to_nan(quarterly_companies[EQUITY])
    quarterly_companies[EQUITY_RATIO] = quarterly_companies[EQUITY] / zero_to_nan(quarterly_companies[ASSETS])

    quarterly_companies = quarterly_companies.groupby(CODE).ffill()

    # Merge daily data and quarterly data.
    available_companies = pd.merge(daily_companies, quarterly_companies, on=[CODE, FISCAL_QUARTER]).reset_index(
        drop=True)

    # Return
    available_companies[RET_D] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P].shift(-1) - x[ADJ_CLOSE_P]) / zero_to_nan(x[ADJ_CLOSE_P])).reset_index(drop=True)
    available_companies[RET_W] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P].shift(-5) - x[ADJ_CLOSE_P]) / zero_to_nan(x[ADJ_CLOSE_P])).reset_index(drop=True)
    available_companies[RET_M] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P].shift(-20) - x[ADJ_CLOSE_P]) / zero_to_nan(x[ADJ_CLOSE_P])).reset_index(drop=True)

    # Value factors
    available_companies[PER] = available_companies[MKTCAP] / zero_to_nan(available_companies.ni12) / 1000
    available_companies[PBR] = available_companies[MKTCAP] / zero_to_nan(available_companies[EQUITY]) / 1000
    available_companies[PCR] = available_companies[MKTCAP] / zero_to_nan(available_companies.cfo12) / 1000
    available_companies[PSR] = available_companies[MKTCAP] / zero_to_nan(available_companies.sales12) / 1000
    available_companies[PGPR] = available_companies[MKTCAP] / zero_to_nan(available_companies.gp12) / 1000
    available_companies[POPR] = available_companies[MKTCAP] / zero_to_nan(available_companies.op12) / 1000

    available_companies[EV] = available_companies[MKTCAP] + available_companies[FIN_LIAB] - available_companies[CASH]
    available_companies[EV_EBITDA] = available_companies[EV] / zero_to_nan(available_companies.ebitda12) / 1000
    available_companies[EBIT_EV] = available_companies.op12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(
        drop=True)
    available_companies[CF_EV] = available_companies.cfo12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(
        drop=True)
    available_companies[S_EV] = available_companies.sales12 * 1000 / zero_to_nan(available_companies[EV]).reset_index(
        drop=True)

    available_companies[E_P] = 1 / zero_to_nan(available_companies[PER]).reset_index(drop=True)
    available_companies[B_P] = 1 / zero_to_nan(available_companies[PBR]).reset_index(drop=True)
    available_companies[C_P] = 1 / zero_to_nan(available_companies[PCR]).reset_index(drop=True)
    available_companies[S_P] = 1 / zero_to_nan(available_companies[PSR]).reset_index(drop=True)
    available_companies[GP_P] = 1 / zero_to_nan(available_companies[PGPR]).reset_index(drop=True)
    available_companies[OP_P] = 1 / zero_to_nan(available_companies[POPR]).reset_index(drop=True)

    # Momentum factors
    available_companies[MOM12_1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P].shift(1) - x[ADJ_CLOSE_P].shift(12)) / zero_to_nan(
            x[ADJ_CLOSE_P].shift(12))).reset_index(
        drop=True)
    available_companies[MOM6_1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P].shift(1) - x[ADJ_CLOSE_P].shift(6)) / zero_to_nan(
            x[ADJ_CLOSE_P].shift(6))).reset_index(
        drop=True)
    available_companies[MOM12] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P] - x[ADJ_CLOSE_P].shift(12)) / zero_to_nan(x[ADJ_CLOSE_P].shift(12))).reset_index(
        drop=True)
    available_companies[MOM6] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P] - x[ADJ_CLOSE_P].shift(6)) / zero_to_nan(x[ADJ_CLOSE_P].shift(6))).reset_index(
        drop=True)
    available_companies[MOM3] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P] - x[ADJ_CLOSE_P].shift(3)) / zero_to_nan(x[ADJ_CLOSE_P].shift(3))).reset_index(
        drop=True)
    available_companies[MOM1] = available_companies.groupby(CODE).apply(
        lambda x: (x[ADJ_CLOSE_P] - x[ADJ_CLOSE_P].shift(1)) / zero_to_nan(x[ADJ_CLOSE_P].shift(1))).reset_index(
        drop=True)

    # Liquidity factors
    available_companies[TRADING_VOLUME_RATIO] = available_companies[TRADING_VOLUME] / available_companies[LISTED_SHARES]
    available_companies[NET_PERSONAL_PURCHASE_RATIO] = available_companies[NET_PERSONAL_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_INSTITUTIONAL_FOREIGN_PURCHASE_RATIO] = available_companies[
                                                                        NET_INSTITUTIONAL_FOREIGN_PURCHASE] / \
                                                                    available_companies[LISTED_SHARES]
    available_companies[NET_INSTITUTIONAL_PURCHASE_RATIO] = available_companies[NET_INSTITUTIONAL_PURCHASE] / \
                                                            available_companies[LISTED_SHARES]
    available_companies[NET_FINANCIAL_INVESTMENT_PURCHASE_RATIO] = available_companies[
                                                                       NET_FINANCIAL_INVESTMENT_PURCHASE] / \
                                                                   available_companies[LISTED_SHARES]
    available_companies[NET_INSURANCE_PURCHASE_RATIO] = available_companies[NET_INSURANCE_PURCHASE] / \
                                                        available_companies[LISTED_SHARES]
    available_companies[NET_TRUST_PURCHASE_RATIO] = available_companies[NET_TRUST_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_PRIVATE_FUND_PURCHASE_RATIO] = available_companies[NET_PRIVATE_FUND_PURCHASE] / \
                                                           available_companies[LISTED_SHARES]
    available_companies[NET_BANK_PURCHASE_RATIO] = available_companies[NET_BANK_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_ETC_FINANCE_PURCHASE_RATIO] = available_companies[NET_ETC_FINANCE_PURCHASE] / \
                                                          available_companies[LISTED_SHARES]
    available_companies[NET_PENSION_PURCHASE_RATIO] = available_companies[NET_PENSION_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_NATIONAL_PURCHASE_RATIO] = available_companies[NET_NATIONAL_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_ETC_CORPORATION_PURCHASE_RATIO] = available_companies[NET_ETC_CORPORATION_PURCHASE] / \
                                                              available_companies[LISTED_SHARES]
    available_companies[NET_FOREIGN_PURCHASE_RATIO] = available_companies[NET_FOREIGN_PURCHASE] / available_companies[
        LISTED_SHARES]
    available_companies[NET_REGISTERED_FOREIGN_PURCHASE_RATIO] = available_companies[NET_REGISTERED_FOREIGN_PURCHASE] / \
                                                                 available_companies[LISTED_SHARES]
    available_companies[NET_ETC_FOREIGN_PURCHASE_RATIO] = available_companies[NET_ETC_FOREIGN_PURCHASE] / \
                                                          available_companies[LISTED_SHARES]
    available_companies[FOREIGN_OWNERSHIP_RATIO] = available_companies[FOREIGN_OWNERSHIP_RATIO] / 100
    available_companies[SHORT_SALE_VOLUME_RATIO] = available_companies[SHORT_SALE_VOLUME] / available_companies[
        LISTED_SHARES]
    available_companies[SHORT_SALE_BALANCE_RATIO] = available_companies[SHORT_SALE_BALANCE] / available_companies[
        LISTED_SHARES]
    available_companies[SHORT_SALE_BALANCE_MOM] = available_companies.groupby(CODE).apply(
        lambda x: (x[SHORT_SALE_BALANCE_RATIO] - x[SHORT_SALE_BALANCE_RATIO].shift(1)) / zero_to_nan(
            np.abs(x[SHORT_SALE_BALANCE_RATIO].shift(1)))).reset_index(drop=True)
    available_companies[SHARE_LENDING_VOLUME_RATIO] = available_companies[SHARE_LENDING_VOLUME] / available_companies[
        LISTED_SHARES]
    available_companies[SHARE_LENDING_BALANCE_RATIO] = available_companies[SHARE_LENDING_BALANCE] / available_companies[
        LISTED_SHARES]
    available_companies[SHARE_LENDING_BALANCE_MOM] = available_companies.groupby(CODE).apply(
        lambda x: (x[SHARE_LENDING_BALANCE_RATIO] - x[SHARE_LENDING_BALANCE_RATIO].shift(1)) / zero_to_nan(
            np.abs(x[SHARE_LENDING_BALANCE_RATIO].shift(1)))).reset_index(drop=True)

    # Technical Indicator factors
    # MA
    available_companies[PRICE_MA20] = available_companies.groupby(CODE).apply(
        lambda x: ta.SMA(x[ADJ_CLOSE_P], 20)).reset_index(drop=True)
    available_companies[PRICE_MA60] = available_companies.groupby(CODE).apply(
        lambda x: ta.SMA(x[ADJ_CLOSE_P], 60)).reset_index(drop=True)
    available_companies[TRADING_VOLUME_MA20] = available_companies.groupby(CODE).apply(
        lambda x: ta.SMA(x[ADJ_TRADING_VOLUME], 20)).reset_index(drop=True)
    available_companies[TRADING_VOLUME_MA5] = available_companies.groupby(CODE).apply(
        lambda x: ta.SMA(x[ADJ_TRADING_VOLUME], 5)).reset_index(drop=True)
    # candle
    available_companies[DOJI_CANDLE] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLDOJI(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies[HAMMER_CANDLE] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLHAMMER(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies.set_index([CODE, DATE], inplace=True)
    available_companies[BIG_BULL_CANDLE] = (available_companies[ADJ_TRADING_VOLUME].shift(1) * 2 < available_companies[
        ADJ_TRADING_VOLUME]) & ((available_companies[ADJ_CLOSE_P] - available_companies[ADJ_OPEN_P]) /
                                available_companies[ADJ_OPEN_P] >= 0.1) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_CLOSE_P].shift(1)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_CLOSE_P].shift(2)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_CLOSE_P].shift(3)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_CLOSE_P].shift(4)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_CLOSE_P].shift(5)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_OPEN_P].shift(1)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_OPEN_P].shift(2)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_OPEN_P].shift(3)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_OPEN_P].shift(4)) & (
                                                   available_companies[ADJ_CLOSE_P] > available_companies[
                                               ADJ_OPEN_P].shift(5))
    available_companies[ACCUMULATION_CANDLE] = (available_companies[ADJ_TRADING_VOLUME].shift(1) * 2 <
                                                available_companies[ADJ_TRADING_VOLUME]) & (
                                                       (available_companies[ADJ_CLOSE_P] - available_companies[
                                                           ADJ_OPEN_P]) / available_companies[ADJ_OPEN_P] <= 0.08) & (
                                                       0 <= (available_companies[ADJ_CLOSE_P] - available_companies[
                                                   ADJ_OPEN_P]) / available_companies[ADJ_OPEN_P])
    available_companies.reset_index(inplace=True)
    available_companies[MORNING_STAR] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLMORNINGSTAR(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies[MORNING_DOJI_STAR] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLMORNINGDOJISTAR(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies[ABANDONED_BABY] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLABANDONEDBABY(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies[THREE_INSIDE_UP] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDL3INSIDE(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(drop=True)
    available_companies[THREE_OUTSIDE_UP] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDL3OUTSIDE(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[UPSIDE_GAP_TWO_CROWS] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLUPSIDEGAP2CROWS(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)

    # sub
    available_companies[BOLLINGER_UPPERBAND] = available_companies.groupby(CODE).apply(
        lambda x: ta.BBANDS(x[ADJ_CLOSE_P], timeperiod=12, nbdevup=2, nbdevdn=2)[0]).reset_index(drop=True)
    available_companies[BOLLINGER_MIDBAND] = available_companies.groupby(CODE).apply(
        lambda x: ta.BBANDS(x[ADJ_CLOSE_P], timeperiod=12, nbdevup=2, nbdevdn=2)[1]).reset_index(drop=True)
    available_companies[BOLLINGER_LOWERBAND] = available_companies.groupby(CODE).apply(
        lambda x: ta.BBANDS(x[ADJ_CLOSE_P], timeperiod=12, nbdevup=2, nbdevdn=2)[2]).reset_index(drop=True)
    available_companies[STOCHASTIC_SLOWK] = available_companies.groupby(CODE).apply(
        lambda x:
        ta.STOCH(x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P], fastk_period=10, slowk_period=5, slowd_period=5)[
            0]).reset_index(drop=True)
    available_companies[STOCHASTIC_SLOWD] = available_companies.groupby(CODE).apply(
        lambda x:
        ta.STOCH(x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P], fastk_period=10, slowk_period=5, slowd_period=5)[
            1]).reset_index(drop=True)
    available_companies[OBV] = available_companies.groupby(CODE).apply(
        lambda x: ta.OBV(x[ADJ_CLOSE_P], x[ADJ_TRADING_VOLUME])).reset_index(drop=True)
    available_companies[DISPARITY] = available_companies.groupby(CODE).apply(
        lambda x: disparity(x[ADJ_CLOSE_P], x[PRICE_MA20])).reset_index(drop=True)
    available_companies[TRIX] = available_companies.groupby(CODE).apply(
        lambda x: ta.TRIX(x[ADJ_CLOSE_P], 30)).reset_index(drop=True)

    # pattern
    available_companies[GAP_RISE] = available_companies.groupby(CODE).apply(
        lambda x: gap_rise(x[ADJ_CLOSE_P], x[ADJ_OPEN_P])).reset_index(drop=True)
    available_companies[GOLDEN_CROSS] = available_companies.groupby(CODE).apply(
        lambda x: golden_cross(x[PRICE_MA20], x[PRICE_MA60])).reset_index(drop=True)
    available_companies[EVENING_STAR] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLEVENINGSTAR(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[EVENING_DOJI_STAR] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLEVENINGDOJISTAR(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[ABANDONED_BABY] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLABANDONEDBABY(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[THREE_INSIDE_DOWN] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDL3INSIDE(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[THREE_OUTSIDE_DOWN] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDL3OUTSIDE(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[UPSIDE_GAP_TWO_CROWS] = available_companies.groupby(CODE).apply(
        lambda x: ta.CDLUPSIDEGAP2CROWS(x[ADJ_OPEN_P], x[ADJ_HIGH_P], x[ADJ_LOW_P], x[ADJ_CLOSE_P]) / 100).reset_index(
        drop=True)
    available_companies[RISE_DIVERGENCE] = available_companies.groupby(CODE).apply(
        lambda x: rise_divergence(x[MORNING_STAR], x[OBV])).reset_index(drop=True)
    available_companies[DOUBLE_BOTTOM] = available_companies.groupby(CODE).apply(
        lambda x: double_bottom(x[THREE_INSIDE_UP],30)).reset_index(drop=True)

    # True -> 1, False -> 0 으로 바꾸는 작업

    # Select result columns
    processed_companies = copy(available_companies[COMPANY_RESULT_COLUMNS])

    # Select rows which RET_1 is not nan before the last month.
    processed_companies.loc[
        (processed_companies[RET_M].isnull()) &
        (processed_companies[DATE] != sorted(processed_companies[DATE].unique())[-1]),
        IS_SUSPENDED
    ] = True

    # 2001년 5월 31일 이후 데이터만 남기기
    processed_companies = processed_companies.loc[processed_companies[DATE] >= '2001-05-31', :].reset_index(drop=True)

    return processed_companies


def process_benchmarks(unprocessed_benchmarks: DataFrame) -> DataFrame:
    """
    Calculate returns of benchmarks.

    :param unprocessed_benchmarks: (DataFrame)
        code        | (String)
        date        | (Datetime)
        price_index | (float)

    :return processed_benchmarks: (DataFrame)
        code                | (String)
        date                | (Datetime)
        benchmark_return_1  | (float)
        benchmark_return_3  | (float)
        benchmark_return_6  | (float)
        benchmark_return_12 | (float)
    """
    unprocessed_benchmarks = unprocessed_benchmarks.reset_index(drop=True)
    unprocessed_benchmarks[BENCHMARK_RET_1] = unprocessed_benchmarks.groupby(CODE).apply(
        lambda x: (x[PRICE_INDEX].shift(-1) - x[PRICE_INDEX]) / x[PRICE_INDEX]
    ).reset_index(level=0)[PRICE_INDEX]
    unprocessed_benchmarks[BENCHMARK_RET_3] = unprocessed_benchmarks.groupby(CODE).apply(
        lambda x: (x[PRICE_INDEX].shift(-3) - x[PRICE_INDEX]) / x[PRICE_INDEX]
    ).reset_index(level=0)[PRICE_INDEX]
    unprocessed_benchmarks[BENCHMARK_RET_6] = unprocessed_benchmarks.groupby(CODE).apply(
        lambda x: (x[PRICE_INDEX].shift(-6) - x[PRICE_INDEX]) / x[PRICE_INDEX]
    ).reset_index(level=0)[PRICE_INDEX]
    unprocessed_benchmarks[BENCHMARK_RET_12] = unprocessed_benchmarks.groupby(CODE).apply(
        lambda x: (x[PRICE_INDEX].shift(-12) - x[PRICE_INDEX]) / x[PRICE_INDEX]
    ).reset_index(level=0)[PRICE_INDEX]
    unprocessed_benchmarks = unprocessed_benchmarks[BENCHMARK_RESULT_COLUMNS].sort_values(by=[CODE, DATE])

    kospi_large = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSPI_LARGE,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]
    kospi_middle = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSPI_MIDDLE,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]
    kospi_small = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSPI_SMALL,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]
    kosdaq_large = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSDAQ_LARGE,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]
    kosdaq_middle = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSDAQ_MIDDLE,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]
    kosdaq_small = unprocessed_benchmarks.loc[
        unprocessed_benchmarks[CODE] == KOSDAQ_SMALL,
        [DATE, BENCHMARK_RET_1, BENCHMARK_RET_3, BENCHMARK_RET_6, BENCHMARK_RET_12]]

    total_large = _calculate_total(TOTAL_LARGE, kospi_large, kosdaq_large)
    total_middle = _calculate_total(TOTAL_MIDDLE, kospi_middle, kosdaq_middle)
    total_small = _calculate_total(TOTAL_SMALL, kospi_small, kosdaq_small)

    unprocessed_benchmarks = pd.concat([unprocessed_benchmarks, total_large, total_middle, total_small],
                                       ignore_index=True, sort=False)

    # 2001년 5월 31일 이후 데이터만 남기기
    processed_benchmarks = unprocessed_benchmarks.loc[unprocessed_benchmarks[DATE] >= '2001-05-31', :].reset_index(
        drop=True)

    return processed_benchmarks


def process_factors(transposed_factors: DataFrame) -> DataFrame:
    """
    Calculate SMB and HML.

    :param transposed_factors: (DataFrame)
        key
            date            | (Datetime)
        column
            BIG_HIGH        | (float) Size & Book Value(2X3) 대형 - High
            BIG_MEDIUM      | (float) Size & Book Value(2X3) 대형 - Medium
            BIG_LOW         | (float) Size & Book Value(2X3) 대형 - Low
            SMALL_HIGH      | (float) Size & Book Value(2X3) 소형 - High
            SMALL_MEDIUM    | (float) Size & Book Value(2X3) 소형 - Medium
            SMALL_LOW       | (float) Size & Book Value(2X3) 소형 - Low

    :return processed_factors: (DataFrame)
        code    | (String)
        date    | (Datetime)
        SMB     | (float)
        HML     | (float)
    """
    transposed_factors.loc[:, SMB] = \
        (transposed_factors.loc[:, SMALL_LOW] + transposed_factors.loc[:, SMALL_MEDIUM]
         + transposed_factors.loc[:, SMALL_HIGH] - transposed_factors.loc[:, BIG_LOW]
         - transposed_factors.loc[:, BIG_MEDIUM] - transposed_factors.loc[:, BIG_HIGH]) / 3
    transposed_factors.loc[:, HML] = \
        (transposed_factors.loc[:, SMALL_LOW] + transposed_factors.loc[:, BIG_LOW]
         - transposed_factors.loc[:, SMALL_HIGH] - transposed_factors.loc[:, BIG_HIGH]) / 2

    transposed_factors = transposed_factors.reset_index(drop=False)

    # 2001년 5월 31일 이후 데이터만 남기기
    processed_factors = transposed_factors.loc[transposed_factors[DATE] >= '2001-05-31', FACTOR_RESULT_COLUMNS] \
        .reset_index(drop=True)

    return processed_factors


def _calculate_total(code, kospi, kosdaq):
    kosdaq_suffix = '_kosdaq'
    kospi_suffix = '_kospi'

    total = pd.merge(left=kospi, right=kosdaq, on=[DATE], suffixes=(kospi_suffix, kosdaq_suffix))
    total[CODE] = code
    total[BENCHMARK_RET_1] = (total[BENCHMARK_RET_1 + kospi_suffix] + total[BENCHMARK_RET_1 + kosdaq_suffix]) / 2
    total[BENCHMARK_RET_3] = (total[BENCHMARK_RET_3 + kospi_suffix] + total[BENCHMARK_RET_3 + kosdaq_suffix]) / 2
    total[BENCHMARK_RET_6] = (total[BENCHMARK_RET_6 + kospi_suffix] + total[BENCHMARK_RET_6 + kosdaq_suffix]) / 2
    total[BENCHMARK_RET_12] = (total[BENCHMARK_RET_12 + kospi_suffix] + total[BENCHMARK_RET_12 + kosdaq_suffix]) / 2

    return total.loc[:, BENCHMARK_RESULT_COLUMNS]


def process_macro_daily(unprocessed_macros: DataFrame) -> DataFrame:
    # Data re-formatting
    raw_cols = unprocessed_macros.loc[:, "Symbol Name"] + "_" + unprocessed_macros.loc[:, "Item Name "]
    unprocessed_macros = unprocessed_macros.T.copy(deep=True)

    # get only data
    unprocessed_macros = unprocessed_macros[
        unprocessed_macros.reset_index()['index'].apply(lambda x: type(x) == datetime).values].copy(deep=True)
    unprocessed_macros.columns = raw_cols

    # make percent to non-percent
    unprocessed_macros = unprocessed_macros.apply(lambda x: x * 0.01 if "(%)" in x.name else x).copy(deep=True)

    # generating meaningful macro variables
    unprocessed_macros["*_*term_spread_kor"] = unprocessed_macros["ECO_시장금리:국고10년(%)"] - unprocessed_macros[
        "ECO_시장금리:국고1년(%)"]
    unprocessed_macros["*_*term_spread_us"] = unprocessed_macros["ECO_국채금리_미국국채(10년)(%)"] - unprocessed_macros[
        "ECO_국채금리_미국국채(1년)(%)"]
    unprocessed_macros["*_*credit_spread_kor"] = unprocessed_macros["ECO_시장금리:회사채(무보증3년BBB-)(%)"] - unprocessed_macros[
        "ECO_시장금리:회사채(무보증3년AA-)(%)"]
    unprocessed_macros["*_*log_usd2krw"] = unprocessed_macros["ECO_시장평균_미국(달러)(통화대원)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*log_chy2krw"] = unprocessed_macros["ECO_시장평균_중국(위안)(통화대원)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*log_euro2krw"] = unprocessed_macros["ECO_시장평균_EU(유로)(통화대원)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*ted_spread"] = unprocessed_macros["ECO_리보(미 달러) 1개월(%)"] - unprocessed_macros[
        "ECO_국채금리_미국국채(1개월)(%)"]
    unprocessed_macros["*_*log_nyse"] = unprocessed_macros["ECO_미국 NYSE Composite(종가)(Pt)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*log_nasdaq"] = unprocessed_macros["ECO_미국 Nasdaq Composite(종가)(Pt)"].apply(
        lambda x: np.log(x))
    unprocessed_macros["*_*log_semi_conductor"] = unprocessed_macros["ECO_NAND 8Gb 1Gx8 (MLC)(단기)($/개)"].apply(
        lambda x: np.log(x))
    unprocessed_macros["*_*log_dollar_index"] = unprocessed_macros["ECO_미국달러지수 (선물, NYBOT)(Pt)"].apply(
        lambda x: np.log(x))
    unprocessed_macros["*_*log_oil"] = unprocessed_macros["ECO_주요상품선물_WTI-1M($/bbl)"].apply(lambda x: np.log(x))

    # columns to use
    new_cols = [col for col in unprocessed_macros.columns if col[0:3] == '*_*']

    # get preprocessed macro
    processed_macros_from_daily = unprocessed_macros[new_cols]
    processed_macros_from_daily.columns = [col.replace("*_*", "") for col in processed_macros_from_daily.columns]

    # get only last observations of each month
    processed_macros_last_obs = processed_macros_from_daily.resample("M").last()
    processed_macros_last_obs.index.name = "date"

    # calculate volatility
    processed_macros_vol = processed_macros_from_daily.resample("M").apply(lambda x: np.std(x))
    processed_macros_vol.columns = [col + "_vol" for col in processed_macros_vol.columns]
    processed_macros_vol.index.name = "date"

    # merge monthly observations and volatility of each variable
    macros_from_daily = processed_macros_last_obs.merge(processed_macros_vol, how="left", left_index=True,
                                                        right_index=True)

    return macros_from_daily


def process_macro_monthly(unprocessed_macros: DataFrame) -> DataFrame:
    # Data re-formatting
    raw_cols = unprocessed_macros.loc[:, "Symbol Name"] + "_" + unprocessed_macros.loc[:, "Item Name "]
    unprocessed_macros = unprocessed_macros.T.copy(deep=True)

    # get only data
    unprocessed_macros = unprocessed_macros[
        unprocessed_macros.reset_index()['index'].apply(lambda x: type(x) == datetime).values].copy(deep=True)
    unprocessed_macros.columns = raw_cols

    # make percent to non-percent
    unprocessed_macros = unprocessed_macros.apply(lambda x: x * 0.01 if "(%)" in x.name else x).copy(deep=True)

    # generate meaningful variables
    unprocessed_macros["*_*log_export"] = unprocessed_macros["ECO_수출금액지수(총지수)(2010=100)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*log_import"] = unprocessed_macros["ECO_수입금액지수(총지수)(2010=100)"].apply(lambda x: np.log(x))
    unprocessed_macros["*_*log_industry_production_us"] = unprocessed_macros["ECO_미국(계절변동조정)(2010=100)"].apply(
        lambda x: np.log(x))
    unprocessed_macros["*_*log_industry_production_euro"] = unprocessed_macros["ECO_유로지역(계절변동조정 OECD)(2010=100)"].apply(
        lambda x: np.log(x))
    unprocessed_macros["*_*log_industry_production_kor"] = unprocessed_macros["ECO_산업생산지수(계절조정)(2010=100)"].apply(
        lambda x: np.log(x))

    new_cols = [col for col in unprocessed_macros.columns if col[0:3] == '*_*']

    # get only meaningful variables
    macros_from_monthly = unprocessed_macros[new_cols]
    macros_from_monthly.columns = [col.replace("*_*", "") for col in macros_from_monthly.columns]
    macros_from_monthly.index.name = "date"

    return macros_from_monthly


def merging_with_macros(processed_companies, processed_macro_from_daily,
                        processed_macro_from_monthly: DataFrame) -> DataFrame:
    macro = processed_macro_from_daily.merge(processed_macro_from_monthly, how="left", left_index=True,
                                             right_index=True)

    lagging_variables = [LOG_EXPORT, LOG_IMPORT, LOG_INDUSTRY_PRODUCTION_US, LOG_INDUSTRY_PRODUCTION_EURO,
                         LOG_INDUSTRY_PRODUCTION_KOR]

    contemporaneous_variables = list(set(list(macro.columns)) - set(lagging_variables))

    macro_contemporaneous = macro[contemporaneous_variables].copy(deep=True)
    macro_lagging = macro[lagging_variables].copy(deep=True)

    processed_companies = processed_companies.merge(macro_contemporaneous, how='left', left_on="date", right_index=True)

    macro_lagging['mdate_lag'] = macro_lagging.index + MonthEnd(-1)
    macro_lagging = macro_lagging.reset_index().set_index('mdate_lag').copy(deep=True)
    macro_lagging = macro_lagging.drop(columns='date').copy(deep=True)

    # Lagging
    merged_companies = processed_companies.merge(macro_lagging, how='left', left_on="date", right_index=True)

    return merged_companies
