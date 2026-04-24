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
print(arr)       # [0.1936349  0.7294812  0.04395402 0.5470296  0.36930658]



arr = np.random.rand(3,4)
print(arr)

                # [[0.33813632 0.32891442 0.30914899 0.64250485]
                #  [0.74456296 0.99442786 0.92856096 0.17922669]
                #  [0.83979184 0.03382966 0.42609758 0.98180577]]


#  randn()  -> the function is used to generate a value close to 0 and this may return positive or negative numbers as well

arr = np.random.randn(5)
print(arr)      # [ 0.40880727 -0.659083    0.11744055 -1.29112291  0.68266396]

arr = np.random.randn(3,4)
print(arr)

                # [[ 0.03775594  0.2287991   2.44219681  2.09836257]
                #  [-0.90708498  0.19727228 -2.55925208  1.98777085]
                #  [-0.67725359 -1.0293192  -2.46284765  1.21420157]]
