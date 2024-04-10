# SOME MORE SETS FUNCTIONS :-

x = {"apple", "32", "cherry",23456}
y = {"google", "microsoft", "facebook"}
z = {"apple","32"}

# isdisjoint() :-Returns whether two sets have a intersection or not
print(x.isdisjoint(y)) 

# issubset() :- Returns whether another set contains this set or not
print(z.issubset(x))
print(z.issubset(y))

# update() :- Update the set with the union of this set and others
x.update(z)
print(x)    

# clear() :- Removes all the elements from the set
y.clear()
print(y)