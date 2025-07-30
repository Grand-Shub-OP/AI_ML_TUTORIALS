# Writing to MS Excel
# install xlrd openpyxl
# Note: Installation not required if anaconda configured
# Writing to an excel file

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4),
                  index=pd.date_range('20190101', periods=6, freq='M'),
                  columns=['A', 'B', 'C', 'D'])

print("data\n", df)

df.to_excel('outputData.xlsx', sheet_name='Sheet1')

print("Data saved in excel file.")