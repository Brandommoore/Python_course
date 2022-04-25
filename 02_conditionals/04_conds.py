# hdistance=int(input("Distance: "))
# nbrothers=int(input("Brothers: "))
# fam_money=int(input("Family salary: "))

# if hdistance>40 and nbrothers>2 and fam_money<=20000:
# 	print("Scolarship confirmed")
# else:
# 	print("Scolarship declined")

print("Optative subjects")
print("Design - Software - Web")
subject=input("Chosen subject: ")

if subject in ("Design", "Software", "Web"):
	print("Chosen subject: " + subject)
else:
	print("Error")
