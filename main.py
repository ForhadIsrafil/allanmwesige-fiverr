import os
import json
import datetime

import pandas as pd
import glob

# todo: read infuencer
influencer_df = pd.read_csv('Influencer names and ID.txt', sep='\t')
# followers = influencer_df[influencer_df['Username'] == 'makeupbynvs']['#Followers'].values[0]

list_of_files = glob.glob('json_data_files/*.info')  # get the list of file

data_list = []
for file_name in list_of_files:
    print(file_name)
    file = open(file_name, 'r', encoding="utf-8")
    to_dict = json.load(file)
    # print(influencer_df[influencer_df['Username'] == to_dict['owner']['username']])
    try:
        no_comment = to_dict['edge_media_to_parent_comment']['count']
    except Exception as e:
        no_comment = 0
    try:
        comments = [comment['node']['text'] for comment in to_dict['edge_media_to_parent_comment']['edges']]
    except Exception as e:
        comments = []
    data = {
        "User ID": to_dict['owner']['id'],
        "Username": to_dict['owner']['username'],
        "Category": influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['Category'].values[0],
        "Comments": comments,
        "No_comments": no_comment,
        "Likes": to_dict['edge_media_preview_like']['count'],
        "Followers": influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['#Followers'].values[0],
        "Engagement Rate": (to_dict['edge_media_preview_like']['count'] + no_comment) /
                           influencer_df[influencer_df['Username'] == to_dict['owner']['username']][
                               '#Followers'].values[0],
        "Time Stamp": datetime.datetime.fromtimestamp(int(to_dict['taken_at_timestamp'])).strftime('%Y-%m-%d %H:%M:%S'),
        "Video or Photo": to_dict['is_video'],
    }
    data_list.append(data)

df = pd.DataFrame(data_list)
df.to_excel('sample_data.xlsx', index=False)
# with open('json_data_files/babimaronna-1940027008320063117.json', 'r', encoding="utf-8") as f:
#     data = json.load(f)
# #     dict_data = {
# #         "username": data['owner']['username'],
# #         "id": data['id'],
# #         "taken_at_timestamp": data["taken_at_timestamp"],
# #         "edge_media_preview_like": data["edge_media_preview_like"]['count'],
# #         "caption": data['edge_media_to_caption']['edges'][0]['node']['text'],
# #     }
# #
# df = pd.DataFrame([data])
# df.to_csv('sample3.csv', index=False)
# print(df.columns)

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
