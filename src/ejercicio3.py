################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""
def superposicion(a,b):
    """
    Esta funcion recorre dos listas retornando la cantidad de veces que
    se superponen los elementos de la listas.
    """
    contador = 0
    numeros = 0
    for i in range(len(a)):
        if numeros >= len(b):
            break
        elif a[numeros] == b[numeros]:
            numeros += 1
            contador +=1
    return contador

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    lista1 = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    lista2 = ['H', 'o', 'l', 'a']
    funcion = superposicion(lista1,lista2)
    print (funcion)

if __name__ == "__main__":
    principal()
