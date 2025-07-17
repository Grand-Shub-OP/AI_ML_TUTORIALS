import numpy as np

print("--- Sum by rows and by columns ---")

# Define a 2x2 array
x = np.array([[1, 2],
              [3, 4]])

# Display the original array
print("x =\n", x)

# Sum of all elements
print("x.sum() =", x.sum())  # 10

# Column-wise sum
print("x.sum(axis=0) column wise sum =", x.sum(axis=0))  # [4, 6]
print(x[:, 0].sum(), x[:, 1].sum())  # Individual column sums: 4, 6

# Row-wise sum
print("x.sum(axis=1) row wise sum =", x.sum(axis=1))  # [3, 7]
print(x[0, :].sum(), x[1, :].sum())  # Individual row sums: 3, 7