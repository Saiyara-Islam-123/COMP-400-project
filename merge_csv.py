import pandas as pd

def merge_csv(file1, file2, new_name):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv(new_name, index=False)

merge_csv("color_10_frames_with_brand0to65.csv", "color_10_frames_with_brand0to414.csv", "color_10_frames_with_brand_all.csv")