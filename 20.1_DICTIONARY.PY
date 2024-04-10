# DICTIONARY :-

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dic={
   # Key   : value
    "Name" :"Ashish",
    "BOD" : "12-05-2002",
    "Course" : "MCA",
    "Roll": 1230259021
}
print(dic)
print(type(dic))

# The dict() Constructor :-
# It is also possible to use the dict() constructor to make a dictionary.
dic1= dict(ID="a001",Name="John")
print(dic1)

# Accesing perticular item.
print(dic["Roll"])

# get()method also give same output.
print(dic.get("Course"))

# The keys() method will return a list of all the keys in the dictionary.
print(dic.keys())

# The value() method will return a list of all the value in the dictionary.
print(dic.values())

# Check if Key Exists
if "Roll" in dic:
    print("Hai..")
else:
    print("Nhi Hai..")

# Change Values..
dic["Roll"]=345688
print(dic)

# update() :-The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
dic.update({"Roll":1230259021})
print(dic)

# Adding Items :-
dic["Subject"]="java"
dic["Id"]=212
print(dic)

# Removing Items :-
# for remove item from dic use pop() method
dic.pop("Subject")
print(dic)

# The popitem() method removes the last inserted item
dic.popitem()
print(dic)