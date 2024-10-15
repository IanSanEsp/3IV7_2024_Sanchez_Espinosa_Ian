Algoritmo chicharronera
	definir a, b ,c Como Entero
	
	mark = 0
	
	Escribir Raiz(0)
	
	Mientras mark <> 5 Hacer
		Escribir "1.- Ingresar termino cuadratico"
		Escribir "2.- Ingresar termino lineal"
		Escribir "3.- Ingresar termino independiente"
		Escribir "4.- Calcular"
		Escribir "5.- Salir"
		
		Leer mark
		
		Segun mark Hacer
			1:
				Escribir "Ingresa el termino cuadratico"
				Leer a
			2:
				Escribir "Ingresa el termino lineal"
				Leer b
			3:
				Escribir "Ingresa el termino independiente"
				leer c
			4:
				Escribir a, b , c
				
				root = Raiz(b - (4 * a * c))
				Escribir root
				denominador = 2 * a
				
				x1 = (-b + root)/denominador
				
				x2 = (-b - root)/denominador
				
				Si root < 0 Entonces
					Escribir "Error, raiz negativa"
				SiNo
					Escribir "x1 = ", x1
					Escribir "x2 = ", x2
				Fin Si
			5:
		Fin Segun
		
		
	Fin Mientras
FinAlgoritmo
