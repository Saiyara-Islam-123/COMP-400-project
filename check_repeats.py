import pandas as pd

df = pd.read_csv("./merged_dataset/generic_search.csv")

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
            print(url, duration)
    return new_ones, durations


u1, d1 = (uniques("not_final/filtered_data2.csv"))
u2, d2 = (uniques("not_final/filtered_data3.csv"))


new_df = pd.DataFrame()

new_df["url"] = u1 + u2
new_df["min"] = d1 + d2

new_df.sort_values(by=['min'], ascending=True, inplace=True)

new_df.to_csv("filtered_data_without_brand_uniques.csv")
