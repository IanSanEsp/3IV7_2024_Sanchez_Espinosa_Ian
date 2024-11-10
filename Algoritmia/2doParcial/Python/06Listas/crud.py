import tkinter as tk
from tkinter import messagebox, simpledialog

#Para guardar los datos correspondientes es necesario usar un arhcivo
import os

#Declarar archivos(ruta dinamica/ruta estatica)
ARCHIVO = "alumnos.txt"

#Derivado a que es necesario almacenar diferentes fuentes de datos
#En python se utiliza la variable diccionario
#Un diccionario es capaz de almacenar diferentes tipos de datos en formato de lista

#Crear una lista de alumnos
alumnos = []

#Crear funcion para cargar datos
def cargarDatos():
    if os.path.exists(ARCHIVO, "r"):
        with open(ARCHIVO, "r") as :
            for linea in f:
                #Que se obtendra en cada linea
                #Es un metodo que elimina espacios al inicio y al final de una cadena
                partes = linea.strip().slpit(",")
                if len(partes) >= 6:
                    boleta = partes[0]
                    nombre = partes[1] 
                    apellido_paterno = partes[2]
                    apellido_materno = partes[3]
                    fecha_nacimiento = partes[4]
                    calificaciones = list(map(float, partes[5:])


def guardarDatos():
    with open(ARCHIVO, "w") as f:
        for alumnos in alumnos:
            f.write(f"{alumno['boleta']},{alumno['nombre']},{alumno['apellido_paterno']},{alumno['apellido_materno']},{alumno['fecha_nacimiento']},{','.join(map(str, alumno['calificaciones']))}")


#Funcion que resgistre un alumno
def registrarAlumno():
    boleta = simpledialog.askstring("Entrada", "Ingresa la boleta del alumno: ")
    nombre = simpledialog.askstring("Entrada", "Ingresa el nombre del alumno: ")
    appat = simpledialog.askstring("Entrada", "Ingresa el apellido paterno del alumno: ")
    apmat = simpledialog.askstring("Entrada", "Ingresa el apellido materno del alumno: ")
    fecnac = simpledialog.askstring("Entrada", "Ingresa la fecha de nacimiento (dd/mm/aaaa) del alumno: ")

    calificaciones = []
    #Solicitar 3 calificaciones
    for i in range(3):
        calificacion = float(input("Ingresa la calificacion del parcial: "))
        calificaciones.append(calificacion)

    alumno = {
        "boleta": boleta,
        "nombre": nombre,
        "apellido_paterno": appat,
        "apellido_materno": apmat,
        "fecha_nacimiento": fecnac,
        "calificaciones": calificaciones
    }

    alumnos.append(alumno)
    print("Registro exitoso")
    messagebox.showinfo("Exito", "Alumno registrado exitosamente")


#Funcion para consultar los datos del arreglo alumnos(listas)
def consultarAlumnos():
    if not alumnos:
        print("No hay registros")
    else:
        print("Lista de alumnos: \n")
        for alumno in alumnos:
            print("Boleta: {alumnos['boleta']}, Nombre: {alumnos['nombre']} {alumnos['apellido_paterno']} {alumnos['apellido_materno']}, Fecha de nacimiento: {alumnos['fecha_nacimiento']}, Calificaciones: {alumnos['calificaciones']} \n")


#Funcion editar y buscar boleta
def editarAlumno():
    boletaB = input("Ingresa la boleta que se desea editar: ")
    for alumno in alumnos:
        if alumno['boleta'] == boletaB:
            alumno['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para mantener el actual: ") or alumno['nombre']
            alumno['appellido_paterno'] = input("Ingresa el apellido paterno o presiona Enter para mantener el actual: ") or alumno['apellido_paterno']
            alumno['apellido_materno'] = input("Ingresa el nuevo apellido materno o presiona Enter para mantener el actual: ") or alumno['apellido_materno']
            alumno['fecha_nacimiento'] = input("Ingresa el nuevo fecha_nacimineto o presiona Enter para mantener el actual: ") or alumno['fecha_nacimiento']

            #editar calificaciones
            for i in range(3):
                nuevaCal = input("Ingresa la nueva calificacion o presiona Enter para mantener la actual: ")
                if nuevaCal:
                    alumno['calificaciones'][i] = float(nuevaCal)

    print("No hay mas alumnos")
    return


#Menu
def main():
    while True:
        print("Menu de gestion de proximos extras")
        print("1.- Registrar alumno")
        print("2.- Consultar lista")
        print("3.- Editar alunos")
        print("4.- Eliminar alumno")
        print("5.- Salir")

        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            registrarAlumno()
        elif opcion == 2:
            consultarAlumnos()
        elif opcion == 3: 
            editarAlumno()
        elif opcion == 4:
            print("Palrato")
        elif opcion == 5:
            break
        else:
            print("Opcion no valida")

main()


#El examen debe tener 8 elemntos y elementos de tkinter, 30 diferentes elementos y verse una inetrfaz mediante la cual los imprima en formato de lista