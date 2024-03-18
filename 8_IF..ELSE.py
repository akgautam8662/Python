# IF ELSE : 
# An "if statement" is written by using the if keyword.
a=int(input("Enter Your Age : "))
print("Your Age is : ", a)

if(a>=18):
    print("You Can Vote.. ✅")
else:
    print("You Can't Vote..❌")

# In condition statement Indentation is very important
# (whitespace at the beginning of a line)

# Elif: 
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

a = 100
b = 45
if a> b:
  print("a is greater than b")
elif a == b:
  print("a and b are equal")
else:
  print("b is greater than a")
