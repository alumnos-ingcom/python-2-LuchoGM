################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import estadistica

"""
Testea la entrada y la salida de la funcion y verifica que sean las correctas
"""


def test_estadistica():
    """
    Testea que la entrada y la salida sea la correcta 
    """
    secuencia = 4
    lista = [5,6,4,8]
    resultado = estadistica(secuencia,lista)
    assert isinstance(secuencia,int), "La entrada debe de ser un entero"
    assert isinstance(resultado,tuple), "La salida debe de ser una tupla"
    assert isinstance(lista,list),"Debe de ser una lista"
    assert isinstance(resultado[2],float),"Debe de ser un numero flotante"
    assert resultado == (8,4,5.75),"La funcion  no opera como es debido"
    