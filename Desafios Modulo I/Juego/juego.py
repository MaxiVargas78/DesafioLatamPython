from random import randint
from sys import argv

piedra = str("piedra")
papel = str("papel")
tijera = str("tijera")
valores = randint(1,3)
entrada = str(argv[1])

def Juego():
    if entrada == piedra or entrada == papel or entrada == tijera:
        if (valores==1): 
            if (entrada == papel):
                print ("Computador juega piedra")
                print ("GANA USER")
            elif( entrada == piedra):
                print("Computador juega piedra")
                print ("HAY EMPATE")
            elif( entrada == tijera):
                print("Computador juega piedra")
                print ("GANA PC")
        elif (valores==2): 
            if (entrada == papel):
                print ("Computador juega papel") 
                print ("HAY EMPATE")
            elif( entrada == piedra):
                print("Computador juega papel") 
                print ("GANA PC")
            elif( entrada == tijera):
                print("Computador juega papel") 
                print ("GANA USER ")
        else:
            if (entrada == papel):
                print ("Computador juega tijera")
                print("GANA PC")
            elif( entrada == piedra):
                print("Computador juega tijera ")
                print(" GANA USER")
            elif( entrada == tijera):
                print("Computador juega tijera ")
                print(" HAY EMPATE ")
    else:
        print("Argumento invalido: Debe ser piedra, papel o tijera.")

Juego()
