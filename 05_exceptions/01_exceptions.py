# exceptions
# Una excepcion es un error que ocurre durante la ejecucion de un programa.
# captura o control de excepcion

def div_nb(nb1, nb2):
    try:
        return nb1/nb2
    except ZeroDivisionError:
        print("It cant be divided by 0")

if __name__ == '__main__':
    div_nb(8, 0)