import tkinter as tk
from tkinter import messagebox

#Crear interfaz
def crearInterfaz(logicaPila):
    #Crear ventana
    ventana = tk.Tk()
    ventana.title("Manejo de pila")
    ventana.geometry("400x400")

#Necesitamos una pila para realizar las invocaciones
pila = logicaPila["crearPila"]()

#Funciones de la interfaz
def manejarApilar():
    elemento = entrada.elemento.get()
    if elemento:
        logicaPila["apilar"](pila, elemento)
        actualizarPila()
        entradaElemento.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacia, ingresa un elmento")

def mensajeDesapilar():
    try:
        elemento = logicaPila["desapilar"](pila)
        messagebox.showinfo("Desapilar", f"Elemento desapilado:  {elemento}")
        actualizarPila()
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def manejarCima():
    try:
        elemento = logicaPila["cima"](pila)
        messagebox.showinfo("Cima", f"Elemento de la cima:  {elemento}")
        actualizarPila()
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def manejarTamano():
    tam = logicaPila["tamano"](pila)
    messagebox.showinfo("Tamaño", f"El tamaño de la pila:  {tam}")

def manejarMostrar():
    pilaActual = logicaPila["mostrarPila"](pila)

def actualizarPila():
    pilaActual = logicaPila["mostrarPila"](pila)
    etiquetaPila.config(text=pilaActual)

#Componentes de interfaz
tk.Label(ventana, text="Manejo de una pila", font=("Arial", 16)).pack(pady=10)

entradaElemento = tk.Entry(ventana, width=30)
entradaElemento.pack(pady=5)

tk.Button(ventana, text="Apilar", command=manejarApilar).pack(pady=5)
tk.Button(ventana, text="Apilar", command=mensajeDesapilar).pack(pady=5)
tk.Button(ventana, text="Apilar", command=manejarCima).pack(pady=5)
tk.Button(ventana, text="Apilar", command=manejarTamano).pack(pady=5)
tk.Button(ventana, text="Apilar", command=manejarMostrar).pack(pady=5)

etiquetaPila = tk.Label(ventana, text="Pila actual:[]", font=("Arial", 12))
etiquetaPila.pack(pady=20)

ventana.mainloop()