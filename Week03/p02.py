"""2. Create two (3 * 3) matrices using NumPy and print it. Perform 
and print the results of the following linear algebra operations 
a. Matrix addition 
b. Matrix subtraction 
c. Matrix multiplication (element-wise and dot product) 
d. Transpose of a matrix 
e. Determinant and inverse (if applicable) """

import numpy as np
print("Enter elements of matrix A: ")
A=np.array([[int(input()) for j in range(3)] for i in range(3)])

print("Enter elements of matrix B: ")
B=np.array([[int(input()) for j in range(3)] for i in range(3)])

print("Matrix A: ")
print(A)
print("Matrix B: ")
print(B)
print("Matrix addition: ")
print(A+B)
print("Matrix Subtraction: ")
print(A-B)
print("Matrix Multiplication: ")
print(A*B)
print("Dot Product: ")
print(A.dot(B))
print("Transpose of matrix A: ")
print(A.T)
print("Determinant: ")
deter=np.linalg.det(A)
print(deter)
if deter!=0:
    print("Inverse of A: ")
    print(np.linalg.inv(A))
else:
    print("Inverse doesn't exist as determinant is zero")
    