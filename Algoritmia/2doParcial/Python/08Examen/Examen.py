import tkinter as tk
from tkinter import simpledialog, messagebox
import os

#Archivo de datos
DATOS = "pilotos_f1.txt"

#Lista de datos y diccionario
lista = []


#Funciones
#Registrar nuevo piloto
def registrarPiloto():
    Piloto = simpledialog.askstring("Entrada", "Ingresa el nuevo piloto", parent=ventana)
    nombreCompleto = simpledialog.askstring("Entrada", "Ingresa el nombre completo del piloto", parent=ventana)
    nacionalidad = simpledialog.askstring("Entrada", "Ingresa la nacionalidad del piloto", parent=ventana)
    fechaNacimiento = simpledialog.askstring("Entrada", "Ingresa la fecha de nacimiento del piloto (dd/mm/aaaa)", parent=ventana)
    equipoActual = simpledialog.askstring("Entrada", "Ingresa el equipo del piloto o si esta retirado", parent=ventana)
    CampeonatosGanados = simpledialog.askinteger("Entrada", "Ingresa los campeonatos del piloto", minvalue=0, parent=ventana)
    victoriasGP = simpledialog.askinteger("Entrada", "Ingresa los gp ganados del piloto", minvalue=0, parent=ventana)
    numPodios = simpledialog.askinteger("Entrada", "Ingresa los podios del piloto", minvalue=0, parent=ventana)
    añoDebut = simpledialog.askinteger("Entrada", "Ingresa el año de debut del piloto", minvalue=0, maxvalue=2025, parent=ventana)

    piloto = {
        "Piloto" : Piloto,
        "nombre_completo" : nombreCompleto,
        "nacionalidad" : nacionalidad,
        "fecha_nacimiento" : fechaNacimiento,
        "equipo_actual" : equipoActual,
        "campeonatos_ganados" : CampeonatosGanados,
        "victorias_gp" : victoriasGP,
        "numero_podios" : numPodios,
        "año_debut" : añoDebut
    }
    lista.append(piloto)
    guardarDatos()
    messagebox.showinfo("Guardado", "Piloto guardado")


#Guardar todos los datos
def guardarDatos():
    with open(DATOS, "w", encoding="utf-8") as f:
        for i in lista:
            f.write(f"Piloto: {i["Piloto"]}\n")
            f.write(f"nombre_completo: {i["nombre_completo"]}\n")
            f.write(f"nacionalidad: {i["nacionalidad"]}\n")
            f.write(f"fecha_nacimiento: {i["fecha_nacimiento"]}\n")
            f.write(f"equipo_actual: {i["equipo_actual"]}\n")
            f.write(f"campeonatos_ganados: {i["campeonatos_ganados"]}\n")
            f.write(f"victorias_gp: {i["victorias_gp"]}\n")
            f.write(f"numero_podios: {i["numero_podios"]}\n")
            f.write(f"año_debut: {i["año_debut"]}\n\n")


#Cargar todos los datos
def cargarDatos():
    piloto = {}
    if os.path.exists(DATOS):
        with open(DATOS, "r", encoding="utf-8") as f:

            for linea in f:
                linea = linea.strip()

                #Comprobar cuando es un nuevo piloto
                if linea.startswith("Piloto"):
                    if piloto:
                        lista.append(piloto)
                        piloto = {}
                    piloto["Piloto"] = linea.split(": ")[1]
            
            #Cargar datos de las lineas
                elif linea.startswith("nombre_completo:"):
                    piloto["nombre_completo"] = linea.split(": ")[1]
                elif linea.startswith("nacionalidad:"):
                    piloto["nacionalidad"] = linea.split(": ")[1]
                elif linea.startswith("fecha_nacimiento:"):
                    piloto["fecha_nacimiento"] = linea.split(": ")[1]
                elif linea.startswith("equipo_actual:"):
                    piloto["equipo_actual"] = linea.split(": ")[1]
                elif linea.startswith("campeonatos_ganados:"):
                    piloto["campeonatos_ganados"] = int(linea.split(": ")[1])
                elif linea.startswith("victorias_gp:"):
                    piloto["victorias_gp"] = int(linea.split(": ")[1])
                elif linea.startswith("numero_podios:"):
                    piloto["numero_podios"] = int(linea.split(": ")[1])
                elif linea.startswith("año_debut:"):
                    piloto["año_debut"] = int(linea.split(": ")[1])
        
        # Agregar el último piloto cuando termine el bucle
            if piloto:
                lista.append(piloto)
    
    return lista


#Editar datos de nuevo piloto
def editarPiloto():
    piloto = simpledialog.askstring("Entrada", "Ingresa el piloto a editar", parent=ventana)
    for i in lista :
        if i['Piloto'] == piloto :
            i['nombre_completo'] = simpledialog.askstring("Entrada", "Ingresa el nuevo nombre completo", parent=ventana) or i['nombre_completo']
            i['nacionalidad'] = simpledialog.askstring("Entrada", "Ingresa la nueva nacionalidad del piloto", parent=ventana) or i['nacionalidad']
            i['fecha_nacimiento'] = simpledialog.askstring("Entrada", "Ingresa la nueva fecha de nacimiento del piloto (dd/mm/aaaa)", parent=ventana) or i['fecha_nacimiento']
            i['equipo_actual'] = simpledialog.askstring("Entrada", "Ingresa el nuevo equipo actual del piloto", parent=ventana) or i['equipo_actual']
            i['campeonatos_ganados'] =  simpledialog.askinteger("Entrada", "Ingresa los nuevos campeonatos ganados del piloto", minvalue=0, parent=ventana) or i['campeonatos_ganados']
            i['victorias_gp'] = simpledialog.askinteger("Entrada", "Ingresa los nuevos gp ganados del piloto", minvalue=0, parent=ventana) or i['victorias_gp']
            i['numero_podios'] = simpledialog.askinteger("Entrada", "Ingresa los nuevos podios del piloto", minvalue=0, parent=ventana) or i['numero_podios']
            i['año_debut'] = simpledialog.askinteger("Entrada", "Ingresa el nuevo año de debut del piloto", minvalue=0, maxvalue=2025, parent=ventana) or i['año_debut']

            messagebox.showinfo("Edicion completada", "Edicion finalizado exitosamente")
    guardarDatos()


#Mostrar lista de todos los pilotos
def mostrarLista():
        #Para mostrar ventana de texto
        ventanaTXT = tk.Tk()
        ventanaTXT.geometry("600x400")
        ventanaTXT.title("Lista de pilotos de F1")
        texto = tk.Text(ventanaTXT, wrap=tk.WORD)
        texto.pack(expand=True, fill='both')

        #Barra para navegar
        scroll = tk.Scrollbar(texto)
        scroll.pack(side='right', fill='y')
        texto.config(yscrollcommand=scroll.set)
        scroll.config(command=texto.yview)

        # Abrir y leer el archivo de datos
        with open(DATOS, 'r', encoding='utf-8') as f:
            contenido = f.read()
            texto.delete(1.0, tk.END)  # Limpiar el contenido anterior

            #Mostar la lista
            texto.insert(tk.END, contenido)

        #Para qu no se pueda editar
            texto.config(state="disabled")


def buscarLista():
    piloto = simpledialog.askstring("Entrada", "Ingresa el piloto a buscar", parent=ventana)

    for i in lista:
        if i["Piloto"] == piloto:
            textoPi = f" Piloto: {i["Piloto"]} \n nombre_completo: {i["nombre_completo"]} \n nacionalidad: {i["nacionalidad"]} \n fecha_nacimiento: {i["fecha_nacimiento"]} \n equipo_actual: {i["equipo_actual"]} \n campeonatos_ganados: {i["campeonatos_ganados"]} \n victorias_gp: {i["victorias_gp"]} \n numero_podios: {i["numero_podios"]} \n año_debut: {i["año_debut"]}"

            #Para mostrar ventana de texto
            ventanaTXT = tk.Tk()
            ventanaTXT.geometry("600x400")
            ventanaTXT.title("Lista de pilotos de F1")
            texto = tk.Text(ventanaTXT, wrap=tk.WORD)
            texto.pack(expand=True, fill='both')

            #Barra para navegar
            scroll = tk.Scrollbar(texto)
            scroll.pack(side='right', fill='y')
            texto.config(yscrollcommand=scroll.set)
            scroll.config(command=texto.yview)

            texto.delete(1.0, tk.END)  # Limpiar el contenido anterior

            #Mostar la lista
            texto.insert(tk.END, textoPi)

            #Para qu no se pueda editar
            texto.config(state="disabled")

            return

    #Cuando finalize el bucle y no se encontro el piloto
    messagebox.showwarning("Error", "Piloto no encontrado")


#Eliminar piloto
def eliminarPiloto():
    j = 0

    piloto = simpledialog.askstring("Entrada", "Ingresa el piloto a eliminar", parent=ventana)
    #Confirmar eliminacion
    confirmacion = messagebox.askyesno("Confirmacion", "Desea continuar?")

    if confirmacion:
        for i in lista:
            if i["Piloto"] == piloto:
                del lista[j]
                guardarDatos()
                messagebox.showinfo("Elimicaion", "Eliminacion completada")
                return
            j += 1
        #Cuando no se encontro piloto
        messagebox.showwarning("Error", "Piloto no encontrado")
    else:
        messagebox.showinfo("Eliminacion", "Eliminacion cancelada")
    

#Principal
cargarDatos()
for pilotoz in lista:
    print(pilotoz)

#Menu principal
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.config(background="#fcd4d2")
ventana.title("Listas de pilotos de F1")

#Titulo
titulo = tk.Label(ventana, text="Listas de pilotos de F1", font=("Comic Sans MS", 20, "bold"))
titulo.pack(pady=15)
titulo.config(background="#fcd4d2")

#Botones
registrarB = tk.Button(ventana, text="Registrar nuevo piloto", font=("Ubuntu Medium", 15), command=registrarPiloto)
registrarB.pack(pady=30)

consultarB = tk.Button(ventana, text="Consultar lista", font=("Ubuntu Medium", 15), command=mostrarLista)
consultarB.pack(pady=30)

editarB = tk.Button(ventana, text="Editar piloto", font=("Ubuntu Medium", 15), command=editarPiloto)
editarB.pack(pady=30)

buscarB = tk.Button(ventana, text="Buscar piloto", font=("Ubuntu Medium", 15), command=buscarLista)
buscarB.pack(pady=30)

eliminarB = tk.Button(ventana, text="Eliminar piloto", font=("Ubuntu Medium", 15), command=eliminarPiloto)
eliminarB.pack(pady=30)



ventana.mainloop()