//Crear un programa para calcular areas y perimetros con subprocesos

//Subproceso del rectangulo
SubProceso Rectangulo(base, altura)
	Definir area, perimetro como reales
	
	area = base * altura
	perimetro = (2 * base) + (2 * altura)
	
	Escribir "El area del rectangulo es: ", area
	Escribir "El perimetro del rectangulo es: ", perimetro
FinSubProceso

//Subproceso triangulo 
SubProceso Triangulo(base, altura, lado1, lado2, lado3)
	Definir area, perimetro como reales
	
	area = (base * altura)/2
	perimetro = lado1 + lado2 + lado3
	
	Escribir "El area del triangulo es: ", area
	Escribir "El perimetro del trinagulo es: ", perimetro
FinSubProceso

//Subproceso trapecio
SubProceso Trapecio(baseM, basem, altura, lado1, lado2)
	Definir area, perimetro como reales
	
	area = ((baseM + basem)/2) * altura
	perimetro = baseM + basem + lado1 + lado2
	
	Escribir "El area del trapecio es: ", area
	Escribir "El perimetro del trapecio es: ", perimetro
FinSubProceso

//Subproceso rombo
SubProceso Rombo(diagonalM, diagonalm, lado1, lado2, lado3, lado4)
	Definir area, perimetro como reales
	
	area = (diagonalM * diagonalm)/2
	perimetro = lado1 + lado2 + lado3 + lado4
	
	Escribir "El area del rombo es: ", area
	Escribir "El perimetro del rombo es: ", perimetro
FinSubProceso

//Subproceso pentagono
SubProceso Pentagono(apotema, lado1, lado2, lado3, lado4, lado5)
	Definir area, perimetro como reales
	
	perimetro = lado1 + lado2 + lado3 + lado4 + lado5
	area = (perimetro * apotema)/2
	
	Escribir "El area del pentagono es: ", area
	Escribir "El perimetro del pentagono es: ", perimetro
FinSubProceso

//Subproceso hexagono
SubProceso Hexagono(apotema, lado1, lado2, lado3, lado4, lado5, lado6)
	Definir area, perimetro como reales
	
	perimetro = lado1 + lado2 + lado3 + lado4 + lado5 + lado6
	area = (perimetro * apotema)/2
	
	Escribir "El area del hexagono es: ", area
	Escribir "El perimetro del hexagono es: ", perimetro
FinSubProceso

//Subproceso heptagono
SubProceso Heptagono(apotema, lado1, lado2, lado3, lado4, lado5, lado6, lado7)
	Definir area, perimetro como reales
	
	perimetro = lado1 + lado2 + lado3 + lado4 + lado5 + lado6 + lado7
	area = (perimetro * apotema)/2
	
	Escribir "El area del heptagono es: ", area
	Escribir "El perimetro del heptagono es: ", perimetro
FinSubProceso



Algoritmo calculadoraFiguras
	Definir opcion Como Caracter
	Definir base, altura, lado1, lado2, lado3 Como Real
	
	//Crear menu
	Escribir "Selecciona una opcion"
	Escribir "A.- Area y perimetro del rectangulo"
	Escribir "B.- Area y perimetro del triangulo"
	Escribir "C.- Area y perimetro del trapecio"
	Escribir "D.- Area y perimetro del rombo"
	Escribir "E.- Area y perimetro del pentagono"
	Escribir "F.- Area y perimetro del hexagono"
	Escribir "G.- Area y perimetro del heptagono"
	
	Leer opcion
	
	Segun opcion Hacer
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
			
		"C":
			Escribir "Ingresa la base mayor"
			Leer baseM
			
			Escribir "Ingresa la base menor"
			Leer basem
			
			Escribir "Ingresa la altura"
			Leer altura
			
			Escribir "Ingresa el lado 1"
			Leer lado1
			
			Escribir "Ingresa el lado 2"
			Leer lado2
			
			Trapecio(baseM, basem, altura, lado1, lado2)
			
		"D":
			Escribir "Ingresa la diagonal mayor"
			Leer diagonalM
			
			Escribir "Ingresa la diagonal menor"
			Leer diagonalm
			
			Escribir "Ingresa el lado 1"
			Leer lado1
			
			Escribir "Ingresa el lado 2"
			Leer lado2
			
			Escribir "Ingresa el lado 3"
			Leer lado3
			
			Escribir "Ingresa el lado 4"
			Leer lado4
			
			Rombo(diagonalM, diagonalm, lado1, lado2, lado3, lado4)
			
		"E":
			Escribir "Ingresa la apotema"
			Leer apotema
			
			Escribir "Ingresa el lado 1"
			Leer lado1
			
			Escribir "Ingresa el lado 2"
			Leer lado2
			
			Escribir "Ingresa el lado 3"
			Leer lado3
			
			Escribir "Ingresa el lado 4"
			Leer lado4
			
			Escribir "Ingresa el lado 5"
			Leer lado5
			
			Pentagono(apotema, lado1, lado2, lado3, lado4, lado5)
			
		"F":
			Escribir "Ingresa la apotema"
			Leer apotema
			
			Escribir "Ingresa el lado 1"
			Leer lado1
			
			Escribir "Ingresa el lado 2"
			Leer lado2
			
			Escribir "Ingresa el lado 3"
			Leer lado3
			
			Escribir "Ingresa el lado 4"
			Leer lado4
			
			Escribir "Ingresa el lado 5"
			Leer lado5
			
			Escribir "Ingresa el lado 6"
			Leer lado6
			
			Hexagono(apotema, lado1, lado2, lado3, lado4, lado5, lado6)
			
		"G":
			Escribir "Ingresa la apotema"
			Leer apotema
			
			Escribir "Ingresa el lado 1"
			Leer lado1
			
			Escribir "Ingresa el lado 2"
			Leer lado2
			
			Escribir "Ingresa el lado 3"
			Leer lado3
			
			Escribir "Ingresa el lado 4"
			Leer lado4
			
			Escribir "Ingresa el lado 5"
			Leer lado5
			
			Escribir "Ingresa el lado 6"
			Leer lado6
			
			Escribir "Ingresa el lado 7"
			Leer lado7
			
			Heptagono(apotema, lado1, lado2, lado3, lado4, lado5, lado6, lado7)
			
		De Otro Modo:
			Escribir "Opcion no valida"
	Fin Segun
	
FinAlgoritmo
