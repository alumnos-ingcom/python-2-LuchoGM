################
# Luciano Mansilla - @LuchoGM
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que determine si una cadena con corchetes está balanceada.
Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.
"""
def esta_balanceado(corchete):
    abierto =0
    cerrado = 0
    for i in corchete:
        if i == "[":
            abierto += 1
        if i == "]":
            cerrado += 1
    return abierto == cerrado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    corchetes1 = "[[]]"
    funcion1 = esta_balanceado(corchetes1)
    corchetes2 = "][["
    funcion2 = esta_balanceado(corchetes2)
    corchetes3 = "[]"
    funcion3 = esta_balanceado(corchetes3)
    print(funcion1)
    print(funcion2)
    print(funcion3)


if __name__ == "__main__":
    principal()
