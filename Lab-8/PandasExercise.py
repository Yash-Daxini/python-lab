from operator import le
from tkinter import ON
import pandas as pd

sal = pd.read_csv( "E:\\Y\\DIET\\Sem-5\\PDS\\Labs\\Salaries.csv")

print(sal)

print(sal.info())

print( sal['BasePay'].mean() )

print( sal['OvertimePay'].max() )

print( sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'] )

print( sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'] )

print( sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'] )

print( sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName'] )

print( sal.groupby('Year').mean()['BasePay'] )

print( len(sal.groupby('JobTitle')) )

sal.groupby('JobTitle').count().sort_values(by=['Id'],ascending=False).head()

sal['JobTitle'].value_counts().head() 

(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1).sum()

len([j for j in [ i for i in sal['JobTitle'] ] if j.lower().find('chief') != -1 ])

sal['title_len'] = sal['JobTitle'].apply(len)

sal[['title_len','TotalPayBenefits']].corr()