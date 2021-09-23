# Chapter 8
# 더미변수를 추가한 seoul apt data 와 실거래가 데이터를 matching
# 이 과정에서 층 정보가 포함되고, 같은 면적유형의 아파트여도 실거래 측면에서는 각기 다른 아파트로 분류될 수 있기 때문에 데이터 수가 확장됨
# 매칭을 하게 하는 key 값은 법정동 + 전용면적 유형 + 건축년도로 구성되어 있음
# 예를들어 2010년에 건축된 회기동 85m^2의 아파트는 실거래가에서 동일 정보를 갖는 아파트와 동일한 정보로 취급

# import packages
from tqdm import tqdm
import pickle
import pandas as pd
import datetime
import numpy as np


########################################################################################################################
# 크롤링 데이터 불러오기
df_seoul = pd.read_excel('Hedonic_index/seoul_replicating_dummy.xlsx', header=0, skipfooter=0)

# 매칭을 위해 KEY 값 만들기
df_seoul['건축년도'] = df_seoul['사용승인일'].dt.year
# 참고 :
# https://www.delftstack.com/ko/howto/python-pandas/how-to-extract-month-and-year-separately-from-datetime-column-in-pandas/

df_seoul['전용면적'] = round(df_seoul['전용면적'], 2)
df_seoul['전용면적1'] = df_seoul['전용면적']

# df_seoul['전용면적1'] = df_seoul['전용면적'].astype(int)
# 참고 : https://www.javaer101.com/ko/article/54022504.html

# 데이터 값을 합쳐주기 위해 문자열로 지정
df_seoul['건축년도'] = df_seoul['건축년도'].astype(str)
df_seoul['전용면적1'] = df_seoul['전용면적1'].astype(str)

# 'matching' KEY 값 만들기
df_seoul['matching'] = df_seoul['법정동'] + " " + df_seoul['전용면적1'] + " " + df_seoul['건축년도']
df_seoul = df_seoul.sort_values(by=['matching'])

########################################################################################################################
'''
49 * 3 으로 실거래가 데이터를 1부터 147으로 명명 
따라서 10년 10월의 실거래가 자료가 1의 값을 갖게된다.

15년 5월의 경우 : 10년 4분기 ~ 15년 1분기, 총 18개의 quarter = 54m 의 값을 갖게되므로 56으로 명명
19년 1월의 경우 : 10년 4분기 ~ 18년 4분기, 총 33개의 quarter = 99m 의 값을 갖게되므로 100으로 명명 
'''

length = 126
# df_dataset.to_pickle("./data_raw/df_dataset_" + str(yyyymm) + ".pkl")
for i in tqdm(range(length)):
    data01 = pd.read_pickle('real_transaction_data/df_dataset_' + str(i + 1) + '.pkl')
    data01.to_pickle("./real_transaction2/df_dataset_" + str(i + 22) + ".pkl")

