# SETS FUNCTIONS :-

a={"Ashish",99,"Harry",12.09,True}
print(a),print(type(a))

# add() :-Adds an element to the set
a.add("Laptop")
print(a)

# remove(),discard() :- Both are use for Removes the specified element
a.remove(True)
print(a)
a.discard("Ashish")
print(a)

# pop() :- Removes random element from the set.
a.pop()
print(a)

# copy() :- Returns a copy of the set
b=a.copy()
print(b)
