import pandas as pd

data={
      "Name":["Ashish","Aman","Vivek","Juhi"],
      "Age":[23,20,22,21],
      "Salary": [45000,44000,45500,30000]
      }
df=pd.DataFrame(data)
print(df)