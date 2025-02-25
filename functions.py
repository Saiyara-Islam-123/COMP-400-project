
import cv2
import os
import requests
import re

from yt_dlp import YoutubeDL

with open('API Key.txt', 'r') as file:
    for line in file:
        API_KEY = line.strip()

def check_duration(video_id):
    url = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + "&part=contentDetails&key=" + API_KEY
    response = requests.get(url)
    data = response.json()
    if len(data["items"]) == 0:
        return None

    return data['items'][0]['contentDetails']["duration"]


def download(url, file_loc):
    print("Downloading Youtube Video" + "url")
    file_loc = file_loc + ".mp4"

    ydl_opts = {
        'outtmpl': file_loc,
        'format': 'mp4',
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def chop(input_file):
    output_directory = input_file.removesuffix(".mp4")
    os.mkdir(output_directory)
    cap = cv2.VideoCapture(input_file)

    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) -1
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        cv2.imwrite(output_directory + "/%d.png" % (count + 1), frame)
        count = count + 1
        print(count)
        if (count > (video_length - 1)):
            cap.release()


def filter_by_duration(video_id):
    duration_string = check_duration(video_id)

    hour_format = r"PT[0-9]+H+"
    if duration_string is None:
        return False, -1

    if re.match(hour_format, duration_string):
        return False, -1
    else:
        min_format = r"M"
        if re.search(min_format, duration_string) == None: #seconds long video
            return True, 0

        splitted = re.split(min_format, duration_string)
        mins = int(re.sub("PT", "", splitted[0]))

        mins = int(mins)
        if mins > 4:
            return False, -1
        else:
            return True, mins


#download("https://www.youtube.com/watch?v=4ARDKad9KwU&ab_channel=Chomsky%27sPhilosophy", "vid")
#chop("vid.mp4")