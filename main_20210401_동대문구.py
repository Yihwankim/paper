# 2021-04-01
# selenium을 이용한 크롤링 일반화 작업
# 면적별 정보 append
# 입력값과 출력값이 상응하는지 확인하기 위해 아파트 명을 dataframe에 추가
# 엑셀 시트를 하나의 dataframe으로 합쳐 최종적으로 구별 아파트 정보를 출력 및 저장

# HKim: PEP8 스타일 가이드를 가급적 준수하세요.
# 1. 패키지를 불러온 이후에는 두 줄 띄웁니다.
# 2. 클래스 및 함수 정의는 패키지 불러온 아래에 붙습니다. 이후 두 줄 띄웁니다.
# 3. 코멘트를 쓸 때에는 샵(#) 붙이고 한칸 띄웁니다.
# 4. 라인 안에서 코멘트를 쓸 때에는 코드 맨 뒤에 두칸 띄우고 # 를 시작합니다.


# Import Packages
from selenium import webdriver
import time
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import numpy as np
from urllib.parse import urlparse  # 출처: https://datamasters.co.kr/67 [데이터마스터]
from datetime import datetime  # HKim: 코드 내에 타이머를 사용하면 여러모로 편리합니다.


########################################################################################################################
# 함수 선언
# HKim: 클래스 및 함수 선언은 패키지 임포트 바로 아래에 있어야 합니다.

# 함수 선언 1: 단지정보 추출
def get_apt_info():
    apt_name_selector = "#complexTitle"
    apt_name.append(chrome.find_element_by_css_selector(apt_name_selector).text)
    number_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(1) > td:nth-child(2)"
    number.append(chrome.find_element_by_css_selector(number_selector).text)
    floor_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(1) > td:nth-child(4)"
    floor.append(chrome.find_element_by_css_selector(floor_selector).text)
    confirm_date_selector = "#detailContents1 > div.detail_box--complex > table > tbody > tr:nth-child(2) > td:nth-child(2)"
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


# 함수선언 2: url 정보 추출
# HKim: PEP8에서 함수 이름은 lowercase_underscore 를 사용합니다.
def get_url_info():
    current_url = chrome.current_url  # url 확인하기
    df_url = pd.DataFrame([urlparse(current_url)])

    path = df_url.loc[0]['path']
    code.append(path.split('/')[2])  # code에 아파트 코드 담기

    query = df_url.loc[0]['query']
    check = query.split('=')[1]
    lat.append(check.split(',')[0])
    long.append(check.split(',')[1])  # lat, long에 각각 위도와 경도 담기


# 함수선언 3: nan 값 입력
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


# 함수선언 4: 면적 정보 추출
def input_value_in_vars(area, room, toilet, n_this_area, structure, i):
    try:
        if i == 0:
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

            time.sleep(2)

        else:
            n = str(i)
            num_capacity = "#tab" + n + "> span"
            chrome.find_element_by_css_selector(num_capacity).click()

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

            time.sleep(2)

    except Exception as ex:
        area.append(np.nan)
        room.append(np.nan)
        toilet.append(np.nan)
        n_this_area.append(np.nan)
        structure.append(np.nan)
        time.sleep(1)


# 함수선언 5: 면적정보 1~10 리스트에 append 하기
def get_capacity_info():
    input_value_in_vars(area1, room1, toilet1, n_this_area1, structure1, i=0)
    input_value_in_vars(area2, room2, toilet2, n_this_area2, structure2, i=1)
    input_value_in_vars(area3, room3, toilet3, n_this_area3, structure3, i=2)
    input_value_in_vars(area4, room4, toilet4, n_this_area4, structure4, i=3)
    input_value_in_vars(area5, room5, toilet5, n_this_area5, structure5, i=4)
    input_value_in_vars(area6, room6, toilet6, n_this_area6, structure6, i=5)
    input_value_in_vars(area7, room7, toilet7, n_this_area7, structure7, i=6)
    input_value_in_vars(area8, room8, toilet8, n_this_area8, structure8, i=7)
    input_value_in_vars(area9, room9, toilet9, n_this_area9, structure9, i=8)
    input_value_in_vars(area10, room10, toilet10, n_this_area10, structure10, i=9)


# 함수선언 6: 크롤링한 data DataFrame 에 append 하기

def appending_to_df():
    df_dongdaemoongu['number'] = number
    df_dongdaemoongu['floor'] = floor
    df_dongdaemoongu['confirm_date'] = confirm_date
    df_dongdaemoongu['car'] = car
    df_dongdaemoongu['FAR'] = FAR
    df_dongdaemoongu['BC'] = BC
    df_dongdaemoongu['con'] = con
    df_dongdaemoongu['heat'] = heat
    df_dongdaemoongu['code'] = code
    df_dongdaemoongu['lat'] = lat
    df_dongdaemoongu['long'] = long

    df_dongdaemoongu['area1'] = area1
    df_dongdaemoongu['room1'] = room1
    df_dongdaemoongu['toilet1'] = toilet1
    df_dongdaemoongu['structure1'] = structure1
    df_dongdaemoongu['n_this_area1'] = n_this_area1

    df_dongdaemoongu['area2'] = area2
    df_dongdaemoongu['room2'] = room2
    df_dongdaemoongu['toilet2'] = toilet2
    df_dongdaemoongu['structure2'] = structure2
    df_dongdaemoongu['n_this_area2'] = n_this_area2

    df_dongdaemoongu['area3'] = area3
    df_dongdaemoongu['room3'] = room3
    df_dongdaemoongu['toilet3'] = toilet3
    df_dongdaemoongu['structure3'] = structure3
    df_dongdaemoongu['n_this_area3'] = n_this_area3

    df_dongdaemoongu['area4'] = area4
    df_dongdaemoongu['room4'] = room4
    df_dongdaemoongu['toilet4'] = toilet4
    df_dongdaemoongu['structure4'] = structure4
    df_dongdaemoongu['n_this_area4'] = n_this_area4

    df_dongdaemoongu['area5'] = area5
    df_dongdaemoongu['room5'] = room5
    df_dongdaemoongu['toilet5'] = toilet5
    df_dongdaemoongu['structure5'] = structure5
    df_dongdaemoongu['n_this_area5'] = n_this_area5

    df_dongdaemoongu['area6'] = area6
    df_dongdaemoongu['room6'] = room6
    df_dongdaemoongu['toilet6'] = toilet6
    df_dongdaemoongu['structure6'] = structure6
    df_dongdaemoongu['n_this_area6'] = n_this_area6

    df_dongdaemoongu['area7'] = area7
    df_dongdaemoongu['room7'] = room7
    df_dongdaemoongu['toilet7'] = toilet7
    df_dongdaemoongu['structure7'] = structure7
    df_dongdaemoongu['n_this_area7'] = n_this_area7

    df_dongdaemoongu['area8'] = area8
    df_dongdaemoongu['room8'] = room8
    df_dongdaemoongu['toilet8'] = toilet8
    df_dongdaemoongu['structure8'] = structure8
    df_dongdaemoongu['n_this_area8'] = n_this_area8

    df_dongdaemoongu['area9'] = area9
    df_dongdaemoongu['room9'] = room9
    df_dongdaemoongu['toilet9'] = toilet9
    df_dongdaemoongu['structure9'] = structure9
    df_dongdaemoongu['n_this_area9'] = n_this_area9

    df_dongdaemoongu['area10'] = area10
    df_dongdaemoongu['room10'] = room10
    df_dongdaemoongu['toilet10'] = toilet10
    df_dongdaemoongu['structure10'] = structure10
    df_dongdaemoongu['n_this_area10'] = n_this_area10


########################################################################################################################
# 엑셀값 출력
df_dongdaemoongu = pd.read_excel('Gangbuk/dongdaemoongu.xlsx', sheet_name='답십리동', header=0, skipfooter=0,
                                 usecols='C:D, G:H')

# (보류) df_dongdaemoongu = pd.read_excel('Gangbuk/dongdaemoongu.xlsx', sheet_name=None, header=0, skipfooter=0, usecols='C:D, G:H')


# 출력한 엑셀값 하나로 합치기
# (보류) df_dongdaemoongu = pd.concat(df_dongdaemoongu, ignore_index='Ture')

df_dongdaemoongu = df_dongdaemoongu.drop_duplicates(['아파트'], keep='first')
df_dongdaemoongu = df_dongdaemoongu.sort_values(by=['아파트'])
df_dongdaemoongu = df_dongdaemoongu.reset_index(drop='Ture')

df_name = df_dongdaemoongu[['읍면동', '아파트']]  # 여러 열을 추출하고 싶을때는 [[ 두개를 사용 ]]

df_name = df_name.astype('str')
se_name = df_name['읍면동'] + " " + df_name['아파트']

# 크롤링 정보를 담을 리스트 선언

# 1. 단지 정보 리스트
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

# 2. 면적별 정보 리스트
# 1)
area1 = []  # 면적 : 공급/전용(전용률)
room1 = []  # 방 갯수
toilet1 = []  # 화장실 개수
structure1 = []  # 현관구조
n_this_area1 = []  # 해당면적 세대수
# 2)
area2 = []
room2 = []
toilet2 = []
structure2 = []
n_this_area2 = []
# 3)
area3 = []
room3 = []
toilet3 = []
structure3 = []
n_this_area3 = []
# 4)
area4 = []
room4 = []
toilet4 = []
structure4 = []
n_this_area4 = []
# 5)
area5 = []
room5 = []
toilet5 = []
structure5 = []
n_this_area5 = []
# 6)
area6 = []
room6 = []
toilet6 = []
structure6 = []
n_this_area6 = []
# 7)
area7 = []
room7 = []
toilet7 = []
structure7 = []
n_this_area7 = []
# 8)
area8 = []
room8 = []
toilet8 = []
structure8 = []
n_this_area8 = []
# 9)
area9 = []
room9 = []
toilet9 = []
structure9 = []
n_this_area9 = []
# 10)
area10 = []
room10 = []
toilet10 = []
structure10 = []
n_this_area10 = []

########################################################################################################################
# 스크래핑 시작

# StopWatch: 코드 시작
time_start = datetime.now()
print("Procedure started at: " + str(time_start))

apt_len = len(se_name)  # 단지명 리스트의 길이.
chrome = webdriver.Chrome('chromedriver.exe')

for i in range(apt_len):
    apt = se_name[i]

    try:
        if i == 0:
            chrome.get('https://land.naver.com/')  # 네이버 부동산 실행
            time.sleep(1)
            # apt = df_name[0]
            # Copy selector 을 해서 원하는 '검색창' 의 정보를 불러온다.
            # queryInputHeader = 해당 검색창의 selector
            input_engine = chrome.find_element_by_css_selector('#queryInputHeader')
            input_engine.clear()
            input_engine.send_keys(apt)  # enter 키를 누르기 전 상태
            input_engine.send_keys(Keys.ENTER)  # 특정키를 입력하고 싶은 경우
            link = chrome.find_element_by_css_selector(
                '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
            link.click()  # '단지정보' 클릭

            time.sleep(1)

            get_apt_info()  # 단지 정보 가져오기
            get_url_info()  # url 에서 위도와 경도 가져오기
            get_capacity_info()  # 면적별 정보 가져오기

            chrome.find_element_by_css_selector('#search_input').clear  # 검색창 초기화

            time.sleep(1)

        else:
            search = chrome.find_element_by_css_selector('#search_input')
            search.clear()
            search.send_keys(apt)  # enter 키를 누르기 전 상태
            # input.submit()
            search.send_keys(Keys.ENTER)  # 특정키를 입력하고 싶은 경우
            time.sleep(4)
            link = chrome.find_element_by_css_selector(
                '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
            link.click()
            time.sleep(4)

            get_apt_info()  # 단지 정보 가져오기
            get_url_info()  # url 에서 위도와 경도 가져오기
            get_capacity_info()  # 면적별 정보 가져오기

            chrome.find_element_by_css_selector('#search_input').clear  # 검색창 초기화


    except:  # 검색 시 여러개의 창이 뜰 때 기능
        try:
            search.clear()
            choice = chrome.find_element_by_css_selector(
                '#ct > div.map_wrap > div.search_panel > div.list_contents > div > div > div:nth-child(2) > div > a')
            choice.click()
            # summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)
            link = chrome.find_element_by_css_selector(
                '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
            link.click()

            time.sleep(3)

            get_apt_info()  # 단지 정보 가져오기
            get_url_info()  # url 에서 위도와 경도 가져오기
            get_capacity_info()  # 면적별 정보 가져오기


        except Exception as ex:
            research = chrome.find_element_by_css_selector('#search_input')
            research.clear()

            input_nan_if_null()  # 원하는 정보를 얻지 못했으므로 전체 nan 값 출력
            get_capacity_info()  # 입력값에 해당하는 정보가 없는 상황에서 자동으로 nan 값 출력

            chrome.back()

            try:
                time.sleep(3)
                input_engine = chrome.find_element_by_css_selector('#queryInputHeader')
                input_engine.send_keys(Keys.ENTER)
            except:
                search = chrome.find_element_by_css_selector('#search_input')
                search.send_keys(Keys.ENTER)

# StopWatch: 코드 종료
time_end = datetime.now()
print("Procedure finished at: " + str(time_end))
print("Elapsed (in this Procedure): " + str(time_end - time_start))

# 엑셀에 append 시키기
appending_to_df()

# 스크래핑 종료
########################################################################################################################


# 결과값 엑셀로 내보내기
df_dongdaemoongu.to_excel('Gangbuk/dongdaemoongu_edit1.xlsx', sheet_name='edit1', index=False)
