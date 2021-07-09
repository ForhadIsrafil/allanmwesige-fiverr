import os
import json
import datetime

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

        if len(comments) > 0:
            rate = (to_dict['edge_media_preview_like']['count'] + no_comment) / \
                   influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['#Followers'].values[0]

            data = {
                "User ID": to_dict['owner']['id'],
                "Username": to_dict['owner']['username'],
                "Category": influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['Category'].values[
                    0],
                "Comments": comments,
                "No of comments": no_comment,
                "Likes": to_dict['edge_media_preview_like']['count'],
                "Followers":
                    influencer_df[influencer_df['Username'] == to_dict['owner']['username']]['#Followers'].values[0],
                "Engagement Rate": float("{:.2f}".format(rate)),
                "Time Stamp": datetime.datetime.fromtimestamp(int(to_dict['taken_at_timestamp'])).strftime(
                    '%Y-%m-%d %H:%M:%S'),
                "Video or Photo": to_dict['is_video'],
            }
            data_list.append(data)
    except Exception as e:
        pass

df = pd.DataFrame(data_list)
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
