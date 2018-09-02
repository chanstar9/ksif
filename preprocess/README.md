# 데이터 전처리 방법
## 소스 데이터 다운로드
(2018년 9월 1일 현재 기준)
### 파일명
180831.xlsx
### company sheet
- Code
    - KSE+KOSDAQ
    - All companies
    - Fiscal Month
    - Ex. Pref.S
    - List => ALL
    - Company
- Calendar
    - 자료기간: 1999-12-01 ~ 2018-08-31 (선택)
    - 자료주기: 월간
    - 통화: KRW
    - 금액: Default
    - 비영업일: Previous
    - 주말포함: ALL
- Item
    - 최신 아이템 항목 즐겨찾기
### benchmark sheet
- Code
    - 최신 benchmark code 즐겨찾기
- Calendar
    - 자료기간: 1999-12-01 ~ 2018-08-31 (선택)
    - 자료주기: 월간
    - 통화: KRW
    - 금액: Default
    - 비영업일: Previous
    - 주말포함: ALL
- Item
    - 최신 아이템 항목 즐겨찾기

## 데이터무결성 검증 1
0. 모든 날짜들이 매월 말일인지 확인
0. 2018년 8월 31일 데이터 중 종가가 없는 회사코드와 회사명을 복사해
상장폐지 스프레드시트의 180831 시트에 붙여넣고 unfiltered column이 TRUE인
회사들을 filter한다.
0. 위 회사들을 검색하여 상장폐지/합병 여부를 확인한다.

## 전처리 코드
ksif/preprocess/core/__init__.py 파일을 실행하되, parameter로 180831 입력

## 데이터업로드
0. 위 코드의 결과로 저장된 180831_company.csv와 180831_benchmark.csv를 Dropbox에 업로드한다.
0. 두 파일의 URL을 KoreaStockDataUrl 스프레드시트에 날짜와 함께 저장한다.
