# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Chankyu Choi
:Date: 2018. 6. 19.
"""
import argparse

import pandas as pd
from tqdm import tqdm

from preprocess.core.data_filter import filter_companies
from preprocess.core.data_processor import process_companies, process_benchmarks, process_macro, process_factors
from preprocess.core.data_reader import read_companies, read_benchmarks, read_macro, read_factors

ENCODING = 'utf-8'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help="The format of date is YYMMDD(ex. 180131)")
    args = parser.parse_args()
    file_name = args.date

    with tqdm(total=100) as progress_bar:
        progress_bar.set_postfix_str("Reading {}.xlsx...".format(file_name))
        excel_file = pd.ExcelFile('data/{}.xlsx'.format(file_name))
        # progress_bar.update(30)

        # progress_bar.set_postfix_str("Processing companies...")
        unfiltered_companies = read_companies(excel_file)
        unprocessed_companies = filter_companies(unfiltered_companies)
        unprocessed_companies.to_csv('data/unprocessed_company.csv', index=False, encoding=ENCODING)
        processed_companies = process_companies(unfiltered_companies)
        processed_companies.to_csv('data/{}_company.csv'.format(file_name), index=False, encoding=ENCODING)
        progress_bar.update(50)

        # progress_bar.set_postfix_str("Processing etf data...")
        # unprocessed_etf = read_etf(csv_etf_file)
        # processed_etf = process_etf(unprocessed_companies)
        # processed_etf.to_csv('data/unprocessed_{}_etf.csv'.format(file_name), index=False, encoding=ENCODING)
        # progress_bar.update(20)

        progress_bar.set_postfix_str("Processing macro data...")
        unprocessed_macros = read_macro(excel_file)
        unprocessed_macros.to_csv('data/unprocessed_macro.csv', index=False, encoding=ENCODING)
        processed_macros = process_macro(unprocessed_macros)
        processed_macros.to_csv('data/{}_macro.csv'.format(file_name), index=False, encoding=ENCODING)
        progress_bar.update(10)

        progress_bar.set_postfix_str("Processing benchmarks...")
        unprocessed_benchmarks = read_benchmarks(excel_file)
        unprocessed_benchmarks.to_csv('data/unprocessed_benchmark.csv', index=False, encoding=ENCODING)
        processed_benchmarks = process_benchmarks(unprocessed_benchmarks)
        processed_benchmarks.to_csv('data/{}_benchmark.csv'.format(file_name), index=False, encoding=ENCODING)
        progress_bar.update(10)

        progress_bar.set_postfix_str("Processing factors...")
        unprocessed_factors = read_factors(excel_file)
        unprocessed_factors.to_csv('data/unprocessed_2010-after_factor.csv', index=False, encoding=ENCODING)
        processed_factors = process_factors(unprocessed_factors)
        processed_factors.to_csv('data/{}_factor.csv'.format(file_name), index=False, encoding=ENCODING)
        progress_bar.update(10)
