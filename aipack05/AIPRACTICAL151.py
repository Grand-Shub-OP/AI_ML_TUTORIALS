# Filling null values using replace() method

import pandas as pd
import numpy as np

# Making DataFrame from CSV file
data = pd.read_csv("employees_with_missing_data.csv")

# Replace the value -99 with numpy's Not a Number (np.nan)
df2 = data.replace(to_replace=-99, value=np.nan)
print(df2)

# Replace 'Male' with 'M'
df3 = df2.replace(to_replace='Male', value='M')

# Replace 'Female' with 'F'
df4 = df3.replace(to_replace='Female', value='F')

print("-" * 30)
print(df4)