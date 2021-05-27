import pandas as pd

df = pd.read_excel('Seoul.xlsx')
df_seoul = df.dropna(axis=0)
df_seoul = df_seoul.drop_duplicates(['아파트코드'], keep='first')
df_seoul = df_seoul.sort_values(by=['아파트코드'])
df_seoul = df_seoul.reset_index(drop='Ture')
