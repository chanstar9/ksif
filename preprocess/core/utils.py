# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 22.
"""
from io import StringIO

import pandas as pd
import numpy as np
import requests
import datetime
from pandas import Series

CSV_DOWNLOAD_REQUEST_URL = 'https://docs.google.com/spreadsheet/ccc?key={}&output=csv'
GID_URL = '&gid={}'


def query_google_spreadsheet(key: str, gid=None) -> pd.DataFrame:
    """
    :param key: (str)
    :param gid: (str or None)

    :return spreadsheet: (DataFrame)
    """
    if not isinstance(key, str):
        raise TypeError("Parameter key should be a string.")
    if gid is not None and not isinstance(gid, str):
        raise TypeError("Parameter gid should be a None or a string.")

    csv_download_request_url = CSV_DOWNLOAD_REQUEST_URL.format(key)
    if gid is not None:
        csv_download_request_url += GID_URL.format(gid)
    response = requests.get(csv_download_request_url)

    assert response.status_code == 200, 'Wrong status code'

    spreadsheet = pd.read_csv(StringIO(response.content.decode(encoding='UTF-8', errors='strict')))

    return spreadsheet


def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


def zero_to_nan(series: Series) -> Series:
    return series.apply(lambda x: np.where(x == 0, np.nan, x))
