from io import open

if __name__ == '__main__':
	file = open("file.txt", "r+")
	print(file.read())
	file.seek(0)  # Modificamos la posicion del puntero lectura/escritura seek(position)
	print(file.read())
	file.close()DW