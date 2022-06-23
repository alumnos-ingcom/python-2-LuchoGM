################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import esta_balanceado

"""
Se prueba la funcion verificando que tanto la entrada como la salida
sean las requeridas.
"""


def test_esta_balanceado():
    """
    Se testea que tanto la entrada como la salida sea la solicitada
    """
    corchete1 = "[[]]"
    corchete2 = "[][]["
    corchete3 = "[]["
    resultado1 = esta_balanceado(corchete1)
    resultado2 = esta_balanceado(corchete2)
    resultado3 = esta_balanceado(corchete3)
    assert isinstance(resultado1,bool), "El resultado debe de ser un booleano"
    assert isinstance(resultado2,bool), "El resultado debe de ser un booleano"
    assert isinstance(resultado3,bool), "El resultado debe de ser un booleano"
    assert isinstance(corchete1,str), "La entrada debe de ser un string"
    assert isinstance(corchete2,str), "La entrada debe de ser un string"
    assert isinstance(corchete3,str), "La entrada debe de ser un string"
    assert resultado1 == True, "El resultado no es el esperado"
    assert resultado2 == False, "El resultado no es el esperado"
    assert resultado3 == False, "El resultado no es el esperado"
    