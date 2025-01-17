from yt_dlp import YoutubeDL
import cv2
import os

def download(url, file_loc):
    print("Downloading Youtube Video" + "url")

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
        if (count > (video_length - 1)):
            cap.release()
        break
