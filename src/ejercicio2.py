################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de
una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
def estadistica(secuencia):
    """
    Esta funcion obtiene los maximos, minimos y promedio de una funcion retornando una tupla
    """
    contador = 0
    lista = []
    suma = 0
    while secuencia > contador:
        numeros = int(input("Ingrese los numeros: "))
        lista.append(numeros)
        lista.sort(reverse = True)
        contador += 1
    for i in lista:
        suma = suma + i
    promedio = suma/secuencia
    del lista[1:secuencia-1]
    lista.append(promedio)
    tupla = tuple(lista)
    return tupla


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    secuencia = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
    funcion = estadistica(secuencia)
    print (funcion)

if __name__ == "__main__":
    principal()
