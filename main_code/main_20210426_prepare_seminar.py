# import packages
import pandas as pd
import numpy as np

df = pd.read_excel('seminar data/Seoul_last.xlsx', header=0, skipfooter=0)

df_description1 = df
df_description2 = df

df_description2 = df_description2.drop_duplicates(['아파트코드'], keep='first')
df_description2 = df_description2.sort_values(by=['지역구'])

df_description1 = df_description1[['주차대수_세대', '전용면적(㎡)', '전용률(%)', '방 개수', '화장실 개수']]
df_description2 = df_description2[['연수', '세대수', '저층', '고층', '주차대수_총', '용적률', '건폐율']]

df_description1.to_excel('seminar data/Seoul_last_description_type.xlsx', sheet_name='total', index=False)
df_description2.to_excel('seminar data/Seoul_last_description_apt.xlsx', sheet_name='total', index=False)