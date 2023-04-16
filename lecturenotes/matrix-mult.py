import numpy as np

# Define the size of the matrix
n = 3

# Generate two n by n matrices with random values
A = np.random.randint(0, 10, size=(n, n))
B = np.random.randint(0, 10, size=(n, n))


# Multiply the two matrices together using nested for loops
C = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# Output the resulting matrix
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Resulting matrix C:")
print(C)
