Algoritmo tienda
	Definir producto como texto
	Definir codigoProducto, cantidad Como Entero
	Definir precio Como Real
	
	
	
	//Crear un menu de seleccion
	Mientras opcion <> 5 Hacer
		Escribir "1.- Ingresa un nuevo producto"
		Escribir "2.- Actualiza un producto"
		Escribir "3.- Consulta inventario"
		Escribir "4.- Generar reporte"
		Escribir "5.- Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			1:
				Escribir "Ingresa el producto"
				Leer producto
				Escribir "Ingresa el codigo del producto"
				Leer codigoProducto
				Escribir "ingresa la cantidad"
				Leer cantidad
				Escribir  "Ingresa el precio"
				Leer precio
			2:
				Escribir "ingresa el codigo del producto"
				Leer codigoProducto
				Escribir "Ingresa la ueva cantidad"
				Leer cantidad
			3:
				Escribir "Consultar el inventario"
				Escribir "nombre del producto:", producto
				Escribir "codigo del producto:", codigoProducto
				Escribir "precio del producto:", precio
				Escribir "cantidad del producto:", cantidad
			4:
				Escribir "Reporte"
		Fin Segun
	Fin Mientras
	
	
	
FinAlgoritmo
