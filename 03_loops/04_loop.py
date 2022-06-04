# while loop

i=0
while i<10:
    print(i)
    i+=1

print("\n\n")

number = int(input("Set a number here: "))
while number<5 or number>100:
    number = int(input("Set a number here between 5 and 100: "))

print(f"The number {number} is correct")