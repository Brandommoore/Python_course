# Dictionaries in python
# They are a data structure that allows us to store values ​​of different types, lists and other dictionaries
# Data is stored associated with a "key" (key:value)
# The elements are not ordered
# NO TWO KEYS CAN BE THE SAME

# SYNTAX
mydict={"Germany":"Berlin","France":"Paris","UK":"London","Spain":"Madrid"}
print(mydict)
print(mydict["France"])

# knowing keys
print(mydict.keys())

#knowing values
print(mydict.values())

# -----------------
print("\nWorking with dicts --> ")

# Adding
mydict["Italy"]="Lisboa"
print(mydict)

# Change. Change values overwirting
mydict["Italy"]="Rome"
print(mydict)

# Deleting.
del mydict["UK"]
print(mydict)
print("\n")

# ------------------ Others ---------
dict2={"Portugal":"Lisbon", 23:"Jordan", "Mosqueteros":3}
print(dict2[23])

# With tuples
mytuple=["Spain", "France", "UK", "Germany"]
dict3={mytuple[0]:"Madrid", mytuple[1]:"Paris", mytuple[2]:"London", mytuple[3]:"Berlin"}
print(dict3["France"])
print("\n")

# Dictionary storing tuples
dict4={23:"Jordan", "Name":"Michael", "Team":"Chicago", "rings":[1991, 1992, 1993, 1996, 1997, 1998]}
print(dict4)
print(dict4["rings"])