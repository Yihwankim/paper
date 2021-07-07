# import packages
import pickle
import pandas as pd
import datetime

data01 = pd.read_pickle('data_processed/df_dataset_201301.pkl')
data02 = pd.read_pickle('data_processed/df_dataset_201302.pkl')
data03 = pd.read_pickle('data_processed/df_dataset_201303.pkl')
data04 = pd.read_pickle('data_processed/df_dataset_201304.pkl')
data05 = pd.read_pickle('data_processed/df_dataset_201305.pkl')
data06 = pd.read_pickle('data_processed/df_dataset_201306.pkl')
data07 = pd.read_pickle('data_processed/df_dataset_201307.pkl')
data08 = pd.read_pickle('data_processed/df_dataset_201308.pkl')
data09 = pd.read_pickle('data_processed/df_dataset_201309.pkl')

####################################################################################################
# 2020년 10월 부터 12월, 4분기 실거래가 데이터와 매칭시키기
data_13 = pd.concat([data01, data02, data03, data04, data05, data06, data07, data08, data09], axis=0)


# 크롤링 데이터와 매칭 시키기
df = data_13.loc[data_13['법정동시군구코드'].str.contains("11")]  # 서울지역은 11 포함
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

# 'matching' KEY 값 만들기
df_edit['matching'] = df_edit['법정동'] + " " + df_edit['전용면적1'] + " " + df_edit['건축년도']
df_edit['matching'].astype('str')
df_edit = df_edit.sort_values(by=['matching'])

df_price_2013 = df_edit[['matching', '아파트', '거래금액', '월', '층']]
df_price_2013 = df_price_2013.sort_values(by=['층'])  # 간혹 층이 음수값으로 기입된 경우가 있을 수 있으니 별도로 확인이 필요하다.
####################################################################################################
# 크롤링 데이터 불러오기
df_seoul = pd.read_excel('Replicate_education/seoul_replicating_dummy.xlsx', header=0, skipfooter=0)

# 매칭을 위해 KEY 값 만들기
df_seoul['건축년도'] = df_seoul['사용승인일'].dt.year
# 참고 : https://www.delftstack.com/ko/howto/python-pandas/how-to-extract-month-and-year-separately-from-datetime-column-in-pandas/

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
#####################################################################################################
# 'matching' 을 기준으로 합쳐보기
df_seoul_2013 = pd.merge(df_seoul, df_price_2013, on="matching")

# 데이터 전처리
# 중복제거 (1) : 동일 아파트에서 비슷한 유형의 경우 같은 매물로 묶이는 문제를 제거하기 위함
df_seoul_2013['sorting1'] = df_seoul_2013['아파트_y'] + " " + df_seoul_2013['층'] + df_seoul_2013['거래금액']
df_seoul_2013 = df_seoul_2013.sort_values(by=['sorting1'])
df_seoul_2013 = df_seoul_2013.drop_duplicates(['sorting1'], keep='first')

# 중북제거 (2) : 데이터 중에서 KEY 값과 층 정보가 같다면 동일한 매물로서 처리하여 중복값 제거
df_seoul_2013['sorting2'] = df_seoul_2013['matching'] + " " + df_seoul_2013['층']
df_seoul_2013 = df_seoul_2013.sort_values(by=['sorting2'])
df_seoul_2013 = df_seoul_2013.drop_duplicates(['sorting2'], keep='first')

# 세부적인 조정
df_seoul_replicating = df_seoul_2013[['지역구', '법정동', '아파트_x', '아파트_y', '아파트코드', '사용승인일', '연수',
                                      '세대수', '저층', '고층', '주차대수_총', '주차대수_세대', '용적률', '건폐율', '위도',
                                      '경도', '건설사', '난방', '구조', '면적유형', '전용면적', '전용률', '방개수', '화장실개수',
                                      'dist_elem', 'dist_middle', 'dist_high', 'dist_sub', 'dist_park', '층', '거래금액',
                                      'H1', 'H2', 'H3', 'T1', 'T2', 'T3', 'G1', 'D100', 'D200', 'D300', 'D400',
                                      'D500', 'D600', 'D700', 'D800', 'D900', 'D1000', 'D1100', 'D1200', 'DOVER']]

df_seoul_replicating['층'] = pd.to_numeric(df_seoul_replicating['층'])
df_seoul_replicating['거래금액'].iloc[0]

df_seoul_replicating['거래금액'] = df_seoul_replicating['거래금액'].str.slice(start=4)
df_seoul_replicating['거래금액'].iloc[0]

cost = df_seoul_replicating['거래금액'].str.split(',')
df_seoul_replicating['거래금액'] = cost.str.get(0) + cost.str.get(1)
df_seoul_replicating['거래금액'] = pd.to_numeric(df_seoul_replicating['거래금액'])

# df_seoul_2020_4q = df_seoul_2020_4q.sort_values(by=['아파트_x'])

df_seoul_replicating = df_seoul_replicating.dropna(axis=0)

# 엑셀파일로 변환 가격정보를 합쳤으므로 어떤 가격정보를 합쳤는지 표기해주기 위해 해당 시기를 붙일 것 ( 예) Seoul + 20204Q )
df_seoul_replicating.to_excel('Replicate_education/Seoul_20131Q3Q.xlsx', index=False)

###########################################
