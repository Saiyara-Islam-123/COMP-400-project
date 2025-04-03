import pandas as pd
import os
import re

def merge(pattern):
    dfs = []
    for i in range(0, len(os.listdir("."))):
        file = os.listdir(".")[i]
        if re.match(pattern, file):
            print(file)
            df = pd.read_csv(file)
            dfs.append(df)

    return pd.concat(dfs)


df_merged = merge(r"xors_10_frames_brand[0-9]+")
df_merged.to_csv("./merged_dataset/brand_search.csv", index=False)

'''
df1 = pd.read_csv("xors_10_frames_more_0to30.csv")
df2 = pd.read_csv("xors_10_frames_more_30to32.csv")
df3 = pd.read_csv("xors_10_frames_more_32to33.csv")

df4 = pd.read_csv("xors_10_frames_to130.csv")
df5 = (merge(r"xors_10_frames_[0-9]+"))

df_merged = pd.concat([df1, df2, df3, df4, df5])

df_merged.to_csv("./merged_dataset/generic_search.csv", index=False)
'''