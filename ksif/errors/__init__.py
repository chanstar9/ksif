# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 6.
"""


class GoogleQueryException(Exception):
    message = 'Google querying is not working. The status code is {}.'

    def __init__(self, status_code: int):
        self._status_code = status_code

    def __str__(self):
        return self.message.format(self._status_code)
