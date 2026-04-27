import pandas as pd

date = pd.date_range(start= '2002-03-08', end='2007-06-21')
print(date)
print()

            # DatetimeIndex(['2002-03-08', '2002-03-09', '2002-03-10', '2002-03-11',
            #                '2002-03-12', '2002-03-13', '2002-03-14', '2002-03-15',
            #                '2002-03-16', '2002-03-17',
            #                ...
            #                '2007-06-12', '2007-06-13', '2007-06-14', '2007-06-15',
            #                '2007-06-16', '2007-06-17', '2007-06-18', '2007-06-19',
            #                '2007-06-20', '2007-06-21'],
            #               dtype='datetime64[us]', length=1932, freq='D')



df_date = pd.DataFrame({'Date':date})
print(df_date)
print()

df = pd.DataFrame({'date':['2002-03-08','1993-10-13','2023-04-16','2007-06-21']})
print(df)
print(df.dtypes)
print()

df['update_date'] = pd.to_datetime(df['date'])
print(df)
print(df.dtypes)
print()

df['Year']  = df['update_date'].dt.year
print(df)
print()

df['Month']  = df['update_date'].dt.month
print(df)
print()

df['Day']  = df['update_date'].dt.day
print(df)
print()