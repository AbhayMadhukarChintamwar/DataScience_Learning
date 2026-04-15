
from array import *

arr1 = array('i', [11,223,12,43])
# arr2 = array('i, arr1.tolist())
# arr2 = array(arr1.typecode, arr1.tolist())

arr2 = array(arr1.typecode, (n for n in arr1))


arr1[2] =54

print(arr1)
print(arr2)

print(type(arr1))
print(type(arr2))
