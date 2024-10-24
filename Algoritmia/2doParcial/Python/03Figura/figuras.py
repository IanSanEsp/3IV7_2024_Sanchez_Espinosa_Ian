import math

#"Funcion para calcular el area y perimetro"

def rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura)/2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def esfera(radio):
    volumen = (4/3) * math.pi * radio**3
    return volumen

def menu():
    print("Bienvenido a python con funciones")
    print("Elige una opcion: ")
    print("A.- Area y perimetro del rectangulo")
    print("B.- Area y perimetro del triangulo")
    print("C.- Volumen de esfera")

#Programa
menu()
opcion = input("Introduce una opcion: ").upper()

if opcion == "A":
    base = float(input("Introduce la base:a "))
    altura = float(input("Introduce la altura: "))
    area, perimetro = rectangulo(base , altura)
    print("El area es de: ", area)
    print("El perimetro es de: ", perimetro)
elif opcion == "B":
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    lado1 = float(input("Introduce el lado1: "))
    lado2 = float(input("Introduce el lado2: "))
    lado3 = float(input("Introduce el lado3: "))
    area, perimetro = triangulo(base , altura, lado1, lado2, lado3)
    print("El area es de: ", area)
    print("El perimetor es de: ", perimetro)
elif opcion == "C":
    radio = float(input("Introduce la radio: "))
    volumen = esfera(radio)
    print("El volmen de la esfera es: ", volumen)