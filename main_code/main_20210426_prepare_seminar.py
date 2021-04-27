# import packages
import pandas as pd
import numpy as np

df = pd.read_excel('Seoul_last.xlsx', header=0, skipfooter=0)

df1 = df


df1 = df1.drop_duplicates(['아파트코드'], keep='first')
df1 = df1.sort_values(by=['지역구'])

df1.to_excel('Seoul_last_sorting.xlsx', sheet_name='last', index=False)

