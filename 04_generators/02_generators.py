# generators II
# yield from
# sirve para simplificar el codigo de los generadores en el caso de
#   usar bucles anidados

def return_cities(*cities):  # Le decimos que va a recibir un numero indeterminado de argumentos
    for city in cities:
        # for letter in city:
        yield from city


if __name__ == '__main__':
    returned_cities = return_cities("Madrid", "Barcelona", "Bilbao", "Valencia")
    print(next(returned_cities))
    print(next(returned_cities))
