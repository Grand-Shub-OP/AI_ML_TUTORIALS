# Reading from an excel file

import pandas as pd

restored_df = pd.read_excel('outputData.xlsx',
                            sheet_name='Sheet1',
                            index_col=0,
                            na_values=['NA'])

print(restored_df)