*****************************************************
****************** 2013 1Q ~ 3Q *********************
*****************************************************

clear all
set more off

import excel Seoul_20131Q3Q.xlsx, firstrow clear

gen floor = 층^2
gen year = 연수^2

gen price = 거래금액*10000
gen lnprice = log(price)

gen perprice = 거래금액*10000 / 전용면적
gen perlnprice = log(perprice)

gen capacity = 전용면적
gen efficiency_rate = 전용률
gen room = 방개수
gen toilet = 화장실개수
gen FAR = 용적률
gen SCR = 건폐율
gen household = 세대수
gen per_parking = 주차대수_세대
gen const = 건설사


global individual efficiency_rate T2 T3 room toilet floor 
global common FAR SCR H2 H3 household per_parking const year
global district G1 dist_elem dist_middle dist_sub dist_park

global high D200 D300 D400 D500 D600 D700 D800 D900 D1000 D1100 D1200 DOVER


sum lnprice perlnprice $individual capacity $common $district $high 

reg lnprice $individual capacity $common $district $high, r
outreg2 using data/table.xls, replace se label dec(1)

reg perlnprice $individual $common $district $high ,r
outreg2 using data/table.xls, append se label dec(2)


*****************************************************
****************** 2020 1Q ~ 3Q *********************
*****************************************************

clear all
set more off

import excel Seoul_20201Q3Q.xlsx, firstrow clear

gen floor = 층^2
gen year = 연수^2

gen price = 거래금액*10000
gen lnprice = log(price)

gen perprice = 거래금액*10000 / 전용면적
gen perlnprice = log(perprice)

gen capacity = 전용면적
gen efficiency_rate = 전용률
gen room = 방개수
gen toilet = 화장실개수
gen FAR = 용적률
gen SCR = 건폐율
gen household = 세대수
gen per_parking = 주차대수_세대
gen const = 건설사


global individual efficiency_rate T2 T3 room toilet floor 
global common FAR SCR H2 H3 household per_parking const year
global district G1 dist_elem dist_middle dist_sub dist_park

global high D200 D300 D400 D500 D600 D700 D800 D900 D1000 D1100 D1200 DOVER


sum lnprice perlnprice $individual capacity $common $district $high 

reg lnprice $individual capacity $common $district $high, r
outreg2 using data/table.xls, append se label dec(1)

reg perlnprice $individual $common $district $high ,r
outreg2 using data/table.xls, append se label dec(2)