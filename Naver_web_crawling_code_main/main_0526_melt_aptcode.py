# 2021-05-26
# 해당 코드의 목적은 작업의 효율성과 가독성을 높이기 위함입니다.
# Chapter 2: melting_ capacity type 을 행으로 넣어 면적별 정보 업데이트
# 목적 : 면적 유형별로 아파트 정보를 분류시키기

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

#############################################################################################################
# 엑셀파일 불러오기
n = 1  # 숫자 조정

# 하단의 코드는 추후 수정되어야 한다. Chapter 1에서 모든 아파트 정보를 크롤링 한 이후 해당 코드를 수정하여 최종 엑셀을 불러오도록 하자
df_data = pd.read_excel('Naver_web_crawling_code_main/' + str(n) + '.xlsx')
df_Gu = pd.read_excel('Naver_web_crawling_code_main/' + str(n) + '.xlsx', usecols='A:P')
#############################################################################################################
# Melting

'''
df_data 를 열어 type_capacity 항목 중 몇번째 항목까지 값이 있는지를 확인한다. 
예를들어 전체 데이터프레임에서 단 한개의 행이라도 (= 단 한개의 아파트라도) type_capacity 20 에 nan 값이 아닌
실측치가 있다면, length 를 20으로 설정하여 코드를 돌리면 된다.

그러나 전체 행 중 가장 긴 항목의 type_capacity 가 10이라면, length 를 10으로 설정하여 코드를 돌려야 한다.  
'''

se_type1 = df_data['type_capacity1'].str.cat(df_data[['area1',
                                                      'room1',
                                                      'toilet1',
                                                      'structure1',
                                                      'n_this_area1']], sep=',')

se_type2 = df_data['type_capacity2'].str.cat(df_data[['area2',
                                                      'room2',
                                                      'toilet2',
                                                      'structure2',
                                                      'n_this_area2']], sep=',')

se_type3 = df_data['type_capacity3'].str.cat(df_data[['area3',
                                                      'room3',
                                                      'toilet3',
                                                      'structure3',
                                                      'n_this_area3']], sep=',')

se_type4 = df_data['type_capacity4'].str.cat(df_data[['area4',
                                                      'room4',
                                                      'toilet4',
                                                      'structure4',
                                                      'n_this_area4']], sep=',')

se_type5 = df_data['type_capacity5'].str.cat(df_data[['area5',
                                                      'room5',
                                                      'toilet5',
                                                      'structure5',
                                                      'n_this_area5']], sep=',')

se_type6 = df_data['type_capacity6'].str.cat(df_data[['area6',
                                                      'room6',
                                                      'toilet6',
                                                      'structure6',
                                                      'n_this_area6']], sep=',')

se_type7 = df_data['type_capacity7'].str.cat(df_data[['area7',
                                                      'room7',
                                                      'toilet7',
                                                      'structure7',
                                                      'n_this_area7']], sep=',')

se_type8 = df_data['type_capacity8'].str.cat(df_data[['area8',
                                                      'room8',
                                                      'toilet8',
                                                      'structure8',
                                                      'n_this_area8']], sep=',')

se_type9 = df_data['type_capacity9'].str.cat(df_data[['area9',
                                                      'room9',
                                                      'toilet9',
                                                      'structure9',
                                                      'n_this_area9']], sep=',')

se_type10 = df_data['type_capacity10'].str.cat(df_data[['area10',
                                                        'room10',
                                                        'toilet10',
                                                        'structure10',
                                                        'n_this_area10']], sep=',')

se_type11 = df_data['type_capacity11'].str.cat(df_data[['area11',
                                                        'room11',
                                                        'toilet11',
                                                        'structure11',
                                                        'n_this_area11']], sep=',')

se_type12 = df_data['type_capacity12'].str.cat(df_data[['area12',
                                                        'room12',
                                                        'toilet12',
                                                        'structure12',
                                                        'n_this_area12']], sep=',')

se_type13 = df_data['type_capacity13'].str.cat(df_data[['area13',
                                                        'room13',
                                                        'toilet13',
                                                        'structure13',
                                                        'n_this_area13']], sep=',')

se_type14 = df_data['type_capacity14'].str.cat(df_data[['area14',
                                                        'room14',
                                                        'toilet14',
                                                        'structure14',
                                                        'n_this_area14']], sep=',')

se_type15 = df_data['type_capacity15'].str.cat(df_data[['area15',
                                                        'room15',
                                                        'toilet15',
                                                        'structure15',
                                                        'n_this_area15']], sep=',')

se_type16 = df_data['type_capacity16'].str.cat(df_data[['area16',
                                                        'room16',
                                                        'toilet16',
                                                        'structure16',
                                                        'n_this_area16']], sep=',')

se_type17 = df_data['type_capacity17'].str.cat(df_data[['area17',
                                                        'room17',
                                                        'toilet17',
                                                        'structure17',
                                                        'n_this_area17']], sep=',')

se_type18 = df_data['type_capacity18'].str.cat(df_data[['area18',
                                                        'room18',
                                                        'toilet18',
                                                        'structure18',
                                                        'n_this_area18']], sep=',')

se_type19 = df_data['type_capacity19'].str.cat(df_data[['area19',
                                                        'room19',
                                                        'toilet19',
                                                        'structure19',
                                                        'n_this_area19']], sep=',')

se_type20 = df_data['type_capacity20'].str.cat(df_data[['area20',
                                                        'room20',
                                                        'toilet20',
                                                        'structure20',
                                                        'n_this_area20']], sep=',')

df_Gu = pd.concat([df_Gu, se_type1, se_type2, se_type3, se_type4, se_type5, se_type6, se_type7, se_type8,
                   se_type9, se_type10, se_type11, se_type12, se_type13, se_type14, se_type15, se_type16, se_type17,
                   se_type18, se_type19, se_type20], axis=1)

df_edit = df_Gu.melt(id_vars=['읍면동', '아파트', '세대수', '입주년월', 'Apt_name', 'number', 'floor',
                              'confirm_date', 'car', 'FAR', 'BC', 'con', 'heat', 'code', 'lat',
                              'long'], value_vars=['type_capacity1', 'type_capacity2', 'type_capacity3',
                                                   'type_capacity4', 'type_capacity5', 'type_capacity6',
                                                   'type_capacity7', 'type_capacity8', 'type_capacity9',
                                                   'type_capacity10', 'type_capacity11', 'type_capacity12',
                                                   'type_capacity13', 'type_capacity14', 'type_capacity15',
                                                   'type_capacity16', 'type_capacity17', 'type_capacity18',
                                                   'type_capacity19', 'type_capacity20'])

df_edit = df_edit.sort_values(by='Apt_name')  # 아파트 이름에 따라 행을 정렬
df_edit2 = df_edit.dropna(axis=0)  # nan 값이 있는 행 제거: 면적이 3개인 아파트의 경우 4~10번째 면적정보는 drop 된다.

type_information = df_edit2['value'].str.split(',')  # 하나의 컬럼으로 만들어둔 면적별 정보를 다시 6개로 나누기

# 데이터 프레임에 각각 고유의 이름으로 합치기
df_edit2['type_capacity'] = type_information.str.get(0)
df_edit2['area'] = type_information.str.get(1)
df_edit2['room'] = type_information.str.get(2)
df_edit2['toilet'] = type_information.str.get(3)
df_edit2['structure'] = type_information.str.get(4)
df_edit2['n_this_area'] = type_information.str.get(5)

df_Gu_last = df_edit2.drop(['value', 'variable', '아파트',
                            '세대수', '입주년월'], axis=1)  # 필요없어진 값 제거