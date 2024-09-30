Algoritmo cobroEstacionamiento
	Definir horaEntrada, minutoEntrada, horaSalida, minutoSalida como entero
	Definir totalHoras, totalMinutos, minutosTotalesCuenta como entero
	Definir totalCobro como entero
	
	//Entrada de datos
	Escribir "Ingrese la hora de entrada en formato de 24 horas"
	Leer horaEntrada
	
	Escribir "Ingrese los minutos de entrada en formato de 0-59"
	Leer minutoEntrada
	
	Escribir "Ingrese la hora de salida en formato de 24 horas"
	Leer horaSalida
	
	Escribir "Ingrese los minutos de salida en formato de 0-59"
	Leer minutoSalida
	
	//Proceso 
	//Calcular tiempo total en minutos
	totalHoras = horaSalida - horaEntrada
	totalMinutos = minutoSalida - minutoEntrada
	
	//Evaluar casos
	Si totalMinutos < 0 Entonces
		totalMinutos = totalMinutos + 60
		totalHoras = totalHoras - 1
	Fin Si
	
	//convertir todo a minutos 
	totalMinutos = (totalHoras * 60) + totalMinutos
	
	//Calcular el cobro
	totalCobro = 0
	
	//Calcular cobro por la hora completa
	Si totalMinutos >= 60 Entonces
		totalCobro = totalCobro + (totalMinutos/60) * 15
	Fin Si
	
	//Calcular el cobro de cada fraccion
	minutosRestantes = totalMinutos % 60
	Si minutosRestantes > 0 Entonces
		fracciones15Min = minutosRestantes
	Fin Si
	
	//Cobrar cada fraccion
	totalCobro = totalCobro + fracciones15Min * 6
	
	//Mostrar resultado
	Escribir "El total a pagar es: ", totalCobro, " pesos"
	FinAlgoritmo
