import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#load unemployment csv to begin EDA
unemployment = pd.read_csv('/Users/mac/Downloads/EDA with Python/clean_unemployment.csv')
print(unemployment.head())
print(unemployment.tail())
print(unemployment.info())
print(unemployment.describe())

print(unemployment['continent'].value_counts())

#create an histogram of unemployment in 2021
sns.histplot(data=unemployment, x="2021", binwidth=1)
plt.title("Unemployment in 2021")
#plt.show()

#Filter our unemployment data for countries whose continent is not oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])
print(unemployment[not_oceania])

#See the min and max employement rates in 2021
print(unemployment["2021"].min(),unemployment["2021"].max())

#boxplot of unemployment in 2021 by continent
sns.boxplot(data=unemployment, x="2021", y="continent")
plt.title("Unemployment in 2021 by continent")
#plt.show()

#summarise data using groupby and aggregates
print(unemployment.groupby('continent')['2021'].agg(['mean','std']))

continent_summary = unemployment.groupby('continent').agg(
    mean_rate_2021 = ('2021','mean'),
    std_rate_2021 = ('2021','std')
)

print(continent_summary)

#A barplot showing continents and their average unemployement rate in 2021
sns.barplot(data=unemployment, x='continent', y='2021')
plt.title('Avg unemployment rate by continent in 2021')
plt.show()

