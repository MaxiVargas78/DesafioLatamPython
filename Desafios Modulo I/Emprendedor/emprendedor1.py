from sys import argv

def Emprendedor():
    PrecioVenta = float(argv[1])
    UserSuscrito = float(argv[2])
    Gastos = float(argv[3])

    Utilidad = PrecioVenta*UserSuscrito - Gastos
    print("Las utilidades son de $"+str(int(Utilidad))+" Dolares.")

Emprendedor()