# Check whether an item in present in the list ?

name=["ashish","aman","pooja","mohan"]
li=input("Check your name :")
if li in name:
    print("Allow.✅")
else:
    print("Not Allow..❌")


# Range of Indexes

num=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10,11,12,13,14,15,16]
print(num[2:5])  # The search will start at index 2 (included) and end at index 5 (not included).

print(num[1:]) # index 1 se last tk..
print(num[:8]) # starting se index 8 tk pr 8 is not included..      