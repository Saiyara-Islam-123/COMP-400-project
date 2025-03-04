import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df_1 = pd.read_csv("xors_10_frames_to130.csv")
df_2 = pd.read_csv("xors_10_frames_130to175.csv")
df = pd.concat([df_1, df_2])

zero_min = []
one_min = []
two_min = []

for i in range(len(df["duration"])):
    if df["duration"].iloc[i] == 0:
        zero_min.append(float(df["ones"].iloc[i]))
    elif df["duration"].iloc[i] == 1:
        one_min.append(float(df["ones"].iloc[i]))
    else:
        two_min.append(float(df["ones"].iloc[i]))


zero_min_np = np.array(zero_min)
one_min_np = np.array(one_min)
two_min_np = np.array(two_min)

categories = ["0 min", "1 min", "2 mins"]
means = [np.mean(zero_min_np), np.mean(one_min_np), np.mean(two_min_np)]
sds = [np.std(zero_min_np), np.std(one_min_np), np.std(two_min_np)]

plt.errorbar(categories, means, sds, linestyle='None', marker='o')
plt.xlabel('Minutes')
plt.ylabel('Mean proportion of 1s in XORs')
plt.title("Proportion of 1s in XORs across video duration")
plt.savefig('Graph for first 175 videos.png')
plt.show()

