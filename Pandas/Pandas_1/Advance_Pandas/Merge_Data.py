import pandas as pd

df = pd.read_xml('it_finance_data.xml')
# print(df)



# Concat --> concat data

concat_df1 = df[['Employee_ID', 'Name', 'Company','City']][0:5]
print(concat_df1)

            #    Employee_ID        Name     Company       City
            # 0            1  Employee_1  Microsoft      Mumbai
            # 1            2  Employee_2      Amazon       Pune
            # 2            3  Employee_3         TCS  Hyderabad
            # 3            4  Employee_4  Microsoft        Pune
            # 4            5  Employee_5   Accenture       Pune


concat_df2 = df[['Employee_ID', 'Name', 'Company','City']][5:10]
print(concat_df2)


            #    Employee_ID         Name    Company       City
            # 5            6   Employee_6     Google  Bangalore
            # 6            7   Employee_7     Google     Mumbai
            # 7            8   Employee_8  Accenture     Mumbai
            # 8            9   Employee_9     Amazon       Pune
            # 9           10  Employee_10     Amazon  Bangalore

concat_Data = pd.concat([concat_df1,concat_df2])
print(concat_Data)

            #    Employee_ID         Name     Company       City
            # 0            1   Employee_1  Microsoft      Mumbai
            # 1            2   Employee_2      Amazon       Pune
            # 2            3   Employee_3         TCS  Hyderabad
            # 3            4   Employee_4  Microsoft        Pune
            # 4            5   Employee_5   Accenture       Pune
            # 5            6   Employee_6      Google  Bangalore
            # 6            7   Employee_7      Google     Mumbai
            # 7            8   Employee_8   Accenture     Mumbai
            # 8            9   Employee_9      Amazon       Pune
            # 9           10  Employee_10      Amazon  Bangalore


concat_Data = pd.concat([concat_df1,concat_df2], axis=1)
print(concat_Data)

            #    Employee_ID        Name     Company       City  Employee_ID         Name    Company       City
            # 0          1.0  Employee_1  Microsoft      Mumbai          NaN          NaN        NaN        NaN
            # 1          2.0  Employee_2      Amazon       Pune          NaN          NaN        NaN        NaN
            # 2          3.0  Employee_3         TCS  Hyderabad          NaN          NaN        NaN        NaN
            # 3          4.0  Employee_4  Microsoft        Pune          NaN          NaN        NaN        NaN
            # 4          5.0  Employee_5   Accenture       Pune          NaN          NaN        NaN        NaN
            # 5          NaN         NaN         NaN        NaN          6.0   Employee_6     Google  Bangalore
            # 6          NaN         NaN         NaN        NaN          7.0   Employee_7     Google     Mumbai
            # 7          NaN         NaN         NaN        NaN          8.0   Employee_8  Accenture     Mumbai
            # 8          NaN         NaN         NaN        NaN          9.0   Employee_9     Amazon       Pune
            # 9          NaN         NaN         NaN        NaN         10.0  Employee_10     Amazon  Bangalore





#  Merge --> Merging data

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

Data_2 = pd.DataFrame({'key1':[1,20,3,40,5],
              'key4':[6,70,8,9,10],
             'key5':[131,120,139,14,150]})

print(Data_2)

            #    key1  key4  key5
            # 0     1     6   131
            # 1    20    70   120
            # 2     3     8   139
            # 3    40     9    14
            # 4     5    10   150

Merge_Data = pd.merge(Data_1,Data_2)
print(Merge_Data) # By default its print inner merge values

            #    key1  key2  key3  key4  key5
            # 0     1     6    11     6   131
            # 1     3     8    13     8   139
            # 2     5    10    15    10   150

Left_Merge = pd.merge(Data_1, Data_2, how='left')
print(Left_Merge)

            #    key1  key2  key3  key4   key5
            # 0     1     6    11   6.0  131.0
            # 1     2     7    12   NaN    NaN
            # 2     3     8    13   8.0  139.0
            # 3     4     9    14   NaN    NaN
            # 4     5    10    15  10.0  150.0


Right_Merge = pd.merge(Data_1, Data_2, how='right')
print(Right_Merge)
            #    key1  key2  key3  key4  key5
            # 0     1   6.0  11.0     6   131
            # 1    20   NaN   NaN    70   120
            # 2     3   8.0  13.0     8   139
            # 3    40   NaN   NaN     9    14
            # 4     5  10.0  15.0    10   150

Outer_Merge = pd.merge(Data_1, Data_2, how='outer')
print(Outer_Merge)

            #   key1  key2  key3  key4   key5
            # 0     1   6.0  11.0   6.0  131.0
            # 1     2   7.0  12.0   NaN    NaN
            # 2     3   8.0  13.0   8.0  139.0
            # 3     4   9.0  14.0   NaN    NaN
            # 4     5  10.0  15.0  10.0  150.0
            # 5    20   NaN   NaN  70.0  120.0
            # 6    40   NaN   NaN   9.0   14.0