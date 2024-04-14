import numpy as np

a1 = np.array([11,12,13,14,15,16])     # 1-D array
a2 = np.array([[21,22,23,24,25,26] , [31,32,33,34,35,36]])        # 2-D array

# NumPy Array Shape :-
print(a1.shape)
print(a2.shape)     # 2 dim hai hai or 6 element hai..

print("-------------------------")

# NumPy Array Reshaping :-
# Reshape From 1-D to 2-D
print(a1.reshape(2,3))      # we create a new variable then print it .

# Flattening the arrays :- 
# Flattening array means converting a multidimensional array into a 1D array.

print(a2.reshape(-1))
