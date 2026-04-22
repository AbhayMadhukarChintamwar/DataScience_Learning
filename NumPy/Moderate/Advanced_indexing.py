import numpy as np

arr = np.array([1,2,3,4,5])

# np.take() function for advanced indexing
ind = [0,2]
print(np.take(arr, ind))  # Output: [1 3]


# iterating over an array with np.nditer()

arr_2d = np.array([[1, 2], [3, 4]])
print('Iterating over 2D array:')
for x in np.nditer(arr_2d):
    print(x, end= ' ')  # Output: 1 2 3 4


# ndenumerate() for indexed iteration

print('\nIndexed iteration over 2D array:')
for idx, x in np.ndenumerate(arr_2d):  # idx is the index of the element and x is the value of the element
    print(idx, x)  # Output: (0, 0) 1, (0, 1) 2, (1, 0) 3, (1, 1) 4


# view vs copies in NumPy

arr = np.array([1, 2, 3, 4, 5])

view = arr[1:4]  # This creates a view of the original array
print('View:', view)  # Output: [2 3 4]

view[0] = 99  # Modifying the view will modify the original array
print('Modified view:', view)  # Output: [99 3 4]
print('Original array after modifying view:', arr)  # Output: [ 1 99  3  4  5]

copy = arr[1:4].copy()  # This creates a copy of the original array
print('Copy:', copy)  # Output: [99 3 4]

copy[0] = 88  # Modifying the copy will not modify the original array

print('Modified copy:', copy)  # Output: [88 3 4]
print('Original array after modifying copy:', arr)  # Output: [ 1 99  3  4  5]

