# read csv files : 

# csv : (Comma Seperated Value) it is a simple way to store the big and biggest data sets. csv files contains plain text .

# Loading the csv into DataFrame
import pandas as pd
df = pd.read_csv('/Users/kshitijsingh/Desktop/Code/PYTHON/PANDAS LIBRARY/data.csv')
print(df)         # Show only 5 data from stating and last 
print(df.to_string())       # to_string() to print the entire DataFrame.

