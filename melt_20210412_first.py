# 2021-04-12
# pandas 의 melt 기능을 사용하여 stack 해보기
# 최종 비교를 위해 Apt_name (네이버 부동산상의 아파트 이름 정보) 열을 인덱스로 지정하기
# 결과값 엑셀로 저장

# 숙지해야하는 부분
# 1. 해당 파일은 아직 _edit1.xlsx 파일들을 전처리하기 전의 내용이다.
# 2. _edit1 에서 면적정보가 10개가 넘어가는 아파트들과 크롤링을 올바르게 하지 못한 아파트 정보들에 대해 재확인한 후
# 3. _edit1 파일이 온전해 지면 그때 해당 코드를 통해 면적별 정보에 따라 리스트를 재정리 해야한다.

# 최종 비교시 고려할 사항
# 1. 아파트 이름(인덱스)과 읍면동, 아파트 정보가 동일한지 여부
# 2. 아파트 세대수가 면적별 세대수의 합과 동일한지 여부

# Import packages
import pandas as pd
import numpy as np

#############################################################################################################
# 엑셀 파일 불러오기
df_data = pd.read_excel('melt_stack_example/Dongdaemoongu_edit2.xlsx')  # 폴더를 나중에는 _edit1 폴더로 바꿀 것

df_Gu = pd.read_excel('melt_stack_example/Dongdaemoongu_edit2.xlsx', usecols='A:P')  # 상기와 마찬가지 조치를 취할 것

#############################################################################################################
# 6개의 컬럼으로 나누어진 면적별 정보를 하나의 칼럼으로 합쳐서 시리즈로 저장하기
# 해당 시리즈는 앞으로 10개 이상의 시리즈로 확장되어야함
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

df_Gu = pd.concat([df_Gu, se_type1, se_type2, se_type3, se_type4, se_type5, se_type6, se_type7, se_type8,
                   se_type9, se_type10], axis=1)  # 만들어 둔 시리즈를 기존의 데이터 프레임에 합치기

#############################################################################################################

# 하나의 컬럼으로 만들어 둔 면적별 정보(type_capacity)에 따라 아파트 기본 정보들을 stack 시키기
df_edit = df_Gu.melt(id_vars=['읍면동', '아파트', '세대수', '입주년월', 'Apt_name', 'number', 'floor',
                              'confirm_date', 'car', 'FAR', 'BC', 'con', 'heat', 'code', 'lat',
                              'long'], value_vars=['type_capacity1', 'type_capacity2', 'type_capacity3',
                                                   'type_capacity4', 'type_capacity5', 'type_capacity6',
                                                   'type_capacity7', 'type_capacity8', 'type_capacity9',
                                                   'type_capacity10'])

df_edit = df_edit.sort_values(by='아파트')  # 아파트 이름에 따라 행을 정렬
df_edit2 = df_edit.dropna(axis=0)  # nan 값이 있는 행 제거: 면적이 3개인 아파트의 경우 4~10번째 면적정보는 drop 된다.

type_information = df_edit2['value'].str.split(',')  # 하나의 컬럼으로 만들어둔 면적별 정보를 다시 6개로 나누기

# 데이터 프레임에 각각 고유의 이름으로 합치기
df_edit2['type_capacity'] = type_information.str.get(0)
df_edit2['area'] = type_information.str.get(1)
df_edit2['room'] = type_information.str.get(2)
df_edit2['toilet'] = type_information.str.get(3)
df_edit2['structure'] = type_information.str.get(4)
df_edit2['n_this_area'] = type_information.str.get(5)

df_Gu_last = df_edit2.drop(['value', 'variable'], axis=1)  # 필요없어진 값 제거

df = df_Gu_last.set_index('Apt_name')  # 비교가 용이하도록 Apt_name 을 인덱스로 설정

df.to_excel('melt_stack_example/Dongdaemoongu_example.xlsx', sheet_name='edit1', index=True)  # 폴더명은 나중에 바꿔야 함
