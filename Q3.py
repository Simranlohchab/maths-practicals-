import numpy as np

# Define a matrix
A = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])

# Calculate the determinant of A
det_A = np.linalg.det(A)
print("Determinant of A: ", det_A)

# Calculate the inverse of A
inv_A = np.linalg.inv(A)
print("Inverse of A: ")
print(inv_A)

# Calculate the adjoint of A
adj_A = np.linalg.inv(A) * det_A
print("Adjoint of A: ")
print(adj_A)

# Calculate the cofactor matrix of A
cof_A = np.zeros(A.shape)
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        sub_matrix = np.delete(np.delete(A, i, axis=0), j, axis=1)
        cof_A[i,j] = (-1)**(i+j) * np.linalg.det(sub_matrix)
print("Cofactor matrix of A: ")
print(cof_A)

