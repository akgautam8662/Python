# STRING METHODS :
# Note: All string methods return new values. They do not change the original string.

a="python language"
b="NALFLFLNAF"
c="sdjsnsnsn"
d="Ashish"
# count() :- Returns the number of times a specified value occurs in a string
print(a.count("a")) 

# capitalize() :- Converts the first character to upper case
print(a.capitalize())

# index() :- Searches the string for a specified value and returns the position of where it was found
print(a.index("l"))

# lower() :- Converts a string into lower case.
print(b.lower())

# upper() :- Converts a string into upper case.
print(c.upper())

# center() :- Returns a centered string
print(d.center(14))
print(d.center(14,"-"))
