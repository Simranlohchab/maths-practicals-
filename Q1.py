import numpy as np

# Creating a vector
vec = np.array([1, 2, 3])
print("Vector:\n", vec)

# Creating a matrix
mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix:\n", mat)

# Transpose of a vector
vec_t = vec.T
print("Transpose of vector:\n", vec_t)

# Transpose of a matrix
mat_t = mat.T
print("Transpose of matrix:\n", mat_t)

# Conjugate transpose of a vector
vec_ct = vec.conj().T
print("Conjugate transpose of vector:\n", vec_ct)

# Conjugate transpose of a matrix
mat_ct = mat.conj().T
print("Conjugate transpose of matrix:\n", mat_ct)
