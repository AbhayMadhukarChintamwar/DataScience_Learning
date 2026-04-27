import pandas as pd

df = pd.DataFrame({'key1':[1,2,3,4,5]})

print(df)
print()
            #    key1
            # 0     1
            # 1     2
            # 2     3
            # 3     4
            # 4     5


print(df['key1'].rolling(window = 3).mean())
print()
            # 0    NaN
            # 1    NaN
            # 2    2.0
            # 3    3.0
            # 4    4.0
            # Name: key1, dtype: float64



print(df['key1'].rolling(window = 3).median())
print()

            # 0    NaN
            # 1    NaN
            # 2    2.0
            # 3    3.0
            # 4    4.0
            # Name: key1, dtype: float64


print(df['key1'].rolling(window = 3).var())
print()

            # 0    NaN
            # 1    NaN
            # 2    1.0
            # 3    1.0
            # 4    1.0
            # Name: key1, dtype: float64

print(df['key1'].rolling(window = 3).sum())
print()

            # 0     NaN
            # 1     NaN
            # 2     6.0
            # 3     9.0
            # 4    12.0
            # Name: key1, dtype: float64



print(df['key1'].rolling(window = 3).min())
print()

            # 0    NaN
            # 1    NaN
            # 2    1.0
            # 3    2.0
            # 4    3.0
            # Name: key1, dtype: float64

print(df['key1'].rolling(window = 3).max())
print()

            # 0    NaN
            # 1    NaN
            # 2    3.0
            # 3    4.0
            # 4    5.0
            # Name: key1, dtype: float64

