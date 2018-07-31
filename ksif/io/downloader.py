# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 7. 18.
"""
import os
from pandas import DataFrame
from pandas import read_csv, read_hdf
from pathlib import Path

from ..core.columns import DATE
from .google_drive import query_google_spreadsheet, GoogleQueryException
from ..util.memoization import memoize
from ..util.retrial import retry

TABLE = 'table'

COMPANY_URL = 'company_url'
BENCHMARK_URL = 'benchmark_url'

# CSV encoding type
ENCODING = 'utf-8'

DATA_DIR = 'data'

KOREA_STOCK_DATA_KEY = '1aew3NOvEOG9hLB5ajA4tkRk7acTWIJrslNS2EPvxtok'


@memoize(copy=True)
@retry(GoogleQueryException)
def download_latest_korea_data() -> (DataFrame, DataFrame):
    korea_stock_data_urls = query_google_spreadsheet(KOREA_STOCK_DATA_KEY)
    korea_stock_data_urls = korea_stock_data_urls.sort_values(by=DATE)
    latest_company_url = korea_stock_data_urls.iloc[-1][COMPANY_URL]
    latest_company_file_name = latest_company_url[42:56]
    latest_benchmark_url = korea_stock_data_urls.iloc[-1][BENCHMARK_URL]
    latest_benchmark_file_name = latest_benchmark_url[42:58]

    if not Path(DATA_DIR).exists():
        os.makedirs(DATA_DIR)

    latest_company_data = _download_data(latest_company_file_name, latest_company_url)
    latest_benchmark_data = _download_data(latest_benchmark_file_name, latest_benchmark_url)

    return latest_company_data, latest_benchmark_data


def _download_data(file_name, url):
    local_company_file_path = '{}/{}.h5'.format(DATA_DIR, file_name)
    if Path(local_company_file_path).exists():
        latest_company_data = custom_read_hdf(local_company_file_path)
    else:
        latest_company_data = custom_read_csv(url)
        latest_company_data.to_hdf(local_company_file_path, TABLE, mode='w')
    return latest_company_data


def custom_read_csv(path):
    latest_korea_data = read_csv(path, sep='|', low_memory=False, encoding=ENCODING, parse_dates=[DATE])
    return latest_korea_data


def custom_read_hdf(path):
    latest_korea_data = read_hdf(path, TABLE)
    return latest_korea_data
