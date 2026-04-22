import numpy as np


# Vectorization : Vectorization is the process of converting an algorithm from operating on a single value at a time to operating on a set of values (arrays) at once. This allows for more efficient computations and can significantly speed up the execution of code.
# Example of vectorization with a simple operation
# np.vectorize() function for vectorization of custom functions

arr = np.array([1, 2, 3, 4, 5])
def my_func(x):
    return x ** 2

vectorized_func = np.vectorize(my_func)
result = vectorized_func(arr)
print('Result of vectorized custom function :')
print(result)  # Output: [ 1  4  9 16 25]

