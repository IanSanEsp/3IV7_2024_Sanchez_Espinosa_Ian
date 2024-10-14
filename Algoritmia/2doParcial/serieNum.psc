Algoritmo serieNum
	Definir n, pos, neg Como Entero
	Escribir "Ingresa la cantidad de digitos que tendar la serie numerica"
	Leer n
	
	Dimension serie[n]
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Escribir "Ingresa el numero ", i, " de la serie numerica"
		Leer serie[i]
		
		Si serie[i] < 0 Entonces
			neg = neg + 1
		SiNo
			Si serie[i] > 0 Entonces
				pos = pos + 1
			FinSi
		Fin Si
	Fin Para
	
	Escribir "En la serie numerica hay ", pos, " numeros positivos"
	Escribir "En la serie numerica hay ", neg, " numeros negativos"
	
	
FinAlgoritmo
