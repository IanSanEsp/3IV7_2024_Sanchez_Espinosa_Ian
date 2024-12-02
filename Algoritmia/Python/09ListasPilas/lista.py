#Una lista es muy parecido a un arreglo, solo que es una estructura mas versatil la cual puede manejar enteros, flotantes, cadenas, caracteres, etc.

estudiantes = ["Ana", "Hugo", "Paco", "Luis"]

#append(x) agrega un elemento al final, insert(i, x) inserta un elemento en una posicion especifica, remove(x) elimina

#Agregar uno
estudiantes.append("Diana")
print("Listas de estudiantes: ", estudiantes)

#Eliminar uno
estudiantes.remove("Hugo")
print("Lista de estudiantes: ", estudiantes)