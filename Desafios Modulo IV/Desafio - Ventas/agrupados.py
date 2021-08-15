ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

dicci = []
dicci1 = {}
for i in ventas:
    dicci.append(ventas[i])

for j in dicci:
    if j in dicci1:
        dicci1[j] += 1
    else:
        dicci1[j] = 1

print(dicci1)