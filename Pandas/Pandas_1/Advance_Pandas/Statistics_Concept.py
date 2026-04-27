import pandas as pd

Data_1 = pd.DataFrame({'key1':[1,2,3,4,5],
                       'key2':[6,7,8,9,10],
                       'key3':[11,12,13,14,15]})

print(Data_1)

            #    key1  key2  key3
            # 0     1     6    11
            # 1     2     7    12
            # 2     3     8    13
            # 3     4     9    14
            # 4     5    10    15

print(Data_1['key1'].mean())
print()
            # 3.0

print(Data_1['key1'].median())
print()
            # 3.0

print(Data_1['key1'].mode())
print()
            # 0    1
            # 1    2
            # 2    3
            # 3    4
            # 4    5
            # Name: key1, dtype: int64

print(Data_1['key1'].std())
print()
            # 1.5811388300841898

print(Data_1['key1'].var())
print()
            # 2.5

print(Data_1['key1'].sum())
print()
            # 15

print(Data_1['key1'].min())
print()
            # 1

print(Data_1['key1'].max())
print()
            # 5
