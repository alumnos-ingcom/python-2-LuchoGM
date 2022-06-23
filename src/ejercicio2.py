################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de
una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""
def estadistica(secuencia,lista):
    """
    Esta funcion obtiene los maximos, minimos y promedio de una funcion retornando una tupla
    """
    suma = 0
    indice = 0
    while indice < len(lista):
        suma = suma + lista[indice]
        indice += 1
    lista.sort(reverse=True)
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
    contador = 0
    lista = []
    while secuencia > contador:
        numeros = int(input("Ingrese los numeros: "))
        lista.append(numeros)
        contador += 1
    funcion = estadistica(secuencia,lista)
    print (funcion)

if __name__ == "__main__":
    principal()
