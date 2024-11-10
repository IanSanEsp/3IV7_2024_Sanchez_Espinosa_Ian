import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mostrar_Saludo():
    nombre = entrada_nombre.get()
    saludo = f"Hola{nombre}"
    etiqueta_saludo.config(text=saludo)

#Funcion mostrar estado de casilla de verificaion
def mostar_estado():
    estado = "Seleccionado" if casilla_var.get() else "No seleccionado"
    etiqueta_casilla.config(text=f"Estado de la casilla : {opcion_var.get()}")

#Barra de progreso
def incrementar_Progreso():
    progreso.step(10)

#Crear ventana 
ventana = tk.Tk()
ventana.title("Ejemplo de interfaz en python")
ventana.geometry("800x600")

#Etiquetas
etiqueta_bienvenida = tk.Label(ventana, text = "Bienvenido a la interfaz", font=("Arial", 16))
etiqueta_bienvenida.pack(pady=10)

#Boton mostrar saludo
boton_saludo = tk.Button(ventana, text = "Saludar, ", command=mostrar_Saludo)
boton_saludo.pack(pady=5)

#Etiqueta saludo
etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack()

ventana.mainloop()