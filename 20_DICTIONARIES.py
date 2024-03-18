# DICTIONARIES:

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:

dic={
    "Name": "David",
    "Age": 25,
    "Email": "david@gmail.com",
    "Number": 984556646
}

print(dic)
print(type(dic))

print(dic["Name"])
print(dic["Email"])

print(len(dic))


# Change Values: 
dic["Number"]=9876543210
print(dic)

# Adding Items:
dic["color"]="red"
print(dic)

# Removing Items:
dic.pop("color")
print(dic)