import requests

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
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        channel = item['snippet']['channelTitle']
        description = item['snippet']['description']
        url = f"https://www.youtube.com/watch?v={video_id}"
        videos.append(Video(video_id, title, channel, description, url))

    return videos

