# 2021-06-30
# chapter 7

# 아파트 단지별로 구한 distance 를 개별 아파트 위도, 경도 데이터를 기준으로 기존의 면적별 데이터에 매칭

# import packages
import pandas as pd


########################################################################################################################
# 엑셀 불러오기

df_seoul = pd.read_excel('seminar data/Seoul_last.xlsx', header=0, skipfooter=0)

df_distance = pd.read_excel('seminar data/Seoul_including_distance.xlsx', header=0, skipfooter=0)

# distance dataframe 조작

# 위도와 경도를 문자열로 바꾸어 인덱스화 시키기
# 인덱스를 기준으로 매칭
#


