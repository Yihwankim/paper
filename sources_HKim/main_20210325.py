# HKim: PEP8 스타일 가이드를 가급적 준수하세요.
# 1. 패키지를 불러온 이후에는 두 줄 띄웁니다.
# 2. 클래스 및 함수 정의는 패키지 불러온 아래에 붙습니다. 이후 두 줄 띄웁니다.
# 3. 코멘트를 쓸 때에는 샵(#) 붙이고 한칸 띄웁니다.
# 4. 라인 안에서 코멘트를 쓸 때에는 코드 맨 뒤에 두칸 띄우고 # 를 시작합니다.

# 2021-03-25
# selenium을 이용한 크롤링 일반화 작업

# 목표:
# 1. 방갯수, 화장실 수, age c정보 append 시키기
# 2. 함수로 엑셀을 호출하면  한번 실행시 알아서 다 할 수 있도록 조치하기

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



area1 = aaa1
room1 = bbb1

class

def input_value_in_vars(area, room, toilet, i):
    area = aaa[i]
    room = bbb[i]
    toilet = ccc[i]

    return area, room, toilet

input_value_in_vars(area1, room1, toilet1, i=1)
input_value_in_vars(area2, room2, toilet2, i=2)


########################################################################################################################
# 엑셀값 출력
df_dongdaemoongu = pd.read_excel('Gangbuk/dongdaemoongu.xlsx', sheet_name=0, header=0, skipfooter=0, usecols='C:D, G:H')

df_dongdaemoongu = df_dongdaemoongu.drop_duplicates(['아파트'],keep='first')
df_dongdaemoongu = df_dongdaemoongu.sort_values(by=['아파트'])
df_dongdaemoongu = df_dongdaemoongu.reset_index(drop='Ture')

df_name = df_dongdaemoongu[['읍면동', '아파트']] # 여러 열을 추출하고 싶을때는 [[ 두개를 사용 ]]

df_name = df_name.astype('str')
se_name = df_name['읍면동'] + " " + df_name['아파트']


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
# office_number = []
# add = [] #주소

### 새롭게 추가 ###

#1
area1 = [] #면적 : 공급/전용(전용률)
room1 = [] #방 갯수
toilet1 = [] #화장실 개수
struc1 = [] #현관구조
n_this_area1 = [] #해당면적 세대수
#2
area2 = [] #면적 : 공급/전용(전용률)
room2 = [] #방 갯수
toilet2 = [] #화장실 개수
struc2 = [] #현관구조
n_this_area2 = [] #해당면적 세대수
#3
area3 = [] #면적 : 공급/전용(전용률)
room3 = [] #방 갯수
toilet3 = [] #화장실 개수
struc3 = [] #현관구조
n_this_area3 = [] #해당면적 세대수
#4
area4 = [] #면적 : 공급/전용(전용률)
room4 = [] #방 갯수
toilet4 = [] #화장실 개수
struc4 = [] #현관구조
n_this_area4 = [] #해당면적 세대수
#5
area5 = [] #면적 : 공급/전용(전용률)
room5 = [] #방 갯수
toilet5 = [] #화장실 개수
struc5 = [] #현관구조
n_this_area5 = [] #해당면적 세대수
#6
area6 = [] #면적 : 공급/전용(전용률)
room6 = [] #방 갯수
toilet6 = [] #화장실 개수
struc6 = [] #현관구조
n_this_area6 = [] #해당면적 세대수
#7
area7 = [] #면적 : 공급/전용(전용률)
room7 = [] #방 갯수
toilet7 = [] #화장실 개수
struc7 = [] #현관구조
n_this_area7 = [] #해당면적 세대수
#8
area8 = [] #면적 : 공급/전용(전용률)
room8 = [] #방 갯수
toilet8 = [] #화장실 개수
struc8 = [] #현관구조
n_this_area8 = [] #해당면적 세대수
#9
area9 = [] #면적 : 공급/전용(전용률)
room9 = [] #방 갯수
toilet9 = [] #화장실 개수
struc9 = [] #현관구조
n_this_area9 = [] #해당면적 세대수
#10
area10 = [] #면적 : 공급/전용(전용률)
room10 = [] #방 갯수
toilet10 = [] #화장실 개수
struc10 = [] #현관구조
n_this_area10 = [] #해당면적 세대수
########################################################################################################################
# 리허설
########################################################################################################################
# 검색하고자 하는 아파트 이름 입력
apt = '제기동 이수브라운'
# apt = df_name[0]

# chromedriver 실행 후 네이버 부동산 홈페이지로 이동
chrome = webdriver.Chrome('chromedriver.exe')
chrome.get('https://land.naver.com/')  # 네이버 부동산 홈페이지
time.sleep(1)

# 검색창에 미리 정의된 아파트 이름 입력
# Copy selector을 해서 원하는 '검색창'의 정보를 불러온다.
# queryInputHeader = 해당 검색창의 selector
input = chrome.find_element_by_css_selector('#queryInputHeader')
input.clear()
input.send_keys(apt)  # enter 키를 누르기 전 상태
input.send_keys(Keys.ENTER)  # 특정키를 입력하고 싶은 경우
# input.submit()

# 단지정보 클릭 (가장 상단에 내가 원하는 아파트가 나온 경우)
# chrome.find_element_by_class_name("title")[ddf.index(Apt_name[i])].click()
link = chrome.find_element_by_css_selector(
    '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
link.click()

time.sleep(1)


# 기본정보 append
get_apt_info()

#area'i' = [] #면적 : 공급/전용(전용률)
#room'i' = [] #방 갯수
#toilet'i' = [] #화장실 개수
#struc'i' = [] #현관구조
#n_this_area'i' = [] #해당면적 세대수

for i in range(10):
    if i==0:
        area1_selector = "#tabpanel > table > tbody > tr:nth-child(1) > td"
        area1.append(chrome.find_element_by_css_selector(area1_selector).text)

        rt1_selector = "#tabpanel > table > tbody > tr:nth-child(2) > td"  # 방 개수와 화장실 개수
        rt1 = chrome.find_element_by_css_selector(rt1_selector).text
        room1.append(rt1.split('/')[0])
        toilet1.append(rt1.split('/')[1])

        struc1_selector = "#tabpanel > table > tbody > tr:nth-child(4) > td"
        struc1.append(chrome.find_element_by_css_selector(struc1_selector).text)

        n_this_area1_selector = "#tabpanel > table > tbody > tr:nth-child(3) > td"
        n_this_area1(chrome.find_element_by_css_selector(n_this_area1_selector).text)

    else:
        try:
            num2 = chrome.find_element_by_css_selector("#tab1 > span")
            num2.click()


#tab1 > span
#tab2 > span

get_url_info()

########################################################################################################################
# 스크래핑 시작

# StopWatch: 코드 시작
time_start = datetime.now()
print("Procedure started at: " + str(time_start))


apt_len = len(se_name)  # 단지명 리스트의 길이.
chrome = webdriver.Chrome('chromedriver.exe')

for i in range(apt_len):
    apt = se_name[i]
    # Copy selector을 해서 원하는 '검색창'의 정보를 불러온다.
    # queryInputHeader = 해당 검색창의 selector
    try:
        if i == 0:
            chrome.get('https://land.naver.com/') # 네이버 부동산 실행
            time.sleep(1)
            # apt = df_name[0]
            # Copy selector을 해서 원하는 '검색창'의 정보를 불러온다.
            # queryInputHeader = 해당 검색창의 selector
            input = chrome.find_element_by_css_selector('#queryInputHeader')
            input.clear()
            input.send_keys(apt)  # enter 키를 누르기 전 상태
            # input.submit()
            input.send_keys(Keys.ENTER)  # 특정키를 입력하고 싶은 경우
            # chrome.find_element_by_class_name("title")[ddf.index(Apt_name[i])].click()
            link = chrome.find_element_by_css_selector(
                '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
            link.click()

            time.sleep(1)
            get_apt_info()
            get_url_info()

            chrome.find_element_by_css_selector('#search_input').clear

            print("Notice: " + i + "/" + apt_len + " scrapping finished")
            time.sleep(1)

        else:
            search = chrome.find_element_by_css_selector('#search_input')
            search.clear()
            search.send_keys(apt)  # enter 키를 누르기 전 상태
            # input.submit()
            search.send_keys(Keys.ENTER)  # 특정키를 입력하고 싶은 경우
            # chrome.find_element_by_class_name("title")[ddf.index(Apt_name[i])].click()
            time.sleep(4)
            link = chrome.find_element_by_css_selector(
                '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
            link.click()
            time.sleep(4)

            get_apt_info()
            get_url_info()

            chrome.find_element_by_css_selector('#search_input').clear
            print("Notice: " + i + "/" + apt_len + " scrapping finished")

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
            get_apt_info()
            get_url_info()

            print("Notice: " + i + "/" + apt_len + " scrapping finished")

        except Exception as ex:
            research = chrome.find_element_by_css_selector('#search_input')
            research.clear()

            input_nan_if_null()

            print("Notice: " + i + "/" + apt_len + " scrapping finished")

            chrome.back()
            try:
                time.sleep(3)
                input = chrome.find_element_by_css_selector('#queryInputHeader')
                input.send_keys(Keys.ENTER)
            except:
                search = chrome.find_element_by_css_selector('#search_input')
                search.send_keys(Keys.ENTER)

# StopWatch: 코드 종료
time_end = datetime.now()
print("Procedure finished at: " + str(time_end))
print("Elapsed (in this Procedure): " + str(time_end - time_start))





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


#엑셀값으로 append 시키기