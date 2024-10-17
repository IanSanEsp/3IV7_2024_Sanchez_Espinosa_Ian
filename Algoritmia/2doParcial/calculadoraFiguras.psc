//Crear un programa para calcular areas y perimetros con subprocesos

//Subproceso del rectangulo
SubProceso Rectangulo(base, altura)
	Definir area, perimetro como reales
	
	area = base * altura
	perimetro = (2 * base) + (2 * altura)
	
	Escribir "El area del rectangulo es: ", area
	Escribir "El perimetor del rectangulo es: ", perimetro
FinSubProceso

//Subproceso triangulo 
SubProceso Triangulo(base, altura, lado1, lado2, lado3)
	Definir area, perimetro como reales
	
	area = (base * altura)/2
	perimetro = lado1 + lado2 + lado3
	
	Escribir "El area del triangulo es: ", area
	Escribir "El perimetor del trinagulo es: ", perimetro
FinSubProceso

//Subproceso trapecio
SubProceso Trapecio(baseM, basem, altura, lado1, lado2)
	Definir area, perimetro como reales
	
	area = ((baseM + basem)/2) * altura
	perimetro = baseM + basem + lado1 + lado2
	
	Escribir "El area del trapecio es: ", area
	Escribir "El perimetor del trapecio es: ", perimetro
FinSubProceso

//Subproceso rombo
SubProceso Rombo(diagonalM, diagonalm,  lado1, lado2, lado3, lado4)
	Definir area, perimetro como reales
	
	area = (diagonalM * diagonalm)/2
	perimetro = lado1 + lado2 + lado3 + lado4
	
	Escribir "El area del rombo es: ", area
	Escribir "El perimetor del rombo es: ", perimetro
FinSubProceso

//Subproceso pentagono
SubProceso Pentagono(apotema,  lado1, lado2, lado3, lado4, lado5)
	Definir area, perimetro como reales
	
	perimetro = lado1 + lado2 + lado3 + lado4 + lado5
	aera = (perimetro * apotema)/2
	
	Escribir "El area del pentagono es: ", area
	Escribir "El perimetor del pentagono es: ", perimetro
FinSubProceso





Algoritmo calculadoraFiguras
	Definir opcion Como Caracter
	Definir base, altura, lado1, lado2, lado3 Como Real
	
	//Crear menu
	Escribir "Selecciona una opcion"
	Escribir "A.- Area y perimetro del rectangulo"
	Escribir "B.- Area y perimetro del triangulo"
	
	Leer opcion
	
	Segun oppcion Hacer
		"A":
			Escribir "Ingresa la base del rectangulo"
			Leer base
			
			Escribir "Ingresa la altura del rectangulo"
			Leer altura
			
			Rectangulo(base,altura)

		"B":
			Escribir "Ingresa la base del triangulo"
			Leer base
			
			Escribir "Ingresa la altura del triangulo"
			Leer altura
			
			Escribir "Ingresa lado 1"
			Leer lado1
			
			Escribir "Ingresa lado 2"
			Leer lado2
			
			Escribir "Ingresa lado 3"
			Leer lado3
			
			Triangulo(base,altura, lado1, lado2, lado3)
			
		De Otro Modo:
			Escribir "Opcion no valida"
	Fin Segun
	
FinAlgoritmo
