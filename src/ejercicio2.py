def estadistica(secuencia):   
    contador = 0
    lista = []
    suma = 0
    while secuencia > contador:
        numeros = int(input("Ingrese los numeros: "))
        lista.append(numeros)
        lista.sort(reverse = True)
        contador += 1
    for i in lista:
        suma = suma + i
    promedio = suma/secuencia
    del lista[1:secuencia-1]
    lista.append(promedio)
    tupla = tuple(lista)
    return tupla
secuencia = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
funcion = estadistica(secuencia)
print (funcion)