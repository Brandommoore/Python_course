# Inheritance

class Vehicle():

	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		self.start = False
		self.accelerate = False
		self.brake = False

	def start_on(self):
		self.start = True

	def accelerate_on(self):
		self.accelerate = True

	def brake_off(self):
		self.brake = True

	def status(self):
		print(f"Brand: {self.brand}. Model: {self.model}\n\
	ON: {self.start}\n\
	ACCELERATE: {self.accelerate}\n\
	BRAKE: {self.brake}\n")


class Scooter(Vehicle):  # Le pasamos la clase Vehicle para que herede su contenido
	pass


if __name__ == '__main__':
	mustang = Vehicle("Ford", "Mustang")
	honda_scoot = Scooter("Honda", "CBR")

	mustang.status()
	honda_scoot.status()
