#Example-09 Part-01
#Use of optimized Pandas data access methods, .at, .iat, .loc, .iloc
import numpy as np
import pandas as pd
df = pd.DataFrame( np.random.randn(6,4),
                   index=pd.date_range( start='20190101', periods=6, freq='D'),
                   columns=['A', 'B', 'C', 'D']
                 )
#Selecting a single column, which yields a Series, equivalent to df.A
print( "nIn df.A = \n", df.A )
print( "\nIn df['A']= \n", df['A'] )
