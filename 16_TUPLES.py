# TUPLES: 

# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered,unchangeableand allow duplicate values.
# Tuples are written with round brackets.     
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.   

tup=("ashish","vivek",12,"rohan",True)
print(tup)
print(type(tup))

# tuples are immutable ,hence if you want to add ,remove or change tuples items then the first you want to must covvert the tuples to list . then again convert into tuple ....

temp=list(tup)
temp[2]="pooja"
tup =tuple(temp)
print(tup)

