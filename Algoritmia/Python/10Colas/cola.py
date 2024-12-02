#Aqui se va a crear toda la logica de programacion de la pila

def crearPila():
    return []

def apilar(pila, elemento):
    pila.append(elemento)

def estaVacia(pila):
    return len(pila) == 0

def desapilar(pila):
    if estaVacia(pila):
        raise IndexError("Error no se puede desapilar, la pila esta vacia")
    return pila.pop()

def cima(pila):
    if estaVacia(pila):
        raise IndexError("La pila esta vacia")
    return pila[-1]

def tamano(pila):
    return len(pila)

def mostrarPila(pila):
    if estaVacia(pila):
        raise IndexError("Error no se puede mostrar, la pila esta vacia")
    return f"Pila actual: {pila}"