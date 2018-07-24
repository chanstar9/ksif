# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 7. 18.
"""
from io import StringIO

import pandas as pd
import requests

from ..errors import GoogleQueryException

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

    if response.status_code != 200:
        raise GoogleQueryException(response.status_code)

    spreadsheet = pd.read_csv(StringIO(response.content.decode(encoding='UTF-8', errors='strict')))

    return spreadsheet
