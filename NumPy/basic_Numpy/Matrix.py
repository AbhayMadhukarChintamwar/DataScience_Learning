import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("Matrix:\n", matrix)
print("Shape:", matrix.shape)

arr = np.ones((3,3,3), dtype ='bool')

print(arr)

                # [[[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]

                #  [[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]

                #  [[ True  True  True]
                #   [ True  True  True]
                #   [ True  True  True]]]


arr = np.ones((3,3,3), dtype ='int')
print(arr)

                # [[[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]

                #  [[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]

                #  [[1 1 1]
                #   [1 1 1]
                #   [1 1 1]]]


#  Diagonal matrix / identity Matrix
arr =  np.eye(5)
print(arr)

                # [[1. 0. 0. 0. 0.]
                #  [0. 1. 0. 0. 0.]
                #  [0. 0. 1. 0. 0.]
                #  [0. 0. 0. 1. 0.]
                #  [0. 0. 0. 0. 1.]]



arr = np.eye(3,6)
print(arr)

                # [[1. 0. 0. 0. 0. 0.]
                #  [0. 1. 0. 0. 0. 0.]
                #  [0. 0. 1. 0. 0. 0.]]


# Create random function  -> rand()- the random module's rand() method returns a random float between 0 and 1

arr = np.random.rand(5)
print(arr)   # [0.1936349  0.7294812  0.04395402 0.5470296  0.36930658]