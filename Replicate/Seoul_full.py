import pandas as pd
import numpy as np
import openpyxl

df_Seoul = pd.read_excel('data(fulltime).xlsx', sheet_name='price', header=0, skipfooter=0, usecols="A:B")


#각 대통령 임기별 부동산 가격 변화를 알아보기 위해 data set을 편집할 경우
#df_dj = df_Seoul.iloc[34:94,:]
#df_mh = df_Seoul.iloc[94:154,:]
#df_mb = df_Seoul.iloc[154:214,:]
#df_gh = df_Seoul.iloc[214:263,:]
#df_ji = df_Seoul.iloc[263:309,:]


df_Seoul['L1_Seoul'] = df_Seoul['Seoul'].shift(1)

df_Seoul['p_rate'] = (df_Seoul['Seoul'] / df_Seoul['L1_Seoul'] - 1) * 100
df_Seoul['p_dot'] = (df_Seoul['Seoul'] / df_Seoul['L1_Seoul']) * 100
df_Seoul = df_Seoul.fillna(method='bfill')

df_Seoul['x0'] = np.where(df_Seoul['p_rate'] < 0, -1, 1)
df_Seoul['cum_x0'] = df_Seoul['x0']

for i in range(len(df_Seoul)):
    if i == 0:
        if df_Seoul['x0'][i] == 1:
            df_Seoul['cum_x0'][i] = 1
        else:
            df_Seoul['cum_x0'][i] = 0
    else:
        if df_Seoul['x0'][i] == df_Seoul['x0'][i - 1]:
            df_Seoul['cum_x0'][i] = df_Seoul['cum_x0'][i - 1] + df_Seoul['x0'][i]
        else:
            df_Seoul['cum_x0'][i] = df_Seoul['x0'][i]

df_Seoul['x'] = df_Seoul['cum_x0']

df_Seoul = df_Seoul.drop(['x0', 'cum_x0'], axis=1)

df_Seoul_ch = pd.read_excel('data(fulltime).xlsx', sheet_name='chonsei', header=0, skipfooter=0, usecols="B")
df_Seoul_ch = df_Seoul_ch.rename({'Seoul':'Seoul_ch'},axis=1)

df_Seoul = pd.concat([df_Seoul, df_Seoul_ch], axis=1)

#sovereign sovereign yield

# sovereign yield
df_sovereign = pd.read_excel('data(fulltime).xlsx', sheet_name='sovereign yield', header=0, skipfooter=0, usecols="B")
df_Seoul = pd.concat([df_Seoul, df_sovereign], axis=1)

df_Seoul['R'] = df_Seoul['Seoul_ch'] * df_Seoul['sovereign yield']

df_Seoul['c'] = df_Seoul['R'] / df_Seoul['Seoul']
df_Seoul['b'] = df_Seoul['Seoul_ch'] / df_Seoul['Seoul']

df_Se = df_Seoul.rename({'sovereign yield': 'i'}, axis=1)

df_Se = df_Se[df_Se['p_dot'] > 0]

df_Se['p_dot-1'] = df_Se['p_dot'].shift(3)
df_Se = df_Se.fillna(method='bfill')

# In the df_Se, we can identify the variables to calculate the regression.
df_Se['lnP'] = np.log(df_Se['p_dot'])
df_Se['lnP-1'] = np.log(df_Se['p_dot-1'])
df_Se['lnc'] = np.log(df_Se['c'])
df_Se['lni'] = np.log(df_Se['i'])
df_Se['lnb'] = np.log(df_Se['b'])

df_SE = df_Se.drop({'Seoul','Seoul_ch','R','p_dot','p_dot-1','i','c','b','p_rate'}, axis=1)

##df = df[['e','c','b','f','d','a']]
df_SE = df_SE[['lnP','lnb','lnc','lnP-1','x','lni']]

df_SE.to_excel('Seoul_full.xlsx')

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as plt
import seaborn as sns

# X1 is independent variable
##X1 = df_Seoul['lnc']
# Y is dependent variable
##Y = df_Seoul['lnP']

###sns.scatterplot(X1, Y)

# Add the constant value
##X = sm.add_constant(X1)

# fitting the variables to model
##results = sm.OLS(Y, X).fit()

# summary of the model
###results.summary()

### okay, Let's start the test
# fitting the regression

##regression 1)
Y = df_SE['lnP']
X1 = df_SE[['lnc', 'lnP-1', 'x']]
X1m = sm.add_constant(X1)

K1m = sm.OLS(Y, X1m).fit()
K1m.summary()

##regression 2)
X2 = df_SE[['lnc','lnP-1','x','lni']]
X2m = sm.add_constant(X2)
K2m = sm.OLS(Y,X2m).fit()
K2m.summary()

##regression 3)
X3 = df_SE[['lnb', 'lnP-1', 'x', 'lni']]
X3m = sm.add_constant(X3)
K3m = sm.OLS(Y,X3m).fit()
K3m.summary()
