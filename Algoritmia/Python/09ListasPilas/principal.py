import pila
import vista

#Definir un diccionario de las funciones del archivo para que se pueda invocarlas

def main():
    #Diccionario de las funciones de pila
    logicaPila = {
        "crearPila" : pila.crearPila,
        "apilar": pila.desapilar,
        "desapilar": pila.desapilar,
        "cima": pila.cima,
        "estaVacia": pila.estaVacia,
        "tamano": pila.tamano,
        "mostrarPila": pila.mostrarPila

    }

    vista.crearInterfaz(logicaPila)

main()