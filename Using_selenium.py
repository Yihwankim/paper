import numpy as np
import pandas as pd
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('.//chromedriver')

arr = ['회기힐스테이트','더하이브B타워']

arr_len = len(arr) #단지명 리스트의 길이, 내가 잡은 예시에서는 2개
jungong_list = [] #준공 년월을 담을 리스트
ganeng_list = [] #거래 가능일 data를 담을 리스트
jungong_ganeng_list = [] #위 두 리스트를 찾기 위해 사용할 여분의 리스트

for i in range (arr_len):
    jungong_ganeng_list = []
    driver.get("https://new.land.naver.com/")
    time.sleep(1)
    danjiname = arr[i]
    elem_search = driver.find_element_by_class_name("search_input")
    elem_search.clear()
    elem_search.send_keys(danjiname)
    elem_search.send_keys(Keys.RETURN)

    try :
        time.sleep(1)
        #driver.find_element_by_class_name("item_list.item_list--search")
        d1 = driver.find_element_by_class_name("title")

        ddf = []
        for i2 in range(len(d1)) :
            ddf.append(d1[i2].text)

        if arr[i] in ddf:
            driver.find_element_by_class_name("title")[ddf.index(arr[i])].click()
            button = driver.find_element_by_class_name("complex_link").click()
            time.sleep(1)
            detail = driver.find_element_by_id("detailContents1")
            deep1 = detail.find_element_by_class_name('table_th')
            deep2 = detail.find_element_by_class_name('table_td')

            for i3 in range(len(ddp1)):
                jungong_ganeng_list.append(deep1[i3].text)
                #ganeng_num_list.append(deep2[i].text)

            jungong_num = jungong_ganeng_list.index('준공년월')
            ganeng_num = jungong_ganeng_list.index('사용승인일')

            jungong_list.append(deep2[jungong_num].text)
            ganeng_list.append(deep2[ganeng_num].text)

        else:
            time.sleep()
            jungong_list.append("정보검색안됨")
            ganeng_list.append("정보검색안됨")

        #print('크롤링 성공')
    except :
        #print('예외진입')
        try:
            d = driver.find_element_by_class_name("text_limit")

            button = driver.find_element_by_class_name("complex_link").click()
            time.sleep(1)
            detail = driver.find_element_by_id("detailContents1")
            deep1 = detail.find_element_by_class_name('table_th')
            deep2 = detail.find_element_by_class_name('table_td')

            for i4 in range(len(deep1)):
                jungong_ganeng_list.append(deep1[i4].text)
                #ganeng_num_list.append(deep2[i].text)

            jungong_num = jungong_ganeng_list.index('준공년월')

            if c in jungong_ganeng_list:
                ganeng_num = jungong_ganeng_list.index('사용승인일')

                jungong_list.append(deep2[jungong_num].text)
                ganeng_list.append(deep2[ganeng_num].text)
            else:
                jungong_list.append(deep2[jungong_num].text)
                ganeng_list.append("거래가능일조회안됨")

        except:
            jungong_list.append("전매 or 부분전매 아님")
            ganeng_list.append("전매 or 부분전매 아님")

    #time.sleep(1)
    cname = arr[i]
    nnum = len(arr)-arr.index(arr[i]) -1

    #nnum = len(arr)-np.where(arr[i] == arr)[0][0] -1

    print('{} 크롤링성공, {}개 남음'.format(cname,nnum))


test_df = pd.DataFrame(arr)
test_df['입주일자'] = jungong_list
test_df['사용승인일'] = ganeng_list
test_df


