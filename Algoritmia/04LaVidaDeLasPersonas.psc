Algoritmo LaVidadeLasPersonas
	Escribir "De cuantas personas sera el listado"
	Leer n
	
	Escribir "Cuantos a�os se analizaran"
	Leer na
	
	Dimension nacimiento[n]
	Dimension fallecimiento[n]
	Dimension a�osAnalizar[na]
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Escribir "Introduce el a�o de nacimiento de la persona ", i
		Leer nacimiento[i]
		
		Escribir "Introduce el a�o de fallecimiento de la persona ", i,  " (En caso de seguir viva poner 0)"
		Leer fallecimiento[i]
	Fin Para
	
	Para i<- 1 Hasta na Con Paso 1 Hacer
		Escribir "Intruduce el a�o ", i, " que se analizara"
		Leer a�osAnalizar[i]
	Fin Para
	
	Escribir "------------------------------------------------------------------"
	
	Dimension vivos[na, n]
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Para c <- 1 Hasta n Con Paso 1 Hacer
			Si a�osAnalizar[f] <= fallecimiento[c] y a�osAnalizar[f] >= nacimiento[c] Entonces
				vivos[f, c] <- nacimiento[c]
			Fin Si
		Fin Para
	Fin Para
	
	Para c <- 1 Hasta na Con Paso 1 Hacer
		Escribir "En el a�o ", a�osAnalizar[c], " estaban vivos los nacidos en: "
		
		Para d <- 1 Hasta n Con Paso 1 Hacer
			Si vivos[c, d] <> 0 Entonces
				Escribir vivos[c, d]
			Fin Si
		Fin Para
	Fin Para
	
	Escribir "------------------------------------------------------------------"
	
	Dimension edades[na, n]
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Para c <- 1 Hasta n Con Paso 1 Hacer
			edades[f, c] <- a�osAnalizar[f] - nacimiento[c]
		Fin Para
	Fin Para
	
	Dimension joven[na, 1]
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		joven[f, 1] <- 999
	Fin Para
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Para c <- 1 Hasta n Con Paso 1 Hacer
			Si edades[f, c] < joven[f, 1] y edades[f, c] >= 0 y vivos[f, c] <> 0 Entonces
				joven[f, 1] <- edades[f, c]
			Fin Si
		Fin Para
	Fin Para
	
	Escribir "Las personas mas jovenes de cada a�o respectivamente son:"
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Si joven[f, 1] = 999 Entonces
			Escribir a�osAnalizar[f], " Nadie vivo"
		SiNo
			Escribir a�osAnalizar[f], ": ", joven[f, 1]
		Fin Si
		
		//Escribir joven[f, 1]
	Fin Para
	
	Escribir "------------------------------------------------------------------"
	
	Dimension viejo[na, 1]
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		viejo[f, 1] <- -1
	Fin Para
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Para c <- 1 Hasta n Con Paso 1 Hacer
			Si edades[f, c] > viejo[f, 1] y edades[f, c] >= 0 y vivos[f, c] <> 0 Entonces
				viejo[f, 1] <- edades[f, c]
			Fin Si
		Fin Para
	Fin Para
	
	Escribir "Las personas mas viejas de cada a�o respectivamente son:"
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Si viejo[f, 1] = -1 Entonces
			Escribir a�osAnalizar[f], " Nadie vivo"
		SiNo
			Escribir a�osAnalizar[f], ": ", viejo[f, 1]
		Fin Si
		
		//Escribir joven[f, 1]
	Fin Para
	//Escribir a�osAnalizar[1]
	//Escribir nacimiento[1]
FinAlgoritmo
