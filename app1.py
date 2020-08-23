import numpy as np

array = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# getting the array shape (rows,columns)
print(array.shape)

# getting a specific element [row,column]
print(array[0,5]) #prints 6
# getting specific row
print(array[1,:])
# getting a specific column
print(array[:,2])
# getting a part of row slices [row,startindex:endindex:steps]
print(array[1,1:5:1])