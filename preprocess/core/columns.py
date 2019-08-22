# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Chankyu Choi
:Date: 2018. 6. 22.
"""
from ksif.core.columns import *

# Company
# Names of raw excel sheets
COMPANY = 'company'
BENCHMARK = 'benchmark'
MACRO = 'macro'
FACTOR = 'factor'

# Special words for companies
SPAC = '스팩'
HOLDING = 'holding'

# Special words for benchmarks
PRICE_INDEX = 'price_index'

# Common columns
FISCAL_QUARTER = 'fiscal_quarter'

# Daily columns
OPEN_P = 'open_p'  # 시가
HIGH_P = 'high_p'  # 고가
LOW_P = 'low_p'  # 저가
CLOSE_P = 'close_p'  # 종가
ADJ_C = 'adj_c'  # 수정계수
DIV_ADJ_C = 'div_adj_p'  # 수정계수(현금배당 반영)
LISTED_SHARES = 'listed_shares'  # 상장주식수 (보통)(주)
CS_TOBEPUB = 'cs_tobepub'  # 상장예정주식수 (보통)(주)
LS_SHARES = 'ms_shares'  # 최대주주보유 주식수 (보통)(주)
OVER_10_QUARTILE_SHARES = 'over_10_quartile_shares'  # 지분 10% 이상 주주 주식수 (보통)(주)
OVER_20_QUARTILE_SHARES = 'over_20_quartile_shares'  # 지분 5% 이상 주주 주식수 (보통)(주)
TRADING_VOLUME = 'trading_volume'  # 거래량(주)
TRADING_VOLUME_P = 'trading_volume_p'  # 거래대금(원)
NET_PERSONAL_PURCHASE = 'net_personal_purchase'  # 순매수수량(개인)(주)
NET_NATIONAL_PURCHASE = 'net_national_purchase'  # 순매수수량(국가)(주)
NET_FINANCIAL_INVESTMENT_PURCHASE = 'net_financial_investment_purchase'  # 순매수수량(금융투자)(주)
NET_INSTITUTIONAL_FOREIGN_PURCHASE = 'net_institutional_foreign_purchase'  # 순매수수량(기관/외국인계)(주)
NET_INSTITUTIONAL_PURCHASE = 'net_institutional_purchase'  # 순매수수량(기관계)(주)
NET_ETC_FINANCE_PURCHASE = 'net_etc_finance_purchase'  # 순매수수량(기타금융)(주)
NET_ETC_CORPORATION_PURCHASE = 'net_etc_corporation_purchase'  # 순매수수량(기타법인)(주)
NET_ETC_FOREIGN_PURCHASE = 'net_etc_foreign_purchase'  # 순매수수량(기타외국인)(주)
NET_REGISTERED_FOREIGN_PURCHASE = 'net_registered_foreign_purchase'  # 순매수수량(등록외국인)(주)
NET_INSURANCE_PURCHASE = 'net_insurance_purchase'  # 순매수수량(보험)(주)
NET_PRIVATE_FUND_PURCHASE = 'net_private_fund_purchase'  # 순매수수량(사모펀드)(주)
NET_PENSION_PURCHASE = 'net_pension_purchase'  # 순매수수량(연기금)(주)
NET_FOREIGN_PURCHASE = 'net_foreign_purchase'  # 순매수수량(외국인계)(주)
NET_BANK_PURCHASE = 'net_bank_purchase'  # 순매수수량(은행)(주)
NET_TRUST_PURCHASE = 'net_trust_purchase'  # 순매수수량(투신)(주)
SHORT_SALE_VOLUME = 'short_sale_volume'  # 공매도거래량 (20일)(주)
SHORT_SALE_BALANCE = 'short_sale_balance'  # 공매도잔고량(주)
SHARE_LENDING_VOLUME = 'share_lending_volume'  # 대차거래 체결 (20일)(주)
SHARE_LENDING_BALANCE = 'share_lending_balance'  # 대차거래 잔고(주)
CONSENSUS_MEAN = 'consensus_mean'  # 적정주가 (E1)(원)
CONSENSUS_CHG = 'consensus_chg'  # 적정주가 (E1, 1W Chg)(%)
CONSENSUS_MAX = 'consensus_max'  # 적정주가 (E1, 최대)(원)
CONSENSUS_MIN = 'consensus_min'  # 적정주가 (E1, 최소)(원)
CONSENSUS_MID = 'consensus_mid'  # 적정주가 (E1,중간)(원)
CONSENSUS_CV = 'consensus_cv'  # 적정주가 CV (E1)
CONSENSUS_DIS = 'consensus_dis'  # 적정주가 괴리율 (E1)(%)
CONSENSUS_UP = 'consensus_up'  # 적정주가 상향수 (E1)
CONSENSUS_STAY = 'consensus_stay'  # 적정주가 유지수 (E1)
CONSENSUS_STD = 'consensus_std'  # 적정주가 표준편차 (E1)
CONSENSUS_DOWN = 'consensus_down'  # 적정주가 하향수 (E1)
CONSENSUS_ADJ_CHG = 'consensus_adj_chg'  # 적정주가(상향-하향)/(전체)(E1)

DAILY_DATA = [
    CODE, DATE, NAME,
    FN_GUIDE_SECTOR, FN_GUIDE_INDUSTRY_GROUP_27, IS_SUSPENDED, EXCHANGE, KRX_SECTOR, HOLDING,
    LISTED_SHARES, CS_TOBEPUB, LS_SHARES, OVER_10_QUARTILE_SHARES, OVER_20_QUARTILE_SHARES, MKTCAP,
    OPEN_P, HIGH_P, LOW_P, CLOSE_P, ADJ_C, DIV_ADJ_C, ADJ_OPEN_P, ADJ_HIGH_P, ADJ_LOW_P, ADJ_CLOSE_P,
    BETA_1D, BETA_1W, BETA_2W, BETA_3M, BETA_5M, VOL_1D, VOL_1W, VOL_2W, VOL_3M, VOL_5M, IS_MANAGED,
    ADJ_TRADING_VOLUME, TRADING_VOLUME, NET_PERSONAL_PURCHASE, NET_NATIONAL_PURCHASE, NET_FINANCIAL_INVESTMENT_PURCHASE,
    NET_INSTITUTIONAL_FOREIGN_PURCHASE, NET_INSTITUTIONAL_PURCHASE, NET_ETC_FINANCE_PURCHASE,
    NET_ETC_CORPORATION_PURCHASE, NET_ETC_FOREIGN_PURCHASE, NET_REGISTERED_FOREIGN_PURCHASE,
    NET_INSURANCE_PURCHASE, NET_PRIVATE_FUND_PURCHASE, NET_PENSION_PURCHASE, NET_FOREIGN_PURCHASE,
    NET_BANK_PURCHASE, NET_TRUST_PURCHASE, FOREIGN_OWNERSHIP_RATIO, SHORT_SALE_VOLUME, SHORT_SALE_BALANCE,
    SHARE_LENDING_VOLUME, SHARE_LENDING_BALANCE, CONSENSUS_MEAN, CONSENSUS_CHG, CONSENSUS_MAX, CONSENSUS_MIN,
    CONSENSUS_MID, CONSENSUS_CV, CONSENSUS_DIS, CONSENSUS_UP, CONSENSUS_DOWN, CONSENSUS_STAY, CONSENSUS_STD,
    CONSENSUS_ADJ_CHG
]

# Quarterly columns
ASSETS = 'assets'  # 자산(*)(천원)
CUR_ASSETS = 'cur_assets'  # 유동자산(*)(천원)
LIAB = 'liab'  # 부채(*)(천원)
CUR_LIAB = 'cur_liab'  # 유동부채(*)(천원)
INV = 'inv'  # 재고자산(*)(천원)
SALES = 'sales'  # 매출액(수익)(*)(천원)
GP = 'gp'  # 매출총이익(손실)(천원)
NI_OWNER = 'ni_owner'  # 지배주주순이익(천원)
NI = 'net_income'  # 당기순이익(천원)
INT_INC = 'int_inc'  # 이자수익(비영업)(천원)
INT_EXP = 'int_exp'  # 이자비용(비영업)(천원)
CFO = 'cfo'  # 영업활동으로인한현금흐름(천원)
AR = 'ar'  # 매출채권(천원)
ALLOWANCE_AR_ = 'allowance_ar'  # (대손충당금)(천원)
AP = 'ap'  # 매입채무(천원)
EBIT = 'ebit'  # EBIT(천원)
EBITDA = 'ebitda'  # EBITDA(천원)
CASH = 'cash'  # 현금및현금성자산(*)(천원)
TAX = 'tax'  # 법인세비용(천원)
RES_EXP = 'res_exp'  # 연구개발비(천원)
EQUITY = 'equity'  # 자본(*)(천원)
TANG_ASSET = 'tang_asset'  # 유형자산(*)(천원)
FIN_LIAB = 'fin_liab'  # *총금융부채(천원)

QUARTERLY_DATA = [
    CODE, DATE, ASSETS, CUR_ASSETS, LIAB, CUR_LIAB, INV, SALES, GP, NI_OWNER, NI, INT_INC, INT_EXP, CFO, AR,
    ALLOWANCE_AR_, AP, EBIT, EBITDA, CASH, TAX, RES_EXP, DIVP, EQUITY, TANG_ASSET, FIN_LIAB,
]

COMPANY_RENAMES = {
    '시가(원)': OPEN_P,
    '고가(원)': HIGH_P,
    '저가(원)': LOW_P,
    '종가(원)': CLOSE_P,
    '수정계수': ADJ_C,
    '수정계수 (현금배당반영)': DIV_ADJ_C,
    'FnGuide Sector': FN_GUIDE_SECTOR,
    'FnGuide Industry Group 27': FN_GUIDE_INDUSTRY_GROUP_27,
    '최대주주등-보통주 수(Q)': LS_SHARES,
    '10%이상(최대주주등제외)주주-보통주 수(Q)': OVER_10_QUARTILE_SHARES,
    '5%이상(10%미만)주주-보통주 수(Q)': OVER_20_QUARTILE_SHARES,
    '상장주식수 (보통)(주)': LISTED_SHARES,
    '상장예정주식수 (보통)(주)': CS_TOBEPUB,
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
    '거래정지여부': IS_SUSPENDED,
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
    '순매수수량(개인)(주)': NET_PERSONAL_PURCHASE,
    '순매수수량(기관/외국인계)(주)': NET_INSTITUTIONAL_FOREIGN_PURCHASE,
    '순매수수량(기관계)(주)': NET_INSTITUTIONAL_PURCHASE,
    '순매수수량(금융투자)(주)': NET_FINANCIAL_INVESTMENT_PURCHASE,
    '순매수수량(보험)(주)': NET_INSURANCE_PURCHASE,
    '순매수수량(은행)(주)': NET_BANK_PURCHASE,
    '순매수수량(투신)(주)': NET_TRUST_PURCHASE,
    '순매수수량(사모펀드)(주)': NET_PRIVATE_FUND_PURCHASE,
    '순매수수량(기타금융)(주)': NET_ETC_FINANCE_PURCHASE,
    '순매수수량(연기금)(주)': NET_PENSION_PURCHASE,
    '순매수수량(국가)(주)': NET_NATIONAL_PURCHASE,
    '순매수수량(기타법인)(주)': NET_ETC_CORPORATION_PURCHASE,
    '순매수수량(외국인계)(주)': NET_FOREIGN_PURCHASE,
    '순매수수량(등록외국인)(주)': NET_REGISTERED_FOREIGN_PURCHASE,
    '순매수수량(기타외국인)(주)': NET_ETC_FOREIGN_PURCHASE,
    '외국인보유비중(티커)(%)': FOREIGN_OWNERSHIP_RATIO,
    '공매도거래량(주)': SHORT_SALE_VOLUME,
    '공매도잔고량(주)': SHORT_SALE_BALANCE,
    '거래량(주)': TRADING_VOLUME,
    '거래대금(원)': TRADING_VOLUME_P,
    '대차거래 체결(주)': SHARE_LENDING_VOLUME,
    '대차거래 잔고(주)': SHARE_LENDING_BALANCE,
    '적정주가 (E1)(원)': CONSENSUS_MEAN,
    '적정주가 (E1, 1W Chg)(%)': CONSENSUS_CHG,
    '적정주가 (E1, 최대)(원)': CONSENSUS_MAX,
    '적정주가 (E1, 최소)(원)': CONSENSUS_MIN,
    '적정주가 (E1,중간)(원)': CONSENSUS_MID,
    '적정주가 CV (E1)': CONSENSUS_CV,
    '적정주가 괴리율 (E1)(%)': CONSENSUS_DIS,
    '적정주가 상향수 (E1)': CONSENSUS_UP,
    '적정주가 유지수 (E1)': CONSENSUS_STAY,
    '적정주가 표준편차 (E1)': CONSENSUS_STD,
    '적정주가 하향수 (E1)': CONSENSUS_DOWN,
    '적정주가(상향-하향)/(전체)(E1)': CONSENSUS_ADJ_CHG
}

COMPANY_RESULT_COLUMNS = list(
    set(
        itertools.chain(
            # Base information
            BASE_INFORMATION,
            # Daily information
            DAILY_DATA,
            # Quarterly information
            QUARTERLY_DATA[2:],
            # Filter
            FILTERS,
            # refined factors
            COMPANY_REFINED_FACTORS
        )
    )
)
# CODE & DATE 앞으로
COMPANY_RESULT_COLUMNS.remove(CODE)
COMPANY_RESULT_COLUMNS.remove(DATE)
COMPANY_RESULT_COLUMNS.insert(0, CODE)
COMPANY_RESULT_COLUMNS.insert(1, DATE)

# Benchmark
BENCHMARK_RESULT_COLUMNS = [CODE, DATE, BENCHMARK_RET_1, BENCHMARK_RET_5, BENCHMARK_RET_20, BENCHMARK_RET_60,
                            BENCHMARK_RET_120]

# Factor
BIG_HIGH = 'Size & Book Value(2X3) 대형 - High'
BIG_MEDIUM = 'Size & Book Value(2X3) 대형 - Medium'
BIG_LOW = 'Size & Book Value(2X3) 대형 - Low'
SMALL_HIGH = 'Size & Book Value(2X3) 소형 - High'
SMALL_MEDIUM = 'Size & Book Value(2X3) 소형 - Medium'
SMALL_LOW = 'Size & Book Value(2X3) 소형 - Low'

FACTOR_RET = 'factor_return'

FACTOR_RESULT_COLUMNS = [DATE, SMB, HML]

# Macro
CALL_RATE = 'call_rate'  # 콜(1일물)금리
CD_RATE = 'cd_rate'  # CD 유통수익률(91)금리
GOV_BOND = 'gov_bond'  # 국채(국민주택채권1종5년)금리
KO_THREE_YEARS_TREASURY_RATE = 'three_years_treasury_rate'  # 국고3년(국채관리기금채3년)금리
CURRENCY_STABILITY_RATE = 'currency_stability_rate'  # 통화안정(364일)금리
AA_MINUS_DEBENTURE_RATE = 'aa_minus_debenture_rate'  # 회사채(무보증3년AA-) 금리
MONETARY_STABILIZATION_BOND_RATE = 'monetary_stabilization_bond_rate'  # 통안증권(91일) 금리
KO_ONE_YEAR_TREASURY_RATE = 'one_tear_treasury_rate'  # 국고1년국고5년(국채관리기금채5년) 금리
KO_FIVE_YEARS_TREASURY_RATE = 'five_years_treasury_rate'  # 국고5년(국채관리기금채5년)
BBB_MINUS_DEBENTURE_RATE = 'bbb_minus_debenture_rate'  # 회사채(무보증3년 BBB-)
KO_TEN_YEARS_TREASURY_RATE = 'ten_years_treasury_rate'  # 국고10년
USD2KRW_EXCHANGE_RATE = 'usd2krw_exchange_rate'  # 시장평균_미국(달러)(통화대원)
CHY2KRW_EXCHANGE_RATE = 'chy2krw_exchange_rate'  # 시장평균_중국(위안)(통화대원)
EURO2KRW_EXCHANGE_RATE = 'euro2krw'  # 시장평균_EU(유로)(통화대원)
US_ONE_MONTH_GOV_BOND = 'us_one_month_gov_bond'  # 국채금리_미국국채(1개월)
US_ONE_YEAR_GOV_BOND = 'us_one_year_gov_bond'  # 국채금리_미국국채(1년)
US_FIVE_YEARS_GOV_BOND = 'us_five_years_gov_bond'  # 국채금리_미국국채(5년)
US_TEN_YEARS_GOV_BOND = 'us_ten_years_gov_bond'  # 국채금리_미국국채(10년)
ONE_MONTH_LIBOR = 'libor'  # 리보(미 달러) 1개월
NYSE = 'nyse'  # 미국 NYSE Composite(종가)
NASDAQ = 'nasdaq'  # 미국 Nasdaq Composite(종가)
NAND_8Gb_P = 'nand_8gb_price'  # NAND 8Gb 1Gx8 (MLC)(단기)($/개)
WTI_OIL_FUTURES_1M = 'wti_oil_futures_1m'  # 주요상품선물_WTI-1M($/bbl)
DOLLAR_INDEX_FUTURES = 'dollar_index_futures'  # 미국달러지수 (선물, NYBOT)
EXPORT = 'export'  # 수출금액지수(총지수)(2010=100)
IMPORT = 'import'  # 수입금액지수(총지수)(2010=100)
FOREIGN_EXCHANGE_RESERVE = 'foreign_exchange_reserve'  # 외환보유고(천달러)
US_INDUSTRY_PRODUCTION = 'us_industry_production'  # 미국산업생산(계절변동조정)(2010=100)
EURO_INDUSTRY_PRODUCTION = 'euro_industry_production'  # 유로지역산업생산(계절변동조정 OECD)(2010=100)
KO_INDUSTRY_PRODUCTION = 'ko_industry_production'  # 한국산업생산지수(계절조정)(2010=100)

MACRO_RENAMES = {
    'ECO_시장금리:콜(1일물)(%)': CALL_RATE,
    'ECO_시장금리:CD유통수익률(91)(%)': CD_RATE,
    'ECO_시장금리:국채(국민주택채권1종5년)(%)': GOV_BOND,
    'ECO_시장금리:국고3년(국채관리기금채3년)(%)': KO_THREE_YEARS_TREASURY_RATE,
    'ECO_시장금리:통화안정(364일)(%)': CURRENCY_STABILITY_RATE,
    'ECO_시장금리:회사채(무보증3년AA-)(%)': AA_MINUS_DEBENTURE_RATE,
    'ECO_시장금리:통안증권(91일)(%)': MONETARY_STABILIZATION_BOND_RATE,
    'ECO_시장금리:국고1년(%)': KO_ONE_YEAR_TREASURY_RATE,
    'ECO_시장금리:국고5년(국채관리기금채5년)(%)': KO_FIVE_YEARS_TREASURY_RATE,
    'ECO_시장금리:회사채(무보증3년BBB-)(%)': BBB_MINUS_DEBENTURE_RATE,
    'ECO_시장금리:국고10년(%)': KO_TEN_YEARS_TREASURY_RATE,
    'ECO_시장평균_미국(달러)(통화대원)': USD2KRW_EXCHANGE_RATE,
    'ECO_시장평균_중국(위안)(통화대원)': CHY2KRW_EXCHANGE_RATE,
    'ECO_시장평균_EU(유로)(통화대원)': EURO2KRW_EXCHANGE_RATE,
    'ECO_국채금리_미국국채(1개월)(%)': US_ONE_MONTH_GOV_BOND,
    'ECO_국채금리_미국국채(1년)(%)': US_ONE_YEAR_GOV_BOND,
    'ECO_국채금리_미국국채(5년)(%)': US_FIVE_YEARS_GOV_BOND,
    'ECO_국채금리_미국국채(10년)(%)': US_TEN_YEARS_GOV_BOND,
    'ECO_리보(미 달러) 1개월(%)': ONE_MONTH_LIBOR,
    'ECO_미국 NYSE Composite(종가)(Pt)': NYSE,
    'ECO_미국 Nasdaq Composite(종가)(Pt)': NASDAQ,
    'ECO_NAND 8Gb 1Gx8 (MLC)(단기)($/개)': NAND_8Gb_P,
    'ECO_주요상품선물_WTI-1M($/bbl)': WTI_OIL_FUTURES_1M,
    'ECO_미국달러지수 (선물, NYBOT)(Pt)': DOLLAR_INDEX_FUTURES,
    'ECO_수출금액지수(총지수)(2010=100)': EXPORT,
    'ECO_수입금액지수(총지수)(2010=100)': IMPORT,
    'ECO_외환(천달러)': FOREIGN_EXCHANGE_RESERVE,
    'ECO_미국(계절변동조정)(2010=100)': US_INDUSTRY_PRODUCTION,
    'ECO_유로지역(계절변동조정 OECD)(2010=100)': EURO_INDUSTRY_PRODUCTION,
    'ECO_산업생산지수(계절조정)(2010=100)': KO_INDUSTRY_PRODUCTION
}

MACRO_RAW = [CALL_RATE, CD_RATE, GOV_BOND, KO_THREE_YEARS_TREASURY_RATE, CURRENCY_STABILITY_RATE,
             AA_MINUS_DEBENTURE_RATE, MONETARY_STABILIZATION_BOND_RATE, KO_ONE_YEAR_TREASURY_RATE,
             KO_FIVE_YEARS_TREASURY_RATE, BBB_MINUS_DEBENTURE_RATE, KO_TEN_YEARS_TREASURY_RATE, USD2KRW_EXCHANGE_RATE,
             CHY2KRW_EXCHANGE_RATE, EURO2KRW_EXCHANGE_RATE, US_ONE_MONTH_GOV_BOND, US_ONE_YEAR_GOV_BOND,
             US_FIVE_YEARS_GOV_BOND, US_TEN_YEARS_GOV_BOND, ONE_MONTH_LIBOR, NYSE, NASDAQ, NAND_8Gb_P,
             WTI_OIL_FUTURES_1M, DOLLAR_INDEX_FUTURES, EXPORT, IMPORT, FOREIGN_EXCHANGE_RESERVE, US_INDUSTRY_PRODUCTION,
             EURO_INDUSTRY_PRODUCTION, KO_INDUSTRY_PRODUCTION]
