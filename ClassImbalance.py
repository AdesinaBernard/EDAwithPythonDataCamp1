import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#load salaries csv to begin EDA
salaries = pd.read_csv('/Users/mac/Downloads/datasets/ds_salaries_clean.csv')
print(salaries.head())
print(salaries.columns)
