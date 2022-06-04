# For loop
# range type
# special notations in print

for i in ["Madrid", "Spain", 3]:
    print("Hola", end=" ")  # Con esto indicamos con que queremos que acabe el print

print("\n\n")

myEmail = input("Set your email here: ")
if myEmail == "":
    myEmail = "uncorreocualquiera@correo.es"

for i in myEmail:
    print(i, end='')

print("\n\nRange:\n")

for i in range(5):
    print(i)