# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 6.
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'ksif',
    version          = '2019.1.17',
    description      = 'Quantitative investment tools for KSIF',
    long_description = long_description,
    author           = 'KSIF Tech',
    author_email     = 'jaekyoungkim@kaist.ac.kr',
    url              = 'https://github.com/willbelucky/ksif',
    download_url     = 'https://github.com/willbelucky/ksif/archive/master.zip',
    install_requires = [
        'pandas',
        'numpy',
        'matplotlib',
        'tqdm',
        'requests',
        'tables',
        'python-dateutil',
        'urllib3',
        'xlrd'
    ],
    packages         = find_packages(exclude = ['tests*']),
    keywords         = ['ksif', 'portfolio', 'backtest', 'finance'],
    python_requires  = '>=3.5,!=3.7.*',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
