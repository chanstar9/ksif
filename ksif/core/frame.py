# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Park Ji woo
:Date: 2018. 7. 18
"""
import sys
from copy import deepcopy as dc
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform
import numpy as np
import pandas as pd
import pandas.core.common as com
from pandas import DataFrame
from pandas import Series
from pandas.core.index import (Index, MultiIndex)
from pandas.core.indexing import convert_to_index_sliceable
from performanceanalytics.charts.performance_summary import create_performance_summary

from .columns import *
from .outcomes import *
from ..io.downloader import download_latest_data
from ..util.checker import not_empty

# Hangul font setting
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
else:
    rc('font', family='AppleGothic')

# Minus sign
matplotlib.rcParams['axes.unicode_minus'] = False

PERCENTAGE = 'percentage'

START_DATE = '2001-05-31'

QUANTILE = 'quantile'
RANK = 'rank'
RANK_CORRELATION = 'Rank correlation'


class Portfolio(DataFrame):
    """

    """
    _benchmark = KOSPI
    benchmarks = None

    @property
    def _constructor(self):
        return Portfolio

    @not_empty
    def __init__(self, data=None, index=None, columns=None, dtype=None, copy: bool = False,
                 start_date: str = START_DATE, end_date: str = None,
                 include_holding: bool = False, include_finance: bool = False,
                 include_managed: bool = False, include_suspended: bool = False):

        try:
            datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, start_date should be YYYY-MM-DD")

        if not end_date:
            end_date = datetime.today().strftime('%Y-%m-%d')

        try:
            datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, end_date should be YYYY-MM-DD")

        if data is None:
            data, self.benchmarks = download_latest_data()

            if not include_holding:
                data = data.loc[~data[HOLDING], :]

            if not include_finance:
                data = data.loc[data[FN_GUIDE_SECTOR] != '금융', :]

            if not include_managed:
                data = data.loc[~data[IS_MANAGED], :]

            if not include_suspended:
                data = data.loc[~data[IS_SUSPENDED], :]

            data = data.loc[(start_date <= data[DATE]) & (data[DATE] <= end_date), :]
        else:
            _, self.benchmarks = download_latest_data()

        DataFrame.__init__(self=self, data=data, index=index, columns=columns, dtype=dtype, copy=copy)

    def __getitem__(self, key):
        # noinspection PyProtectedMember
        key = com._apply_if_callable(key, self)

        # shortcut if we are an actual column
        is_mi_columns = isinstance(self.columns, MultiIndex)
        # noinspection PyBroadException
        try:
            if key in self.columns and not is_mi_columns:
                self._getitem_column(key)
        except:
            pass

        # see if we can slice the rows
        indexer = convert_to_index_sliceable(self, key)
        if indexer is not None:
            return self._getitem_slice(indexer)

        if isinstance(key, (Series, np.ndarray, Index, list)):
            # either boolean or fancy integer index
            return self._getitem_array(key)
        elif isinstance(key, DataFrame):
            return self._getitem_frame(key)
        elif is_mi_columns:
            return self._getitem_multilevel(key)
        else:
            return self._getitem_column(key)

    @property
    def benchmark(self):
        return self._benchmark

    @not_empty
    def get_benchmark(self, benchmark: str = None) -> DataFrame:
        """
        Return a benchmark of this portfolio period.

        :param benchmark: (str) The name of benchmark to use. If benchmark is None, use self.benchmark.

        :return selected_benchmark: (DataFrame)
            code                | (str) The name of benchmark. ex) 코스피, 코스닥...
            date                | (datetime)
            benchmark_return_1  | (float) 1 month return.
            benchmark_return_3  | (float) 3 month return.
            benchmark_return_6  | (float) 6 month return.
            benchmark_return_12 | (float) 12 month return.
        """
        if benchmark is not None and benchmark not in BENCHMARKS:
            raise ValueError('{} is not registered.'.format(benchmark))

        if benchmark:
            selected_benchmark = self.benchmarks.loc[(self.benchmarks[CODE] == benchmark) &
                                                     (self.benchmarks[DATE] >= min(self[DATE])) &
                                                     (self.benchmarks[DATE] <= max(self[DATE])), :]
        else:
            selected_benchmark = self.benchmarks.loc[(self.benchmarks[CODE] == self._benchmark) &
                                                     (self.benchmarks[DATE] >= min(self[DATE])) &
                                                     (self.benchmarks[DATE] <= max(self[DATE])), :]

        return selected_benchmark

    def set_benchmark(self, benchmark):
        if benchmark not in BENCHMARKS:
            raise ValueError('{} is not registered.'.format(benchmark))
        else:
            self._benchmark = benchmark

    @not_empty
    def to_dataframe(self, deepcopy: bool = True) -> DataFrame:
        """
        Convert portfolio to dataframe type.

        :param deepcopy : (bool) If deepcopy is True, convert to dataframe based on deepcopy. Or, convert to dataframe
                                  based on shallow copy.

        :return dataframe : (DataFrame) Converted dataframe type portfolio
        """
        if deepcopy:
            dataframe = DataFrame(dc(self))
        else:
            dataframe = DataFrame(self)

        return dataframe

    def outcome(self, benchmark: str = None, weighted: bool = False, show_plot: bool = False):
        """
        Calculate various indices of the portfolio.

        :param benchmark: (str) The name of benchmark. If benchmark is None, use a default benchmark.
        :param weighted: (bool) If weighted is True, use market capitalization to calculate weighted portfolio.
        :param show_plot: (bool) If show_plot is True, show a performance summary graph.

        :return result: (dict)
            portfolio_return            | (float) Total compound return of the portfolio.
            benchmark_return            | (float) Total compound return of the benchmark.
            active_return               | (float) Annualized average excess return.
            active_risk                 | (float) Annualized tracking error.
            information_ratio           | (float) Average excess return / tracking error
            compound_annual_growth_rate | (float) Annual compound return of the portfolio.
        """
        portfolio = dc(self)

        if benchmark is not None:
            if benchmark not in BENCHMARKS:
                raise ValueError('{} is not registered.'.format(benchmark))

        portfolio_returns = pd.DataFrame()
        if weighted:
            portfolio_returns[PORTFOLIO_RETURN] = portfolio.dropna(subset=[RET_1]).groupby([DATE]).apply(
                lambda x: np.average(x[RET_1], weights=x[MKTCAP])
            )
        else:
            portfolio_returns[PORTFOLIO_RETURN] = portfolio.dropna(subset=[RET_1]).groupby([DATE]).apply(
                lambda x: np.average(x[RET_1])
            )

        portfolio_returns = portfolio_returns.reset_index()
        merged_returns = pd.merge(portfolio_returns, portfolio.get_benchmark()[
            [DATE, BENCHMARK_RET_1]
        ], on=DATE)

        portfolio_return = self._calculate_total_return(merged_returns[PORTFOLIO_RETURN])

        benchmark_return = self._calculate_total_return(merged_returns[BENCHMARK_RET_1])

        period_len = len(portfolio[DATE].unique())
        compound_annual_growth_rate = (portfolio_return + 1) ** (12 / period_len) - 1
        benchmark_excess_returns = merged_returns[PORTFOLIO_RETURN] - merged_returns[BENCHMARK_RET_1]

        average_excess_return = np.average(benchmark_excess_returns)
        tracking_error = np.std(benchmark_excess_returns)

        active_return = average_excess_return * 12
        active_risk = tracking_error * np.sqrt(12)
        information_ratio = average_excess_return / tracking_error

        result = {
            PORTFOLIO_RETURN: portfolio_return,
            BENCHMARK_RETURN: benchmark_return,
            ACTIVE_RETURN: active_return,
            ACTIVE_RISK: active_risk,
            IR: information_ratio,
            CAGR: compound_annual_growth_rate,
        }

        if show_plot:
            merged_returns[DATE] = pd.to_datetime(merged_returns[DATE])
            merged_returns.set_index(keys=[DATE], inplace=True)
            create_performance_summary(merged_returns, other_cols=range(1, 2))
            plt.show()

        return result

    @not_empty
    def _calculate_total_return(self, grouped_data):
        data = grouped_data.dropna()
        total_return = self._cumulate(data).iloc[-1]
        return total_return

    @not_empty
    def periodic_rank(self, min_rank: int = 1, max_rank: int = sys.maxsize, factor: str = MKTCAP,
                      bottom: bool = False, drop_rank: bool = True):
        """
        Select companies which have a rank bigger than or equal to min_rank, and smaller than or equal to max_rank
        for each period.

        :param min_rank: (int) The minimum rank of selected companies.
                               The selected_companies includes the minimum ranked company.
        :param max_rank: (int) The maximum rank of selected companies.
                               The selected_companies includes the maximum ranked company.
        :param factor: (str) The factor used to determine rank.
        :param bottom: (bool) If bottom is True, select the companies from bottom. Or, select the companies from top.
        :param drop_rank: (bool) If drop_rank is True, delete rank column from the selected_companies.

        :return selected_companies: (DataFrame) Selected companies for each period by rank of the factor.
        """
        assert min_rank > 0, "min_rank should be bigger than 0."
        assert max_rank > min_rank, "max_rank should be bigger than min_rank."

        all_companies = dc(self)
        all_companies = all_companies.dropna(subset=[factor])
        all_companies[RANK] = all_companies.groupby(by=[DATE])[factor].transform(
            lambda x: x.rank(ascending=bottom)
        )
        selected_companies = all_companies.loc[(all_companies[RANK] >= min_rank) & (all_companies[RANK] <= max_rank), :]
        selected_companies = selected_companies.sort_values(by=[DATE, RANK])

        if drop_rank:
            del selected_companies[RANK]

        return selected_companies

    @not_empty
    def periodic_percentage(self, min_percentage: float, max_percentage: float, factor: str = MKTCAP,
                            bottom: bool = False):
        """
        Select companies which have a percentage bigger than or equal to min_percentage, and smaller than or equal to
        max_percentage for each period.

        :param min_percentage: (float) The minimum percentage of selected companies.
                               The selected_companies includes the minimum percent company.
        :param max_percentage: (float) The maximum percentage of selected companies.
                               The selected_companies does not include the maximum percent company.
        :param factor: (str) The factor used to determine rank.
        :param bottom: (bool) If bottom is True, select the companies from bottom. Or, select the companies from top.

        :return selected_companies: (DataFrame) Selected companies for each period by quantile of the factor.
        """
        assert min_percentage >= 0, "min_percentage should be bigger than or equal to 0."
        assert max_percentage > min_percentage, "max_percentage should be bigger than min_percentage."
        assert max_percentage <= 1, "max_percentage should be smaller than or equal to 0."

        all_companies = dc(self)
        all_companies = all_companies.dropna(subset=[factor])
        all_companies[PERCENTAGE] = all_companies.groupby(by=[DATE])[factor].transform(
            lambda x: x.rank(ascending=bottom, pct=True)
        )
        selected_companies = all_companies.loc[
                             (all_companies[PERCENTAGE] >= min_percentage) &
                             (all_companies[PERCENTAGE] < max_percentage), :]

        del selected_companies[PERCENTAGE]

        return selected_companies

    @not_empty
    def periodic_standardize(self, factor: str, prefix: str = 'std_'):
        """
        Standardize a factor periodically.

        :param factor: (str) The name of factor will be standardized.
        :param prefix: (str) The prefix preceding a name of standardized factor.

        :return standardized_companies: (DataFrame) Standardized companies for each period by factor.
        """
        unstandardized_companies = dc(self.loc[~np.isnan(self[factor]), :])
        unstandardized_companies[prefix + factor] = unstandardized_companies.groupby(by=[DATE])[factor].transform(
            lambda x: (x - x.mean()) / x.std()
        )
        standardized_companies = unstandardized_companies

        return standardized_companies

    @not_empty
    def quantile_distribution_ratio(self, factor: str, chunk_num: int = 10, cumulative: bool = True,
                                    weighted: bool = False, only_positive: bool = False, show_plot: bool = False,
                                    show_bar_chart: bool = False, title: str = None) -> DataFrame:
        """
        Make quantile portfolios by the given factor, and calculate returns.

        :param factor: (str) The name of factor used to make quantile portfolios.
        :param chunk_num: (int) The number of portfolios.
        :param cumulative: (bool) If cumulative is true, calculate cumulative returns.
        :param weighted: (bool) If weighted is true, each portfolio is a weighted portfolio based on MKTCAP
        :param only_positive: (bool) If only_positive is true, use only positive value of the factor.
        :param show_plot: (bool) If show_plot is true, show a time series line chart of groups.
        :param show_bar_chart: (bool) If show_bar_chart is true, show a arithmetic average bar chart of groups.
        :param title: (str) If title is not None, set the title.

        :return quantile_portfolio_returns: (DataFrame) The returns of each group
            --------------------------------------------------------------
            date    | (datetime)
            --------------------------------------------------------------
            1       | (float) The return of group 1 portfolio at the date.
            2       | (float) The return of group 2 portfolio at the date.
            3       | (float) The return of group 3 portfolio at the date.
            ...
            --------------------------------------------------------------
        """
        assert chunk_num > 1, "chunk_num should be bigger than 1."

        labels = [str(x) for x in range(1, chunk_num + 1)]

        portfolio = dc(self)
        portfolio = portfolio.dropna(subset=[factor, RET_1])

        if only_positive:
            portfolio = portfolio.loc[portfolio[factor] > 0, :]

        portfolio[QUANTILE] = portfolio.groupby(by=[DATE])[factor].transform(
            lambda x: pd.qcut(x, chunk_num, labels=labels)
        )
        portfolio[QUANTILE] = portfolio[QUANTILE].apply(int).apply(str)

        quantile_portfolio_returns = DataFrame()
        for label in labels:
            labelled_data = portfolio.loc[portfolio[QUANTILE] == label, :]
            if weighted:
                grouped_data = labelled_data.groupby([DATE]).apply(lambda x: np.average(x[RET_1], weights=x[MKTCAP]))
            else:
                grouped_data = labelled_data.groupby([DATE])[RET_1].mean()
            grouped_data = grouped_data.rename(label)
            grouped_data = self._cumulate(grouped_data, cumulative)
            quantile_portfolio_returns = pd.concat([quantile_portfolio_returns, grouped_data], axis=1, sort=True)

        if show_plot:
            plt.figure()
            quantile_portfolio_returns.plot()
            if title:
                plt.title(title)
            else:
                plt.title(factor.upper())
            plt.ylabel("Return")
            plt.xlabel("Date")
            plt.legend(loc='upper left')
            plt.show()

        if show_bar_chart:
            plt.figure()
            quantile_result = portfolio.quantile_distribution_ratio(
                factor, chunk_num=chunk_num, cumulative=False, weighted=weighted, only_positive=only_positive,
                show_plot=False, show_bar_chart=False, title=None
            )
            quantile_result.mean(axis=0).plot(kind='bar')
            if title:
                plt.title(title)
            else:
                plt.title(factor.upper())
            plt.ylabel("Return")
            plt.xlabel("Group")
            plt.show()

        return quantile_portfolio_returns

    def rank_correlation(self, factor: str, ranked_by: str = RET_1, rolling: int = 6,
                         show_plot=False, title: str = '') -> DataFrame:
        portfolio = dc(self.dropna(subset=[ranked_by]))
        portfolio = portfolio.periodic_rank(factor=factor, drop_rank=False)
        factor_rank = "{factor}_rank".format(factor=factor)
        portfolio = portfolio.rename(index=str, columns={"rank": factor_rank})
        portfolio = portfolio.periodic_rank(factor=ranked_by, drop_rank=False)
        actual_rank = "{ranked_by}_rank".format(ranked_by=ranked_by)
        portfolio = portfolio.rename(index=str, columns={"rank": actual_rank})
        rank_ic = portfolio.groupby(by=[DATE]).apply(
            lambda x: 1 - (6 * ((x[factor_rank] - x[actual_rank]) ** 2).sum()) / (len(x) * (len(x) ** 2 - 1)))

        rank_ic = pd.DataFrame(rank_ic, columns=[RANK_CORRELATION])
        rolling_column_name = 'rolling_{}'.format(rolling)
        rank_ic[rolling_column_name] = rank_ic[RANK_CORRELATION].rolling(window=rolling).mean()

        if show_plot:
            rank_ic.plot()
            plt.title(title)
            plt.axhline(y=0, color='black')
            plt.ylabel('Rank IC')
            plt.xlabel('Date')
            plt.show()

        return rank_ic

    def show_plot(self, cumulative: bool = True, weighted: bool = False, title: str = None,
                  show_benchmark: bool = True):
        portfolio = self.dropna(subset=[RET_1])

        if weighted:
            grouped_data = portfolio.groupby([DATE]).apply(lambda x: np.average(x[RET_1], weights=x[MKTCAP]))
        else:
            grouped_data = portfolio.groupby([DATE])[RET_1].mean()

        # noinspection PyProtectedMember
        grouped_data = self._cumulate(grouped_data, cumulative)

        plt.figure()

        if show_benchmark:
            benchmark = self.get_benchmark()[[DATE, BENCHMARK_RET_1]]
            benchmark = benchmark.set_index(keys=[DATE])
            benchmark = self._cumulate(benchmark, cumulative).dropna().reset_index(drop=False)
            grouped_data = grouped_data.reset_index(drop=False)
            grouped_data = pd.merge(grouped_data, benchmark, on=[DATE])
            grouped_data = grouped_data.rename(index=str, columns={
                RET_1: 'Portfolio',
                BENCHMARK_RET_1: self.benchmark
            })
            grouped_data = grouped_data.set_index(keys=[DATE])

        grouped_data.plot()

        if title:
            plt.title(title)
        else:
            plt.title("Portfolio Simulation")
        plt.ylabel("Return")
        plt.xlabel("Date")

        plt.show()

    @staticmethod
    @not_empty
    def _cumulate(ret, cumulative=True):
        ret.iloc[0] = 0
        if cumulative:
            ret = ret + 1
            ret = ret.cumprod()
            ret = ret - 1
        return ret
