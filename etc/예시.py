from selenium import webdriver
import time
import openpyxl
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys


# 2021.03.12 연구노트 작성

df_dongdaemoongu = pd.read_excel('Gangbuk/dongdaemoongu.xlsx',sheet_name='답십리동', header=0, skipfooter=0, usecols='C:D, G:H')

df_dongdaemoongu = df_dongdaemoongu.sort_values(by=['아파트'])
df_dongdaemoongu = df_dongdaemoongu.reset_index(drop='Ture')

df_name = df_dongdaemoongu[['읍면동','아파트']] #여러 열을 추출하고 싶을때는 [[ 두개를 사용 ]]

df_name = df_name.astype('str')
df_name = df_name['읍면동'] + " " + df_name['아파트']

print(len(df_name))

df_example = pd.DataFrame({df_name.loc[0]}) #예시

chrome = webdriver.Chrome('chromedriver.exe')

apt_len = len(df_name)  #단지명 리스트의 길이.
number = [] #세대수
floor = [] #저/최고층
confirm_date = [] #사용승인일
car = [] #주차대수
#Floor Area Ratio
FAR = [] #용적률
#Building Coverage
BC = [] #건폐율
con = [] #건설사
heat = [] #난방 / 난방방식
#office_number = []
#add = [] #주소
#area = [] #면적

chrome.get('https://land.naver.com/')
time.sleep(1)
#apt = df_name[0]
    # Copy selector을 해서 원하는 '검색창'의 정보를 불러온다.
    # queryInputHeader = 해당 검색창의 selector
apt = df_example[0]

input = chrome.find_element_by_css_selector('#queryInputHeader')
        #검색 자동화 실행
input.clear()
input.send_keys(apt) # enter 키를 누르기 전 상태
    #input.submit()
input.send_keys(Keys.ENTER) #특정키를 입력하고 싶은 경우
#chrome.find_element_by_class_name("title")[ddf.index(Apt_name[i])].click()
link = chrome.find_element_by_css_selector('#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
link.click()
time.sleep(1)
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

df_example['number'] = number
df_example['floor'] = floor
df_example['confirm_date'] = confirm_date
df_example['car'] = car
df_example['FAR'] = FAR
df_example['BC'] = BC
df_example['con'] = con
df_example['heat'] = heat

print(df_example)


time.sleep(3) # 3초간 정지
#chrome.quit()
input.clear()
