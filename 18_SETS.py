# SETS :

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets {} and sperated with commas .

s={2,5,"cherry",2,3.55,56} #Duplicates Not Allowed
print(type(s)) 
print(s)
print(len(s)) #Length of a Set


# How to Create empty set 
temp={} # Ye ek empty sets nhi hai .. ye dict hai ...
print(type(temp)) 

temp1=set()
print(type(temp1))

# Access Items: 
# Through Loop we can access the items of sets

for x in s:
    print(x)

