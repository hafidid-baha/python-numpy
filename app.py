import numpy as np

array = np.array([1,2,3])
# array = np.array([1,2,3],dtype='int16')

print(array)

twodimarray = np.array([[0,1,2],[4,5,6]])
print(twodimarray)

# getting the number of array dimentions
print("number of dimentions")
print(array.ndim)
print(twodimarray.ndim)
#getting the number of columns and rows
print("the shape of array")
print(array.shape)
print(twodimarray.shape)
#getting the type of array
print("array type")
print(array.dtype)
print(twodimarray.dtype)
# getting the numpy array size
print("numpy array size")
print(array.itemsize)
print(twodimarray.itemsize)
# get total items size
print("total array size")
print(array.size * array.itemsize)
# getting the size of array using nbytes
print(array.nbytes)
print(twodimarray.size * twodimarray.itemsize)