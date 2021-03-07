import pandas as pd
import numpy as np
import openpyxl

df_Gangbuk = pd.read_excel('data(95to07).xlsx', sheet_name='price', header=0, skipfooter=0, usecols="A,C")

df_Gangbuk['L1_Gangbuk'] = df_Gangbuk['Gangbuk'].shift(1)

df_Gangbuk['p_rate'] = (df_Gangbuk['Gangbuk'] / df_Gangbuk['L1_Gangbuk'] - 1) * 100
df_Gangbuk['p_dot'] = (df_Gangbuk['Gangbuk'] / df_Gangbuk['L1_Gangbuk']) * 100
df_Gangbuk = df_Gangbuk.drop('L1_Gangbuk', axis=1)
df_Gangbuk = df_Gangbuk.fillna(method='bfill')

df_Gangbuk['x0'] = np.where(df_Gangbuk['p_rate'] < 0, -1, 1)
df_Gangbuk['cum_x0'] = df_Gangbuk['x0']

for i in range(len(df_Gangbuk)):
    if i == 0:
        if df_Gangbuk['x0'][i] == 1:
            df_Gangbuk['cum_x0'][i] = 1
        else:
            df_Gangbuk['cum_x0'][i] = 0
    else:
        if df_Gangbuk['x0'][i] == df_Gangbuk['x0'][i - 1]:
            df_Gangbuk['cum_x0'][i] = df_Gangbuk['cum_x0'][i - 1] + df_Gangbuk['x0'][i]
        else:
            df_Gangbuk['cum_x0'][i] = df_Gangbuk['x0'][i]

df_Gangbuk['x'] = df_Gangbuk['cum_x0']

df_Gangbuk = df_Gangbuk.drop(['x0', 'cum_x0'], axis=1)

df_Gangbuk_ch = pd.read_excel('data(95to07).xlsx', sheet_name='chonsei', header=0, skipfooter=0, usecols="C")
df_Gangbuk_ch = df_Gangbuk_ch.rename({'Gangbuk':'Gangbuk_ch'},axis=1)

df_Gangbuk = pd.concat([df_Gangbuk, df_Gangbuk_ch], axis=1)

# sovereign yield
df_sovereign = pd.read_excel('data(95to07).xlsx', sheet_name='sovereign yield', header=0, skipfooter=0, usecols="B")
df_Gangbuk = pd.concat([df_Gangbuk, df_sovereign], axis=1)

df_Gangbuk['R'] = df_Gangbuk['Gangbuk_ch'] * df_Gangbuk['sovereign yield']

df_Gangbuk['c'] = df_Gangbuk['R'] / df_Gangbuk['Gangbuk']
df_Gangbuk['b'] = df_Gangbuk['Gangbuk_ch'] / df_Gangbuk['Gangbuk']

df_Gb = df_Gangbuk.rename({'sovereign yield': 'i'}, axis=1)

df_Gb = df_Gb[df_Gb['p_dot'] > 0]

df_Gb['p_dot-1'] = df_Gb['p_dot'].shift(3)
df_Gb = df_Gb.fillna(method='bfill')

### print the descriptive statistics for the variables used in the logits
mean = df_Gb.mean(axis=0)
std = df_Gb.std(axis=0)
min = df_Gb.min(axis=0)
max = df_Gb.max(axis=0)

# In the df_GB, we can identify the variables to calculate the regression.
df_Gb['lnP'] = np.log(df_Gb['p_dot'])
df_Gb['lnP-1'] = np.log(df_Gb['p_dot-1'])
df_Gb['lnc'] = np.log(df_Gb['c'])
df_Gb['lni'] = np.log(df_Gb['i'])
df_Gb['lnb'] = np.log(df_Gb['b'])

df_GB = df_Gb.drop({'Gangbuk','Gangbuk_ch','R','p_dot','p_dot-1','i','c','b','p_rate'}, axis=1)

##df = df[['e','c','b','f','d','a']]
df_GB = df_GB[['lnP','lnb','lnc','lnP-1','x','lni']]

df_GB.to_excel('Gangbuk_95to07.xlsx')

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as plt
import seaborn as sns

# X1 is independent variable
##X1 = df_Gangbuk['lnc']
# Y is dependent variable
##Y = df_Gangbuk['lnP']

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
Y = df_GB['lnP']
X1 = df_GB[['lnc', 'lnP-1', 'x']]
X1m = sm.add_constant(X1)

K1m = sm.OLS(Y, X1m).fit()
K1m.summary()

##regression 2)
X2 = df_GB[['lnc','lnP-1','x','lni']]
X2m = sm.add_constant(X2)
K2m = sm.OLS(Y,X2m).fit()
K2m.summary()

##regression 3)
X3 = df_GB[['lnb', 'lnP-1', 'x', 'lni']]
X3m = sm.add_constant(X3)
K3m = sm.OLS(Y,X3m).fit()
K3m.summary()
