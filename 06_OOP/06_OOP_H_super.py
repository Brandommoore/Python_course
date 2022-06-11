# Inheritance
#	super() --> llama al metodo de la clase padre

class Person():

	def __init__(self, name, age, direction):
		self.name = name
		self.age = age
		self.direction = direction

	def description(self):
		print(f"Name: {self.name}\nAge: {self.age}\nDirection: {self.direction}")


class Employee(Person):

	def __init__(self, salary, antiquity):
		super().__init__("Manu", 25, "Spain")
		self.salary = salary
		self.antiquity = antiquity


if __name__ == '__main__':
	manu = Employee(1500, 2)
	manu.description()

