# 2021-04-23

# 최종 비교시 고려할 사항
#

# Import packages
import pandas as pd
import numpy as np

#############################################################################################################
# 엑셀 파일 한번에 불러오기
# 강북 엑셀파일 불러오기

filenames_GB = [
    'Dobonggu_edit4', 'Dongdaemoongu_edit4',
    'Eunpyeonggu_edit4', 'Gangbukgu_edit4',
    'Gwangjingu_edit4', 'Jongnogu_edit4',
    'Junggu_edit4', 'Jungnanggu_edit4',
    'Mapogu_edit4', 'Nowongu_edit4',
    'Seodaemungu_edit4', 'Seongbukgu_edit4',
    'Seongdonggu_edit4', 'Yongsangu_edit4'
]

dfs = []

for fname in filenames_GB:
    print('Loading {}'.format(fname))

    df = pd.read_excel('Gangbuk_edit4/{}.xlsx'.format(fname))
    # df.columns = [fname]

    dfs.append(df)

print('Data loading is completed!')

df_GB = pd.concat(dfs, axis=0)  # axis=0 : 밑으로 붙이기

# 강남 엑셀파일 불러오기

filenames_GN = [
    'Dongjakgu_edit4', 'Gangdonggu_edit4',
    'Gangnamgu_edit4', 'Gangseogu_edit4',
    'Geumcheongu_edit4', 'Gurogu_edit4',
    'Gwanakgu_edit4', 'Seochogu_edit4',
    'Songpagu_edit4', 'Yangcheongu_edit4',
    'Yeongdeungpogu_edit4']

dfs2 = []

for fname in filenames_GN:
    print('Loading {}'.format(fname))

    df = pd.read_excel('Gangnam_edit4/{}.xlsx'.format(fname))
    # df.columns = [fname]

    dfs2.append(df)

print('Data loading is completed!')

df_GN = pd.concat(dfs2, axis=0)  # axis=0 : 밑으로 붙이기

###########################################################################################

# 강북데이터와 강남데이터를 각각 edit4 폴더에 새롭게 저장한 후 합치기

df_GB.to_excel('Gangbuk_edit4/Gangbuk_total.xlsx', sheet_name='Gangbuk', index=False)
df_GN.to_excel('Gangnam_edit4/Gangnam_total.xlsx', sheet_name='Gangnam', index=False)

df_seoul = pd.concat([df_GB, df_GN], axis=0)

# seoul data 편집하기

df_seoul.replace('-', np.nan)

df = df_seoul[['Gu', '읍면동', 'Apt_name']]

# number 편집
df['세대수'] = df_seoul['number'].str.split('(', n=1, expand=True)
df['세대수'] = df['세대수'].str.slice(start=0, stop=-2)
df['세대수'] = pd.to_numeric(df['세대수'])

# floor 편집
df[['저층', '고층']] = df_seoul['floor'].str.split('/', expand=True)
df['저층'] = df['저층'].str.slice(start=0, stop=-1)
df['저층'] = pd.to_numeric(df['저층'])
df['고층'] = df['고층'].str.slice(start=0, stop=-1)
df['고층'] = pd.to_numeric(df['고층'])

# car 편집
df[['주차대수_총', '주차대수_세대']] = df_seoul['car'].str.split('(', n=1, expand=True)
df['주차대수_총'] = df['주차대수_총'].str.slice(start=0, stop=-1)
df['주차대수_총'] = pd.to_numeric(df['주차대수_총'])

df['주차대수_세대'] = df['주차대수_세대'].str.slice(start=4, stop=-2)
df['주차대수_세대'] = pd.to_numeric(df['주차대수_세대'])

# FAR (용적률) 편집
df['용적률'] = pd.to_numeric(df_seoul['FAR'].str.slice(start=0, stop=-1))

# BC (건폐율) 편집
df['건폐율'] = pd.to_numeric(df_seoul['BC'].str.slice(start=0, stop=-1))

# 건설사, 난방
df[['건설사', '난방']] = df_seoul[['con', 'heat']]

# 아파트코드, 위도, 경도
df['아파트코드'] = pd.to_numeric(df_seoul['code'])
df['위도'] = pd.to_numeric(df_seoul['lat'])
df['경도'] = pd.to_numeric(df_seoul['long'])

# 면적정보
df['면적유형'] = df_seoul['type_capacity']

# 크기
area_inform = df_seoul['area'].str.split('/')
df['공급면적(㎡)'] = area_inform.str.get(0)
df['공급면적(㎡)'] = df['공급면적(㎡)'].str.slice(start=0, stop=-1)
df['공급면적(㎡)'] = pd.to_numeric(df['공급면적(㎡)'])  # 오류발생

area_inform2 = area_inform.str.get(1)
area_inform2 = area_inform2.str.split('(')

df['전용면적(㎡)'] = area_inform2.str.get(0)
df['전용면적(㎡)'] = df['전용면적(㎡)'].str.slice(start=0, stop=-1)
df['전용면적(㎡)'] = pd.to_numeric(df['전용면적(㎡)'])

df['전용률(%)'] = area_inform2.str.get(1)
df['전용률(%)'] = df['전용률(%)'].str.slice(start=4, stop=-2)

# 방, 화장실 개수
df['방 개수'] = df_seoul['room'].str.slice(start=0, stop=-1)
df['방 개수'] = pd.to_numeric(df['방 개수'])  # 오류발생

df['화장실 개수'] = df_seoul['toilet'].str.slice(start=0, stop=-1)
df['화장실 개수'] = pd.to_numeric(df['화장실 개수'])  # 오류발생

# 구조, 해당면적 세대수
df['구조'] = df_seoul['structure']

df['해당면적 세대수'] = df_seoul['n_this_area'].str.slice(start=0, stop=-2)
df['해당면적 세대수'] = pd.to_numeric(df['해당면적 세대수'])  # 오류발생

# 해당면적 세대수, 화장실 개수, 방 개수, 공급면적이 숫자로 처리되지 않고 문자열로 처리되어 있는 상태
# 확인 및 변경이 요구됨

df.to_excel('Seoul.xlsx', sheet_name='total', index=False)
