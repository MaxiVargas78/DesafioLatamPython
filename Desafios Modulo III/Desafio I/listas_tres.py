from listas_dos import *
from listas_uno import Autos

a = promedio()

i= 0
for i in range(len(Autos)):
    if ( Autos[i][1] > a):
        print(Autos[i][0])
    else:
        None

