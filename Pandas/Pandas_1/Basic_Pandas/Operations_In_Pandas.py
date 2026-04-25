import pandas as pd

df = pd.read_xml('it_finance_data.xml')
print(df)

#  describe() --> it is only showing integer or float values
described = df.describe()
print(described)
print()

            #       Employee_ID        Salary  Experience_Years
            # count  12000.00000  1.200000e+04      12000.000000
            # mean    6000.50000  1.152899e+06          7.798700
            # std     3464.24595  4.936764e+05          4.171116
            # min        1.00000  3.000730e+05          0.500000
            # 25%     3000.75000  7.248252e+05          4.200000
            # 50%     6000.50000  1.156995e+06          7.800000
            # 75%     9000.25000  1.587310e+06         11.400000
            # max    12000.00000  1.999967e+06         15.000000

print(df.dtypes)
print()

            # Employee_ID           int64
            # Name                    str
            # Department              str
            # Role                    str
            # Company                 str
            # City                    str
            # Salary                int64
            # Experience_Years    float64

dtype: object
add_describe_at_str = df[df.dtypes[df.dtypes=='str'].index].describe()
print(add_describe_at_str)
print()

            #               Name Department               Role   Company   City
            # count        12000      12000              12000     12000  12000
            # unique       12000          2                 10         8      5
            # top     Employee_1         IT  Financial Analyst  Deloitte   Pune
            # freq             1       6008               1239      1603   2491
