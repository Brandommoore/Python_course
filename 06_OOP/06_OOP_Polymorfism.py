# Polymorphism
#	Es cuando un objeto cambia su forma y propiedades
#	No hay que esecificar de que tipo es el objeto

class Car():

	def displacement(self):
		print("I'm moving with four wheels")


class Scooter():

	def displacement(self):
		print("I'm moving with two wheels")


class Truck():

	def displacement(self):
		print("I'm moving with six wheels")


def vehicle_displacement(vehicle):
	vehicle.displacement()


if __name__ == '__main__':
	vehicle = Scooter()
	vehicle.displacement()

	myTruck = Truck()
	vehicle_displacement(myTruck)