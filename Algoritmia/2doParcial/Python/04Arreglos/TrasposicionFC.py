def eleccion():
    print("Selecciona una opcion:")
    print("A.- Matriz 3x3")
    print("B.- Matriz 5x5")
    opc = input("....: ").upper()

    return opc

def matriz5x5():
    matriz5 = []

    for f in range(3):
        fila = []
        for c in range(3):
            print("Ingresa el valor de la fila: ", f, ", columna: ", c)
            num = float(input("....: "))
            fila.append(num)
        matriz5.append(fila)

    matriz5Tr = []
    for cTr in range(3):
        nFila = []
        for fTr in range(3):
            numTr= matriz5[fTr][cTr]
            nFila.append(numTr)
        matriz5Tr.append(nFila)

    for f in matriz5:
        print(f)

    print("")
    for f in matriz5Tr:
        print(f)

    print(matriz5[0][0])
#Principal
matriz5x5()