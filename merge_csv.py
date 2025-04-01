import pandas as pd

def merge_csv(file1, file2, new_name):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv(new_name, index=False)

merge_csv("filtered_data_with_brand1.csv", "filtered_data_with_brand2.csv", "filtered_data_with_brand_merged.csv")