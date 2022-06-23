################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una funcion que codifique un texto rotandolo
una cantidad de posiciones ajustable.

Implementar la funcion que decodifique el texto rotado una
cantidad de posiciones ajustable.
"""
def codifique(texto, cantidad):
    vacio = ""
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    for i in texto:
        if i in abecedario:
            letra = abecedario[abecedario.find(i)+cantidad]
            vacio += str(letra)+ ""
    return vacio
def descodifique(texto, cantidad):
    vacio = ""
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    for i in texto:
        if i in abecedario:
            letra = abecedario[abecedario.find(i)-cantidad]
            vacio += str(letra)+""
    return vacio

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cantidad = int(input("Ingrese un numero: "))
    texto = input("Ingres el texto: ")
    funcion = codifique(texto, cantidad)
    print (funcion)
    cantidad2 = int(input("Ingrese un numero: "))
    texto2 = input("Ingres el texto: ")
    funcion2 = descodifique(texto2, cantidad2)
    print (funcion2)


if __name__ == "__main__":
    principal()