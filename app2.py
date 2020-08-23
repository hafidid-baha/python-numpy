import numpy as np

# initlize array in numpy module
# create 0s matrix
array =  np.zeros((2,2)) #create two dim array 2 rows and 2 cols
# print(array)

#create 0s matrix
array2 = np.ones((3,2))
# print(array2)

#create and init array with specific number
array3 = np.full((2,3,4),4)
# print(array3)
#using full like function to clone the shape of existing array
array4 = np.full_like(array3,7)
# print(array4)
# create rondom array
array5 = np.random.rand(4,2)
# print(array5)
#creating random integer values
array6 = np.random.randint(8,40,size=(4,2))
# print(array6)
# creating identity matrix
array7 = np.identity(7)
print(array7)