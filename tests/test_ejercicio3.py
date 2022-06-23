################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import superposicion

"""
Se testea la salida y la entrada de la funcion y en caso de que
la primera lista sea de mayor o  menor longitud.
"""


def test_superposicion():
    """
    Se prueba que la segunda lista tenga menor longitud que la primera lista,
    ademas se verifica la entrada  y la salda
    """
    lista1 = ['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
    lista2 = [ "H",'o', 'l', 'a']
    resultado = superposicion(lista1,lista2)
    assert isinstance (lista1,list),"Debe de ser una lista"
    assert isinstance (lista2,list),"Debe de ser una lista"
    assert isinstance(resultado, int), "El resultado debe de ser un numero entero"
    assert resultado == 4, "La funcion no opera como es debido"
    assert len(lista2) == resultado, "La funcion no opera como es requerido"
def test_superposicion2():
    """
    Se prueba que la primera lista tenga menor longitud que la segunda lista,
    ademas se verifica la entrada  y la salda
    """
    lista1 = ['H', 'o', 'l']
    lista2 = [ "H",'o', 'l', 'a']
    resultado = superposicion(lista1,lista2)
    assert isinstance (lista1,list),"Debe de ser una lista"
    assert isinstance (lista2,list),"Debe de ser una lista"
    assert isinstance(resultado, int), "El resultado debe de ser un numero entero"
    assert resultado == 3, "La funcion no opera como es debido"
    assert len(lista1) == resultado, "La funcion no opera como es requerido"
    