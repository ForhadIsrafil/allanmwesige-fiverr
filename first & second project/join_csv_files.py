import os
import json
import datetime

import pandas as pd


df1 = pd.read_csv('json_data_1.csv')
df2 = pd.read_csv('final_data.csv')
df3 = pd.concat([df1, df2],)
df3.to_csv('final.csv', index=False)