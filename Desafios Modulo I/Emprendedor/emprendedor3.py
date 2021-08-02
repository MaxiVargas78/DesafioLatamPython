from sys import argv

def Emprendedor3():
    if len(argv) < 5:
        PrecioVenta = float(argv[1])
        UserSuscrito = float(argv[2])
        Gastos = float(argv[3])
        LastUtilidad = int(1000)
        Utilidad = PrecioVenta*UserSuscrito - Gastos

        Razon = Utilidad/LastUtilidad
        if Razon >= 1:
            print("Utilidad Actual: $"+str(int(Utilidad))+" Dolares.")
            print("Utilidad Pasada: $"+str(int(LastUtilidad))+" Dolares.")
            print("La razon entre la utilidad actual y la anterior es:"+str(float(Razon)))
            print("Utilidades actuales superiores a las anteriores")
        else:
            print("Utilidad Actual: $"+str(int(Utilidad))+" Dolares.")
            print("Utilidad Pasada: $"+str(int(LastUtilidad))+" Dolares.")
            print("La razon entre la utilidad actual y la anterior es:"+str(float(Razon)))
            print("Utilidades actuales inferiores a las anteriores")

    elif len(argv) == 5:
        PrecioVenta = float(argv[1])
        UserSuscrito = float(argv[2])
        Gastos = float(argv[3])
        LastUtilidad = float(argv[4])
        Utilidad = PrecioVenta*UserSuscrito - Gastos

        Razon1 = Utilidad/LastUtilidad
        if Razon1 >= 1:
            print("Utilidad Actual: $"+str(int(Utilidad))+" Dolares.")
            print("Utilidad Pasada: $"+str(int(LastUtilidad))+" Dolares.")
            print("La razon entre la utilidad actual y la anterior es:"+str(float(Razon1)))
            print("Utilidades actuales superiores a las anteriores")
        else:
            print("Utilidad Actual: $"+str(int(Utilidad))+" Dolares.")
            print("Utilidad Pasada: $"+str(int(LastUtilidad))+" Dolares.")
            print("La razon entre la utilidad actual y la anterior es:"+str(float(Razon1)))
            print("Utilidades actuales inferiores a las anteriores")

Emprendedor3()