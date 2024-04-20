# DataFrames : 

# It is 2D data structure like a 2D array with table incl, row and columns .

import pandas as pd

data = {"FM" : [100,100,100,100,100],
        "OM" : [80,72,89,78,85]}
df = pd.DataFrame(data)
print(df)
print("\n")

# Locate row : Pandas use the loc attribute to return one or more specified row.

print(df.loc[0])
print("\n" )

# Name index : with the index agr , we can name your own index.

data = {"FM" : [100,100,100,100,100],
        "OM" : [80,72,89,78,85]}
df = pd.DataFrame(data , index= ["Maths", "Science ", "S.ST","Hindi","English"])
print(df)
print("\n" )

# Locate the name index : 
print(df.loc["S.ST"]) 
print("\n" )

