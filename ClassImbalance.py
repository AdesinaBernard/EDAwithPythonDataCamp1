import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#load salaries csv to begin EDA
salaries = pd.read_csv('/Users/mac/Downloads/datasets/ds_salaries_clean.csv')
print(salaries.head())
print(salaries.columns)

#Checking for class imbalance using value count, normalize
print(salaries['Designation'].value_counts(normalize=True))

#using a crosstab
print(pd.crosstab(salaries['Experience'], salaries['Company_Size']))

print(pd.crosstab(salaries['Designation'], salaries['Company_Size']))

print(pd.crosstab(salaries['Designation'], salaries['Company_Size'], values=salaries['Salary_USD'], aggfunc='mean'))

#Extracting features for correlation
#salaries['month'] = salaries['date_of_response'].dt.month
#salaries['weekday'] = salaries['date_of_response'].dt.weekday

#sns.heatmap(salaries.corr(), annot=True)
#plt.show()

#Calculating Salary Percentile
twenty_fifth = salaries['Salary_USD'].quantile(0.25)
salary_median = salaries['Salary_USD'].median()
seventy_fifth = salaries['Salary_USD'].quantile(0.75)

print(twenty_fifth,salary_median,seventy_fifth)

#Categorizing salaries
#Create salary labels
salary_labels = ['Entry','Mid','Senior', 'Exec']
#Create the salary range list
salary_ranges = [0,twenty_fifth,salary_median,seventy_fifth,salaries['Salary_USD'].max()]
#Create the salary level
salaries['salary_level'] = pd.cut(salaries['Salary_USD'], bins=salary_ranges, labels=salary_labels)
print(salaries['salary_level'].value_counts())

#Count of salary level at different company sizes
sns.countplot(data=salaries, x='Company_Size', hue='salary_level')
plt.title('Salary Levels By Company Size')
plt.show()

