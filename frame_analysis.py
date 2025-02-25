from functions import *
import pandas as pd
import shutil
import cv2
import numpy as np
import os


df = pd.read_csv("filtered_data.csv")

def xor():
    list_of_xor = []
    for i in range(1, len(os.listdir("vid"))):
        frame_a = cv2.imread("vid/"+str(i)+".png")
        frame_a_arr = np.array(frame_a)
        frame_b = cv2.imread("vid/"+str(i+1)+".png")
        frame_b_arr = np.array(frame_b)
        print(i, i+1)

        list_of_xor.append(np.bitwise_xor(frame_a_arr, frame_b_arr))

    return np.array(list_of_xor)


def process_all():
    list_all_xor = []
    for i in range(130):
        url = df["url"][i]
        download(url, "vid")
        chop("vid.mp4")

        list_all_xor.append(xor())

        shutil.rmtree("vid")
        os.remove("vid.mp4")
        print("video deleted with folder and frames" + str(i))

    array = np.array(list_all_xor)
    df_xor = pd.DataFrame(array)
    df_xor.to_csv('xors.csv', index=False, header=False)


process_all()