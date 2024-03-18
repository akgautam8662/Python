# LISTS :

# Lists are used to store multiple items in a single variable..
# list are mutable and enclose with in square bracket []..

# Create a List:
l1=[1,"ashish",3.14,True,5+1j]
print(type(l1))

# LISTS ITEMS: 

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

l2=[1,"car","car","apple",123]
print(l2)
print(l2[0])
print(l2[3])

# Negative Indexing:
# -1 refers to the last item
print(l2[-1])
print(l2[-2])

# LISTS LENGHT:
# use the len() function..

print(len(l2))