# A tuple is an immutable list, that is, it cannot be modified after its creation.
# Benefits?
#	More quik
#	Less space
#	String format
#	Dictionary

print("Defining tuples\n")

# defining

myTuple=("Name", 12, 1, 1980)
print(myTuple[1])

# TUPLES to LIST
myList=list(myTuple)
print(myList[:])

# LIST to TUPLES
myTuple=tuple(myList)
print(myTuple)

print("Tuples with --> '()' Lists with --> '[]'\n")

# Find in a tupla
print("Surname" in myTuple)

# Count. counts the number of times the element is found in the tuple
print(myTuple.count(1980))

# Len. length of the tuple
print(len(myTuple))

# ----------------------
# Another way to create a tuple
tuple2="Name", 13, 1, 1995
print(tuple2)
print("\n")
# this method is called "tuple packing"

# TUPLE UNPACKING
tuple3=("Name", 13, 1, 1995)
name, day, month, year=tuple3
print(name)
print(day)
print(month)
print(year)