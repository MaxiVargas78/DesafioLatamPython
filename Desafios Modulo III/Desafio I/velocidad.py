velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
 11, 11, 12, 12, 12, 12, 13, 13,
 13, 13, 14, 14, 14, 14, 15, 15,
 15, 16, 16, 17, 17, 17, 18, 18,
 18, 18, 19, 19, 19, 20, 20, 20,
 20, 20, 22, 23, 24, 24, 24, 24, 25]

def promedio(i):
    suma = 0 
    for x in i:
        suma += x
    media = suma/len(i)
    #print("Velocidad promedio es: "+str(media)) #para revisar el resultado descomente esta linea
    return media

promedio(velocidad)