#AIPractical_147

# Count total NaN at each column in DataFrame.

import numpy as np
import pandas as pd

# List of Tuples
players = [ ('John',    22,     'Lucknow',   'Male'),
            ('Sachin',  np.nan, 'Delhi',     np.nan),
            ('Priti',   16,     'Patna',    'Female'),
            ('Trump',   41,     'Delhi',    'Male'),
            ('Alisha', np.nan, 'Delhi',     'Female'),
            ('Virat',   35,     'Mumbai',    np.nan),
            ('Obama',   35,      np.nan,    'Male'),
            (np.nan,    35,     'Uk',       'Male'),
            ('Jeet',    35,     'Guj',      'Male'),
            (np.nan,    np.nan, np.nan,     np.nan)
           ]

# Create a DataFrame object from list of tuples with columns and indices.
df = pd.DataFrame(players,  columns=['Name', 'Age', 'Place', 'Sex'],
                            index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k'])

print("Original Dataframe = \n", df)


# show the boolean dataframe
print(" \nshow the boolean Dataframe : \n\n", df.isnull())

report = df.isnull().sum()
# Count total NaN at each column in a DataFrame
print(" \nCount total NaN at each column in a DataFrame : \n\n", report )


print("df.info() = \n" )
df.info()
