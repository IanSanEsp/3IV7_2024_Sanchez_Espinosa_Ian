Algoritmo conversionBinario
	Definir n, r como entero
	Definir binario como texto //el binario se debe concatenar
	
	binario <- ""
	
	Escribir "Ingresa el numero decimal"
	Leer n
	
	Si n >= 0 Entonces
		Mientras n > 0 Hacer
			r = n % 2
			
			//armar el binario
			Nbinario = ConvertirATexto(r)
			binario = Nbinario + binario
			
			n = Trunc(n/2)
		Fin Mientras
		
		//Si el numero es 0
	SiNo
		si binario = "" Entonces
			binario = "0"
		FinSi
	Fin Si
	
	Escribir "El binario es ", binario
	
FinAlgoritmo
