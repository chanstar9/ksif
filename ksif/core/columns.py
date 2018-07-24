# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 7. 18.
"""
import itertools

# Base information
CODE = 'code'
NAME = 'name'
DATE = 'date'
ADJP = 'adjp'
ENDP = 'endp'
MKTCAP = 'mktcap'
FN_GUIDE_SECTOR = 'fn_guide_sector'
RET_1 = 'ret1'
TD_VALUE = 'td_value'
TD_VOLUMN = 'td_volumn'
BASE_INFORMATION = [CODE, NAME, DATE, ADJP, ENDP, MKTCAP, FN_GUIDE_SECTOR, RET_1, TD_VALUE, TD_VOLUMN]

# Filter
EXCHANGE = 'exchange'
HOLDING = 'holding'
IS_MANAGED = 'is_managed'
WHY_MANAGED = 'why_managed'
IS_SUSPENDED = 'is_suspended'
WHY_SUSPENDED = 'why_suspended'
FILTERS = [EXCHANGE, HOLDING, IS_MANAGED, WHY_MANAGED, IS_SUSPENDED, WHY_SUSPENDED]

# Value factors
PER = 'per'
PBR = 'pbr'
PSR = 'psr'
PCR = 'pcr'
PGPR = 'pgpr'
POPR = 'popr'
EV_EBITDA = 'ev_ebitda'
VALUE_FACTORS = [PER, PBR, PSR, PCR, PGPR, POPR, EV_EBITDA]

# Reverse value factors
EBIT_EV = 'ebit_ev'
CF_EV = 'cf_ev'
S_EV = 's_ev'
E_P = 'e_p'
B_P = 'b_p'
C_P = 'c_p'
S_P = 's_p'
GP_P = 'gp_p'
OP_P = 'op_p'
REVERSE_VALUE_FACTORS = [EBIT_EV, CF_EV, S_EV, E_P, B_P, C_P, S_P, GP_P, OP_P]

# Profit factors
S_A = 's_a'
GP_A = 'gp_a'
OP_A = 'op_a'
CF_A = 'cf_a'
ROA = 'roa'
ROE = 'roe'
QROA = 'qroa'
QROE = 'qroe'
EBT_E = 'ebt_e'
ROIC = 'roic'
GP_S = 'gp_s'
LIQ_RATIO = 'liq_ratio'
DEBT_RATIO = 'debt_ratio'
PROFIT_FACTORS = [S_A, GP_A, OP_A, CF_A, ROA, ROE, QROA, QROE, EBT_E, ROIC, GP_S, LIQ_RATIO, DEBT_RATIO]

# Growth factors
SALESQOQ = 'salesqoq'
GPQOQ = 'gpqoq'
OPQOQ = 'opqoq'
ROAQOQ = 'roaqoq'
ROAYOY = 'roayoy'
GP_SYOY = 'gp_syoy'
GP_AYOY = 'gp_ayoy'
GROWTH_FACTORS = [SALESQOQ, GPQOQ, OPQOQ, ROAQOQ, ROAYOY, GP_SYOY, GP_AYOY]

# Momentum factors
MOM12_1 = 'mom12-1'
MOM6 = 'mom6'
MOM3 = 'mom3'
MOM1 = 'mom1'
MOMENTUM_FACTORS = [MOM12_1, MOM6, MOM3, MOM1]

# Safety factors
BETA_1D = 'beta_1d'
BETA_3M = 'beta_3m'
BETA_5M = 'beta_5m'
BETA_1W = 'beta_1w'
BETA_2W = 'beta_2w'
VOL_1D = 'vol_1d'
VOL_3M = 'vol_3m'
VOL_5M = 'vol_5m'
VOL_1W = 'vol_1w'
VOL_2W = 'vol_2w'
SAFETY_FACTORS = [BETA_1D, BETA_1W, BETA_2W, BETA_3M, BETA_5M, VOL_1D, VOL_1W, VOL_2W, VOL_3M, VOL_5M]

FACTORS = list(
    itertools.chain(
        # Values factors
        VALUE_FACTORS,
        # Reverse value factors
        REVERSE_VALUE_FACTORS,
        # Profit factors
        PROFIT_FACTORS,
        # Growth factors
        GROWTH_FACTORS,
        # Momentum factors
        MOMENTUM_FACTORS,
        # Safety factors
        SAFETY_FACTORS,
    )
)

# Benchmarks
MKF_2000 = 'MKF2000'
KOSDAQ = '코스닥'
KOSDAQ_LARGE = '코스닥 대형주'
KOSDAQ_MIDDLE = '코스닥 중형주'
KOSDAQ_SMALL = '코스닥 소형주'
KOSPI = '코스피'
KOSPI_200 = '코스피 200'
KOSPI_LARGE = '코스피 대형주'
KOSPI_MIDDLE = '코스피 중형주'
KOSPI_SMALL = '코스피 소형주'
CD_91 = 'CD_91'

BENCHMARKS = [
    MKF_2000,
    KOSDAQ, KOSDAQ_LARGE, KOSDAQ_MIDDLE, KOSDAQ_SMALL,
    KOSPI, KOSPI_200, KOSPI_LARGE, KOSPI_MIDDLE, KOSPI_SMALL,
    CD_91,
]
