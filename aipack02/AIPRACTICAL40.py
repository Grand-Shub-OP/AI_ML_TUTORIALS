# NOTE: seed value makes the random numbers predictable & regeneratable
# Virtual random numbers are deterministic if seeded

import numpy as np

# Random numbers without seed (different each run)
res1 = np.random.rand(4)
print("\nres1 =", res1)

# Set seed to 1 and generate random numbers
np.random.seed(1)
res2 = np.random.rand(4)
print("\nres2 =", res2)

# Set seed to 0 and generate random numbers
np.random.seed(0)
res3 = np.random.rand(4)
print("\nres3 =", res3)

# Reset seed to 1 and generate again (same as res2)
np.random.seed(1)
res4 = np.random.rand(4)
print("\nres4 =", res4)

np.random.seed(1234567890)
res5 = np.random.rand(4)
print("\nres5 =",res5)
