# NumPy Array Slicing :-

import numpy as np

arr = np.array([2, 4, 3, 5, 8, 1, 7])
# indexing :    0  1  2  3  4  5  6

print(arr[1:5])     # [2 3 4 5]

# Slice elements from index 3 to the end of the array:
print(arr[3:])

# Slice elements from the beginning to index 4 :
print(arr[:5])

print(arr[-3 : -1])


