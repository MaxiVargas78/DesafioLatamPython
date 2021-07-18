import math
from sys import argv

def Escape():
    g = float(argv[1])
    r = float(argv[2])*1000
    resultado = math.sqrt(2*g*r)
    print("La velocidad de escape es de "+str(int(resultado))+" m/s" )
Escape()