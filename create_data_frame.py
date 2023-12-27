import pandas as pd

# Create Data Frame

data = {"Name":['Sachin', 'Vijay', 'Kumar','Sandeep'],
        "Age":[23,34,25,32],
        "Salary":[20000,30000,40000,50000]}
df = pd.DataFrame(data)
print(df)


# read csv and other files(.csv, .xlsx)
#data = pd.read_csv("File Name")