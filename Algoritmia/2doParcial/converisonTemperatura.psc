Algoritmo converisonTemperatura
	definir f Como Entero
	
	Escribir "Escribe la temperatura en fahrenheit"
	Leer f
	
	m = 0
		
		Mientras m <> 4 Hacer
			
			Escribir "1.- Convertir a celsius"
			Escribir "2.- Convertir a kelvin"
			Escribir "3.- Convertir a rankine"
			Escribir "4.- Salir"
			
			Leer m
			
			Segun m Hacer
				1:
					c = (f - 32) * (5/9)
					Escribir "Celsius = ", c
				2:
					k = (f - 32) * (5/9) + 273.15
					Escribir "kelvin = ", k
				3:
					r = f + 459.67
					Escribir "Rankine = ", r
			Fin Segun
		Fin Mientras
	
FinAlgoritmo

