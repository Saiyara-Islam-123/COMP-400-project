import pandas as pd

df = pd.read_pickle('xors0to30.pkl')

print(df["xor"].iloc[0].shape)
