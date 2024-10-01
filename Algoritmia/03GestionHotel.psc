Algoritmo ReservasHotel
	nh <- 999
	dia <- 999
	mes <- 999
	año <- 1
	totalh <- 0
	hocupadas <- 0
	
	Escribir "Cuantas habitaciones tiene el hotel"
	Leer totalh
	Dimension habitaciones[totalh]
	Dimension diaD[totalh]
	Dimension mesD[totalh]
	Dimension añoD[totalh]
	
	Mientras opcion <> 5 Hacer
		Escribir "1.- Reservar"
		Escribir "2.- Cancelar reserva"
		Escribir "3.- Consultar disponibiidad"
		Escribir "4.- Gestionar ocupacion del hotel"
		Escribir "5.- Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			1:
				Mientras nh > totalh Hacer
				Escribir "Ingresa el numero de habitacion"
				Leer nh
				Si nh > totalh Entonces
					Escribir "Error la habitacion es mayor al total"
				Fin Si
			    Fin Mientras

				
				Mientras dia > 30 hacer
				Escribir "Ingresa el dia de reservacion"
				Leer dia
				Si dia > 30 Entonces
					Escribir "Error dias mayores a 31"
				Fin Si
				Fin Mientras
				
				Mientras mes > 12 hacer
				Escribir "Ingresa el mes de reservacion"
				Leer mes
				Si mes > 12 Entonces
					Escribir "Error mes mayor a 12"
				Fin Si
				Fin Mientras
				
				Mientras año < 2024 hacer
				Escribir "Escribe el año de reservacion"
				Leer año
				Si año < 2024 Entonces
					Escribir "Error año no valido"
				Fin Si
				Fin Mientras
				
				habitaciones[nh]<- nh
				diaD[nh] <- dia
				mesD[nh] <- mes
				añoD[nh] <- año
				
				nh <- 999
				dia <- 999
				mes <- 999
				año <- 1
				
				hocupadas <- hocupadas + 1
			2:
				Escribir "Ingresa la habiitacion que desea cancelar"
				Leer eliminarh
				
				habitaciones[eliminarh] <- 0
			3:
				Escribir "Las habitaciones ocupadas son:"
				Para i <- 1 Hasta totalh Con Paso 1 Hacer
					Si habitaciones[i] <> 0 Entonces
						Escribir habitaciones[i]
					Fin Si
				Fin Para
				Escribir "De las ", totalh, " que hay"
				Escribir " "
			4:
				Para i <- 1 Hasta totalh Con Paso 1 Hacer
					Si habitaciones[i] <> 0 Entonces
						ocupadas <- ocupadas + 1
					Fin Si
				Fin Para
				porcentaje <- (ocupadas * 100) / totalh
				Escribir "El porcentaje de ocupacion es del ", porcentaje, "%"
				Escribir " "
		Fin Segun
		
	Fin Mientras
	
FinAlgoritmo
