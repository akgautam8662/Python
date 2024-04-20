# JSON  : Big data is sets are normally strord as JSON . JSON is a plain text , but it sis has a formate of an object .

# JSON = Python Dictionary
# JSON objects have the same format as Python dictionaries.

# loading the JSON into a DataFrame : 

import pandas as pd
js = pd.read_json('/Users/kshitijsingh/Desktop/Code/PYTHON/PANDAS LIBRARY/data.js')
print(js.to_string())