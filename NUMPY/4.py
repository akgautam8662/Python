# NumPy Data Types :- 
'''
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
'''

# Checking the Data Type of an Array :-
# By using dtype eturns the data type of the array

import numpy as np
a1 = np.array([10,20,30,40],)
print(a1.dtype)

a2 = np.array(["a","b","c","d"])
print(a2.dtype) 

