import os
import json
import datetime

import pandas as pd

import re

df1 = pd.read_csv('final_updated.csv')


# def re_sp_c(x):
#     re_d = re.sub('[^A-Za-z0-9]+', str(x))
#     return re_d


df1['Comments'] = df1['Comments'].apply(lambda x: re.sub('[^A-Za-z0-9]+',' ', str(x)))
# print(df1['Comments'].dtypes)
nan_value = float("NaN")
df1.replace(" ", nan_value, inplace=True)
df1.dropna(subset = ["Comments"],inplace=True)
print(df1['Comments'].head(30))
print(df1.shape)
df1.to_csv('re_sp_c.csv', index=False)
# df1['Engagement Rate'] = df1['Engagement Rate'] * 100
# g = df1.sample(frac=1).reset_index(drop=True)
# g.to_csv('final_remove_.csv', index=False)

# print(g.head())
