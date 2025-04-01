import pandas as pd

df = pd.read_csv("filtered_data.csv")

urls = {}
for i in range(len(df["url"])):
    u = df["url"].iloc[i]
    urls[u] = 1


def uniques(csv_file):

    df2 = pd.read_csv(csv_file)
    new_ones = []
    durations  = []
    for i in range(len(df2["url"])):
        url = df2["url"].iloc[i]
        duration = df2["min"].iloc[i]

        if url not in urls:
            new_ones.append(url)
            durations.append(duration)

    return new_ones, durations


u1, d1 = (uniques("filtered_data2.csv"))

u2, d2 = (uniques("filtered_data3.csv"))



merged_urls = u1 + u2
merged_durations = d1 + d2

new_df = pd.DataFrame()

new_df["url"] = merged_urls
new_df["min"] = merged_durations

new_df.sort_values(by=['min'], ascending=True, inplace=True)

new_df.to_csv("filtered_data_more.csv")
