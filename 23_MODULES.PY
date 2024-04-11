# Python Modules :

# Module is same as library.
# Module  are the .py files , that contains set of function you want to include in your program.
# Module me code already likha hota hai , bs use import kr k call krna  hota hai aapne program me. uske bad hm uske functions ko use kr skte hai..

# Built-in Modules

# DATE MODULE ---

import datetime  
x = datetime.datetime.now()    

print(x)      # year-mouth-data hours:minutes:secounds.minisecounds

print(x.year)

# The strftime() Method
y = datetime.datetime(1947,8,15)
print(y.strftime("%A"))     # Return Day with Full Name

print(y.strftime("%a"))     # Return Day with Short Name 

print(y.strftime("%B"))     # Return Month with Full Name

print(y.strftime("%b"))     # Return Month with Short Name

print(y.strftime("%Y"))     # Return Year with century

print(y.strftime("%y"))     # Retuen Year Without Century 

print(y.strftime("%m"))     # Return Month as a Number 1-12

# For know more about this visit here :-  https://www.w3schools.com/python/python_datetime.asp