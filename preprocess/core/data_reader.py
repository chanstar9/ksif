# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 19.
"""
import pandas as pd
import numpy as np

from preprocess.core.columns import *

KIND = 'Kind'
SYMBOL = 'Symbol'
NAME = 'name'
ITEM_NAME = 'Item Name '
ITEM = 'Item'
FREQUENCY = 'Frequency'

SYMBOL_NAME = 'Symbol Name'

DIR = 'data/{}.xlsx'
COMPANY_UNNECESSARY_COLUMNS = [KIND, NAME, ITEM_NAME, ITEM, FREQUENCY]
BENCHMARK_UNNECESSARY_COLUMNS = [SYMBOL, KIND, ITEM, ITEM_NAME, FREQUENCY]


# noinspection PyShadowingNames
def read_companies(file_name: str) -> pd.DataFrame:
    """
    :param file_name: (String) A file name of the raw data Excel file, except '.xlsx'.

    :return melted_companies: (DataFrame)
         code   | (String)
         date   | (Datetime)
         name   | (String)
         ...
    """
    # Read excel file.
    raw_companies = pd.read_excel(DIR.format(file_name), sheet_name=COMPANY, skiprows=8)

    # Rename Symbol -> code, Symbol Name -> name
    raw_companies = raw_companies.rename(columns={
        'Symbol': CODE,
        'Symbol Name': NAME,
    })

    # Save symbol names and item names.
    names = raw_companies.drop_duplicates(subset=CODE, keep='last').loc[:, [CODE, NAME]]
    names = names.set_index(CODE)
    item_name_num = len(raw_companies.loc[:1000, ITEM_NAME].unique())
    item_names = raw_companies.loc[:item_name_num - 1, ITEM_NAME]

    # Remove unnecessary columns, for example, Symbol, Kind, Item, Item Name, Frequency
    raw_companies = raw_companies.drop(columns=COMPANY_UNNECESSARY_COLUMNS)

    # Melt every items.
    melted_companies = pd.DataFrame(columns=[CODE, DATE])
    melted_companies = melted_companies.set_index([CODE, DATE])
    for index, item_name in enumerate(item_names):
        # Melt raw_benchmark. Symbole name -> code, column names -> date
        item_companies = pd.melt(raw_companies.iloc[index::item_name_num, :], id_vars=[CODE], var_name=DATE,
                                 value_name=item_name)
        item_companies[DATE] = pd.to_datetime(item_companies[DATE], format='%Y-$m-%D')
        item_companies = item_companies.set_index([CODE, DATE])
        melted_companies = melted_companies.join(item_companies, how='outer')

    melted_companies = melted_companies.rename(columns=RENAMES)

    # Add the names of company.
    melted_companies = melted_companies.join(names)

    melted_companies = melted_companies.reset_index()
    melted_companies = melted_companies.sort_values([CODE, DATE])

    # IS_MANAGED, IS_SUSPENDED: '정지' -> True, na -> False
    melted_companies[IS_MANAGED] = melted_companies[IS_MANAGED].replace('관리', True)
    melted_companies[IS_MANAGED] = melted_companies[IS_MANAGED].fillna(False)
    melted_companies[IS_SUSPENDED] = melted_companies[IS_SUSPENDED].replace('정지', True)
    melted_companies[IS_SUSPENDED] = melted_companies[IS_SUSPENDED].fillna(False)

    # 0 -> nan
    to_nan_columns = [NI_OWNER, NI, INT_INC, INT_EXP, CFO, EBIT, EBITDA]
    melted_companies.loc[:, to_nan_columns] = \
        melted_companies.loc[:, to_nan_columns].replace(0, np.nan)

    # nan -> 0
    to_zero_columns = [
        CFO, ALLOWANCE_AR_, TRADING_VOLUME, RES_EXP, AR, DIVP, AP,
        NET_PERSONAL_PURCHASE, NET_NATIONAL_PURCHASE, NET_FINANCIAL_INVESTMENT_PURCHASE,
        NET_INSTITUTIONAL_FOREIGN_PURCHASE, NET_INSTITUTIONAL_PURCHASE, NET_ETC_FINANCE_PURCHASE,
        NET_ETC_CORPORATION_PURCHASE, NET_ETC_FOREIGN_PURCHASE, NET_REGISTERED_FOREIGN_PURCHASE,
        NET_INSURANCE_PURCHASE, NET_PRIVATE_FUND_PURCHASE, NET_PENSION_PURCHASE, NET_FOREIGN_PURCHASE,
        NET_BANK_PURCHASE, NET_TRUST_PURCHASE, SHORT_SALE_VOLUME, SHORT_SALE_BALANCE, FOREIGN_OWNERSHIP_RATIO
    ]
    melted_companies.loc[:, to_zero_columns] = \
        melted_companies.loc[:, to_zero_columns].replace(np.nan, 0)

    melted_companies = melted_companies.sort_values([CODE, DATE])

    return melted_companies


# noinspection PyShadowingNames
def read_benchmarks(file_name: str) -> pd.DataFrame:
    """
    :param file_name: (String) A file name of the raw data Excel file, except '.xlsx'.

    :return melted_benchmarks: (DataFrame)
        code        | (String)
        date        | (Datetime)
        price_index | (float)
    """
    # Read excel file.
    raw_benchmarks = pd.read_excel(DIR.format(file_name), sheet_name=BENCHMARK, skiprows=8)

    # Remove unnecessary columns, for example, Symbol, Kind, Item, Item Name, Frequency
    raw_benchmarks = raw_benchmarks.drop(columns=BENCHMARK_UNNECESSARY_COLUMNS)

    # Melt benchmarks. Symbole name -> code, column names -> date
    melted_benchmarks = pd.melt(raw_benchmarks, id_vars=[SYMBOL_NAME], var_name=DATE, value_name=PRICE_INDEX)
    melted_benchmarks[DATE] = pd.to_datetime(melted_benchmarks[DATE], format='%Y-$m-%D')
    melted_benchmarks = melted_benchmarks.rename(columns={SYMBOL_NAME: CODE})

    melted_benchmarks = melted_benchmarks.dropna()

    # Sort by code and date
    melted_benchmarks = melted_benchmarks.sort_values([CODE, DATE])

    return melted_benchmarks
