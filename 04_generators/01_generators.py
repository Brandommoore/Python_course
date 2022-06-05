# generators
# son estructuras que extraen valores de una funcion y se almacenan en objetos iterables
# los valores se almacenan de uno en uno en un objeto generador iterable
#   - son mas eficientes
#   - muy utiles con listas de valores infinitos
#   - que nos devuelva valores de 1 en 1

# SIN GENERADOR
def gen_parnbs_nogen(limit):
    num = 1
    myList = []
    while num<limit:
        myList.append(num*2)
        num+=1
    return myList

# CON GENERADOR
def gen_parnbs_withgen(limit):
    num = 1
    while num<limit:
        yield num*2
        num+=1

if __name__ == '__main__':
    print(f"{gen_parnbs_nogen(10)}\n")

    # almacenamos el objeto iterable de la funcion
    ret_pars=gen_parnbs_withgen(10)

    #iteramos el objeto
    #for i in ret_pars:
    #    print(i)

    # tambien podemos iterarlo manualmente
    print(next(ret_pars))
    print(next(ret_pars))
    print(next(ret_pars))

