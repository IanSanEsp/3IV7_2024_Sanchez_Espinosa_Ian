#Funcion que sume dos arreglos
def sumarAreglos(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        print("Error, arreglos de diefrentes tamaños")
        return None
    else:
        suma = []
        for i in range(len(arreglo1)):
            suma.append(arreglo1[i] + arreglo2[i])
            return suma
        
#Programa principal

arreglo1 = []
arreglo2 = []

n = int(input("Introduce el tamaño de los arreglos"))

print("Introduce los elementos del primer arreglo")

for i in range(n):
    num = float(input("Ingresa el elemento: "))
    arreglo1.append(num)

print("Introduce los elementos del segundo arreglo")

for i in range(n):
    num = float(input("Ingresa el elemento: "))
    arreglo2.append(num)

resultado = sumarAreglos(arreglo1, arreglo2)

#Mostrar resultado
if resultado is not None:
    print("El resultado de la suma es: ", resultado)