# Import NumPy :-
import numpy as np

# Creating NumPay Array :-
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr)) # ndarray = N-Dimensional array
print('---------------------')


# Creating 0-D Arrays:-
a = np.array(55)
print(a)
# print(type(a))
print('---------------------')


# Creating 1-D Arrays:-
b = np.array([1,2,3])
print(b)
# print(type(a))
print('---------------------')


# Creating 2-D Arrays:-
c = np.array([[1,3,5], [2,4,6]])
print(c)
print('---------------------')


# Creating 3-D Arrays:-
d = np.array([[[1,3,5],[2,4,6]],[[5,7,8],[9,7,3]]])
print(d)
print('---------------------')


# Check Number of Dimensions ?
# ndim attribute that returns an integer that tells us how many dimensions the array have.

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
