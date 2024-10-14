import numpy as np

arr = np.array([1, 2, 3, 4, 5])           # Print an array having in a list

print(arr) 
print(type(arr))

#================================================================================
arr_tuple = np.array((1,2,3,4,5))              # Creating an array using tuple

print(arr_tuple)

#=================================================================================

array2d = np.array([[1,2,3],[4,5,6]])       # Creating a 2 dimensional array 
print(array2d)

#=================================================================================

array3d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # Creating a 3 dimensional array
print(array3d)
print(array3d.ndim)

#==================================================================================

arr = np.array([1, 2, 3, 4, 5])           # Printing the value of an index

#              [0],[1],[2],[3],[4]           respective indexes

print(arr[1]) 
print(arr[0]+arr[1])                      #using the index value, adding the value
print(arr[2]*arr[3])                      #using the index value, multiple the value
#===================================================================================