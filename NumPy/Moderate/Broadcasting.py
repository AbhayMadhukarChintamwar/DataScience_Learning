import numpy as np

# Broadcasting in NumPy
# Broadcasting allows NumPy to perform operations on arrays of different shapes and sizes without explicitly reshaping them.
# Example of broadcasting with different shapes
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1], [2], [3]])
result = arr_1d + arr_2d
print('Broadcasting result of adding 1D and 2D arrays:')
print(result)  # Output: [[2 3 4]
              #          [3 4 5]
              #          [4 5 6]]

# Example of broadcasting with different sizes
arr_1d = np.array([1, 2, 4])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
result = arr_1d + arr_2d
print('Broadcasting result of adding 1D and 2D arrays with different sizes:')
print(result)  # Output: [[2 4 7]
              #          [5 7 10]]


image = np.array([[1, 2],
                  [3, 4]])

brightness = image + 10    # Broadcasting adds 10 to each element of the image array
print('Brightness increased by 10 :')
print(brightness)  # Output: [[11 12]
                          #   [13 14]]


