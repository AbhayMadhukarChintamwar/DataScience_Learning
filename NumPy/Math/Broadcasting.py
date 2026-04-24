import numpy as np

# Broadcasting
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1],[2],[3],[4]])
# sum  = arr1 + arr2
# print(sum)
print(np.add(arr1, arr2))
            # [[2 3 4 5]
            #  [3 4 5 6]
            #  [4 5 6 7]
            #  [5 6 7 8]]

arr3 = np.array([[1],[2]])
print(np.shape(arr3))
arr4 = np.array([[1,2,3],[2,3,4]])
print(np.shape(arr4))

print(np.add(arr3,arr4))
            # [[2 3 4]
            #  [4 5 6]]

print(np.subtract(arr3,arr4))
            # [[ 0 -1 -2]
            #  [ 0 -1 -2]]
