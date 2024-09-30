Algoritmo LaVidadeLasPersonas
	Escribir "De cuantas personas sera el listado"
	Leer n
	
	Escribir "Cuantos años se analizaran"
	Leer na
	
	Dimension nacimiento[n]
	Dimension fallecimiento[n]
	Dimension añosAnalizar[na]
	
	Para i <- 1 Hasta n Con Paso 1 Hacer
		Escribir "Introduce el año de nacimiento de la persona ", i
		Leer nacimiento[i]
		
		Escribir "Introduce el año de fallecimiento de la persona ", i,  " (En caso de seguir viva poner 0)"
		Leer fallecimiento[i]
	Fin Para
	
	Para i<- 1 Hasta na Con Paso 1 Hacer
		Escribir "Intruduce el año ", i, " que se analizara"
		Leer añosAnalizar[i]
	Fin Para
	
	Escribir "------------------------------------------------------------------"
	
	Dimension vivos[na, n]
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Para c <- 1 Hasta n Con Paso 1 Hacer
			Si añosAnalizar[f] <= fallecimiento[c] y añosAnalizar[f] >= nacimiento[c] Entonces
				vivos[f, c] <- nacimiento[c]
			Fin Si
		Fin Para
	Fin Para
	
	Para c <- 1 Hasta na Con Paso 1 Hacer
		Escribir "En el año ", añosAnalizar[c], " estaban vivos los nacidos en: "
		
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
			edades[f, c] <- añosAnalizar[f] - nacimiento[c]
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
	
	Escribir "Las personas mas jovenes de cada año respectivamente son:"
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Si joven[f, 1] = 999 Entonces
			Escribir añosAnalizar[f], " Nadie vivo"
		SiNo
			Escribir añosAnalizar[f], ": ", joven[f, 1]
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
	
	Escribir "Las personas mas viejas de cada año respectivamente son:"
	
	Para f <- 1 Hasta na Con Paso 1 Hacer
		Si viejo[f, 1] = -1 Entonces
			Escribir añosAnalizar[f], " Nadie vivo"
		SiNo
			Escribir añosAnalizar[f], ": ", viejo[f, 1]
		Fin Si
		
		//Escribir joven[f, 1]
	Fin Para
	//Escribir añosAnalizar[1]
	//Escribir nacimiento[1]
FinAlgoritmo
