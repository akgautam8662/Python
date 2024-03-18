s1={2,4,6,8,10}
s2={3,6,9,12,15}
print(s1.union(s2)) # Dono ka combnation ho jayega..

print(s1.intersection(s2)) # Dono me jo common hoga wo aayega..

s1.update(s2) #	Update the set with the union of this set and others
print(s1)

s1.add("PYTHON")  #Adds an element to the set
print(s1)

s3=s1.difference(s2) # Only present in the original set not in both the sets 
print(s3)

print(s1.isdisjoint(s2)) #Returns whether two sets have a intersection or not

s1.remove("PYTHON")#	Removes the specified element
print(s1)