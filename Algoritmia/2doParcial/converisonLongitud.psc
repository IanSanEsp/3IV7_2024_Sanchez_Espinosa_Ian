Algoritmo converisonLongitud
	definir pies Como Entero
	
	Escribir "Escribe longitud en pies"
	Leer pies
	
	m = 0
	
	Si pies > 0 Entonces
	
	Mientras m <> 5 Hacer
		
		Escribir "1.- Convertir a pulgadas"
		Escribir "2.- Convertir a yardas"
		Escribir "3.- Convertir a centimetros"
		Escribir "4.- Convertir a metros"
		Escribir "5.- Salir"
		
		Leer m
		
		Segun m Hacer
			1:
				pulgadas = pies * 12
				Escribir "La unidad en pulgadas es ", pulgadas
			2:
				yardas = pies / 3
				Escribir "La unidad en yardas es ", yardas
			3:
				centimetros = pies * 30.48
				Escribir "La unidad en centimetros es ", centimetros
			4:
				metros = pies / 3.281
				Escribir "La unidad en metros es ", metros
		Fin Segun
	Fin Mientras
	
	SiNo
		Escribir "Error, longitud negativa"
		
	FinSi

	
	
FinAlgoritmo
