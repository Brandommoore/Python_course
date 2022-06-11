# Object Oriented Programming
#	--> Encapsulating Methods

class Car():

	# Metodo Constructor
	def __init__(self):
		self.__length = 250
		self.__width = 250
		self.__wheels = 4
		self.__engine = False

	def start(self, mount):
		self.__engine = mount
		if self.__engine:
			check = self.__internal_checkup()
		if self.__engine and check:
			return "Engine is successfully installed and \033[92mCHECKED\033[0m. Turning on..."
		elif self.__engine and check == False:
			return "Engine is successfully installed. \033[91mCHECK FAILED\033[0m. Cant turning on"
		else:
			return "There is no engine mounted. Turning off..."

	def status(self):
		print(f"The car have {self.__wheels} wheels, its size is {self.__length}x{self.__width}cms")

	# Encapsulamos este metodo
	def __internal_checkup(self):
		print("Making a internal checkup...")
		self.gas = "OK"
		self.oil = "KO"
		self.doors = "OK"

		if self.gas=="OK" and self.oil=="OK" and self.doors=="OK":
			return True
		else:
			return False


if __name__ == '__main__':
	print("\n\033[95m--------------First Object-----------------\033[0m")
	mustang = Car()
	print(mustang.start(True))
	mustang.status()

	print("\n\033[95m--------------Second Object----------------\033[0m")
	shelvy = Car()
	print(shelvy.start(False))
	shelvy.status()
