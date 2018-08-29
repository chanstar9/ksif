# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
:Date: 2018. 6. 22.
"""
from ksif.core.columns import *

# Names of raw excel sheets
COMPANY = 'company'
BENCHMARK = 'benchmark'

# Special words for companies
SPAC = '스팩'
HOLDING = 'holding'

# Special words for benchmarks
PRICE_INDEX = 'price_index'

# Common columns
FISCAL_QUARTER = 'fiscal_quarter'

# Daily columns
OUTCST = 'outcst'
CS_TOBEPUB = 'cs_tobepub'
CS_TR = 'cs_tr'
OUTPST = 'outpst'
PS_TOBEPUB = 'ps_tobepub'
PS_TR = 'ps_tr'
TD_VALUE = 'td_value'
TD_VOLUMN = 'td_volumn'
KRX_SECTOR = 'krx_sector'
ENDP_PS = 'endp_ps'
NET_PERSONAL_PURCHASE = 'net_personal_purchase'
NET_NATIONAL_PURCHASE = 'net_national_purchase'
NET_FINANCIAL_INVESTMENT_PURCHASE = 'net_personal_purchase'
NET_INSTITUTIONAL_FOREIGNER_PURCHASE = 'net_personal_purchase'
NET_INSTITUTIONAL_PURCHASE = 'net_personal_purchase'
NET_ETC_FINANCE_PURCHASE = 'net_personal_purchase'
NET_ETC_CORPORATION_PURCHASE = 'net_personal_purchase'
NET_ETC_FOREIGNER_PURCHASE = 'net_personal_purchase'
NET_REGISTERED_FOREIGNER_PURCHASE = 'net_personal_purchase'
NET_INSURANCE_PURCHASE = 'net_personal_purchase'
NET_PRIVATE_FUND_PURCHASE = 'net_personal_purchase'
NET_PENSION_PURCHASE = 'net_personal_purchase'
NET_FOREIGNER_PURCHASE = 'net_personal_purchase'
NET_BANK_PURCHASE = 'net_personal_purchase'
NET_TRUST_PURCHASE = 'net_personal_purchase'
SHORT_SALE_VOLUME = 'short_sale_volume'
SHORT_SALE_BALANCE = 'short_sale_balance'

DAILY_DATA = [
    CODE, DATE, NAME, FN_GUIDE_SECTOR, FN_GUIDE_INDUSTRY_GROUP_27, ADJP, OUTCST, CS_TOBEPUB, CS_TR, ENDP, OUTPST,
    PS_TOBEPUB, PS_TR, BETA_1D, BETA_1W, BETA_2W, BETA_3M, BETA_5M, VOL_1D, VOL_1W, VOL_2W, VOL_3M, VOL_5M, IS_MANAGED,
    WHY_MANAGED, IS_SUSPENDED, WHY_SUSPENDED, TD_VALUE, TD_VOLUMN, EXCHANGE, KRX_SECTOR, ENDP_PS, HOLDING,
]

MKTCAP_CS = 'mktcap_cs'

# Quarterly columns
ASSETS = 'assets'
CUR_ASSETS = 'cur_assets'
LIAB = 'liab'
CUR_LIAB = 'cur_liab'
INV = 'inv'
SALES = 'sales'
GP = 'gp'
NI_OWNER = 'ni_owner'
NI = 'ni'
INT_INC = 'int_inc'
INT_EXP = 'int_exp'
CFO = 'cfo'
AR = 'ar'
ALLOWANCE_AR_ = '(allowance_ar)'
AP = 'ap'
EBIT = 'ebit'
EBITDA = 'ebitda'
CASH = 'cash'
TAX = 'tax'
RES_EXP = 'res_exp'
DIVP = 'divp'
EQUITY = 'equity'
TANG_ASSET = 'tang_asset'
FIN_LIAB = 'fin_liab'
PS_DIV = 'ps_div'

QUARTERLY_DATA = [
    CODE, DATE, ASSETS, CUR_ASSETS, LIAB, CUR_LIAB, INV, SALES, GP, NI_OWNER, NI, INT_INC, INT_EXP, CFO, AR,
    ALLOWANCE_AR_, AP, EBIT, EBITDA, CASH, TAX, RES_EXP, DIVP, EQUITY, TANG_ASSET, FIN_LIAB, PS_DIV,
]

RENAMES = {
    'FnGuide Sector': FN_GUIDE_SECTOR,
    'FnGuide Industry Group 27': FN_GUIDE_INDUSTRY_GROUP_27,
    '수정주가 (현금배당반영)(원)': ADJP,
    '상장주식수 (보통)(주)': OUTCST,
    '상장예정주식수 (보통)(주)': CS_TOBEPUB,
    '자기주식수 (보통)(주)': CS_TR,
    '종가(원)': ENDP,
    '상장주식수 (우선)(주)': OUTPST,
    '상장예정주식수 (우선)(주)': PS_TOBEPUB,
    '자기주식수 (우선)(주)': PS_TR,
    '베타 (D,1Yr)': BETA_1D,
    '베타 (W,1Yr)': BETA_1W,
    '베타 (W,2Yr)': BETA_2W,
    '베타 (M,3Yr)': BETA_3M,
    '베타 (M,5Yr)': BETA_5M,
    '변동성 (D,1Yr)': VOL_1D,
    '변동성 (W,1Yr)': VOL_1W,
    '변동성 (W,2Yr)': VOL_2W,
    '변동성 (M,3Yr)': VOL_3M,
    '변동성 (M,5Yr)': VOL_5M,
    '관리종목여부': IS_MANAGED,
    '관리종목지정사유': WHY_MANAGED,
    '거래정지여부': IS_SUSPENDED,
    '거래정지사유': WHY_SUSPENDED,
    '거래대금 (60일 평균)(원)': TD_VALUE,
    '거래량 (60일 평균)(주)': TD_VOLUMN,
    '거래소(시장)': EXCHANGE,
    '자산(*)(천원)': ASSETS,
    '유동자산(*)(천원)': CUR_ASSETS,
    '부채(*)(천원)': LIAB,
    '유동부채(*)(천원)': CUR_LIAB,
    '재고자산(*)(천원)': INV,
    '매출액(수익)(*)(천원)': SALES,
    '매출총이익(손실)(천원)': GP,
    '지배주주순이익(천원)': NI_OWNER,
    '당기순이익(천원)': NI,
    '이자수익(비영업)(천원)': INT_INC,
    '이자비용(비영업)(천원)': INT_EXP,
    '영업활동으로인한현금흐름(천원)': CFO,
    '매출채권(천원)': AR,
    '(대손충당금)(천원)': ALLOWANCE_AR_,
    '매입채무(천원)': AP,
    'EBIT(천원)': EBIT,
    'EBITDA(천원)': EBITDA,
    '현금및현금성자산(*)(천원)': CASH,
    '법인세비용(천원)': TAX,
    '연구개발비(천원)': RES_EXP,
    '배당수익률(보통주,현금)(%)': DIVP,
    '자본(*)(천원)': EQUITY,
    '유형자산(*)(천원)': TANG_ASSET,
    '*총금융부채(천원)': FIN_LIAB,
    '거래소 업종': KRX_SECTOR,
    '종가 (우선)(원)': ENDP_PS,
    '배당금(우선주,현금)(천원)': PS_DIV,
'순매수수량(개인)(주)': ,
'순매수수량(국가)(주)': ,
'순매수수량(금융투자)(주)': ,
'순매수수량(기관/외국인계)(주)': ,
'순매수수량(기관계)(주)': ,
'순매수수량(기타금융)(주)': ,
'순매수수량(기타법인)(주)': ,
'순매수수량(기타외국인)(주)': ,
'순매수수량(등록외국인)(주)': ,
'순매수수량(보험)(주)': ,
'순매수수량(사모펀드)(주)': ,
'순매수수량(연기금)(주)': ,
'순매수수량(외국인계)(주)': ,
'순매수수량(은행)(주)': ,
'순매수수량(투신)(주)': ,
'공매도거래량(주)': ,
'공매도잔고량(주)': ,
'외국인보유비중(티커)(%)': ,
}

COMPANY_RESULT_COLUMNS = list(
    itertools.chain(
        # Base information
        [CODE, NAME, DATE, ADJP, ENDP, MKTCAP, FN_GUIDE_SECTOR, FN_GUIDE_INDUSTRY_GROUP_27, KRX_SECTOR, RET_1, TD_VALUE,
         TD_VOLUMN],
        # Filter
        [EXCHANGE, HOLDING, IS_MANAGED, WHY_MANAGED, IS_SUSPENDED, WHY_SUSPENDED],
        # Values factors
        [PER, PBR, PSR, PCR, PGPR, POPR, EV_EBITDA],
        # Reverse value factors
        [EBIT_EV, CF_EV, S_EV, E_P, B_P, C_P, S_P, GP_P, OP_P],
        # Profit factors
        [S_A, GP_A, OP_A, CF_A, ROA, ROE, QROA, QROE, EBT_E, ROIC, GP_S, LIQ_RATIO, DEBT_RATIO],
        # Growth factors
        [SALESQOQ, GPQOQ, OPQOQ, ROAQOQ, ROAYOY, GP_SYOY, GP_AYOY],
        # Momentum factors
        [MOM12_1, MOM6, MOM3, MOM1],
        # Safety factors
        [BETA_1D, BETA_1W, BETA_2W, BETA_3M, BETA_5M, VOL_1D, VOL_1W, VOL_2W, VOL_3M, VOL_5M],
        # Liquidity factors
        [],
    )
)

BENCHMARK_RESULT_COLUMNS = [CODE, DATE, RET_1]
