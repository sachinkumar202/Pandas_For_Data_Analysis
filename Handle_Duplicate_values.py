import pandas as pd


data = pd.read_csv('dataset-1.csv')
# print(data)


# find Duplicate Values
# print(data.duplicated())
print(data.duplicated().sum())
