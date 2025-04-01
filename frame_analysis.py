from functions import *
import pandas as pd
import shutil
import cv2
import numpy as np
import os
import random
import colorsys


df = pd.read_csv("filtered_data.csv")


def sample_colour():
    random.seed(50)
    sampled = []

    sampled_indices = random.sample(range(60, len(os.listdir("vid")) - 60), 50)

    for i in sampled_indices:
        frame_a = cv2.imread("vid/" + str(i) + ".png")
        frame_a_arr = np.array(frame_a)
        sampled.append(frame_a_arr)

    saturations_all = []
    for k in range(len(sampled)):
        arr =  sampled[k]
        saturations_arr = []
        for i in range(arr.shape[0]):
            for j in range (arr.shape[1]):
                b = arr[i, j,0]/255
                g = arr[i, j,1]/255
                r = arr[i, j,2]/255

                h, s, l = colorsys.rgb_to_hls(r, g, b)

                s = s * 100
                saturations_arr.append(s)
        print(k)
        saturations_all.append(np.mean(saturations_arr))

    return np.mean(saturations_all)


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


def process_all(start, end):

    urls = []
    one_prop = []
    durations = []

    for i in range(start, end):

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


    df_xor.to_csv('xors_10_frames_' + str(start) + "to" + str(end) + '.csv')
    print("Saved to xors.csv")
    #return urls, xors


#process_all(0, 1)
