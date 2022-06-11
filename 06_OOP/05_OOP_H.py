# Inheritance
# Multiple Inheritance

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
		print(f"\033[95mBrand: {self.brand}. Model: {self.model}\033[0m\n\
	ON: {self.start}\n\
	ACCELERATE: {self.accelerate}\n\
	BRAKE: {self.brake}\n")


class Van(Vehicle):

	def charging(self, charged):
		self.charged = charged
		if self.charged:
			return "Van is charged"
		else:
			return "Van is not charged"


class Scooter(Vehicle):
	horsed = ""

	def horsing(self):
		self.horsed = "Im horsing!!"

	def status(self):
		print(f"\033[95mBrand: {self.brand}. Model: {self.model}\033[0m\n\
	ON: {self.start}\n\
	ACCELERATE: {self.accelerate}\n\
	BRAKE: {self.brake}\n\
	HORSING: {self.horsed}\n")


class VElectric():

	def __init__(self):
		self.autonomy = 100

	def charge_energy(self):
		self.charging = True


class EBicycle(VElectric, Vehicle):  # Multiple herencia
	pass

# Al tener una multiple herencia, tiene preferencia la primera clase introducida por parametro.
#	Hereda su metodo constructor


if __name__ == '__main__':
	mustang = Vehicle("Ford", "Mustang")
	honda_scoot = Scooter("Honda", "CBR")
	kangoo = Van("Renault", "Kangoo")

	mustang.status()
	honda_scoot.horsing()
	honda_scoot.status()

