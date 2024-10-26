#Menu
def eleccion():
    print("Selecciona una opcion:")
    print("A.- Matriz 3x3")
    print("B.- Matriz 5x5")
    print("C.- Salir")
    opc = input("....: ").upper()

    if opc == "A" or opc =="B" or opc == "C":
        return opc
    else:
        print("Opcion no valida")
        return eleccion()

#Crear matriz 3x3
def matriz3x3():
    matriz3 = []
    for f in range(3):
        fila = []
        for c in range(3):
            print("Ingresa el valor de la fila: ", f, ", columna: ", c)
            num = float(input("....: "))
            fila.append(num)
        matriz3.append(fila)

    matriz3Tr = []
    for cTr in range(3):
        nFila = []
        for fTr in range(3):
            numTr= matriz3[fTr][cTr]
            nFila.append(numTr)
        matriz3Tr.append(nFila)

    return matriz3, matriz3Tr

#Matriz 5x5
def matriz5x5():
    matriz5 = []
    for f in range(5):
        fila = []
        for c in range(5):
            print("Ingresa el valor de la fila: ", f, ", columna: ", c)
            num = float(input("....: "))
            fila.append(num)
        matriz5.append(fila)

    matriz5Tr = []
    for cTr in range(5):
        nFila = []
        for fTr in range(5):
            numTr= matriz5[fTr][cTr]
            nFila.append(numTr)
        matriz5Tr.append(nFila)

    return matriz5, matriz5Tr

#Imprimir matriz
def impMatriz(matriz, matrizTr):
    print("La matriz original es: ")
    for f in matriz:
        print(f)

    print("")

    print("La trasposicion de filas y columnas es: ")
    for f in matrizTr:
        print(f)

#Principal
opc = eleccion()

if opc == "A":
    matriz, matrizTr = matriz3x3()
    impMatriz(matriz, matrizTr)
elif opc == "B":
    matriz, matrizTr = matriz5x5()
    impMatriz(matriz, matrizTr)
elif opc == "C":
    print("Programa cerrado")