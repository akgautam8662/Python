# EXCEPTION_HANDLING:

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.


x=input("Enter Some Value:")
y=input("Enter other Some Value:")

sum=int(x)+int(y)
print(sum)

print("Some Important Line")

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


a=input("Enter Some Value:")
b=input("Enter other Some Value:")
try:
    sum=int(a)+int(b)
    print(sum)
except:
    print("Something worng plz enter valid values")

print("Some Important Line")