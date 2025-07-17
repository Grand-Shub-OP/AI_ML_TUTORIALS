# Practical-43: Reshaping 2D arrays into 1D/column/row vectors

import numpy as np

# Generate a 2x3 matrix of random values
ar1 = np.random.rand(2, 3)
print("ar1 =\n", ar1)

# Reshape to a single row with 6 columns
ar2 = ar1.reshape(1, 6)
print("ar2 =\n", ar2)

# Reshape to a single column with 6 rows
ar3 = ar1.reshape(6, 1)
print("ar3 =\n", ar3)
