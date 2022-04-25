# Declaring lists

print("Declaring_lists\n")
# declaring
myList=["Orange", "Apple", "Watermelon", "Burberrys"]
print(myList[3])

# We can call an element from last of list
print(myList[-2] + "\n")
# This will print "Watermelon", because the count start at -1
# -----------------------------

# We can acces to a piece of the list, like 0-3 elements. (exclude the second number [0:x])
print(myList[0:3])
print(myList[1:3])

# Abbreviated nomenclature
# I can do the last example avoiding the cero
print(myList[:3])

# I can access to the last two elements
print(myList[2:])

# I can print the whole list
print(myList[:])

# Knowing the index of the element
print(myList.index("Apple"))

# Knowing if the element exist
print("Kiwi" in myList)
print("Apple" in myList)

# ----------------------------
print("\nWorking with lists")
print("Adding --> \n")

# Append. add the element to the end of the list
myList.append("Raspberry")
print(myList[:])

# Insert. add the element to a custom position (index, element)
myList.insert(2, "Papaya")
print(myList[:])

# Adding more elements at once
myList.extend(["Lemon", "Grapes", "Pineapple"])
print(myList[:])

# - - - - - - - - - - -
print("\nDeleting --> \n")

# Remove. remove an element from list
myList.remove("Burberrys")
print(myList[:])

# Pop. remove the last element of the list
myList.pop()
print(myList[:])

# -------------------------
print("\n\nLists addition")

elem1=["Water", "Fire"]
elem2=["Air", "Earth"]

# Adding lists have a "union" result
elements=elem1+elem2
print(elements[:])

# -------------------------
print("\n\nLists multiply")

# Multiply lists have a "duplication" result
multi=["Cold", "Heat"] * 3
print(multi[:])