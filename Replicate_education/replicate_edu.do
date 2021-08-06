clear all
set more off

import excel Seoul_including_distance.xlsx, firstrow clear

gen H1=0
replace H1=1 if 난방 == "개별난방"

gen H2=0 
replace H2=1 if 난방 == "지역난방"

gen H3=0
replace H3=1 if 난방 == "중앙난방"

gen T1=0
replace T1=1 if 구조 == "계단식"

gen T2=0
replace T2=1 if 구조 == "복도식"

gen T3=0
replace T3=1 if 구조 == "복합식"

gen G1=0
replace G1=1 if 지역구 == "강서구" 
replace G1=1 if 지역구 == "양천구" 
replace G1=1 if 지역구 == "구로구" 
replace G1=1 if 지역구 == "영등포구" 
replace G1=1 if 지역구 == "동작구" 
replace G1=1 if 지역구 == "관악구" 
replace G1=1 if 지역구 == "금천구" 
replace G1=1 if 지역구 == "서초구" 
replace G1=1 if 지역구 == "강남구" 
replace G1=1 if 지역구 == "송파구" 
replace G1=1 if 지역구 == "강동구"

export excel using seoul_plus_dummy.xlsx, firstrow 

gen high = dist_high * 1000

gen D100=0
replace D100=1 if high < 100

gen D200=0
replace D200=1 if 100 < high & high < 200

gen D300=0
replace D300=1 if 200 < high & high < 300

gen D400=0
replace D400=1 if 300 < high & high < 400

gen D500=0
replace D500=1 if 400 < high & high < 500

gen D600=0
replace D600=1 if 500 < high & high < 600

gen D700=0
replace D700=1 if 600 < high & high < 700

gen D800=0
replace D800=1 if 700 < high & high < 800

gen D900=0
replace D900=1 if 800 < high & high < 900

gen D1000=0
replace D1000=1 if 900 < high & high < 1000

gen D1100=0
replace D1100=1 if 1000 < high & high < 1100

gen D1200=0
replace D1200=1 if 1100 < high & high < 1200

gen DOVER=0
replace DOVER=1 if 1200 < high

export excel using seoul_replicating_dummy.xlsx, firstrow(variables) 






