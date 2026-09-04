import numpy as np


array_1d = np.arange(1, 11)
array_2d = np.arange(1, 10).reshape(3, 3)
array_from_list = np.array([10, 20, 30, 40, 50])


print("1D array shape:", array_1d.shape)
print("1D array data type:", array_1d.dtype)

print("2D array shape:", array_2d.shape)
print("2D array data type:", array_2d.dtype)

print("Array from list shape:", array_from_list.shape)
print("Array from list data type:", array_from_list.dtype)