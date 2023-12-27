import pandas as pd


# Load Data
data = pd.read_csv("dataset-1.csv")
# print(data)

# Read Top 10 Values(.head())
print(data.head(10))

# read Botton 10 rows(.tail())
print(data.tail(10))

# Find Data Types (.info())
print(data.info())

# Describe Data (describe())
print(data.describe())

# Find Null Values (.isnull().sum())
print(data.isnull().sum())