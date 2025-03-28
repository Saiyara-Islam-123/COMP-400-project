import pandas as pd

df = pd.read_csv("filtered_data.csv")

urls = {}
for i in range(len(df["url"])):
    url = df["url"].iloc[i]

    if url not in urls:
        urls[url] = 1

df2 = pd.read_csv("filtered_data2.csv")
new_ones = {}
for i in range(len(df2["url"])):
    url = df["url"].iloc[i]

    if url not in urls:
        new_ones[url] = df2["min"]

print(len(new_ones.keys()))