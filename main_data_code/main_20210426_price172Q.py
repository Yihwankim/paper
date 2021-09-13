# import packages
import pickle
import pandas as pd
import datetime

data04 = pd.read_pickle('data_processed/df_dataset_201704.pkl')

data05 = pd.read_pickle('data_processed/df_dataset_201705.pkl')

data06 = pd.read_pickle('data_processed/df_dataset_201706.pkl')


####################################################################################################
# 2020년 10월 부터 12월, 4분기 실거래가 데이터와 매칭시키기
data_2q = pd.concat([data04, data05, data06], axis=0)


# 크롤링 데이터와 매칭 시키기
df = data_2q.loc[data_2q['법정동시군구코드'].str.contains("11")]
df = df.sort_values(by=['법정동시군구코드'])
df = df.reset_index(drop='Ture')

df = df[df['법정동시군구코드'].str.startswith("11")]

df_edit = df[['아파트', '법정동', '전용면적', '건축년도', '거래금액', '월', '층']]

# area = df10df_edit['전용면적'].str.split('.')
# df10df_edit['전용면적1'] = area.str.get(0)  # 전용면적 중 정수부분만 추출

# 숫자로 바꾸어 추출
df_edit['전용면적'] = pd.to_numeric(df_edit['전용면적'])
df_edit['전용면적1'] = round(df_edit['전용면적'], 2)
df_edit['전용면적1'] = df_edit['전용면적1'].astype(str)  # matching 을 위해 다시 합치기

df_edit['법정동'] = df_edit['법정동'].str.slice(start=1)

df_edit['matching'] = df_edit['법정동'] + " " + df_edit['전용면적1'] + " " + df_edit['건축년도']
df_edit['matching'].astype('str')
df_edit = df_edit.sort_values(by=['matching'])

df_price_202010 = df_edit[['matching', '아파트', '거래금액', '월', '층']]
df_price_202010 = df_price_202010.sort_values(by=['층'])  # 간혹 층이 음수값으로 기입된 경우가 있을 수 있으니 별도로 확인이 필요하다.
####################################################################################################
# 크롤링 데이터 불러오기
df_seoul = pd.read_excel('seminar data/Seoul_last.xlsx', header=0, skipfooter=0)

# 매칭을 위해 겹치는 열 만들기
df_seoul['건축년도'] = df_seoul['사용승인일'].dt.year
# 참고 : https://www.delftstack.com/ko/howto/python-pandas/how-to-extract-month-and-year-separately-from-datetime-column-in-pandas/

df_seoul['전용면적(㎡)'] = round(df_seoul['전용면적(㎡)'], 2)
df_seoul['전용면적1'] = df_seoul['전용면적(㎡)']

# df_seoul['전용면적1'] = df_seoul['전용면적(㎡)'].astype(int)
# 참고 : https://www.javaer101.com/ko/article/54022504.html

df_seoul['건축년도'] = df_seoul['건축년도'].astype(str)
df_seoul['전용면적1'] = df_seoul['전용면적1'].astype(str)

df_seoul['matching'] = df_seoul['법정동'] + " " + df_seoul['전용면적1'] + " " + df_seoul['건축년도']
df_seoul = df_seoul.sort_values(by=['matching'])
#####################################################################################################
# 'matching' 을 기준으로 합쳐보기

df_seoul_2017 = pd.merge(df_seoul, df_price_202010, on="matching")

df_seoul_2017['sorting1'] = df_seoul_2017['아파트_y'] + " " + df_seoul_2017['층'] + df_seoul_2017['거래금액']
df_seoul_2017 = df_seoul_2017.sort_values(by=['sorting1'])
df_seoul_2017 = df_seoul_2017.drop_duplicates(['sorting1'], keep='first')

df_seoul_2017['sorting2'] = df_seoul_2017['matching'] + " " + df_seoul_2017['층']
df_seoul_2017 = df_seoul_2017.sort_values(by=['sorting2'])
df_seoul_2017 = df_seoul_2017.drop_duplicates(['sorting2'], keep='first')

# 세부적인 조정
df_seoul_2017_2q = df_seoul_2017[['지역구', '법정동', '아파트_x', '아파트_y', '아파트코드', '사용승인일', '연수',
                                  '세대수', '주차대수_세대', '용적률', '건폐율', '위도', '경도', '건설사', '난방', '구조',
                                  '면적유형', '전용면적(㎡)', '전용률(%)', '방 개수', '화장실 개수', '층', '거래금액']]

df_seoul_2017_2q['층'] = pd.to_numeric(df_seoul_2017_2q['층'])

df_seoul_2017_2q['거래금액'] = df_seoul_2017_2q['거래금액'].str.slice(start=3)
df_seoul_2017_2q['거래금액'].iloc[0]
cost = df_seoul_2017_2q['거래금액'].str.split(',')
df_seoul_2017_2q['거래금액'] = cost.str.get(0) + cost.str.get(1)
df_seoul_2017_2q['거래금액'] = pd.to_numeric(df_seoul_2017_2q['거래금액'])

# df_seoul_2020_4q = df_seoul_2020_4q.sort_values(by=['아파트_x'])

df_seoul_2017_2q = df_seoul_2017_2q.dropna(axis=0)

# 엑셀파일로 변환 가격정보를 합쳤으므로 어떤 가격정보를 합쳤는지 표기해주기 위해 해당 시기를 붙일 것 ( 예) Seoul + 20204Q )
df_seoul_2017_2q.to_excel('seminar data/Seoul_20172Q.xlsx', index=False)

###########################################
