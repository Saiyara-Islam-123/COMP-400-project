from fetch_vid import *
from functions import *

videos = get_video_info("cocomelon", 3)

for video in videos:
    download(video.url, video.video_id)
    chop(video.video_id + ".mp4")
