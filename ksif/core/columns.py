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
RET_1 = 'return_1'  # 1개월 수익
RET_3 = 'return_3'  # 3개월 수익
RET_6 = 'return_6'  # 6개월 수익
ADJP = 'adjp'  # 수정종가
ENDP = 'endp'  # 종가
MKTCAP = 'mktcap'  # 시가총액
BASE_INFORMATION = [CODE, NAME, DATE, RET_1, RET_3, RET_6, ADJP, ENDP, MKTCAP]

# Filter
EXCHANGE = 'exchange'  # 거래소
FN_GUIDE_SECTOR = 'fn_guide_sector'
FN_GUIDE_INDUSTRY_GROUP_27 = 'fn_guide_industry_group_27'
KRX_SECTOR = 'krx_sector'
HOLDING = 'holding'  # 지주사 여부
IS_MANAGED = 'is_managed'  # 관리종목 여부
WHY_MANAGED = 'why_managed'  # 관리종목 지정사유
IS_SUSPENDED = 'is_suspended'  # 거래정지 여부
WHY_SUSPENDED = 'why_suspended'  # 거래정지 지정사유
FILTERS = [EXCHANGE, FN_GUIDE_SECTOR, FN_GUIDE_INDUSTRY_GROUP_27, KRX_SECTOR, HOLDING, IS_MANAGED,
           WHY_MANAGED, IS_SUSPENDED, WHY_SUSPENDED]

# Value factors
PER = 'per'
PBR = 'pbr'
PSR = 'psr'
PCR = 'pcr'
PGPR = 'pgpr'
POPR = 'popr'
EV_EBITDA = 'ev_ebitda'
EBIT_EV = 'ebit_ev'
CF_EV = 'cf_ev'
S_EV = 's_ev'
E_P = 'e_p'
B_P = 'b_p'
C_P = 'c_p'
S_P = 's_p'
GP_P = 'gp_p'
OP_P = 'op_p'
VALUE_FACTORS = [PER, PBR, PSR, PCR, PGPR, POPR, EV_EBITDA, EBIT_EV, CF_EV, S_EV, E_P, B_P, C_P, S_P, GP_P, OP_P]

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
MOM6_1 = 'mom6-1'
MOM6 = 'mom6'
MOM3 = 'mom3'
MOM1 = 'mom1'
MOMENTUM_FACTORS = [MOM12_1, MOM6_1, MOM6, MOM3, MOM1]

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

# Liquidity factors
TRADING_VOLUME_RATIO = 'trading_volume_ratio'  # 거래비율
NET_PERSONAL_PURCHASE_RATIO = 'net_personal_purchase_ratio'  # 개인순매수비율
NET_INSTITUTIONAL_FOREIGN_PURCHASE_RATIO = 'net_institutional_foreign_purchase_ratio'  # 기관/외국인순매수비율
NET_INSTITUTIONAL_PURCHASE_RATIO = 'net_institutional_purchase_ratio'  # 기관순매수비율
NET_FINANCIAL_INVESTMENT_PURCHASE_RATIO = 'net_financial_investment_purchase_ratio'  # 금융투자순매수비율
NET_INSURANCE_PURCHASE_RATIO = 'net_insurance_purchase_ratio'  # 보험순매수비율
NET_TRUST_PURCHASE_RATIO = 'net_trust_purchase_ratio'  # 투신순매수비율
NET_PRIVATE_FUND_PURCHASE_RATIO = 'net_private_fund_purchase_ratio'  # 사모펀드순매수비율
NET_BANK_PURCHASE_RATIO = 'net_bank_purchase_ratio'  # 은행순매수비율
NET_ETC_FINANCE_PURCHASE_RATIO = 'net_etc_finance_purchase_ratio'  # 기타금융순매수비율
NET_PENSION_PURCHASE_RATIO = 'net_pension_purchase_ratio'  # 연기금순매수비율
NET_NATIONAL_PURCHASE_RATIO = 'net_national_purchase_ratio'  # 국가순매수비율
NET_ETC_CORPORATION_PURCHASE_RATIO = 'net_etc_corporation_purchase_ratio'  # 기타법인순매수비율
NET_FOREIGN_PURCHASE_RATIO = 'net_foreign_purchase_ratio'  # 외국인순매수비율
NET_REGISTERED_FOREIGN_PURCHASE_RATIO = 'net_registered_foreign_purchase_ratio'  # 등록외국인순매수비율
NET_ETC_FOREIGN_PURCHASE_RATIO = 'net_etc_foreign_purchase_ratio'  # 기타외국인순매수비율
SHORT_SALE_VOLUME_RATIO = 'short_sale_volume_ratio'  # 공매도거래비율
SHORT_SALE_BALANCE_RATIO = 'short_sale_balance_ratio'  # 공매도잔고비율
FOREIGN_OWNERSHIP_RATIO = 'foreign_ownership_ratio'  # 외국인보유비중
LIQUIDITY_FACTORS = [
    TRADING_VOLUME_RATIO, NET_PERSONAL_PURCHASE_RATIO, NET_INSTITUTIONAL_FOREIGN_PURCHASE_RATIO,
    NET_INSTITUTIONAL_PURCHASE_RATIO, NET_FINANCIAL_INVESTMENT_PURCHASE_RATIO, NET_INSURANCE_PURCHASE_RATIO,
    NET_TRUST_PURCHASE_RATIO, NET_PRIVATE_FUND_PURCHASE_RATIO, NET_BANK_PURCHASE_RATIO,
    NET_ETC_FINANCE_PURCHASE_RATIO, NET_PENSION_PURCHASE_RATIO, NET_NATIONAL_PURCHASE_RATIO,
    NET_ETC_CORPORATION_PURCHASE_RATIO, NET_FOREIGN_PURCHASE_RATIO, NET_REGISTERED_FOREIGN_PURCHASE_RATIO,
    NET_ETC_FOREIGN_PURCHASE_RATIO, SHORT_SALE_VOLUME_RATIO, SHORT_SALE_BALANCE_RATIO,
    FOREIGN_OWNERSHIP_RATIO
]

COMPANY_FACTORS = list(
    itertools.chain(
        # Values factors
        VALUE_FACTORS,
        # Profit factors
        PROFIT_FACTORS,
        # Growth factors
        GROWTH_FACTORS,
        # Momentum factors
        MOMENTUM_FACTORS,
        # Safety factors
        SAFETY_FACTORS,
        # Liquidity factors
        LIQUIDITY_FACTORS,
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
TOTAL_LARGE = '코스피/코스닥 대형주 평균'
TOTAL_MIDDLE = '코스피/코스닥 중형주 평균'
TOTAL_SMALL = '코스피/코스닥 소형주 평균'

BENCHMARKS = [
    MKF_2000,
    KOSDAQ, KOSDAQ_LARGE, KOSDAQ_MIDDLE, KOSDAQ_SMALL,
    KOSPI, KOSPI_200, KOSPI_LARGE, KOSPI_MIDDLE, KOSPI_SMALL,
    TOTAL_LARGE, TOTAL_MIDDLE, TOTAL_SMALL,
]
