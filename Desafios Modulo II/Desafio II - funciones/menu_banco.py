

def depositar():
    hola = 1
    print(hola)

def MainMenu():
    print(" Bienvenido al portal del Banco Amigo. Escoja una opción:\n")
    print("1. Consultar saldo")
    print("2. Hacer depósito")
    print("3. Realizar giro")
    print("4. Salir")

    select = int(input("-> "))

    if select == 1:
        return depositar()
    elif select == 2:
        return MainMenu()
    elif select == 3:
        return MainMenu()
    elif select == 4:
        None
    else:
        "Opción inválida. Por favor ingrese 1, 2, 3 ó 4."


MainMenu()



