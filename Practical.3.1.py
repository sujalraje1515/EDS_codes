import numpy as np

# Input matrices
print("Enter Matrix A:")
matrix_a = np.array([list(map(int, input().split())) for i in range(3)])

print("Enter Matrix B:")
matrix_b = np.array([list(map(int, input().split())) for i in range(3)])


# Addition
addition = matrix_a + matrix_b
print("Addition (A + B):")
print(addition)
# Subtraction
subtraction = matrix_a - matrix_b
print("Subtraction (A - B):")
print(subtraction)
# Multiplication (element-wise)
element_wise_mult = matrix_a * matrix_b
print("Element-wise Multiplication (A * B):")
print(element_wise_mult)
# Matrix multiplication (dot product)
matrix_mult = np.dot(matrix_a, matrix_b)
print("A dot B:")
print(matrix_mult)
# Transpose
transpose_a = matrix_a.T
print("Transpose of A:")
print(transpose_a)