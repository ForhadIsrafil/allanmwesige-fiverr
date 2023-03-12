import os
import json
import datetime

import pandas as pd


df1 = pd.read_csv('final.csv')
# df1['Engagement Rate'] = df1['Engagement Rate'] * 100
g = df1.sample(frac=1).reset_index(drop=True)
g.to_csv('final_updated.csv', index=False)

print(g.head())