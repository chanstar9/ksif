# -*- coding: utf-8 -*-
"""
:Author: Jaekyoung Kim
         Chankyu Choi
:Date: 2018. 7. 18.
"""
import itertools

# Base information
CODE = 'code'
NAME = 'name'
DATE = 'date'
RET_1 = 'return_1'  # 1일 수익률
RET_5 = 'return_5'  # 5일 수익률
RET_20 = 'return_20'  # 20일 수익률
RET_60 = 'return_60'  # 60일 수익률
RET_120 = 'return_120'  # 120일 수익률
ADJ_OPEN_P = 'adj_open_p'  # 수정시가
ADJ_HIGH_P = 'adj_high_p'  # 수정고가
ADJ_LOW_P = 'adj_low_p'  # 수정고가
ADJ_CLOSE_P = 'adj_close_p'  # 수정종가
ADJ_TRADING_VOLUME = 'adj_trading_volume'  # 수정거래량
MKTCAP = 'mktcap'  # 시가총액
OS_SHARES = 'os_shares'  # 유통 주식수 (보통)(주)
BASE_INFORMATION = [CODE, NAME, DATE, RET_1, RET_5, RET_1, RET_60, RET_120, ADJ_OPEN_P, ADJ_HIGH_P, ADJ_LOW_P,
                    ADJ_CLOSE_P, MKTCAP]

# Fundamental
REVTQ = 'revtq'  # 매출액 분기별 Revenue total quarterly
REVT12 = 'revt12'  # 매출액  4분기 누적
GPQ = 'gpq'  # 매출총이익 분기별 Gross profit quartelry
GP12 = 'gp12'  # 매출총이익 4분기 누적
OPQ = 'opq'  # 영업이익 분기별 Operating Profit quarterly
OP12 = 'op12'  # 영업이익 4분기 누적
NIQ = 'niq'  # 순이익 분기별 Net income quarterly
NI12 = 'ni12'  # 순이익 4분기 누적
ATQ = 'atq'  # 총자산 분기별 Asset total quarterly
ATQ_MEAN4 = 'atq_mean4'  # 총자산 4분기 평균
SEQ = 'seq'  # 자본 Shareholder's equity quarterly
SEQ_MEAN4 = 'seq_mean4'  # 자본 4분기 평균
LTQ = 'ltq'  # 총부채 Total liabilities quarterly

CF_DEP = 'cf_dep'  # 현금흐름 감가상각비
CFOQ = 'cfoq'  # 현금흐름 영업활동 분기별
CFO12 = 'cfo12'  # 현금흐름 영업활동 연간

A_TANG = 'a_tang'  # 유형자산 분기별 Tangible asset quarterly
A_TANG_MEAN12 = 'a_tang_mean12'  # 유형자산 4분기 누적
A_CUR = 'a_cur'  # 유동자산 분기별 Current asset quarterly
A_CUR_MEAN12 = 'a_cur_mean12'  # 유동자산 4분기 누적
L_CUR = 'l_cur'  # 유동부채 분기별 Current liability quarterly
L_CUR_MEAN12 = 'l_cur_mean12'  # 유동부채 4분기 누적

# Filter
EXCHANGE = 'exchange'  # 거래소
FN_GUIDE_SECTOR = 'fn_guide_sector'  # FN Guide 섹터
FN_GUIDE_INDUSTRY_GROUP_27 = 'fn_guide_industry_group_27'  # FN Guide 산업구분
KRX_SECTOR = 'krx_sector'  # 한국거래소 섹터
HOLDING = 'holding'  # 지주사 여부
IS_MANAGED = 'is_managed'  # 관리종목 여부
IS_SUSPENDED = 'is_suspended'  # 거래정지 여부
FILTERS = [EXCHANGE, FN_GUIDE_SECTOR, FN_GUIDE_INDUSTRY_GROUP_27, KRX_SECTOR, HOLDING, IS_MANAGED,
           IS_SUSPENDED]

# Value factors
PER = 'per'  # 주가수익률 Per Earnings Ratio
PBR = 'pbr'  # 주가순자산비율 Price to Book-value Ratio
PSR = 'psr'  # 주가매출비율 Price to Sales Ratio
PCR = 'pcr'  # 주가현금흐름비율 Price to Cash flow Ratio
PGPR = 'pgpr'  # 주가매출총이익비율 Price to Gross Profit Ratio
POPR = 'popr'  # 주가영업이익비율 Price to Operating Profit Ratio
EV_EBITDA = 'ev_ebitda'  # 시장가격/세금이자지급전이익
EBIT_EV = 'ebit_ev'  # 영업이익/시장가격
CF_EV = 'cf_ev'  # 영업현금흐름/시장가격
S_EV = 's_ev'  # 매출/시장가격
E_P = 'e_p'  # 1/PER
B_P = 'b_p'  # 1/PBR
C_P = 'c_p'  # 1/PCR
S_P = 's_p'  # 1/PSR
GP_P = 'gp_p'  # 1/PGPR
OP_P = 'op_p'  # 1/POPR
VALUE_FACTORS = [PER, PBR, PSR, PCR, PGPR, POPR, EV_EBITDA, EBIT_EV, CF_EV, S_EV, E_P, B_P, C_P, S_P, GP_P, OP_P]

# Profit factors
S_A = 's_a'  # 매출/자산 Sale over Assets
GP_A = 'gp_a'  # 매출총이익/자산 Gross Profit over Assets
OP_A = 'op_a'  # 영업이익/자산 EBIT over Assets
CF_A = 'cf_a'  # 영업활동으로 인한 현금흐름/자산 Cash Flow from operation over Assets
ROA = 'roa'  # 연간 순이익/자산 Return On Assets
ROE = 'roe'  # 연간 순이익/자본 Return On Equity
QROA = 'qroa'  # 분기간 순이익/자산
QROE = 'qroe'  # 분기간 순이익/자본
EBT_E = 'ebt_e'  # (순이익+세금)/자본
ROIC = 'roic'  # 투하자본수익률 Return On Invested Capital
GP_S = 'gp_s'  # 매출총이익/매출
DIVP = 'divp'  # 배당률 Dividend rate(12 month rolling)
PROFIT_FACTORS = [S_A, GP_A, OP_A, CF_A, ROA, ROE, QROA, QROE, EBT_E, ROIC, GP_S, DIVP]

# Growth factors
SALESQOQ = 'salesqoq'  # 분기간 매출 변화율
GPQOQ = 'gpqoq'  # 분기간 매출총이익 변화율
OPQOQ = 'opqoq'  # 분기간 영업이익 변화율
ROAQOQ = 'roaqoq'  # 분기간 ROA 변화율
ROAYOY = 'roayoy'  # 연간 ROA 변화율
GP_SYOY = 'gp_syoy'  # 연간 매출총이익/매출 변화율
GP_AYOY = 'gp_ayoy'  # 연간 매출총이익/자산 변화율
ASSETSYOY = 'assetsyoy'  # 연간 자산 변화율
ASSETSQOQ = 'assetsqoq'  # 분기간 자산 변화율
GROWTH_FACTORS = [SALESQOQ, GPQOQ, OPQOQ, ROAQOQ, ROAYOY, GP_SYOY, GP_AYOY, ASSETSYOY, ASSETSQOQ]

# Momentum factors
MOM120 = 'mom120'  # 120일 모멘텀
MOM60 = 'mom60'  # 60일 모멘텀
MOM20 = 'mom20'  # 20일 모멘텀
MOM5 = 'mom5'  # 5일 모멘텀
MOM1 = 'mom1'  # 1일 모멘텀
MOMENTUM_FACTORS = [MOM120, MOM60, MOM20, MOM5, MOM1]

# Safety factors
BETA_1D = 'beta_1d'  # 일일 베타
BETA_3M = 'beta_3m'  # 3개월 베타
BETA_5M = 'beta_5m'  # 5개월 베타
BETA_1W = 'beta_1w'  # 1주 베타
BETA_2W = 'beta_2w'  # 2주 베타
VOL_1D = 'vol_1d'  # 일일 변동성
VOL_3M = 'vol_3m'  # 3개월 변동성
VOL_5M = 'vol_5m'  # 5개월 변동성
VOL_1W = 'vol_1w'  # 1주 변동성
VOL_2W = 'vol_2w'  # 2주 변동성
LIQ_RATIO = 'liq_ratio'  # 유동비율
DEBT_RATIO = 'debt_ratio'  # 부채비율
EQUITY_RATIO = 'equity_ratio'  # 자본비율
SAFETY_FACTORS = [BETA_1D, BETA_1W, BETA_2W, BETA_3M, BETA_5M, VOL_1D, VOL_1W, VOL_2W, VOL_3M, VOL_5M, LIQ_RATIO,
                  DEBT_RATIO, EQUITY_RATIO]

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
FOREIGN_OWNERSHIP_RATIO = 'foreign_ownership_ratio'  # 외국인보유비중
SHORT_SALE_VOLUME_RATIO = 'short_sale_volume_ratio'  # 공매도거래비율
SHORT_SALE_BALANCE_RATIO = 'short_sale_balance_ratio'  # 공매도잔고비율
SHORT_SALE_BALANCE_MOM = 'short_sale_balance_mom'  # 월간 공매도잔고변화율
SHARE_LENDING_VOLUME_RATIO = 'share_lending_volume_ratio'  # 대차거래비율
SHARE_LENDING_BALANCE_RATIO = 'share_lending_balance_ratio'  # 대차잔고비율
SHARE_LENDING_BALANCE_MOM = 'share_lending_balance_mom'  # 월간 공매도잔고변화율
LIQUIDITY_FACTORS = [
    TRADING_VOLUME_RATIO, NET_PERSONAL_PURCHASE_RATIO, NET_INSTITUTIONAL_FOREIGN_PURCHASE_RATIO,
    NET_INSTITUTIONAL_PURCHASE_RATIO, NET_FINANCIAL_INVESTMENT_PURCHASE_RATIO, NET_INSURANCE_PURCHASE_RATIO,
    NET_TRUST_PURCHASE_RATIO, NET_PRIVATE_FUND_PURCHASE_RATIO, NET_BANK_PURCHASE_RATIO,
    NET_ETC_FINANCE_PURCHASE_RATIO, NET_PENSION_PURCHASE_RATIO, NET_NATIONAL_PURCHASE_RATIO,
    NET_ETC_CORPORATION_PURCHASE_RATIO, NET_FOREIGN_PURCHASE_RATIO, NET_REGISTERED_FOREIGN_PURCHASE_RATIO,
    NET_ETC_FOREIGN_PURCHASE_RATIO, FOREIGN_OWNERSHIP_RATIO, SHORT_SALE_VOLUME_RATIO, SHORT_SALE_BALANCE_RATIO,
    SHORT_SALE_BALANCE_MOM, SHARE_LENDING_VOLUME_RATIO, SHARE_LENDING_BALANCE_RATIO, SHARE_LENDING_BALANCE_MOM,
]

# Technical Indicator Factor
# average
PRICE_MA20 = 'price_ma20'  # 20일 가격 이동평균
PRICE_MA60 = 'price_ma60'  # 60일 가격 이동평균
TRADING_VOLUME_MA5 = 'trading_volume_ma5'  # 20일 거래량 이동평균
TRADING_VOLUME_MA20 = 'trading_volume_ma20'  # 20일 거래량 이동평균
# candle
DOJI_CANDLE = 'doji_candle'  # 도지형 캔들
HAMMER_CANDLE = 'hammer_candle'  # 망치형 캔들
BIG_BULL_CANDLE = 'big_bull_candle'  # 장대양봉
ACCUMULATION_CANDLE = 'accumulation_candle'  # 매집봉
# sub
BOLLINGER_UPPERBAND = 'bollinger_upperband'  # 볼린저밴드 상한선
BOLLINGER_MIDBAND = 'bollinger_midband'  # 볼린저밴드 중심선
BOLLINGER_LOWERBAND = 'bollinger_lowerband'  # 볼린저밴드 하한선
STOCHASTIC_SLOWK = 'stochastic_slowk'  # 스토케스틱 K
STOCHASTIC_SLOWD = 'stochastic_slowd'  # 스토케스틱 D
OBV = 'obv'  # OBV
DISPARITY = 'disparity'  # 이격도
TRIX = 'trix'  # trix
# pattern
GAP_RISE = 'gap_rise'  # 갭상승
GOLDEN_CROSS = 'golden_cross'  # 골든크로스
MORNING_STAR = 'morning_star'
MORNING_DOJI_STAR = 'morning_doji_star'
EVENING_STAR = 'evening_star'
EVENING_DOJI_STAR = 'evening_doji_star'
ABANDONED_BABY = 'abandoned_baby'
THREE_INSIDE_DOWN = 'three_inside_down'
THREE_OUTSIDE_DOWN = 'three_outside_down'
UPSIDE_GAP_TWO_CROWS = 'upside_gap_two_crows'
RISE_DIVERGENCE = 'rise_divergence'  # 상승 다이버젼스
DOUBLE_BOTTOM = 'double_bottom'  # 쌍바닥

TA_FACTOR = [PRICE_MA20, PRICE_MA60, TRADING_VOLUME_MA5, TRADING_VOLUME_MA20, DOJI_CANDLE, HAMMER_CANDLE,
             BIG_BULL_CANDLE, ACCUMULATION_CANDLE, BOLLINGER_UPPERBAND, BOLLINGER_MIDBAND, BOLLINGER_LOWERBAND,
             STOCHASTIC_SLOWK, STOCHASTIC_SLOWD, OBV, DISPARITY, TRIX, GAP_RISE, GOLDEN_CROSS, MORNING_STAR,
             MORNING_DOJI_STAR, EVENING_STAR, EVENING_DOJI_STAR, ABANDONED_BABY, THREE_INSIDE_DOWN, THREE_OUTSIDE_DOWN,
             UPSIDE_GAP_TWO_CROWS]

# Consensus Factor
CONSENSUS_MEAN = 'consensus_mean'
CONSENSUS_CHG = 'consensus_chg'
CONSENSUS_MAX = 'consensus_max'
CONSENSUS_MIN = 'consensus_min'
CONSENSUS_MID = 'consensus_mid'
CONSENSUS_CV = 'consensus_cv'
CONSENSUS_DIS = 'consensus_dis'
CONSENSUS_UP = 'consensus_up'
CONSENSUS_STAY = 'consensus_stay'
CONSENSUS_STD = 'consensus_std'
CONSENSUS_DOWN = 'consensus_down'
CONSENSUS_ADJ_CHG = 'consensus_adj_chg'

CONSENSUS_FACTOR = [CONSENSUS_MEAN, CONSENSUS_CHG, CONSENSUS_MAX, CONSENSUS_MIN, CONSENSUS_MID, CONSENSUS_CV,
                    CONSENSUS_DIS, CONSENSUS_UP, CONSENSUS_DOWN, CONSENSUS_STAY, CONSENSUS_STD, CONSENSUS_ADJ_CHG]

COMPANY_REFINED_FACTORS = list(
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
        # Technical Analysis factor
        TA_FACTOR,
        # Consensus Factor
        CONSENSUS_FACTOR
    )
)

# Macro factors
TERM_SPREAD_KOR = "term_spread_kor"  # 장단기 국채 금리차이 10 - 1, 한국 국채; 장기 경제 전망
TERM_SPREAD_US = "term_spread_us"  # 장단기 국채 금리차이 10 - 1, 미국 국채
CREDIT_SPREAD_KOR = "credit_spread_kor"  # 회사채 BBB- - AA- ; 신용위험도
LOG_USD2KRW = "log_usd2krw"  # 1달러 당 원화 가격의 로그
LOG_CHY2KRW = "log_chy2krw"  # 1위안 당 원화 가격의 로그
LOG_EURO2KRW = "log_euro2krw"  # 1유로 당 원화 가격의 로그
TED_SPREAD = "ted_spread"  # 리보금리 - 미국 국채 스프레드 (1개월물) ; 미국 역외 달러 조달의 위험성 ; 무역과 internal banking system의 안정성 지표
LOG_NYSE = "log_nyse"  # 뉴욕증권거래소 지수의 로그
LOG_NASDAQ = "log_nasdaq"  # 나스닥 거래소 지수의 로그
LOG_SEMI_CONDUCTOR = "log_semi_conductor"  # 반도체가격의 로그
LOG_DOLLAR_INDEX = "log_dollar_index"  # 달러 인덱스의 로그; 달러가 다른 통화대비 얼마나 강세인지 보여줌
LOG_OIL = "log_oil"  # 유가의 로그
LOG_EXPORT = "log_export"  # 한국의 수출량 로그
LOG_IMPORT = "log_import"  # 한국의 수입량 로그
LOG_FOREIGN_EXCHANGE_RESERVE = 'log_foreign_exchange_reserve'  # 한국의 외환보유고 로그
LOG_INDUSTRY_PRODUCTION_US = "log_industry_production_us"  # 미국의 산업생산 로그
LOG_INDUSTRY_PRODUCTION_EURO = "log_industry_production_euro"  # 유로지역의 산업생산 로그
LOG_INDUSTRY_PRODUCTION_KOR = "log_industry_production_kor"  # 한국의 산업생산 로그

MACRO_FACTORS = [
    TERM_SPREAD_KOR, TERM_SPREAD_US, CREDIT_SPREAD_KOR, LOG_USD2KRW, LOG_CHY2KRW, LOG_EURO2KRW, TED_SPREAD, LOG_NYSE,
    LOG_NASDAQ, LOG_SEMI_CONDUCTOR, LOG_DOLLAR_INDEX, LOG_OIL,
]

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
CD91 = 'CD 91일'

BENCHMARK_RET_1 = 'benchmark_return_1'
BENCHMARK_RET_5 = 'benchmark_return_5'
BENCHMARK_RET_20 = 'benchmark_return_20'
BENCHMARK_RET_60 = 'benchmark_return_60'
BENCHMARK_RET_120 = 'benchmark_return_120'

BENCHMARKS = [
    MKF_2000,
    KOSDAQ, KOSDAQ_LARGE, KOSDAQ_MIDDLE, KOSDAQ_SMALL,
    KOSPI, KOSPI_200, KOSPI_LARGE, KOSPI_MIDDLE, KOSPI_SMALL,
    TOTAL_LARGE, TOTAL_MIDDLE, TOTAL_SMALL,
    CD91,
]

# Factors
SMB = 'SMB'
HML = 'HML'
