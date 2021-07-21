import os
import json
import datetime

import pandas as pd
import numpy as np
import re

df1 = pd.read_csv('final_updated.csv')

# def re_sp_c(x):
#     re_d = re.sub('[^A-Za-z0-9]+', str(x))
#     return re_d


df1['Comments'] = df1['Comments'].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', str(x)))
# print(df1['Comments'].dtypes)
nan_value = float("NaN")
df1.replace(" ", nan_value, inplace=True)
df1.dropna(subset=["Comments"], inplace=True)
# print(df1['Comments'].head(30))
filters = [(df1['Engagement Rate'] >= 0.08) & (df1['Engagement Rate'] <= 0.14), (df1['Engagement Rate'] <= 0.07)]
values = [1, 2]
df1['Ratings'] = np.select(filters, values)

filters2 = [(df1['Ratings'] == 1), (df1['Ratings'] == 2)]
values2 = ['happy', 'not happy']
df1['Is_Response'] = np.select(filters2, values2)

df1.to_csv('re_sp_c.csv', index=False)
# df1['Engagement Rate'] = df1['Engagement Rate'] * 100
# g = df1.sample(frac=1).reset_index(drop=True)
# g.to_csv('final_remove_.csv', index=False)

# print(g.head())

# The first column is Ratings : if Engagement.rate = 0,08 to 0.14,
# Ratings =1, Engagement.rate = 0 to 0.07 Ratings =2

# The second column is : Is_Response, if Ratings =1, Is_Response = happy, if Ratings =2, Is_Response = not happy
