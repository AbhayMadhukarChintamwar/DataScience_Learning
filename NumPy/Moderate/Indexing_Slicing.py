import numpy as np

arr = np.array([1,2,3,4,5])

# Slicing
print(arr[1:4])  # Output: [2 3 4]

# Indexing with boolean array
bool_idx = (arr > 2)
print(arr[bool_idx])  # Output: [3 4 5]

# Fancy indexing
indices = [0, 2, 4]
print(arr[indices])  # Output: [1 3 5]

indices = arr[0:5:2]  # Get every second element
print(indices)  # Output: [1 3 5]

# Negative indexing
print(arr[-1])  # Output: 5
print(arr[-3:-1])  # Output: [3 4]

