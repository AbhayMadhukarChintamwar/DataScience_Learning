import numpy as np

a = np.array([1, 2, 3]) # This creates a 1D array with integer values from 1 to 3.
b = np.array([4, 5, 6]) # This creates another 1D array with integer values from 4 to 6.
print(a + b) # Output: [5 7 9] This performs element-wise addition of the two arrays 'a' and 'b', resulting in a new array where each element is the sum of the corresponding elements from 'a' and 'b': [1+4, 2+5, 3+6] = [5, 7, 9].
print(a - b) # Output: [-3 -3 -3] This performs element-wise subtraction of the two arrays 'a' and 'b', resulting in a new array where each element is the difference of the corresponding elements from 'a' and 'b': [1-4, 2-5, 3-6] = [-3, -3, -3].
print(a * b) # Output: [ 4 10 18] This performs element-wise multiplication of the two arrays 'a' and 'b', resulting in a new array where each element is the product of the corresponding elements from 'a' and 'b': [1*4, 2*5, 3*6] = [4, 10, 18].
print(a // b) # Output: [0.25 0.4  0.5 ] This performs element-wise division of the two arrays 'a' and 'b', resulting in a new array where each element is the quotient of the corresponding elements from 'a' and 'b': [1/4, 2/5, 3/6] = [0.25, 0.4, 0.5].
print(a % b)
print(a ** b)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)