'''
목표)
1. Time_dummy 만들기
2. 현재 추가된 더미변수: 건설사
3. 해야할 작업:
    a) 건설사 더미 이름 변경: C1
    b) 시점에 따라 Time _dummy 추가하기: D1 ~ D42 , clear
    c) 층, 연수 등의 변수를 로그화 시키기
    d) 최종 회귀분석
'''

# import packages
from tqdm import tqdm
import pandas as pd
import datetime
import numpy as np
import statsmodels.api as sm

########################################################################################################################
for i in tqdm(range(42)):
    df_q = pd.read_excel('Hedonic_index/Quarterly/seoul_apt' + str(i + 1) + '.xlsx', header=0, skipfooter=0,
                         usecols='B:AU')
    df_q['log_per_Pr'] = np.log(df_q['per_Pr'])

    X = sm.add_constant(df_q[['year', 'year_sq', 'num', 'car', 'car_per', 'area', 'room', 'toilet', 'floor', 'floor_sq',
                              'H1', 'H2', 'H3', 'T1', 'T2', 'T3', 'C1', 'FAR', 'BC', 'Efficiency', 'dist_elem',
                              'dist_middle', 'dist_high', 'dist_sub', 'dist_park', 'G1', 'G2', 'G3', 'G4', 'G5', 'S1',
                              'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11']])
    Y = df_q['log_per_Pr']

    rlm_model = sm.RLM(Y, X.values, M=sm.robust.norms.HuberT())
    res = rlm_model.fit()
    print('Number' + str(i + 1) + 'regression result: ')
    print(res.summary(xname=X.columns.tolist()))
    print('#########################################################################################')



#####################################################################################################################


