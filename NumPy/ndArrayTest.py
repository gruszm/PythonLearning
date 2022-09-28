import numpy as np

arr = np.array([1, 2, 3])

print("%s = %s" % (type(arr), arr))

scalar = np.array(12)                                                     # Scalar - 0-D array
array1D = np.array([2, 0, 5])                                             # 1-D array
array2D = np.array([[17, -5, 4], [2, 11, 2]])                             # 2-D array
array3D = np.array([[[12, 2, 1], [1, 1, 53]], [[52, 1, 22], [9, 81, 5]]]) # 3-D array

# Dimensions of every array
print(scalar.ndim)
print(array1D.ndim)
print(array2D.ndim)
print(array3D.ndim)