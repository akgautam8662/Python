# NumPy Array Indexing :-

# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0])       # Return first element = 10
print(arr[1])       # Return secound element = 20
print(arr[-1])      # Return last element = 50
print(arr[1:4])     # Return given range value = [20 30 40]

# Adding element of array 
print(arr[3] + arr[4])      # arr[3]= 40 ,arr[4]= 50 

print("-------------------------")

# Access 2-D Arrays 

arr1 = np.array([[2,4,6,8], [1,3,7,9]])
# Access the element on the 1nd row, 3th column:
print(arr1[0,2])

# Access the element on the 2nd row, 4th column:
print(arr1[1,3])

print("-------------------------")


# Access 3-D Arrays

arr2 = np.array([[[1,2,3,4], [2,4,6,8]], [[5,7,9,1], [7,2,5,3]]])
# Access the third element of the second array of the first array:
print(arr2)
print(arr2[0 , 1 , 2])