import tkinter as tk
from tkinter import messagebox

def crear_interfaz(logica_cola):
    ventana = tk.Tk()
    ventana.title("Ejemplo de cola sencilla")
    ventana.geometry("400x400")

    #Definir cola
    cola = logica_cola["crear_cola"]()

    def manejar_cola():
        elemento = entrada_elemento.get()
        if elemento:
            logica_cola["encolar"](cola, elemento)
            actualizar_cola()
            entrada_elemento.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacia", "Porfavor ingrese un elemnto")

    def manejar_desencolar():
        try:
            elemento = logica_cola["desencolar"](cola)
            messagebox.showinfo("Desencolar", f"Elemento desencolado: {elemento}")
            actualizar_cola()
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def manejar_frente():
        try:
            elemento = logica_cola["frente"](cola)
            messagebox.showinfo("Frente", f"Elemento en el frente es: {elemento}")
        except IndexError as e:
            messagebox.showerror("Error", str(e))

    def tamano():
        tam = logica_cola["tamano"](cola)
        messagebox.showinfo("Tamaño", f"El tamaño de la cola es: {tam}")

    def manejar_mostar():
        cola_actual = logica_cola["mostrar_cola"](cola)
        messagebox.showinfo("Cola actual", cola_actual)

    def actualizar_cola():
        cola_actual = logica_cola["mostrar_cola"](cola)
        etiqueta_cola.config(text=cola_actual)

    def manejar_cola():
        cola_actual = logica_cola["mostrar_cola"](cola)
        etiqueta_cola.config(text=cola_actual)


    tk.Label(ventana, text="Manejo de una cola", font=("Arial", 16)).pack(pady=10)

    entrada_elemento = tk.Entry(ventana, width=30)
    entrada_elemento.pack(pady=5)

    tk.Button(ventana, text="Encolar", command=manejar_cola).pack(pady=5)
    tk.Button(ventana, text="Desencolar", command=manejar_desencolar).pack(pady=5)
    tk.Button(ventana, text="Ver frente", command=manejar_frente).pack(pady=5)
    tk.Button(ventana, text="Ver tamaño", command=tamano).pack(pady=5)
    tk.Button(ventana, text="Mostar cola", command=manejar_mostar).pack(pady=5)

    etiqueta_cola = tk.Label(ventana, text="Cola actual:[]", font=("Arial", 12))
    etiqueta_cola.pack(pady=20)

    ventana.mainloop()
