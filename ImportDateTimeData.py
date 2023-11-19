import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy

#load planes csv to begin EDA
divorce = pd.read_csv('/Users/mac/Downloads/EDA with Python/divorce.csv', parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'])
print(divorce.dtypes)

divorce['marriage_year'] = divorce['marriage_date'].dt.year
#sns.lineplot(data=divorce, x='marriage_year', y='num_kids')
plt.title('Average number of kids per year')
#plt.show()

#Visualizing variable relationships
#sns.scatterplot(data=divorce, x='marriage_duration', y='num_kids')
plt.title('Length of marriage vs number of kids')
#plt.show()

#Visualizing multiple variable relationships
#sns.pairplot(data=divorce, vars=['income_woman','marriage_duration'])
plt.title('')
#plt.show()

#Creating a categorical data in scatterplot
divorce['womens_age_marriage'] = (divorce['marriage_date'].dt.year - divorce['dob_woman'].dt.year)

print(divorce['womens_age_marriage'].head())

#sns.scatterplot(data=divorce, x='womens_age_marriage', y='income_woman', hue='education_woman')
plt.title('Womens age before marriage by income, categorized by level of education')
#plt.show()

#Kernel Density Estimate Plot
sns.kdeplot(data=divorce, x='marriage_duration', hue='num_kids', cut=0, cumulative=True)
plt.show()

#My first commit via pychrm
