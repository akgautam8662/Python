# CHECK STRING:
# To check if a certain phrase or character is present in a string, we can use the keyword (in).

str="The best things in life are free!"
print("free" in str)

# Use it in an if statement:

if "things" in str:
    print("Yes, 'things' is present.");


#Check if NOT :
# we can use the keyword not in.

if "apple"not in str:
    print("No, 'apple' is not present.");

# STRING SLICING :

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

a="Python Learing"
print(a[2:8]) #last characters  not included...

# Note: The first character has index 0.

# Slice From the Start:
print(a[:8])

# Slice To the End: 
print(a[2:])

# Negative Indexing:
# lenght of string -value
print(a[0:-3]) # 14-3 = 11
print(a[-9:-2]) 
# 14-9 : 14-2 = 5:12




 
    