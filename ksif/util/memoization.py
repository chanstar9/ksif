# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 7. 18.
"""
import functools
from copy import deepcopy as do_copy


def memoize(copy=False):
    def deco_memoize(func):
        cache = func.cache = {}

        @functools.wraps(func)
        def memoized_func(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            if copy:
                return do_copy(cache[key])
            return cache[key]

        return memoized_func

    return deco_memoize
