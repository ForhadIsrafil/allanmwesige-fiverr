import os
import json
import datetime

import pandas as pd
import numpy as np
import re

df = pd.read_csv('data/1000clean.csv')
df1 = df[df['Comments'].astype(str).map(len) > 25]
# def re_sp_c(x):
#     re_d = re.sub('[^A-Za-z0-9]+', str(x))
#     return re_d


df1['Comments'] = df1['Comments'].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', str(x)))
# print(df1['Comments'].dtypes)
# nan_value = float("NaN")
# df1.replace(" ", nan_value, inplace=True)
df1.dropna(subset=["Comments"], inplace=True)
# print(df1['Comments'].head(30))
filters = [(df1['Engagement_Rate'] >= 0.08) & (df1['Engagement_Rate'] <= 0.14), (df1['Engagement_Rate'] <= 0.07)]
values = [1, 2]
df1['Ratings'] = np.select(filters, values)

filters2 = [(df1['Ratings'] == 1), (df1['Ratings'] == 2)]
values2 = ['happy', 'not happy']
df1['Is_Response'] = np.select(filters2, values2)
df1.columns = df1.columns.str.replace(' ', '_')
# df2 = df1[df1['Comments'].astype(str).map(len) > 25]
df2 = df1
df2.loc[df2['Ratings'] == 0, 'Ratings'] = 1
df2.loc[df2['Is_Response'] == '0', 'Is_Response'] = 'happy'
# df2.drop(columns=['Category', 'Video_or_Photo'], axis=1, inplace=True)
df2.dropna(subset=['Comments'], inplace=True)
# df2.set_index("User_ID")
df2.sort_values("User_ID", inplace=True)
print(df2.shape)
print(df2.head())
# ======================
csv1 = df2.iloc[:106456, :]
# csv2 = df2.iloc[106456:212913, :]
# csv3 = df2.iloc[212913:319369, :]
# csv4 = df2.iloc[319369:425825, :]
#
csv1.to_csv('csv1.csv', index=False)
# csv2.to_csv('csv2.csv', index=False)
# csv3.to_csv('csv3.csv', index=False)
# csv4.to_csv('csv4.csv', index=False)
# ======================

# 106,456
# total 425824
# df1.to_csv('re_sp_c_final.csv', index=False)
# df1['Engagement Rate'] = df1['Engagement Rate'] * 100
# g = df1.sample(frac=1).reset_index(drop=True)
# g.to_csv('final_remove_.csv', index=False)

# print(g.head())

# The first column is Ratings : if Engagement.rate = 0,08 to 0.14,
# Ratings =1, Engagement.rate = 0 to 0.07 Ratings =2

# The second column is : Is_Response, if Ratings =1, Is_Response = happy, if Ratings =2, Is_Response = not happy
