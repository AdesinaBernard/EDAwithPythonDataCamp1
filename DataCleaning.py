import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#load planes csv to begin EDA
planes = pd.read_csv('/Users/mac/Downloads/EDA with Python/planes.csv')
print(planes.head(5))
print(planes.columns)
print(planes.shape)

#Count the number of missing values in each column
print(planes.isna().sum())

#find the 5% threshold
threshold = len(planes) * 0.05

#create a filter
cols_to_drop = planes.columns[planes.isna().sum() <= threshold]

planes.dropna(subset=cols_to_drop, inplace=True)

print(planes.isna().sum())

#Strategy to remove the remaining missing values
print(planes['Additional_Info'].value_counts())
planes = planes.drop(['Additional_Info'], axis=1)

#sns.boxplot(data=planes, x='Airline', y='Price')
plt.title('Price by Airline')
#plt.show()

#Imputing missing prices
airline_prices = planes.groupby('Airline')['Price'].median()
print(airline_prices)

#convert to dictionary
price_dict = airline_prices.to_dict()

#mapping dictionary with the missing values
planes['Price'] = planes['Price'].fillna(planes['Airline'].map(price_dict))

print(planes.isna().sum())

#Finding the number of unique values
non_numeric = planes.select_dtypes('object')
for names in non_numeric.columns:
    print(f'Number of unique values in {names} column: ', non_numeric[names].nunique())

#Creating a list of categories
flight_categories = ['Short_haul', 'Medium', 'Long_haul']

short_flights = "^0h|^1h|^2h|^3h|^4h"
medium_flights = "^5h|^6h|^7h|^8h|^9h|"
long_flights = "10h|11h|12h|13h|14h|15h|16h"

#Adding a new category
conditions = [
    (planes['Duration'].str.contains(short_flights)),
    (planes['Duration'].str.contains(medium_flights)),
    (planes['Duration'].str.contains(long_flights))
]

planes['Duration_Category'] = np.select(conditions,flight_categories,default='Extreme durations')

#sns.countplot(data=planes, x='Duration_Category')
plt.title('Flight Duration Categories')
#plt.show()

#Show the new category created in the list of categories
print(planes.columns)

#Convert a column data type
print(planes['Duration'].head())
#planes['Duration'] = planes['Duration'].str.replace('h', '')
#planes['Duration'] = planes['Duration'].astype(float)
#sns.histplot(data=planes, x='Duration')
#plt.title('Count by Duration')
#plt.show()

#Adding descriptive statistics
planes['price_std_dev'] = planes.groupby('Airline')['Price'].transform(lambda x: x.std())
print(planes[['Airline', 'price_std_dev']].value_counts())

#planes['duration_median'] = planes.groupby('Airline')['Duration'].transform(lambda x: x.median())
#print(planes[['Airline', 'duration_median']].value_counts())

planes['price_destination_mean'] = planes.groupby('Destination')['Price'].transform(lambda x: x.std())
print(planes[['Airline', 'price_destination_mean']].value_counts())

#Identifying outliers
sns.histplot(data=planes, x='Price')
plt.show()
print(planes['Duration'].describe())

#removing outliers
price_seventy_fifth = planes['Price'].quantile(0.75)
price_twenty_fifth = planes['Price'].quantile(0.25)

IQR = price_seventy_fifth - price_twenty_fifth

upper = price_seventy_fifth + (1.5 * IQR)
lower = price_twenty_fifth - (1.5 * IQR)

planes = planes[(planes['Price'] < upper) & (planes['Price'] > lower)]

print(planes['Price'].describe())