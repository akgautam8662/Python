
# BRACK STATEMENT: 
# The break statement we can stop the loop..
my_prog=["python","C++","java","PHP","Rube"]
print("____________________")
for i in my_prog:
    print(i)
    if i=="PHP":
        break

# CONTINUE STATEMENT:
# The continue statement we can stop the current iteration of the loop, and continue with the next..

print("____________________")
for i in my_prog:
    if i=="PHP":
        continue
    print(i)