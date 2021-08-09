from listas_uno import Autos
from listas_dos import *

a = promedio()
Autos1 = []

for j in Autos:
    Autos1.append(j[1])

i = 0
for i in range(len(Autos1)):
    floating = filter(lambda x: x > a, Autos1)
    
print(list(floating))