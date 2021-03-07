import pandas as pd

df_areacode = pd.read_csv('https://goo.gl/tM6r3v', sep='\t', dtype={'법정동코드':str})
df_areacode.head()

len(df_areacode)

# Get rid of the unused data.
## 폐지여부가 존재인 행만 남기는 방식
df_areacode = df_areacode[df_areacode['폐지여부']=='존재']
len(df_areacode)

# 지역 구분은 5가지 레벨로 이루어져 있다.
# 이중에서 시/도 를 추출하고자 한다면, 총 10자리 숫자중 뒤쪽 8자리가 모두 '0'인 행을 추출하는 방법을 사용 가능하다.
# 앞의 2자리는 임의의 정수, 뒤의 8자리는 0으로 배정
df_province = df_areacode[ df_areacode['법정동코드'].str.contains('\d{2}0{8}')]
df_province

# 그렇지만 예외로서 '세종특별자치시'가 있으므로 이를 넣어준다.
# 3611000000 : 세종특별자치시

df_province = df_areacode[ df_areacode['법정동코드'].str.contains('\d{2}0{8}|36110{6}')]
df_province

# 간단하게 함수로 정리 해보자.

def get_areacode():
    df_areacode = pd.read_csv('https://goo.gl/tM6r3v', sep='\t', dtype={'법정동코드':str, '법정동명':str})
    df_areacode = df_areacode[df_areacode['폐지여부'] == '존재']
    df_areacode = df_areacode[['법정동코드', '법정동명']]
    return df_areacode

def get_province():
    df_areacode = get_areacode()
    df_province = df_areacode[ df_areacode['법정동코드'].str.contains('\d{2}0{8}|36110{6}')]
    return df_province

get_province()

p = '제주특별자치도'
df_province.loc[df_province['법정동명']==p, '법정동코드'].values[0]

# 법정동 데이터를 활용해서 특정 지역의 아파트 단지명을 불러오는 방법에 대해 공부해보기
