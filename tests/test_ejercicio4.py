################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import fibonacci

"""
Se verifica que la entrada y la salida de la funcion retorne lo que es requerido,
ademas se prueba que la sucesion funcion como debe
"""


def test_fibonacci():
    """
    Se testea que la funcion retorne la salida requerida
    """
    termino1 = 3
    termino2 = 4
    termino3 = 5
    resultado1 = fibonacci(termino1)
    resultado2 = fibonacci(termino2)
    resultado3 = fibonacci(termino3)
    assert isinstance(termino1,int), "El termino debe de ser un numero entero"
    assert isinstance(resultado1,int), "El resultado debe de ser un numero entero"
    assert isinstance(termino2,int), "El termino debe de ser un numero entero"
    assert isinstance(resultado2,int), "El resultado debe de ser un numero entero"
    assert isinstance(termino3,int), "El termino debe de ser un numero entero"
    assert isinstance(resultado3,int), "El resultado debe de ser un numero entero"
    assert resultado1 == 1, "La funcion no retorna los resultados deseados"
    assert resultado3 == resultado1 + resultado2, "La funcion no opera como es debido"
    