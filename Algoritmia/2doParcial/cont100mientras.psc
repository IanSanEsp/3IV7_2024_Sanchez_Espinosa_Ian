Algoritmo cont100mientras
	Definir opc Como Entero
	opc <- 0
	n <- 0
	
	Mientras opc <> 2 Hacer
		Escribir "1,-Mostar conteo"
		Escribir "2.-Finalizar programa"
		Leer opc
		
		Segun opc Hacer
			1:
				Mientras n < 100 Hacer
					n <- n + 1
					Escribir n
				Fin Mientras
				n <- 0
		Fin Segun
	Fin Mientras
FinAlgoritmo
