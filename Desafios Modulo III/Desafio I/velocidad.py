import pandas as pd

data = pd.read_csv("cars.csv")
vel = []
distancia = []

for j in range(len(data)):
    vel.append(data["speed"].values[j])
    distancia.append(data["dist"].values[j])

def promedio(i):
    suma = 0 
    for x in i:
        suma += x
    media = suma/len(i)
    #print("Velocidad promedio es: "+str(media)) #para revisar el resultado descomente esta linea
    return media

promedio(vel)