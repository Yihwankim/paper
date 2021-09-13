#!/usr/bin/env python
# coding: utf-8

# In[37]:


pip install Stargazer


# In[38]:


# import packages
from tqdm import tqdm
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from stargazer.stargazer import Stargazer

from urllib.request import urlopen
import json
 
import plotly.express as px #빠르게 사용
import plotly.graph_objects as go  #디테일하게 설정해야할때
import plotly.figure_factory as ff
from plotly.subplots import make_subplots # 여러 subplot을 그릴때 
from plotly.validators.scatter.marker import SymbolValidator # 마커사용


# filenames = []
# 
# for i in range(9):
#     file = 'seoul_20'+str(i+11)
#     filenames.append(file)

# ### Before Covid

# #### Time dummy를 만들어 before covid data 만들기

# In[16]:


dfs = []
for i in range(9):
    df = pd.read_excel('yearly_edit/'+'seoul_20'+str(i+11)+'.xlsx')
    df['time'] = i+1
    dfs.append(df)


# dfs = []
# for fname in filenames:
#     df = pd.read_excel('yearly_edit/{}.xlsx'.format(fname))
#     df
#     dfs.append(df)    

# In[17]:


df_bf_covid = pd.concat(dfs, axis=0)


# In[20]:


for i in range(9):
    df_bf_covid['D'+str(i+11)] = np.where(df_bf_covid['time'] == i+1, 1, 0)


# df_bf_covid = df_bf_covid.dropna() 
# df_bf_covid.to_excel('before_after/before_covid.xlsx')

# #### 데이터 분석

# In[ ]:


est = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:4]])).fit()
est2 = sm.OLS(endog=df['target'], exog=sm.add_constant(df[df.columns[0:6]])).fit()


# In[66]:


df_bf_covid['log_per_Pr'] = np.log(df_bf_covid['per_Pr'])
df_bf_covid['log_num'] = np.log(df_bf_covid['num'])

X = sm.add_constant(df_bf_covid[['year', 'year_sq', 'log_num', 'car_per', 'area', 'room', 'toilet', 'floor', 'floor_sq',
                                 'H2', 'H3', 'T2', 'T3', 'C1', 'FAR', 'BC', 'Efficiency', 'dist_elem', 'dist_middle', 
                                 'dist_high', 'dist_sub', 'dist_park',
                                 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 
                                 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19']])

Y = df_bf_covid['log_per_Pr']

bf_res = sm.OLS(endog=Y, exog=X).fit()
#ols_model = sm.OLS(Y, X.values)
#bf_res = ols_model.fit()
bf_result = bf_res.summary(xname=X.columns.tolist())
bf_result


# In[60]:





# ### After Covid

# In[27]:


df_af_covid = pd.read_excel('yearly_edit/seoul_2020.xlsx')


# In[28]:


df_af_covid['log_per_Pr'] = np.log(df_af_covid['per_Pr'])


# df_af_covid = df_af_covid.dropna()
# df_af_covid.to_excel('before_after/after_covid.xlsx')

# In[67]:


df_af_covid['log_num'] = np.log(df_af_covid['num'])

X = sm.add_constant(df_af_covid[['year', 'year_sq', 'log_num', 'car_per', 'area', 'room', 'toilet', 'floor', 'floor_sq', 
                                 'H2', 'H3', 'T2', 'T3', 'C1', 'FAR', 'BC', 'Efficiency',
                                 'dist_elem', 'dist_middle', 'dist_high', 'dist_sub', 'dist_park', 
                                 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11']])

Y = df_af_covid['log_per_Pr']

af_res = sm.OLS(endog=Y, exog=X).fit()
#ols_model = sm.OLS(Y, X.values)
#af_res = ols_model.fit()
af_result = af_res.summary(xname=X.columns.tolist())
af_result


# ### 기술통계량 분석

# In[72]:


pd.set_option('display.max_columns',None)


# In[73]:


df_bf_covid.describe()


# In[71]:


df_bf_covid.sum()


# In[74]:


df_af_covid.describe()


# In[75]:


df_af_covid.sum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 결과값 출력

# In[50]:


from IPython.core.display import HTML


# In[58]:


stargazer = Stargazer([bf_res, af_res])


# In[59]:


HTML(stargazer.render_html())


# In[47]:


html_file = open('html_file.html', 'w')
html_file.write(results)
html_file.close()


# In[48]:


stargazer.render_latex()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




