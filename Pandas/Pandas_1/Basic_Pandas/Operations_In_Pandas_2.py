import pandas as pd

df = pd.read_xml('it_finance_data.xml')
# print(df)

a = df['Name'][0:10]
print(a)
            # 0     Employee_1
            # 1     Employee_2
            # 2     Employee_3
            # 3     Employee_4
            # 4     Employee_5
            # 5     Employee_6
            # 6     Employee_7
            # 7     Employee_8
            # 8     Employee_9
            # 9    Employee_10
            # Name: Name, dtype: str

print(type(a))  # <class 'pandas.Series'>


l = ['a1','a2','a3','a4','a5','a6','a7','a8','a9','a10']

n = pd.Series(a, index = l)
print(n)
            # a1     NaN
            # a2     NaN
            # a3     NaN
            # a4     NaN
            # a5     NaN
            # a6     NaN
            # a7     NaN
            # a8     NaN
            # a9     NaN
            # a10    NaN
            # Name: Name, dtype: str

m = pd.Series(list(a),index= l)
print(m)

            # a1      Employee_1
            # a2      Employee_2
            # a3      Employee_3
            # a4      Employee_4
            # a5      Employee_5
            # a6      Employee_6
            # a7      Employee_7
            # a8      Employee_8
            # a9      Employee_9
            # a10    Employee_10
            # dtype: str

print(m['a5'])  # Employee_5


# Arithmetic Operations

d1 = pd.Series([100,200,300,400,500], index = [1,2,3,4,5])
print(d1)
            # 1    100
            # 2    200
            # 3    300
            # 4    400
            # 5    500
            # dtype: int64
d2 = pd.Series([101,201,301,401,501], index = [1,2,3,4,5])
print(d2)
            # 1    101
            # 2    201
            # 3    301
            # 4    401
            # 5    501
            # dtype: int64

print(d1 + d2)
            # 1     201
            # 2     401
            # 3     601
            # 4     801
            # 5    1001
            # dtype: int64

print(d1 - d2)
            # 1   -1
            # 2   -1
            # 3   -1
            # 4   -1
            # 5   -1
            # dtype: int64

print(d1 * d2)
            # 1     10100
            # 2     40200
            # 3     90300
            # 4    160400
            # 5    250500
            # dtype: int64

print(d1 // d2)
            # 1    0
            # 2    0
            # 3    0
            # 4    0
            # 5    0
            # dtype: int64


#  Delete functions

delete_Data = df.drop('Name',axis=1)
print(delete_Data)

            #        Employee_ID Department                Role     Company       City   Salary  Experience_Years
            # 0                1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4
            # 1                2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9
            # 2                3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9
            # 3                4         IT   Software Engineer  Microsoft        Pune  1345806               0.6
            # 4                5         IT      Data Scientist   Accenture       Pune  1962417              10.2
            # ...            ...        ...                 ...         ...        ...      ...               ...
            # 11995        11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0
            # 11996        11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9
            # 11997        11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8
            # 11998        11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0
            # 11999        12000         IT             Auditor       Wipro  Bangalore   999198               9.5

            # [12000 rows x 7 columns]


            # Indexing

Set_Index = df.set_index('Salary')

print(Set_Index)
            # Salary   Employee_ID            Name Department                Role     Company       City  Experience_Years
            # 1514341            1      Employee_1         IT   Backend Developer  Microsoft      Mumbai               2.4
            # 1495105            2      Employee_2    Finance     DevOps Engineer      Amazon       Pune               8.9
            # 1387438            3      Employee_3         IT  Frontend Developer         TCS  Hyderabad              13.9
            # 1345806            4      Employee_4         IT   Software Engineer  Microsoft        Pune               0.6
            # 1962417            5      Employee_5         IT      Data Scientist   Accenture       Pune              10.2
            # ...              ...             ...        ...                 ...         ...        ...               ...
            # 1537932        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi               1.0
            # 1970199        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi               6.9
            # 650399         11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad               8.8
            # 1551349        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi               9.0
            # 999198         12000  Employee_12000         IT             Auditor       Wipro  Bangalore               9.5

            # [12000 rows x 7 columns]



print(df.reset_index())

            #       index  Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years
            # 0          0            1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4
            # 1          1            2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9
            # 2          2            3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9
            # 3          3            4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6
            # 4          4            5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2
            # ...      ...          ...             ...        ...                 ...         ...        ...      ...               ...
            # 11995  11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0
            # 11996  11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9
            # 11997  11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8
            # 11998  11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0
            # 11999  11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5

            # [12000 rows x 9 columns]



#  Convert salary

df['Salary_INR'] = df['Salary'].apply(lambda x : x * 100)
print(df)

            #      Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years  Salary_INR
            # 0                1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4   151434100
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9   149510500
            # 2                3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9   138743800
            # 3                4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6   134580600
            # 4                5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2   196241700
            # ...            ...             ...        ...                 ...         ...        ...      ...               ...         ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0   153793200
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9   197019900
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8    65039900
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0   155134900
            # 11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5    99919800

            # [12000 rows x 9 columns]



# another type to convert salary

def euro_inr(x):
    return x * 80
df['Salary_INR'] = df['Salary'].apply(euro_inr)
print(df)

            #        Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years  Salary_INR
            # 0                1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4   121147280
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9   119608400
            # 2                3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9   110995040
            # 3                4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6   107664480
            # 4                5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2   156993360
            # ...            ...             ...        ...                 ...         ...        ...      ...               ...         ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0   123034560
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9   157615920
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8    52031920
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0   124107920
            # 11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5    79935840

            # [12000 rows x 9 columns]

#  Calculate length of Role

df['Role_Length'] = df['Role'].apply(len)
print(df)

            #       Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years  Salary_INR  Role_Length
            # 0                1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4   121147280           17
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9   119608400           15
            # 2                3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9   110995040           18
            # 3                4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6   107664480           17
            # 4                5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2   156993360           14
            # ...            ...             ...        ...                 ...         ...        ...      ...               ...         ...          ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0   123034560           17
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9   157615920           17
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8    52031920           17
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0   124107920           14
            # 11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5    79935840            7

            # [12000 rows x 10 columns]

#  Conditional statement on experience  years

def Check_Exp(x):
    if x<3:
        return 'Fresher Level'
    elif x >= 3 and x < 7:
        return 'Moderate Level'
    else:
        return 'Advance Level'

df['Check_Experience'] = df['Experience_Years'].apply(Check_Exp)
print(df)

            #        Employee_ID            Name Department                Role     Company       City   Salary  Experience_Years  Salary_INR  Role_Length Check_Experience
            # 0                1      Employee_1         IT   Backend Developer  Microsoft      Mumbai  1514341               2.4   121147280           17    Fresher Level
            # 1                2      Employee_2    Finance     DevOps Engineer      Amazon       Pune  1495105               8.9   119608400           15    Advance Level
            # 2                3      Employee_3         IT  Frontend Developer         TCS  Hyderabad  1387438              13.9   110995040           18    Advance Level
            # 3                4      Employee_4         IT   Software Engineer  Microsoft        Pune  1345806               0.6   107664480           17    Fresher Level
            # 4                5      Employee_5         IT      Data Scientist   Accenture       Pune  1962417              10.2   156993360           14    Advance Level
            # ...            ...             ...        ...                 ...         ...        ...      ...               ...         ...          ...              ...
            # 11995        11996  Employee_11996    Finance   Investment Banker  Microsoft       Delhi  1537932               1.0   123034560           17    Fresher Level
            # 11996        11997  Employee_11997    Finance   Investment Banker    Deloitte      Delhi  1970199               6.9   157615920           17   Moderate Level
            # 11997        11998  Employee_11998         IT   Financial Analyst         TCS  Hyderabad   650399               8.8    52031920           17    Advance Level
            # 11998        11999  Employee_11999         IT      Data Scientist       Wipro      Delhi  1551349               9.0   124107920           14    Advance Level
            # 11999        12000  Employee_12000         IT             Auditor       Wipro  Bangalore   999198               9.5    79935840            7    Advance Level

            # [12000 rows x 11 columns]