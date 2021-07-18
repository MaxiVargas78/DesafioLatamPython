from sys import argv

def Emprendedor2():
    NormalUser = float(argv[1])
    PremiumUser = float(argv[2])
    TrialUser = float(argv[3])
    EstandarServ = float(argv[4])
    Gastos = float(argv[5])

    Utilidad1 = EstandarServ*NormalUser - Gastos
    Utilidad2 = (2*EstandarServ)*PremiumUser - Gastos
    print("Las utilidades de los usuarios normales es de $"+str(int(Utilidad1))+" Dolares.")
    print("Las utilidades de los usuarios premium es de $"+str(int(Utilidad2))+" Dolares.")
    print("Las utilidades de los usuarios de prueba es de $"+str(int(-Gastos))+" Dolares.")

Emprendedor2()