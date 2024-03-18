# CHANGE LISTS ITEMS:

game=["Ludo", "Carrom", "Table tennis", "Chess"]
print(game)
print("\n") #New Line....
game[1]="Cricket"
print(game)


# INSERT ITEMS:

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:

game.insert(3,"FootBall")   
print(game)
print("\n")

# ADD LISTS ITEMS: 

# To add an item to the end of the list, use the append() method:
game.append("Cricket")
print(game)