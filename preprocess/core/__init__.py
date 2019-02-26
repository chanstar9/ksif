# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 19.
"""
import argparse

from preprocess.core.data_filter import filter_companies
from preprocess.core.data_processor import process_companies, process_benchmarks, process_macro_daily, \
    process_macro_monthly, merging_with_macros
from preprocess.core.data_reader import read_companies, read_benchmarks, read_macro_daily, read_macro_monthly

ENCODING = 'utf-8'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help="The format of date is YYMMDD(ex. 180131)")
    args = parser.parse_args()
    file_name = args.date

    print("Start companies...")
    companies = read_companies(file_name)
    filtered_companies = filter_companies(companies)
    processed_companies = process_companies(filtered_companies)
    print("Finish companies")

    print("Start benchmarks...")
    benchmarks = read_benchmarks(file_name)
    processed_benchmarks = process_benchmarks(benchmarks)
    processed_benchmarks.to_csv('data/{}_benchmark.csv'.format(file_name), index=False, encoding=ENCODING)
    print("Finish benchmarks")

    print("Start macro...")
    macro_daily = read_macro_daily(file_name)
    macro_monthly = read_macro_monthly(file_name)
    processed_macro_daily = process_macro_daily(macro_daily)
    processed_macro_monthly = process_macro_monthly(macro_monthly)
    processed_companies_with_macros = merging_with_macros(processed_companies, processed_macro_daily,
                                                          processed_macro_monthly)
    print("Finish macro")

    processed_companies_with_macros.to_csv('data/{}_company.csv'.format(file_name), index=False, encoding=ENCODING)
