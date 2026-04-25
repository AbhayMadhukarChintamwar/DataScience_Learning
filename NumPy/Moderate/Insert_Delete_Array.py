import numpy as np

# insert function

arr = np.array([5,32,32,44,5,55])
print(np.insert(arr,3,60))  # [ 5 32 32 60 44  5 55]


arr = np.array([5,32,32,44,5,55])
print(np.insert(arr,(3,4),(70,80)))  # [ 5 32 32 44 70  5 80 55]

arr_2d = np.array([[5,32,32,44,5,55],
                   [45,42,3,4,54,65]])
print(arr_2d)
            # [ 5 32 32 60 44  5 55]
            # [ 5 32 32 70 44 80  5 55]


insert_2d = np.insert(arr_2d,1,100,axis =0)
print(insert_2d)
            # [[  5  32  32  44   5  55]
            #  [100 100 100 100 100 100]
            #  [ 45  42   3   4  54  65]]


insert_2d = np.insert(arr_2d,3,100,axis =1)
print(insert_2d)
            # [[  5  32  32 100  44   5  55]
            #  [ 45  42   3 100   4  54  65]]


insert_2d = np.insert(arr_2d,1,[100,101,102,103,104,105],axis =0)
print(insert_2d)
            # [[  5  32  32  44   5  55]
            #  [100 101 102 103 104 105]
            #  [ 45  42   3   4  54  65]]


insert_2d = np.insert(arr_2d,1,[100,101],axis =1)
print(insert_2d)
            # [[  5 100  32  32  44   5  55]
            #  [ 45 101  42   3   4  54  65]]

# append

arr = np.array([5,32,32,44,5,55])
append_arr = np.append(arr,3.5)
print(append_arr)

arr_2d = np.array([[5,32,32,44,5,55],
                   [45,42,3,4,54,65]])
            # [ 5.  32.  32.  44.   5.  55.   3.5]


append_2d = np.append(arr_2d, [[4,5,6,7,8,9]], axis = 0)
print(append_2d)
            # [[ 5 32 32 44  5 55]
            #  [45 42  3  4 54 65]
            #  [ 4  5  6  7  8  9]]

arr_2d = np.array([[5,32,32,44,5,55],
                   [45,42,3,4,54,65]])

append_2d = np.append(arr_2d, [[4],[5]], axis = 1)
print(append_2d)
            # [[ 5 32 32 44  5 55  4]
            #  [45 42  3  4 54 65  5]]


# Delete

arr = np.array([5,32,32,44,5,55])
delete_arr = np.delete(arr, [1])
print(delete_arr) # [ 5 32 44  5 55]

arr_2d = np.array([[5,32,32,44,5,55],
                   [45,42,3,4,54,65],
                   [44,23,33,42,88,66]])

delete_2d = np.delete(arr_2d,[[1]], axis = 0)
print(delete_2d)
            # [[ 5 32 32 44  5 55]
            #  [44 23 33 42 88 66]]

arr_2d = np.array([[5,32,32,44,5,55],
                   [45,42,3,4,54,65],
                   [44,23,33,42,88,66]])

delete_2d = np.delete(arr_2d,[[4]], axis = 1)
print(delete_2d)
            # [[ 5 32 32 44 55]
            #  [45 42  3  4 65]
            #  [44 23 33 42 66]]
