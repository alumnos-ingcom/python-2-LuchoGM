################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio6 import codifique, descodifique

"""
Se prueba ambas funciones verificando que la salida
y la entrada sean las requeridas
"""


def test_codifique():
    """
    Se prueba que la entrada y la salida sean las requeridas
    """
    texto = "asd"
    cantidad = 3
    resultado = codifique(texto, cantidad)
    assert isinstance(texto,str), "Debe de ser un string"
    assert isinstance(cantidad,int),"Debe de ser un numero entero"
    assert isinstance(resultado,str), "El resultado debe de ser un string"
    assert resultado == "dvg", "La funcion no opera como es debido"

def test_descodifique():
    """
    Se prueba que la entrada y la salida sean las requeridas
    """
    texto = "dvg"
    cantidad = 3
    resultado = descodifique(texto, cantidad)
    assert isinstance(texto,str), "Debe de ser un string"
    assert isinstance(cantidad,int),"Debe de ser un numero entero"
    assert isinstance(resultado,str), "El resultado debe de ser un string"
    assert resultado == "asd", "La funcion no opera como es debido"
    