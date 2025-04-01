import requests
import pandas as pd

import os

class Video:
    def __init__(self, video_id, title, channel, description, url):
        self.video_id = video_id
        self.title = title
        self.channel = channel
        self.description = description
        self.url = url

with open('API Key.txt', 'r') as file:
    for line in file:
        API_KEY = line.strip()

def get_video_info(search_query, maxResults):
    URL = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'part': 'snippet',
        'q': search_query,
        'key': API_KEY,
        'maxResults': maxResults
    }

    response = requests.get(URL, params=params)

    data = response.json()

    videos = []

    for item in data['items']:

        video_id = item['id']

        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        description = item['snippet']['description']

        videos.append(Video(video_id, title, channel, description, video_id))

    return videos


def save_to_csv(search_query, maxResults):
    videos = get_video_info(search_query, maxResults)

    columns = ["search_query", "max results", "title", "channel", "description", "url"]
    df = pd.DataFrame(columns=columns)

    for video in videos:
        df.loc[len(df)] = [search_query, maxResults, video.title, video.channel, video.description, video.url]

    if not os.path.exists("data_with_brand.csv.csv"):
        df.to_csv("data3.csv", index=False)

    else:
        df = pd.read_csv("data3.csv")
        for video in videos:
            df.loc[len(df)] = [search_query, maxResults, video.title, video.channel, video.description, video.url]
            df.to_csv("data3.csv", index=False)


def search_all(keywords, max_results = 50):
    for keyword in keywords:
        save_to_csv(keyword, max_results)


def generate_queries():
    queries  = []
    patterns1 = ["cocomelon", "baby shark", "amazing digital circus", "spiderman", "elsa", 'poppy playtime', "sprunki",
                 'peppa pig', "minecraft", "roblox", "among us"]
    patterns2 = ["cartoon", "animation", "song", "content", "channel", "fun", "rhyme", "nursery rhyme"]


    for pattern in patterns1:
        for i in range(len(patterns2)):
            queries.append( pattern + " " + patterns2[i])
            for j in range(len(patterns2)):
                if j != i:
                    queries.append(pattern + " " + patterns2[i] + " " + patterns2[j])

    return queries

search_all(generate_queries())