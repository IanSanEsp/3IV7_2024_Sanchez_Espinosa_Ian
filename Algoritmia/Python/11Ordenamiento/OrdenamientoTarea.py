import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time

# Métodos de ordenamiento
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def seleccion_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]

    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]

    return quick_sort(izquierda) + medio + quick_sort(derecha)

def ordenar():
    entrada = entrada_numeros.get()
    metodo = metodo_seleccionado.get()

    try:
        lista_original = [int(x.strip()) for x in entrada.split(",")]
        if len(lista_original) > 40:
            messagebox.showerror("Error", "La lista no puede tener más de 40 números.")
            return
    except ValueError:
        messagebox.showerror("Error", "ingresar solo números separados por comas.")
        return

    if metodo == "":
        messagebox.showerror("Error", "selecciona un método de ordenamiento.")
        return

    lista = lista_original.copy()
    inicio = time.time()

    # Selección del método
    if metodo == "Burbuja":
        lista_ordenada = burbuja(lista)
    elif metodo == "Selección":
        lista_ordenada = seleccion_sort(lista)
    elif metodo == "Inserción":
        lista_ordenada = insercion(lista)
    elif metodo == "Merge Sort":
        lista_ordenada = merge_sort(lista)
    elif metodo == "Quick Sort":
        lista_ordenada = quick_sort(lista)

    fin = time.time()
    tiempo = fin - inicio

    # Mostrar resultados
    resultado_original.set(f"Lista original: {lista_original}")
    resultado_ordenada.set(f"Lista ordenada: {lista_ordenada}")
    resultado_tiempo.set(f"Tiempo de ejecución: {tiempo:.6f} segundos")

ventana = tk.Tk()
ventana.title("Ordenamiento de Listas")
ventana.geometry("500x400")

tk.Label(ventana, text="Ingresa una lista de números (máximo 40, separados por comas):").pack(pady=5)
entrada_numeros = tk.Entry(ventana, width=50)
entrada_numeros.pack(pady=5)

tk.Label(ventana, text="Selecciona un método de ordenamiento:").pack(pady=5)
metodo_seleccionado = tk.StringVar()
metodos = ["Burbuja", "Selección", "Inserción", "Merge Sort", "Quick Sort"]
menu_metodos = ttk.Combobox(ventana, textvariable=metodo_seleccionado, values=metodos, state="readonly")
menu_metodos.pack(pady=5)

boton_ordenar = tk.Button(ventana, text="Ordenar", command=ordenar)
boton_ordenar.pack(pady=10)

resultado_original = tk.StringVar()
resultado_ordenada = tk.StringVar()
resultado_tiempo = tk.StringVar()

tk.Label(ventana, textvariable=resultado_original).pack(pady=5)
tk.Label(ventana, textvariable=resultado_ordenada).pack(pady=5)
tk.Label(ventana, textvariable=resultado_tiempo).pack(pady=5)

# Iniciar
ventana.mainloop()
