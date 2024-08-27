import numpy as np


a = np.arange(1, 11)
print(a)
print(a.reshape(5, 2))
print(a[2:4])
print(a[(a >= 5)])
ones = np.ones(10, dtype=int)
print(a - ones)
print(a.sum())