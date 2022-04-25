print("Age verification")

age=int(input("Insert age "))

if age<18:
	print("Error")
elif age>100:
	print("Incorrect age")
else:
	print("Pass")