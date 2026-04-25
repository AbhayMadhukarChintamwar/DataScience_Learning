import numpy as np



#  Matrix Creation
matrix_1 = np.matrix([[1, 2],
                      [4, 5]])

matrix_2 = np.matrix([[1, 2],
                      [4, 5]])

product_matrix = matrix_1 * matrix_2
print('This is the product of matrix :')
print(product_matrix)

print()

array_1 = np.array([[1, 2],
                      [4, 5]])

array_2 = np.array([[1, 2],
                      [4, 5]])
product_array = array_1 * array_2
print('This is the product of arrays :')
print(product_array)
