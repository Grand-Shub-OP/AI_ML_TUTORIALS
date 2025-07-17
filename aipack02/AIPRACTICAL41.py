# Practical-41: Reshaping arrays with NumPy

import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape into 2 rows and 3 columns
reshaped_arr = np.reshape(arr, (6, 1))
print("Reshaped to 2x3:\n", reshaped_arr)

