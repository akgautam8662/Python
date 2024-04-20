# A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

# Here we will create a simple pandas series .

import pandas as pd
a = [12,14,16]
a_new = pd.Series(a)
print(a_new)

print("\n")
# Labeling - lable can be use to access a specified value.

print(a_new[0])
print(a_new[1])

print("\n" )
# With create lable we can create you own name lables: 

a_new = pd.Series(a, index=["A", "B", "C"])
print(a_new)