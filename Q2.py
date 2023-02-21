
import numpy as np

def echelon_form(A):
    n, m = np.shape(A)
    for i in range(n):
        # Find the pivot element
        pivot = A[i][i]
        if pivot == 0:
            # If the pivot is zero, swap the current row with a row below it
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[i], A[j] = A[j], A[i]
                    pivot = A[i][i]
                    break
        if pivot != 0:
            # Eliminate the elements below the pivot
            for j in range(i+1, n):
                factor = A[j][i] / pivot
                for k in range(i, m):
                    A[j][k] = A[j][k] - factor * A[i][k]
    return A

def rank(A):
    echelon_matrix = echelon_form(A)
    n, m = np.shape(echelon_matrix)
    rank = 0
    for i in range(n):
        # Check if the current row is a zero row
        zero_row = True
        for j in range(m):
            if echelon_matrix[i][j] != 0:
                zero_row = False
                break
        if not zero_row:
            # If the current row is not a zero row, increment the rank
            rank += 1
    return rank

# Example usage
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix:")
print(A)
print("Echelon form:")
print(echelon_form(A))
print("Rank:", rank(A))
