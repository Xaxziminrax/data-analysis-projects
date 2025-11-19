import pandas as pd
import numpy as np

array1 = np.array([8, 5, 3, 2, 1, 1])
print(array1)

array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
print(array2)

# import numpy as np

# Create a NumPy multi-dimensional array from nested lists
# array2 = np.array([[5, 1, 3], [1, 8, 7], [3, 7, 9]])
# Number of dimensions of array2
print(array2.ndim)
# Number of elemets (rows & columns in this instance) of array2
print(array2.shape)