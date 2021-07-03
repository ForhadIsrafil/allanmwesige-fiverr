import os
import json
import datetime

import pandas as pd

df = pd.read_csv('Influencer names and ID.txt', sep='\t')
print(df[df['Username'] == 'makeupbynvs']['#Followers'].values[0])
# print(df.shape)