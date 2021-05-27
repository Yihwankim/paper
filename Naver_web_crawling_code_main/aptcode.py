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

chrome = webdriver.Chrome('chromedriver.exe')

# apt_len = [0, 30000]
apt_len = [0,5]
# 2) apt_len = [0, 30000]
# 100000 + i
for i in range(apt_len):
    apt = str(i)
    chrome.get('https://new.land.naver.com/complexes/' + apt)
    time.sleep(2)

    city_name = chrome.find_element_by_css_selector('#region_filter > div > a > span:nth-child(2)')
    con_type_name = chrome.find_element_by_css_selector('#summaryInfo > div.complex_title > span')

    try :
        if city_name == '서울시':
            if con_type_name == '아파트':
                print('yes')

            elif con_type_name == '주상복합':
                print('yes')

            else:
                print('nan')

        else:
            print('nan')
    except:
        print('nan')


i=1
i = str(i)
chrome.get('https://new.land.naver.com/complexes/' + i)  # 네이버 부동산 실행
time.sleep(1)
chrome.get('https://new.land.naver.com/complexes/2')  # 네이버 부동산 실행
code = chrome.find_element_by_css_selector('#region_filter > div > a > span:nth-child(2)')

con_type = chrome.find_element_by_css_selector('#summaryInfo > div.complex_title > span')
con_type.text
if code.text == '서울시':
    if con_type.text == '아파트':
        print('yes')

    elif con_type.text == '주상복합':
        print('yes')

    else:
        print('no')
else:
    print('no')



input_engine = chrome.find_element_by_css_selector('#queryInputHeader')
input_engine.clear()
input_engine.send_keys(apt)  # apt 이름을 입력하고, enter 키를 누르기 전 상태
input_engine.send_keys(Keys.ENTER)  # 특정키(enter) 를 입력
link = chrome.find_element_by_css_selector(
    '#summaryInfo > div.complex_summary_info > div.complex_detail_link > button:nth-child(1)')
link.click()  # '단지정보' 클릭

time.sleep(1)

get_apt_info()  # 함수 1 사용
get_url_info()  # 함수 2 사용
get_capacity_info()  # 함수 5 사용

chrome.find_element_by_css_selector('#search_input').clear  # 검색창 초기화
