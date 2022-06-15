################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
La sucesión de Fibonacci es una sucesión infinita donde cada elemento
es la suma de los dos anteriores. En la misma, los dos primeros términos son 1.
(En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la sucesión de Fibonacci.
Siendo este número un entero positivo mayor a 2.
"""
def fibonacci(numero):
    """
    Esta funcion retorna el termino ingresado por el usuario.
    Precondicion "Entrada" deberia de ser un numero entero mayor a 2
    Postcondicion "Salida" deberia de retornar el termino de la sucesion ingresado
    """
    if numero < 2:
        return "El numero debe de ser mayor a 2"
    else:
        termino1 = 0
        termino2 = 1
        for i in range(numero):
            termino1 += termino2
            termino2 = termino1 - termino2
        return termino2

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero= int(input("Ingrese un numero: "))
    funcion = fibonacci(numero)
    print(funcion)

if __name__ == "__main__":
    principal()