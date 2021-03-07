import pandas as pd
import numpy as np
import openpyxl

df_Gangnam = pd.read_excel('data(95to07).xlsx', sheet_name='price', header=0, skipfooter=0, usecols="A,D")

df_Gangnam['L1_Gangnam'] = df_Gangnam['Gangnam'].shift(1)

df_Gangnam['p_rate'] = (df_Gangnam['Gangnam']/df_Gangnam['L1_Gangnam'] -1) *100

df_Gangnam['p_dot'] = (df_Gangnam['Gangnam'] / df_Gangnam['L1_Gangnam']) * 100
df_Gangnam = df_Gangnam.drop('L1_Gangnam', axis=1)
df_Gangnam = df_Gangnam.fillna(method='bfill')

df_Gangnam['x0'] = np.where(df_Gangnam['p_rate'] < 0, -1, 1)
df_Gangnam['cum_x0'] = df_Gangnam['x0']

for i in range(len(df_Gangnam)):
    if i == 0:
        if df_Gangnam['x0'][i] == 1:
            df_Gangnam['cum_x0'][i] = 1
        else:
            df_Gangnam['cum_x0'][i] = 0
    else:
        if df_Gangnam['x0'][i] == df_Gangnam['x0'][i - 1]:
            df_Gangnam['cum_x0'][i] = df_Gangnam['cum_x0'][i - 1] + df_Gangnam['x0'][i]
        else:
            df_Gangnam['cum_x0'][i] = df_Gangnam['x0'][i]

df_Gangnam['x'] = df_Gangnam['cum_x0']

df_Gangnam = df_Gangnam.drop(['x0', 'cum_x0'], axis=1)

df_Gangnam_ch = pd.read_excel('data(95to07).xlsx', sheet_name='chonsei', header=0, skipfooter=0, usecols="D")
df_Gangnam_ch = df_Gangnam_ch.rename({'Gangnam':'Gangnam_ch'},axis=1)

df_Gangnam = pd.concat([df_Gangnam, df_Gangnam_ch], axis=1)

# sovereign yield
df_sovereign = pd.read_excel('data(95to07).xlsx', sheet_name='sovereign yield', header=0, skipfooter=0, usecols="B")
df_Gangnam = pd.concat([df_Gangnam, df_sovereign], axis=1)

df_Gangnam['R'] = df_Gangnam['Gangnam_ch'] * df_Gangnam['sovereign yield']

df_Gangnam['c'] = df_Gangnam['R'] / df_Gangnam['Gangnam']
df_Gangnam['b'] = df_Gangnam['Gangnam_ch'] / df_Gangnam['Gangnam']

df_Gn = df_Gangnam.rename({'sovereign yield': 'i'}, axis=1)

df_Gn['p_dot-1'] = df_Gn['p_dot'].shift(3)
df_Gn = df_Gn.fillna(method='bfill')

### print the descriptive statistics for the variables used in the logits
mean = df_Gn.mean(axis=0)
std = df_Gn.std(axis=0)
min = df_Gn.min(axis=0)
max = df_Gn.max(axis=0)

# In the df_GN, we can identify the variables to calculate the regression.
df_Gn['lnP'] = np.log(df_Gn['p_dot'])
df_Gn['lnP-1'] = np.log(df_Gn['p_dot-1'])
df_Gn['lnc'] = np.log(df_Gn['c'])
df_Gn['lni'] = np.log(df_Gn['i'])
df_Gn['lnb'] = np.log(df_Gn['b'])

df_GN = df_Gn.drop({'Gangnam','Gangnam_ch','R','p_dot','p_dot-1','i','c','b','p_rate'}, axis=1)

##df = df[['e','c','b','f','d','a']]
df_GN = df_GN[['lnP','lnb','lnc','lnP-1','x','lni']]

df_GN.to_excel('Gangnam_95to07.xlsx')

import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as plt
import seaborn as sns

# X1 is independent variable
##X1 = df_Gangnam['lnc']
# Y is dependent variable
##Y = df_Gangnam['lnP']

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
Y = df_GN['lnP']
X1 = df_GN[['lnc', 'lnP-1', 'x']]
X1m = sm.add_constant(X1)

K1m = sm.OLS(Y, X1m).fit()
K1m.summary()

##regression 2)
X2 = df_GN[['lnc','lnP-1','x','lni']]
X2m = sm.add_constant(X2)
K2m = sm.OLS(Y,X2m).fit()
K2m.summary()

##regression 3)
X3 = df_GN[['lnb', 'lnP-1', 'x', 'lni']]
X3m = sm.add_constant(X3)
K3m = sm.OLS(Y,X3m).fit()
df_1 = K3m.summary()
