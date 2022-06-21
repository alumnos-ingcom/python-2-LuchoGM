################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import es_par

"""
Se pruba la funcion "es_par" verificando que la entrada
y la salida sean las requeridas.
"""


def test_es_par():
    """
    Se prueba que la entrada y la salida de la funcion sean las correctas
    """
    numero1 = 2
    numero2 = 5
    resultado1 = es_par(numero1)
    resultado2 = es_par(numero2)
    assert isinstance(numero1, int), "La entrada debe de ser un numero entero"
    assert isinstance(numero2, int), "La entrada debe de ser un numero entero"
    assert isinstance(resultado1,bool), "La salida debe de ser un booleano"
    assert isinstance(resultado2,bool), "La salida debe de ser un booleano"
    assert resultado1 == True, "La funcion no funciona como es debido"
    assert resultado2 == False, "La funcion no funciona como es debido"
    assert numero1 > 0, "El numero debe de ser positivo"
    assert numero2 > 0, "El numero debe de ser positivo"
    