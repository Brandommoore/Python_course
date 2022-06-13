#  upper() sube todo en mayúsculas
#  lower() baja todo en minúscula
#  capitalize() todas la primera letra en mayúscula
#  count() contar una y cuantas aparecen dentro de una cadena
#  find() representa el índice donde aparece un carácter dentro de un texto
#  isdigit() devuelve un booleano si es un valor numérico o no
#  isalum() comprueba si es alfanuméricos
#  isalpha() si es alpha comprueba si son solo letras
#  split()  separa por palabras utilizando espacios
#  strip() borra los espacios sobrante al principio y al final
#  replace() cambia una palabra o una letra por otra
#  rfind() representa el índice de un carácter contando desde atrás

if __name__ == '__main__':
	str = input("\033[95mSet your str: \033[0m")
	print(str)
	print(f"Str to Upper: {str.upper()}")
	print(f"Str to Lower: {str.lower()}")
	print(f"Str Capitalizing: {str.capitalize()}")

	#  print("\n\n")
	#  nb = input("\033[95mSet your number: \033[0m")
	#  print(f"The number {nb} is a number?: {nb.isdigit()}")