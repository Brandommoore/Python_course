# Open, close and edit files
import time
from io import open

if __name__ == '__main__':
	file = open("file.txt", "w")  # Modo escritura
	content = "FILE START\nThis is the content of the file\nEND FILE"

	# Añadir contenido al archivo
	file.write(content)

	# Cerrar el archivo
	file.close()

	# Abrimos en modo solo lectura
	file = open("file.txt", "r")

	# Leemos del archivo
	# con readlines() leemos linea a linea y lo almacena en una lista
	#file_content = file.read()
	content_in_list = file.readlines()
	#print("\n read by READ\n")
	#print(file_content)
	print("\n read by READLINE\n")
	print(content_in_list)

	file.close()