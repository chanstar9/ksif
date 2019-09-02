# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         ChanKyu Choi
:Date: 2018. 6. 6.
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='ksif',
    version='2019.3.18',
    description='Quantitative investment tools for KSIF',
    long_description=long_description,
    author='KSIF Tech',
    author_email='traintion9@kaist.ac.kr',
    url='https://github.com/chanstar9/ksif',
    download_url='https://github.com/chanstar9/ksif/archive/master.zip',
    install_requires=[
        'h5py==2.8.0',
        'pandas==0.24.2',
        'numpy==1.15.4',
        'matplotlib',
        'scikit-learn',
        'scipy==1.2.0',
        'statsmodels',
        'patsy',
        'performanceanalytics',
        'pymysql',
        'tqdm',
        'requests',
        'tables==3.4.4',
        'python-dateutil',
        'urllib3',
        'xlrd'
    ],
    packages=find_packages(exclude=['tests*']),
    keywords=['ksif', 'portfolio', 'backtest', 'finance'],
    python_requires='>=3.5',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
