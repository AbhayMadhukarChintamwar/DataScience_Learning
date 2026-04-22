import pandas as pd

df = pd.read_csv("finance_small_data.csv")
print(df.head())
print(df.info())
print(df.shape)
print(df.loc[0:99, "Date"])
print(df.loc[:, "Transaction_Type"])