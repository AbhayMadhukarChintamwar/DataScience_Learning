import numpy as np


#  Dealing with missing values:
# np.nan -> represents missing values in NumPy arrays
arr_with_nan = np.array([1, 2, np.nan, 4, 5])
print('Array with NaN value :')
print(arr_with_nan)  # Output: [ 1.  2. nan  4.  5.]

# np.inf and -np.inf -> represent positive and negative infinity in NumPy arrays
arr_with_inf = np.array([1, 2, np.inf, -np.inf, 5])
print('Array with Inf and -Inf values :')
print(arr_with_inf)  # Output: [ 1.  2. inf -inf  5.]

# np.isnan() function to check for NaN values
print('Check for NaN values in the array :')
print(np.isnan(arr_with_nan))  # Output: [False False  True False False]

# np.isinf() function to check for Inf values
print('Check for Inf values in the array :')
print(np.isinf(arr_with_inf))  # Output: [False False  True  True False]

# np.isfinite() function to check for finite values (not NaN or Inf)
print('Check for finite values in the array :')
print(np.isfinite(arr_with_inf))  # Output: [ True  True False False  True]


new_arr = np.nan_to_num(arr_with_nan)  # Replace NaN with 0 and Inf with large finite numbers
print('Array after replacing NaN and Inf values :')
print(new_arr)  # Output: [1. 2. 0. 4. 5.]
