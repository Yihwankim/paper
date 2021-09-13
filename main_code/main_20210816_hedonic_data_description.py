# import packages
from typing import Any

from tqdm import tqdm
import pandas as pd
import datetime
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
########################################################################################################################
df_hedonic = pd.read_excel('results/hedonic_variable.xlsx', header=0, skipfooter=0)
'''
df_independent = df_hedonic.iloc[:, 1:]

X = df_independent
Y = df_hedonic['Pr']

mlr = LinearRegression()
mlr.fit(X, Y)
'''

