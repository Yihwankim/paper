
#############################################################################
# import packages
import pandas as pd
import numpy as np

############################################################################

df_172q = pd.read_excel('seminar data/Seoul_20172Q.xlsx', header=0, skipfooter=0)
df_204q = pd.read_excel('seminar data/Seoul_20204Q.xlsx', header=0, skipfooter=0)

df_characteristic = pd.read_excel('seminar data/Seoul_last_sorting.xlsx', header=0, skipfooter=0)

#####################################################################################################
# for 17년 2분기
df_172q['전용면적1'] = df_172q['전용면적(㎡)']
df_172q['전용면적1'] = df_172q['전용면적1'].astype(str)


df_172q['matching'] = df_172q['법정동'] + " " + df_172q['아파트_y'] + " " + df_172q['전용면적1']
df_172q = df_172q.sort_values(by=['matching'])
df_172q = df_172q.drop_duplicates(['matching'], keep='first')

# for 20년 4분기
df_204q['전용면적1'] = df_204q['전용면적(㎡)']
df_204q['전용면적1'] = df_204q['전용면적1'].astype(str)

df_204q['matching'] = df_204q['법정동'] + " " + df_204q['아파트_y']+ " " + df_204q['전용면적1']
df_204q = df_204q.sort_values(by=['matching'])
df_204q = df_204q.drop_duplicates(['matching'], keep='first')
df_204q = df_204q[['matching', '거래금액']]
#####################################################################################################
# matching and comparing btw 2017 2Q and 2020 4Q

df_comparing = pd.merge(df_172q, df_204q, on="matching")
df_comparing = df_comparing.sort_values(by=['지역구'])
df_comparing = df_comparing.reset_index(drop='Ture')

df_comparing['아파트'] = df_comparing['아파트_x']
df_comparing['2017_2분기'] = df_comparing['거래금액_x']
df_comparing['2020_4분기'] = df_comparing['거래금액_y']

df_comparing_moon = df_comparing[['지역구', '법정동', '아파트', '아파트코드', '사용승인일', '연수', '세대수', '주차대수_세대',
                                  '용적률', '건폐율', '위도', '경도', '건설사', '난방', '구조', '면적유형', '해당면적 세대수',
                                  '공급면적(㎡)', '전용면적(㎡)', '전용률(%)', '방 개수', '화장실 개수',
                                  '2017_2분기', '2020_4분기']]

df_comparing_moon_price = df_comparing_moon[['지역구', '법정동', '아파트', '아파트코드', '공급면적(㎡)', '전용면적(㎡)',
                                             '위도', '경도', '2017_2분기', '2020_4분기']]

#####################################################################################################
# Export to excel
df_comparing_moon.to_excel('seminar data/comparing_information.xlsx', index=False)
df_comparing_moon_price.to_excel('seminar data/comparing_price_directly.xlsx', index=False)

