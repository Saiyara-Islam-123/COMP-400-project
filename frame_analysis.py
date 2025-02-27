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

def get_max_dim():
    max_dims = (0, 0)
    for i in range(len(df["url"])):
        url = df["url"][i]
        dims = get_dimensions(url)
        print(dims, i)

        if dims[0] > max_dims[0]:
            max_dims = dims
        if dims[1] > max_dims[1]:
            max_dims = dims
    return max_dims

def process_all():


    urls = []
    xors = []

    for i in range(30, 60):

        url = df["url"][i]
        download(url, "vid")

        if os.path.exists("vid.mp4"):
            chop("vid.mp4")

            list_xor = xor()

            shutil.rmtree("vid")
            os.remove("vid.mp4")
            print("video deleted with folder and frames" + str(i))

            array_xor = np.array(list_xor)
            xors.append(array_xor)
            urls.append(url)
            print(array_xor.shape)

    df_xor = pd.DataFrame()
    df_xor["url"] = urls
    df_xor["xor"] = xors

    df_xor.to_pickle('xors30to60.pkl')
    print("Saved to xors30to60.pkl")
    #return urls, xors


#print(get_max_dim())
#(640, 360)

(process_all())