import re
import json
import datetime
import numpy as np
import pandas as pd
import glob

# todo: read infuencer
influencer_df = pd.read_csv('Influencer names and ID.txt', sep='\t')
# followers = influencer_df[influencer_df['Username'] == 'makeupbynvs']['#Followers'].values[0]

list_of_files = glob.glob('json_data_1/*.info')  # get the list of file

data_list = []
for file_name in list_of_files[:500]:
    # print(file_name)
    # print(influencer_df[influencer_df['Username'] == to_dict['owner']['username']])
    try:
        file = open(file_name, 'r', encoding="utf-8")
        to_dict = json.load(file)
        try:
            no_comment = to_dict['edge_media_to_parent_comment']['count']
        except Exception as e:
            no_comment = 0
        try:
            comments = [comment['node']['text'] for comment in to_dict['edge_media_to_parent_comment']['edges']]
        except Exception as e:
            comments = []

        if len(comments) > 25:
            rate = (to_dict['edge_media_preview_like']['count'] + no_comment) / \
                   influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['#Followers'].values[0]

            data = {
                "User ID": to_dict['owner']['id'],
                "Username": to_dict['owner']['username'],
                # "Category": influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['Category'].values[0],
                "Comments": comments,
                "No of comments": no_comment,
                "Likes": to_dict['edge_media_preview_like']['count'],
                "Followers":
                    influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['#Followers'].values[0],
                "Engagement Rate": float("{:.2f}".format(rate)),
                "Time Stamp": datetime.datetime.fromtimestamp(int(to_dict['taken_at_timestamp'])).strftime(
                    '%Y-%m-%d %H:%M:%S'),
                # "Video or Photo": to_dict['is_video'],
            }
            data_list.append(data)
    except Exception as e:
        pass

df = pd.DataFrame(data_list)
df['Comments'] = df['Comments'].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', str(x)))
# print(df1['Comments'].dtypes)
nan_value = float("NaN")
df.replace(" ", nan_value, inplace=True)
df.dropna(subset=["Comments"], inplace=True)
# print(df1['Comments'].head(30))
filters = [(df['Engagement Rate'] >= 0.08) & (df['Engagement Rate'] <= 0.14), (df['Engagement Rate'] <= 0.07)]
values = [1, 2]
df['Ratings'] = np.select(filters, values)

filters2 = [(df['Ratings'] == 1), (df['Ratings'] == 2)]
values2 = ['happy', 'not happy']
df['Is_Response'] = np.select(filters2, values2)
df.columns = df.columns.str.replace(' ','_')

# df2 = df.sample(frac=1).reset_index(drop=True) # randomize the rows
df.to_csv('json_data_1.csv', index=False)

# https://drive.google.com/drive/folders/1UxNZ32HYsgL9xDgGyd4xJThRwFZnQzsZ

# d = datetime.datetime.fromtimestamp(
#     int("1520889929")
# ).strftime('%Y-%m-%d %H:%M:%S')

'''
1. User ID
2. Username
3. Category
4. Comments
5. Number of comments of the post
6. Likes of the post
7. Followers
8. Engagement Rate (likes,shares, and comments / number of followers)
9. Time Stamp
10. Video or Photo
'''
