# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 19.
"""
import argparse

from data_reader import read_companies, read_benchmarks
from data_filter import filter_companies
from data_processor import process_companies, process_benchmarks

ENCODING = 'utf-8'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help="The format of date is YYMMDD(ex. 180131)")
    args = parser.parse_args()
    file_name = args.date

    companies = read_companies(file_name)
    filtered_companies = filter_companies(companies)
    processed_companies = process_companies(filtered_companies)
    processed_companies.to_csv('{}_company.csv'.format(file_name), index=False, encoding=ENCODING)

    benchmarks = read_benchmarks(file_name)
    processed_benchmarks = process_benchmarks(benchmarks)
    processed_benchmarks.to_csv('{}_benchmark.csv'.format(file_name), index=False, encoding=ENCODING)
