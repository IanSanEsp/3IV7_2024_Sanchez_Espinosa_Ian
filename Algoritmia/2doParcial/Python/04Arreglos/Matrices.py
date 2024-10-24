#Suma de matriz 3 x 3

def ingresarMatriz():
    matriz = []
    print("Introduce los valores de la matriz 3 x 3")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input("Elemento [{i + 1}], [{j + 1}] : "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumarMatriz(matriz1, matriz2):
    matrizSuma = []

    for i in range(3):
        fila = []
        for j in range(3):
            
            fila.append(matriz1[i][j] + matriz2[i][j])
        matrizSuma.append(fila)
    return matrizSuma

def imprimirMatriz(matriz):
    for fila in matriz:
        print(fila)

#Principal
print("Matriz 1: ")
matriz1 = ingresarMatriz()

print("Matriz 2: ")
matriz2 = ingresarMatriz()

matrizRes = sumarMatriz(matriz1, matriz2)

print("El resultado es: ")
imprimirMatriz(matrizRes)