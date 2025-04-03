import pandas as pd

def merge_csv(file1, file2, new_name):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv(new_name, index=False)

merge_csv("xors_10_frames_without_brand0to2.csv", "./merged_dataset/generic_search.csv", "generic_search_updated.csv")