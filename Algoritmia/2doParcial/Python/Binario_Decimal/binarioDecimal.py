def decimalBinario(decimal):
    binarioF = bin(decimal).replace("0b", "")
    print("El binario es: " + binarioF)
    return binarioF

def binarioDecimal(binario):
    decimalF = int(binario, 2)
    print("El decimal es: ", decimalF)
    return decimalF

def repeticion():
    print("Seleccione una opcion")
    print("1.- Decimal a bianrio")
    print("2.- Binario a decimal")
    print("3.- Salir")

    opc = int(input("...: "))

    if opc == 1:
        decimal = int(input("Ingrese el decimal: "))
        decimalBinario(decimal)
        return repeticion()

    elif opc == 2:
        binario = str(input("Ingrese el binario: "))
        binarioDecimal(binario)
        return repeticion()

    elif opc == 3:
        return

    else:
        print("Error, opcion no valida")
        return repeticion()


#Principal
repeticion()
