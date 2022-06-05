# lanzando excepciones
# instruccion raise
# creacion de excepciones propias
import math


def check_age(age):
    if age < 0:
        raise TypeError("Please, insert a real age. USAGE: +0")

    if age < 20:
        print("You are so young")
    elif age < 40:
        print("You are young")
    elif age < 65:
        print("You are old")
    elif age < 100:
        print("You are soo old")


def compute_sqrt(nb):
    if nb < 0:
        raise ValueError("Number must be positive")
    else:
        return math.sqrt(nb)


if __name__ == '__main__':
    check_age(15)
    print("\n\n\n")
    try:
        compute_sqrt(-8)
    except ValueError as e:
        print(e)
    print("Finished")
