import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#Load salaries csv to begin EDA
salaries = pd.read_csv('/Users/mac/Downloads/datasets/ds_salaries_clean.csv')
print(salaries.columns)
print(salaries['Employee_Location'].head())

#Filter out employees in USA and GB
usa_and_gb = salaries[salaries['Employee_Location'].isin(['US','GB'])]
#sns.barplot(data=usa_and_gb, x='Employee_Location', y='Salary_USD')
#plt.title('Salaries of Employees in USA and GB')
#plt.show()

#Choosing a hypothesis
#View salary by company size based on employment status
sns.barplot(data=salaries, x='Company_Size', y='Salary_USD', hue='Employment_Status')
plt.title('Salary by Company Size Based on Employment Status')
plt.show()