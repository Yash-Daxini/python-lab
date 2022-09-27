import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


data = np.arange(1,6,1)

index = [101,102,103,104,105]

# arr = pd.Series([1,2,3,4,5])

arr = pd.Series(data=data , index = index)

# print(arr)

startDate = pd.to_datetime('13/09/2022' , infer_datetime_format=True)

index = startDate + pd.to_timedelta(np.arange(1,5),'W')

data = np.random.randint(1,100,4)

arr = pd.Series(data=data , index=index)

# print(arr)

# arr.plot()

# plt.show()
np.random.seed(121)
data = np.random.randint(1,101,(5,5))

index = np.arange(101,106)

column = np.array(["PDS","ADA","PE","SE","CN"])

df = pd.DataFrame(data,index,column)

# print(df)
# print(df["ADA"])
# print(df["ADA"][101])
# print(df.loc[101]["ADA"])
# print(df.loc[101]["PDS"])
# print(df.loc[[101 , 105]])
# print(df.loc[[101 , 105]][['PDS','CN']])
# print(df[['PDS','CN']].loc[[101,102]])
# print(df.loc[[101,102],['PDS','CN']])
# print(df.loc[101:104,'PDS':'SE'])

# print(df.drop('PDS',axis=1))

df.drop('PDS',axis=1)

# print(df.drop(102))

df.drop('PE',axis=1 , inplace=True )

df["TOTAL"] = df["CN"] + df["SE"] + df["PDS"] +df["ADA"]

df.drop('TOTAL', axis = 1 , inplace=True)

# print(df.loc[:,df.columns != 'SE'])

# print(df[df['ADA'] >= 60]['ADA'])

tempdf = df[df > 35]

# tempdf.dropna(inplace=True)
# print(tempdf.dropna(axis=1))

# print(tempdf.fillna('FAIL'))

# print(tempdf.interpolate())

# print(tempdf)

df.index.name = 'ROLLNO'

# df.reset_index(inplace=True)

# df.set_index('ADA',inplace=True)

# df.reset_index(inplace=True)

# df.set_index('ROLLNO',inplace=True)

# df = []

df = pd.read_csv("E:\\Y\\DIET\\Sem-5\\PDS\\Labs\\MultiIndexDemo.csv" , index_col=[0,1,2,3])

# df.set_index(["Col","Dep","Sem","RN"],inplace=True)

# print(df.loc['Darshan',"CE",5,101])

df = pd.read_excel("E:\\Y\\DIET\\Sem-5\\PDS\\Labs\\Studentdata.xlsx")

# print(df['SPI'])

groups = df.groupby(['Dep','Col'])

# print(groups)

for groupname , data in groups:
    print("-----",groupname,"-----")
    print(data["SPI"])
