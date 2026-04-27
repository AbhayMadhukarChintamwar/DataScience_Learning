import pandas as pd


#  Convert Dictionary to data frame

Dictionary = {'key1':[1,2,3,4,5],
              'key2':[6,7,8,9,10],
             'key3':[11,12,13,14,15]}

print(Dictionary)
            # {'key1': [1, 2, 3, 4, 5], 'key2': [6, 7, 8, 9, 10], 'key3': [11, 12, 13, 14, 15]}


Dictionary_To_DataFrame  =  pd.DataFrame(Dictionary)
print(Dictionary_To_DataFrame)

            #    key1  key2  key3
            # 0     1     6    11
            # 1     2     7    12
            # 2     3     8    13
            # 3     4     9    14
            # 4     5    10    15

print(Dictionary_To_DataFrame.min().transpose())
            # key1     1
            # key2     6
            # key3    11
            # dtype: int64

print(Dictionary_To_DataFrame.min().transpose())

            #       0   1   2   3   4
            # key1   1   2   3   4   5
            # key2   6   7   8   9  10
            # key3  11  12  13  14  15

