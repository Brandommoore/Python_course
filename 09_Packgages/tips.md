# Paquetes

### ¿Que son?
Son directorios en donde se almacenarán los modulos relacionados entre si

### ¿Para que sirven?
PAra organizar y reutilizar los modulos

### ¿Como se crea un paquete?
Creando una carpeta con un archivo ```__init__.py```

## setup.py
Sirve para realizar una descripcion, iformacion y mas relativo acerca del paquete

Una vez hecho y rellenado de esta manera:

```python
from setuptools import setup

setup(
	name="calculus",
	version="0.1",
	description="A couple of mathematical functions",
	author="brandommoore",
	author_email="brmo@localhost.com",
	url="localhost",
	packages=["calculus"] # El nombre del paquete

)
```

## Generar el archivo distribuible
Ejecutamos el archivo en la terminal de la siguiente manera:

```python setup.py sdist```

## Instalar

```pip3 install nombre_del_paquete```