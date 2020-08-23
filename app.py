import numpy as np

array = np.array([1,2,3])

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