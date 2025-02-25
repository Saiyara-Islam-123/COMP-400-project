import pandas as pd
import re
from functions import filter_by_duration

from functools import cmp_to_key
import yt_dlp

def format_url(url):
    splitted = re.split(r" ", url)

    return "https://www.youtube.com/watch?v=" + re.sub(r"}", "", splitted[-1]).strip("'")

def vid_id(url):
    splitted = re.split(r" ", url)
    return re.sub(r"}", "", splitted[-1]).strip("'")

def check_livestream(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if info_dict.get('is_live', False):
            return True
        else:
            return False

#formating urls
df_data_trial1 = pd.read_csv("data_trial1.csv")
df_data = pd.read_csv("data.csv")

merged_df = pd.concat([df_data_trial1, df_data], ignore_index=True)
merged_df["corrected_url"] = merged_df['url'].apply(format_url)
merged_df["video id"] = merged_df['url'].apply(vid_id)


filtered_urls = {}
for i in range(len(merged_df["url"])):


    if "videoId" in merged_df["url"].iloc[i] and merged_df["corrected_url"].iloc[i] not in filtered_urls: #getting rid of repeats
        boolean, length = filter_by_duration(merged_df["video id"].iloc[i])
        if boolean and not (check_livestream(merged_df["corrected_url"].iloc[i])):
            print(i, merged_df["corrected_url"].iloc[i])
            filtered_urls[merged_df["corrected_url"].iloc[i]] = length

#sorting according to time

def less_than(k1, k2):
    if filtered_urls[k1] < filtered_urls[k2]:
        return True
    elif filtered_urls[k1] > filtered_urls[k2]:
        return False


def compare(k1, k2):
    if less_than(k1, k2):
        return -1
    elif less_than(k2, k1):
        return 1
    else:
        return 0

sorted_keys = sorted(filtered_urls, key=cmp_to_key(compare))

sorted_dict = {}
for j in range(len(sorted_keys)):
    sorted_dict[sorted_keys[j]] = filtered_urls[sorted_keys[j]]

print(sorted_dict)

df_filtered = pd.DataFrame(list(sorted_dict.items()), columns=['url', 'min'])

df_filtered.to_csv('filtered_data.csv', index=False)