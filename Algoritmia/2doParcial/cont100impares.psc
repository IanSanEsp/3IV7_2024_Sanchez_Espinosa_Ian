Algoritmo cont100impares
	Definir opc Como Entero
	opc <- 0
	n <- 0
	div <- 0
	
	Mientras opc <> 2 Hacer
		Escribir "1,-Mostar conteo"
		Escribir "2.-Finalizar programa"
		Leer opc
		
		Segun opc Hacer
			1:
				Para n <- 0 Hasta 100 Con Paso 1 Hacer
					Si n % 2 <> 0 Entonces
						Escribir n
					Fin Si
				Fin Para
				n <- 0
		Fin Segun
	Fin Mientras
FinAlgoritmo

