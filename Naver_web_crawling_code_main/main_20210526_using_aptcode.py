# 2021-05-26
# 해당 코드의 목적은 작업의 효율성과 가독성을 높이기 위함입니다.
# Chapter 1: crawling using apt_code
# 목적 : apt code 를 활용하여 아파트 정보 크롤링

# import packages
from selenium import webdriver
import time
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import numpy as np
from urllib.parse import urlparse  # 출처: https://datamasters.co.kr/67 [데이터마스터]
from datetime import datetime  # 코드 내에 타이머를 사용하면 여러모로 편리합니다.


########################################################################################################################
# 함수 선언

# 함수 1) 단지정보 호출
def get_apt_info():
    apt_name_selector = "#complexTitle"
    apt_name.append(chrome.find_element_by_css_selector(apt_name_selector).text)
    number_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(1) > td:nth-child(2)"
    number.append(chrome.find_element_by_css_selector(number_selector).text)
    floor_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(1) > td:nth-child(4)"
    floor.append(chrome.find_element_by_css_selector(floor_selector).text)
    confirm_date_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(2) > " \
                            "td:nth-child(2) "
    confirm_date.append(chrome.find_element_by_css_selector(confirm_date_selector).text)
    car_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(2) > td:nth-child(4)"
    car.append(chrome.find_element_by_css_selector(car_selector).text)
    FAR_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(3) > td:nth-child(2)"
    FAR.append(chrome.find_element_by_css_selector(FAR_selector).text)
    BC_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(3) > td:nth-child(4)"
    BC.append(chrome.find_element_by_css_selector(BC_selector).text)
    con_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(4) > td"
    con.append(chrome.find_element_by_css_selector(con_selector).text)
    heat_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(5) > td"
    heat.append(chrome.find_element_by_css_selector(heat_selector).text)


'''
네이버 부동산을 통해 얻을 수 있는 단지정보의 종류는 
'아파트 이름', '세대수', '저층 / 고층', '입주승인일', 
'주차대수 (총, 세대당)', 'FAR', 'BC', '건설사', '난방방식' 등이다.
'''


# 함수 2) url 정보 추출
def get_url_info():
    current_url = chrome.current_url  # url 확인
    df_url = pd.DataFrame([urlparse(current_url)])

    path = df_url.loc[0]['path']
    code.append(path.split('/')[2])  # code 에 '아파트코드' 담기

    query = df_url.loc[0]['query']
    check = query.split('=')[1]
    lat.append(check.split(',')[0])
    long.append(check.split(',')[1])  # lat, long에 각각 위도와 경도 담기


'''
각 아파트의 url 을 통해서 얻을 수 있는 정보는
해당 아파트의 '아파트 코드' 와 '위도', '경도' 이다.  
'''


# 함수 3) nan 값 입력
def input_nan_if_null():
    apt_name.append(np.nan)
    number.append(np.nan)
    floor.append(np.nan)
    confirm_date.append(np.nan)
    car.append(np.nan)
    FAR.append(np.nan)
    BC.append(np.nan)
    con.append(np.nan)
    heat.append(np.nan)
    code.append(np.nan)
    lat.append(np.nan)
    long.append(np.nan)


'''
함수 3의 목적은 input data 를 입력했을때
다음과 같은 이유로 확인되지 않는 아파트의 정보를
nan 값으로 처리하여, 다음단계로 넘어가도록 하기 위함이다.

오류의 원인
1. 한자어 포함, 2. 유사한 이름의 아파트 종류가 여러개 있을 경우 etc
'''


# 함수 4) 면적 유형별 정보 추출
def input_value_in_vars(type_capacity, area, room, toilet, n_this_area, structure, i):
    try:
        if i == 0:
            type_capacity_selector = "#tab0 > span"
            type_capacity.append(chrome.find_element_by_css_selector(type_capacity_selector).text)

            area_selector = "#tabpanel > table > tbody > tr:nth-child(1) > td"
            area.append(chrome.find_element_by_css_selector(area_selector).text)

            rt_selector = "#tabpanel > table > tbody > tr:nth-child(2) > td"  # 방 개수와 화장실 개수
            rt = chrome.find_element_by_css_selector(rt_selector).text
            room.append(rt.split('/')[0])
            toilet.append(rt.split('/')[1])

            n_this_area_selector = "#tabpanel > table > tbody > tr:nth-child(3) > td"
            n_this_area.append(chrome.find_element_by_css_selector(n_this_area_selector).text)

            structure_selector = "#tabpanel > table > tbody > tr:nth-child(4) > td"
            structure.append(chrome.find_element_by_css_selector(structure_selector).text)

            time.sleep(1)

        elif i == 7:
            down_scroll = "#detailContents1 > div.detail_box--floor_plan > div.detail_sorting_tabs > div > " \
                          "div.btn_moretab_box > button "
            chrome.find_element_by_css_selector(down_scroll).click()
            time.sleep(1)

            n = str(i)
            num_capacity = "#tab" + n + "> span"
            chrome.find_element_by_css_selector(num_capacity).click()

            type_capacity.append(chrome.find_element_by_css_selector(num_capacity).text)

            area_selector = "#tabpanel > table > tbody > tr:nth-child(1) > td"
            area.append(chrome.find_element_by_css_selector(area_selector).text)

            rt_selector = "#tabpanel > table > tbody > tr:nth-child(2) > td"  # 방 개수와 화장실 개수
            rt = chrome.find_element_by_css_selector(rt_selector).text
            room.append(rt.split('/')[0])
            toilet.append(rt.split('/')[1])

            n_this_area_selector = "#tabpanel > table > tbody > tr:nth-child(3) > td"
            n_this_area.append(chrome.find_element_by_css_selector(n_this_area_selector).text)

            structure_selector = "#tabpanel > table > tbody > tr:nth-child(4) > td"
            structure.append(chrome.find_element_by_css_selector(structure_selector).text)

            time.sleep(1)


        else:
            n = str(i)
            num_capacity = "#tab" + n + "> span"
            chrome.find_element_by_css_selector(num_capacity).click()

            type_capacity.append(chrome.find_element_by_css_selector(num_capacity).text)

            area_selector = "#tabpanel > table > tbody > tr:nth-child(1) > td"
            area.append(chrome.find_element_by_css_selector(area_selector).text)

            rt_selector = "#tabpanel > table > tbody > tr:nth-child(2) > td"  # 방 개수와 화장실 개수
            rt = chrome.find_element_by_css_selector(rt_selector).text
            room.append(rt.split('/')[0])
            toilet.append(rt.split('/')[1])

            n_this_area_selector = "#tabpanel > table > tbody > tr:nth-child(3) > td"
            n_this_area.append(chrome.find_element_by_css_selector(n_this_area_selector).text)

            structure_selector = "#tabpanel > table > tbody > tr:nth-child(4) > td"
            structure.append(chrome.find_element_by_css_selector(structure_selector).text)

            time.sleep(1)

    except Exception as ex:
        type_capacity.append(np.nan)
        area.append(np.nan)
        room.append(np.nan)
        toilet.append(np.nan)
        n_this_area.append(np.nan)
        structure.append(np.nan)
        time.sleep(1)


'''
함수 4의 목적은 각 면적 유형별 정보를 포착해내기 위함이다.
우선 면적 유형별로 확인할 수 있는 정보는 
'면적 유형의 이름', '공급면적/ 전용면적', '방 개수', '화장실 개수', '해당 면적 세대수', '구조' 이며

각 면적 유형에 해당하는 버튼을 클릭해야 해당 면적에 대한 정보를 확인할 수 있으므로 
함수 상에 클릭 기능을 추가하였다. 특히 7번째 면적 이후에는 화살표 버튼을 클릭해야
8번째 면적 유형에 대한 정보를 확인할 수 있으므로, 화살표를 누르는 기능 또한 함수에 추가하였다.

1차적인 목표는 각 아파트 단지별로 10개의 면적유형 정보를 확보하는 것인데, 
단지의 면적 유형이 10개 미만인 아파트 또한 많기 때문에 다음으로 넘어가기 위한 목적으로
try-except 구문을 사용하여 예외처리를 진행하였다. 
'''


# 함수 5) 면적유형별 정보를 1~10 리스트에 append 하기
def get_capacity_info():
    input_value_in_vars(type_capacity1, area1, room1, toilet1, n_this_area1, structure1, i=0)
    input_value_in_vars(type_capacity2, area2, room2, toilet2, n_this_area2, structure2, i=1)
    input_value_in_vars(type_capacity3, area3, room3, toilet3, n_this_area3, structure3, i=2)
    input_value_in_vars(type_capacity4, area4, room4, toilet4, n_this_area4, structure4, i=3)
    input_value_in_vars(type_capacity5, area5, room5, toilet5, n_this_area5, structure5, i=4)
    input_value_in_vars(type_capacity6, area6, room6, toilet6, n_this_area6, structure6, i=5)
    input_value_in_vars(type_capacity7, area7, room7, toilet7, n_this_area7, structure7, i=6)
    input_value_in_vars(type_capacity8, area8, room8, toilet8, n_this_area8, structure8, i=7)
    input_value_in_vars(type_capacity9, area9, room9, toilet9, n_this_area9, structure9, i=8)
    input_value_in_vars(type_capacity10, area10, room10, toilet10, n_this_area10, structure10, i=9)
    input_value_in_vars(type_capacity11, area11, room11, toilet11, n_this_area11, structure11, i=10)
    input_value_in_vars(type_capacity12, area12, room12, toilet12, n_this_area12, structure12, i=11)
    input_value_in_vars(type_capacity13, area13, room13, toilet13, n_this_area13, structure13, i=12)
    input_value_in_vars(type_capacity14, area14, room14, toilet14, n_this_area14, structure14, i=13)
    input_value_in_vars(type_capacity15, area15, room15, toilet15, n_this_area15, structure15, i=14)
    input_value_in_vars(type_capacity16, area16, room16, toilet16, n_this_area16, structure16, i=15)
    input_value_in_vars(type_capacity17, area17, room17, toilet17, n_this_area17, structure17, i=16)
    input_value_in_vars(type_capacity18, area18, room18, toilet18, n_this_area18, structure18, i=17)
    input_value_in_vars(type_capacity19, area19, room19, toilet19, n_this_area19, structure19, i=18)
    input_value_in_vars(type_capacity20, area20, room20, toilet20, n_this_area20, structure20, i=19)


'''
함수 5의 목적은 단지별 10개의 면적 유형 정보를 확보하는 것이다.
직관적인 이해를 위해 함수 4를 10개 늘려붙이는 방식으로 함수를 새로 만들었다.
'''


# 함수 6) 크롤링한 data DataFrame 에 append 하기

def append_to_df():
    df_code['Apt_name'] = apt_name
    df_code['number'] = number
    df_code['floor'] = floor
    df_code['confirm_date'] = confirm_date
    df_code['car'] = car
    df_code['FAR'] = FAR
    df_code['BC'] = BC
    df_code['con'] = con
    df_code['heat'] = heat
    df_code['code'] = code
    df_code['lat'] = lat
    df_code['long'] = long

    df_code['type_capacity1'] = type_capacity1
    df_code['area1'] = area1
    df_code['room1'] = room1
    df_code['toilet1'] = toilet1
    df_code['structure1'] = structure1
    df_code['n_this_area1'] = n_this_area1

    df_code['type_capacity2'] = type_capacity2
    df_code['area2'] = area2
    df_code['room2'] = room2
    df_code['toilet2'] = toilet2
    df_code['structure2'] = structure2
    df_code['n_this_area2'] = n_this_area2

    df_code['type_capacity3'] = type_capacity3
    df_code['area3'] = area3
    df_code['room3'] = room3
    df_code['toilet3'] = toilet3
    df_code['structure3'] = structure3
    df_code['n_this_area3'] = n_this_area3

    df_code['type_capacity4'] = type_capacity4
    df_code['area4'] = area4
    df_code['room4'] = room4
    df_code['toilet4'] = toilet4
    df_code['structure4'] = structure4
    df_code['n_this_area4'] = n_this_area4

    df_code['type_capacity5'] = type_capacity5
    df_code['area5'] = area5
    df_code['room5'] = room5
    df_code['toilet5'] = toilet5
    df_code['structure5'] = structure5
    df_code['n_this_area5'] = n_this_area5

    df_code['type_capacity6'] = type_capacity6
    df_code['area6'] = area6
    df_code['room6'] = room6
    df_code['toilet6'] = toilet6
    df_code['structure6'] = structure6
    df_code['n_this_area6'] = n_this_area6

    df_code['type_capacity7'] = type_capacity7
    df_code['area7'] = area7
    df_code['room7'] = room7
    df_code['toilet7'] = toilet7
    df_code['structure7'] = structure7
    df_code['n_this_area7'] = n_this_area7

    df_code['type_capacity8'] = type_capacity8
    df_code['area8'] = area8
    df_code['room8'] = room8
    df_code['toilet8'] = toilet8
    df_code['structure8'] = structure8
    df_code['n_this_area8'] = n_this_area8

    df_code['type_capacity9'] = type_capacity9
    df_code['area9'] = area9
    df_code['room9'] = room9
    df_code['toilet9'] = toilet9
    df_code['structure9'] = structure9
    df_code['n_this_area9'] = n_this_area9

    df_code['type_capacity10'] = type_capacity10
    df_code['area10'] = area10
    df_code['room10'] = room10
    df_code['toilet10'] = toilet10
    df_code['structure10'] = structure10
    df_code['n_this_area10'] = n_this_area10

    df_code['type_capacity11'] = type_capacity11
    df_code['area11'] = area11
    df_code['room11'] = room11
    df_code['toilet11'] = toilet11
    df_code['structure11'] = structure11
    df_code['n_this_area11'] = n_this_area11

    df_code['type_capacity12'] = type_capacity12
    df_code['area12'] = area12
    df_code['room12'] = room12
    df_code['toilet12'] = toilet12
    df_code['structure12'] = structure12
    df_code['n_this_area12'] = n_this_area12

    df_code['type_capacity13'] = type_capacity13
    df_code['area13'] = area13
    df_code['room13'] = room13
    df_code['toilet13'] = toilet13
    df_code['structure13'] = structure13
    df_code['n_this_area13'] = n_this_area13

    df_code['type_capacity14'] = type_capacity14
    df_code['area14'] = area14
    df_code['room14'] = room14
    df_code['toilet14'] = toilet14
    df_code['structure14'] = structure14
    df_code['n_this_area14'] = n_this_area14

    df_code['type_capacity15'] = type_capacity15
    df_code['area15'] = area15
    df_code['room15'] = room15
    df_code['toilet15'] = toilet15
    df_code['structure15'] = structure15
    df_code['n_this_area15'] = n_this_area15

    df_code['type_capacity16'] = type_capacity16
    df_code['area16'] = area16
    df_code['room16'] = room16
    df_code['toilet16'] = toilet16
    df_code['structure16'] = structure16
    df_code['n_this_area16'] = n_this_area16

    df_code['type_capacity17'] = type_capacity17
    df_code['area17'] = area17
    df_code['room17'] = room17
    df_code['toilet17'] = toilet17
    df_code['structure17'] = structure17
    df_code['n_this_area17'] = n_this_area17

    df_code['type_capacity18'] = type_capacity18
    df_code['area18'] = area18
    df_code['room18'] = room18
    df_code['toilet18'] = toilet18
    df_code['structure18'] = structure18
    df_code['n_this_area18'] = n_this_area18

    df_code['type_capacity19'] = type_capacity19
    df_code['area19'] = area19
    df_code['room19'] = room19
    df_code['toilet19'] = toilet19
    df_code['structure19'] = structure19
    df_code['n_this_area19'] = n_this_area19

    df_code['type_capacity20'] = type_capacity20
    df_code['area20'] = area20
    df_code['room20'] = room20
    df_code['toilet20'] = toilet20
    df_code['structure20'] = structure20
    df_code['n_this_area20'] = n_this_area20


'''
함수 6의 경우 사전에 선언된 리스트들을 데이터프레임에 편입시키는 것을 목적으로 한다.
'''


def check_length():
    print('apt_name: ', len(apt_name))
    print('number: ', len(number))
    print('floor: ', len(floor))
    print('confirm_date: ', len(confirm_date))
    print('car: ', len(car))
    print('FAR: ', len(FAR))
    print('BC: ', len(BC))
    print('con: ', len(con))
    print('heat: ', len(heat))
    print('lat: ', len(lat))
    print('long: ', len(long))
    print('code: ', len(code))
    print('type_capacity1: ', len(type_capacity1))
    print('area1: ', len(area1))
    print('room1: ', len(room1))
    print('toilet1: ', len(toilet1))
    print('structure1: ', len(structure1))
    print('n_this_area1: ', len(n_this_area1))
    print('type_capacity2: ', len(type_capacity2))
    print('area2: ', len(area2))
    print('room2: ', len(room2))
    print('toilet2: ', len(toilet2))
    print('structure2: ', len(structure2))
    print('n_this_area2: ', len(n_this_area2))
    print('type_capacity3: ', len(type_capacity3))
    print('area3: ', len(area3))
    print('room3: ', len(room3))
    print('toilet3: ', len(toilet3))
    print('structure3: ', len(structure3))
    print('n_this_area3: ', len(n_this_area3))
    print('type_capacity4: ', len(type_capacity4))
    print('area4: ', len(area4))
    print('room4: ', len(room4))
    print('toilet4: ', len(toilet4))
    print('structure4: ', len(structure4))
    print('n_this_area4: ', len(n_this_area4))
    print('type_capacity5: ', len(type_capacity5))
    print('area5: ', len(area5))
    print('room5: ', len(room5))
    print('toilet5: ', len(toilet5))
    print('structure5: ', len(structure5))
    print('n_this_area5: ', len(n_this_area5))
    print('type_capacity6: ', len(type_capacity6))
    print('area6: ', len(area6))
    print('room6: ', len(room6))
    print('toilet6: ', len(toilet6))
    print('structure6: ', len(structure6))
    print('n_this_area6: ', len(n_this_area6))
    print('type_capacity7: ', len(type_capacity7))
    print('area7: ', len(area7))
    print('room7: ', len(room7))
    print('toilet7: ', len(toilet7))
    print('structure7: ', len(structure7))
    print('n_this_area7: ', len(n_this_area7))
    print('type_capacity8: ', len(type_capacity8))
    print('area8: ', len(area8))
    print('room8: ', len(room8))
    print('toilet8: ', len(toilet8))
    print('structure8: ', len(structure8))
    print('n_this_area8: ', len(n_this_area8))
    print('type_capacity9: ', len(type_capacity9))
    print('area9: ', len(area9))
    print('room9: ', len(room9))
    print('toilet9: ', len(toilet9))
    print('structure9: ', len(structure9))
    print('n_this_area9: ', len(n_this_area9))
    print('type_capacity10: ', len(type_capacity10))
    print('area10: ', len(area10))
    print('room10: ', len(room10))
    print('toilet10: ', len(toilet10))
    print('structure10: ', len(structure10))
    print('n_this_area10: ', len(n_this_area10))


'''
간혹 Apt name 리스트에서 다른 항목의 길이와 length 가 다른 문제가 발생한다.
만약 append 가 제대로 이뤄지지 않을 경우, 문제가 되는 항목을 찾아야하므로 해당 함수를 통해
어떤 리스트의 길이가 다른 리스트와 상응하지 않는지 확인할 필요가 있다.
'''


# 리스트 선언

# 리스트 타입 1) 단지 정보
apt_name = []  # 아파트 이름; input 과 output 이 제대로 일치하는지 확인하기 위함
number = []  # 세대수
floor = []  # 저/최고층
confirm_date = []  # 사용승인일
car = []  # 주차대수
FAR = []  # 용적률 (Floor Area Ratio)
BC = []  # 건폐율 (Building Coverage)
con = []  # 건설사
heat = []  # 난방 / 난방방식
lat = []  # 위도
long = []  # 경도
code = []  # 아파트 코드

# 리스트 타입 2) 면적 유형별 정보
type_capacity1 = []  # 면적 유형의 이름 ex) 86A㎡
area1 = []  # 면적 : 공급/전용(전용률)
room1 = []  # 방 갯수
toilet1 = []  # 화장실 개수
structure1 = []  # 현관구조
n_this_area1 = []  # 해당면적 세대수

type_capacity2 = []
area2 = []
room2 = []
toilet2 = []
structure2 = []
n_this_area2 = []

type_capacity3 = []
area3 = []
room3 = []
toilet3 = []
structure3 = []
n_this_area3 = []

type_capacity4 = []
area4 = []
room4 = []
toilet4 = []
structure4 = []
n_this_area4 = []

type_capacity5 = []
area5 = []
room5 = []
toilet5 = []
structure5 = []
n_this_area5 = []

type_capacity6 = []
area6 = []
room6 = []
toilet6 = []
structure6 = []
n_this_area6 = []

type_capacity7 = []
area7 = []
room7 = []
toilet7 = []
structure7 = []
n_this_area7 = []

type_capacity8 = []
area8 = []
room8 = []
toilet8 = []
structure8 = []
n_this_area8 = []

type_capacity9 = []
area9 = []
room9 = []
toilet9 = []
structure9 = []
n_this_area9 = []

type_capacity10 = []
area10 = []
room10 = []
toilet10 = []
structure10 = []
n_this_area10 = []

type_capacity11 = []
area11 = []
room11 = []
toilet11 = []
structure11 = []
n_this_area11 = []

type_capacity12 = []
area12 = []
room12 = []
toilet12 = []
structure12 = []
n_this_area12 = []

type_capacity13 = []
area13 = []
room13 = []
toilet13 = []
structure13 = []
n_this_area13 = []

type_capacity14 = []
area14 = []
room14 = []
toilet14 = []
structure14 = []
n_this_area14 = []

type_capacity15 = []
area15 = []
room15 = []
toilet15 = []
structure15 = []
n_this_area15 = []

type_capacity16 = []
area16 = []
room16 = []
toilet16 = []
structure16 = []
n_this_area16 = []

type_capacity17 = []
area17 = []
room17 = []
toilet17 = []
structure17 = []
n_this_area17 = []

type_capacity18 = []
area18 = []
room18 = []
toilet18 = []
structure18 = []
n_this_area18 = []

type_capacity19 = []
area19 = []
room19 = []
toilet19 = []
structure19 = []
n_this_area19 = []

type_capacity20 = []
area20 = []
room20 = []
toilet20 = []
structure20 = []
n_this_area20 = []


########################################################################################################################
# web_scraping
df_code = pd.read_excel('etc/empty.xlsx')

#n = 1

#code_len = range((n - 1) * 10000 + 1, 10000 * n + 1)

code_len = range(133, 135)

chrome = webdriver.Chrome('chromedriver.exe')

time_start = datetime.now()  # StopWatch: 코드 시작
print("Procedure started at: " + str(time_start))

for i in code_len:
    apt = str(i)
    try:
        chrome.get('https://new.land.naver.com/complexes/' + apt)
        time.sleep(2)

        city_name = chrome.find_element_by_css_selector('#region_filter > div > a > span:nth-child(2)')
        con_type_name = chrome.find_element_by_css_selector('#summaryInfo > div.complex_title > span')

        if city_name.text == '서울시':
            if con_type_name.text == '아파트':
                link = chrome.find_element_by_css_selector(
                    '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
                link.click()  # '단지정보' 클릭

                time.sleep(1)

                get_apt_info()  # 함수 1 사용
                get_url_info()  # 함수 2 사용
                get_capacity_info()

                time.sleep(1)

            elif con_type_name.text == '주상복합':
                link = chrome.find_element_by_css_selector(
                    '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
                link.click()  # '단지정보' 클릭

                time.sleep(1)

                get_apt_info()  # 함수 1 사용
                get_url_info()  # 함수 2 사용
                get_capacity_info()

                time.sleep(1)

            else:
                input_nan_if_null()  # 원하는 정보를 얻지 못했으므로 전체 nan 값 출력, 함수 3 사용
                get_capacity_info()  # 입력값에 해당하는 정보가 없는 상황에서 자동으로 nan 값 출력

    except:
        input_nan_if_null()  # 원하는 정보를 얻지 못했으므로 전체 nan 값 출력, 함수 3 사용
        get_capacity_info()  # 입력값에 해당하는 정보가 없는 상황에서 자동으로 nan 값 출력

time_end = datetime.now()  # StopWatch: 코드 종료
print("Procedure finished at: " + str(time_end))
print("Elapsed (in this Procedure): " + str(time_end - time_start))  # 스크래핑 종료

check_length()  # 함수 7 사용, 각 항목의 length 확인하기
append_to_df()  # dataframe 에 모든 리스트 append 시키기

# 문제가 발생한 부분 처리해주기

# df_apt_name = pd.DataFrame(apt_name)
# df_check = pd.concat([df_code, df_apt_name], axis=1)
# df_check
# print(apt_name[?])
# apt_name.pop(?)

'''
append 가 되지 않는 문제가 발생할 경우
ex) apt_name 의 length 가 맞지 않아 데이터 프레임이 합쳐지지 않는 상황
다른 length 와 일치하지 않는 부분이 어디인지 확인하여 drop 시킬 필요가 있다. 
'''


df_code

df_apt = df_code.dropna(subset=['Apt_name'])

df_apt.to_excel('Naver_web_crawling_code_main/' + str(n) + '.xlsx', sheet_name='1', index=False)  # 엑셀로 내보내기
########################################################################################################################

