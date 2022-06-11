# Object Oriented Programming

class Car():
    length = 250
    width = 250
    wheels = 4
    engine = False

    def start(self):  # Con self como parametro, le introducimos el propio objeto a la funcion
        self.engine = True  # Cuando usamos self, estamos editando las propiedades del objeto (dentro)

    def status(self):
        if (self.engine):
            return "Mustang has a engine"
        else:
            return "Mustang hasn´t an engine"

if __name__ == '__main__':
    # Instanciamos la clase
    mustang = Car()
    print(f"Mustang has {mustang.wheels} wheels")
    mustang.start()
    print(mustang.status())