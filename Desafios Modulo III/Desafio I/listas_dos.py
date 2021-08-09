from listas_uno import Autos

def promedio():
    suma = 0 
    for i in range(len(Autos)):
       suma += Autos[i][1]
    promedy = suma/len(Autos)
    return promedy

promedio()
#print("Velocidad promedio es: "+str(promedio())) #para revisar el resultado descomente esta linea