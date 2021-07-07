import os
import json
import datetime

import pandas as pd

# df = pd.read_csv('Influencer names and ID.txt', sep='\t')
# print(df[df['Username'] == 'makeupbynvs']['#Followers'].values[0])
# print(df.count())


df1 = pd.read_csv('json_data_1.csv')
df2 = pd.read_csv('json_data_2.csv')
df3 = pd.concat([df1, df2],)
df3.to_csv('final.csv', index=False)