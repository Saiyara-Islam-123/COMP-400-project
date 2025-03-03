import pandas as pd
import matplotlib as plt

df1 = pd.read_csv("xors0to10.csv")
df2 = pd.read_csv("xors10to40.csv")
df3 = pd.read_csv("xors40to100.csv")
df4 = pd.read_csv("xors100to130.csv")

df_ones = pd.concat([df1, df2, df3, df4])
df_fours = pd.read_csv("xors_4_frames_to130.csv")
df_tens = pd.read_csv("xors_10_frames_to130.csv")

df_duration = pd.read_csv("filtered_data.csv") #I have a trick

#I wanna match videos with their duration coz I hadn't done it :<