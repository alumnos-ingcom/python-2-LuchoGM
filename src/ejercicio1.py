################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un número entero es par y
False cuando no lo sea, sin utilizar módulo. (%)
"""
def es_par(numero):
    cociente = 0  
    while numero >= 2:
        numero -= 2
    return numero == 0


def principal():
    numero= int(input("Ingrese un numero: "))
    print(es_par(numero))


if __name__ == "__main__":
    principal()
