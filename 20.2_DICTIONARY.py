dic1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Copy a Dictionary :-
# dict2 = dict1    its not possible
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
dic2 = dic1.copy()
print(dic2)

# Nested Dictionaries :-
# A dictionary can contain dictionaries, this is called nested dictionaries.

college ={
    "MCA" : {
        "Name" : "Aman",
        "Roll" : 232396952
    },
    "MCADS" : {
        "Name" : "Ashish",
        "Roll" : 1230288    
    }
}

print(college)
print(college["MCA"])