clear all
set more off

log using Regression_data.log, replace

********************************
********** 2017. 2Q ************
********************************
clear

import excel data/Seoul_20172Q.xlsx, firstrow clear


* 개별난방인 경우 더미변수 D1에 1의 값을 부여
gen D1 = 0
replace D1 =1 if 난방 == "개별난방"

* 지역난방인 경우 더미변수 D2에 1의 값을 부여
gen D2 = 0
replace D2=1 if 난방 == "지역난방"

* 중앙난방인 경우 더미변수 D3에 1의 값을 부여
gen D3 = 0
replace D3=1 if 난방 == "중앙난방"

* 계단식일 경우 더미변수 D4에 1의 값을 부여
gen D4 = 0
replace D4=1 if 구조 == "계단식"

* 복도식일 경우 더미변수 D5에 1의 값을 부여
gen D5 = 0
replace D5=1 if 구조 == "복도식"

* 복합식일 경우 더미변수 D6에 1의 값을 부여
gen D6 = 0
replace D6=1 if 구조 == "복합식"

* 연수를 조정해주기 
gen age = 연수 - 48

* 통계량 확인하기
global variable 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용면적 전용률 ///
방개수 화장실개수 층 D1 D2 D3 D4 D5 D6 

su $variable

* 현재 사용가능한 모든 변수를 활용하여 회귀분석
reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용면적 전용률 방개수 화장실개수 층 D1 D2 D3 ///
D4 D5 D6 

* 전용면적 제외, 더미변수 D1와 D4 제외
reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6 

reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6  ,r

outreg2 using data/table.xls, replace se label dec(1)

* 종속변수에 log를 취하여 분석
gen ln_price = ln(거래금액)

reg ln_price age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6 ,r
outreg2 using data/table.xls, append se label dec(2)


export excel using 2017_2Q_data.xlsx, replace

********************************
********** 2020. 4Q ************
********************************
clear

import excel data/Seoul_20204Q.xlsx, firstrow clear


* 개별난방인 경우 더미변수 D1에 1의 값을 부여
gen D1 = 0
replace D1 =1 if 난방 == "개별난방"

* 지역난방인 경우 더미변수 D2에 1의 값을 부여
gen D2 = 0
replace D2=1 if 난방 == "지역난방"

* 중앙난방인 경우 더미변수 D3에 1의 값을 부여
gen D3 = 0
replace D3=1 if 난방 == "중앙난방"

* 계단식일 경우 더미변수 D4에 1의 값을 부여
gen D4 = 0
replace D4=1 if 구조 == "계단식"

* 복도식일 경우 더미변수 D5에 1의 값을 부여
gen D5 = 0
replace D5=1 if 구조 == "복도식"

* 복합식일 경우 더미변수 D6에 1의 값을 부여
gen D6 = 0
replace D6=1 if 구조 == "복합식"

* 연수를 조정해주기 
gen age = 연수 - 6

* 통계량 확인하기
global variable 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용면적 전용률 ///
방개수 화장실개수 층 D1 D2 D3 D4 D5 D6 

su $variable

* 현재 사용가능한 모든 변수를 활용하여 회귀분석
reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용면적 전용률 방개수 화장실개수 층 D1 D2 D3 ///
D4 D5 D6 

* 전용면적 제외, 더미변수 D3와 D6 제외
reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6 

* 종속변수에 log를 취하여 분석
gen ln_price = ln(거래금액)


reg 거래금액 age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6  ,r

outreg2 using data/table.xls, append se label dec(3)

reg ln_price age 세대수 주차대수_세대 용적률 건폐율 전용률 방개수 화장실개수 층 D2 D3 ///
D5 D6 ,r
outreg2 using data/table.xls, append se label dec(4)

export excel using data/2020_4Q_data.xlsx, replace

log close
