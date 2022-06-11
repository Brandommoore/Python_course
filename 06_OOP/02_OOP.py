# Object Oriented Programming
#	--> Instanciating
#	--> Pass by parameters in functions
#	--> Constructor
#			|-> Con el metodo constructor, dotamos de vaslores iniciales al objeto
#	--> Encapsulation: No hacer una variable accesible desde el exterior

class Car():

	# Metodo Constructor
	def __init__(self):  # Asi seteamos los valores iniciales
		self.__length = 250
		self.__width = 250
		self.__wheels = 4  # Variable encapsulada (ecribir con __ todas las veces que sea llamada)
		self.__engine = False

	def start(self, mount):  # On call, pasamos por parametro todo menos self
		self.__engine = mount
		if self.__engine:
			return "Engine is succesfully installed. Turning on..."
		else:
			return "There is no engine mounted. Turning off..."

	def status(self):
		print(f"The car have {self.__wheels} wheels, its size is {self.__length}x{self.__width}cms")



if __name__ == '__main__':
	mustang = Car()
	#print(f"Mustang has {mustang.wheels} wheels")
	print(mustang.start(True))
	mustang.status()

	print("\n--------------Second Object----------------")
	shelvy = Car()
	#print(f"Shelvy measures {shelvy.length}cm long")
	print(shelvy.start(False))
	shelvy.status()
