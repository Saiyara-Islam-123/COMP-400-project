from functions import *
import pandas as pd
import shutil
import cv2
import numpy as np
import os


df = pd.read_csv("filtered_data.csv")



def xor():
    list_of_xor = []
    for i in range(1, len(os.listdir("vid"))-9):
        frame_a = cv2.imread("vid/"+str(i)+".png")
        frame_a_arr = np.array(frame_a)
        frame_b = cv2.imread("vid/"+str(i+10)+".png")
        frame_b_arr = np.array(frame_b)
        print(i, i+10)

        list_of_xor.append(np.logical_xor(frame_a_arr, frame_b_arr))

    return np.array(list_of_xor)

def get_proportion_one(xors):
    sums = xors.sum()

    return sums / xors.size


def process_all():

    urls = []
    one_prop = []
    durations = []

    for i in range(175, 200):

        url = df["url"][i]
        duration = df["min"][i]
        download(url, "vid")


        if os.path.exists("vid.mp4"):
            chop("vid.mp4")

            list_xor = xor()

            shutil.rmtree("vid")
            os.remove("vid.mp4")
            print("video deleted with folder and frames" + str(i))

            array_xor = np.array(list_xor)
            one_prop.append(get_proportion_one(array_xor))


            urls.append(url)
            durations.append(duration)
            print(array_xor.shape)


    df_xor = pd.DataFrame()
    df_xor["url"] = urls
    df_xor["ones"] = one_prop
    df_xor["duration"] = durations


    df_xor.to_csv('xors_10_frames_175to200.csv')
    print("Saved to xors.csv")
    #return urls, xors


(process_all())






