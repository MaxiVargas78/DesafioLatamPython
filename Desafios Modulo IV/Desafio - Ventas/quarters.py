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

conver = list(ventas.items())
Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0

for i in range(len(conver)):
    if i < 3:
        Q1 += int(conver[i][1])
    elif i < 6:
        Q2 += int(conver[i][1])
    elif i < 9:
        Q3 += int(conver[i][1])
    elif i < 12:
        Q4 += int(conver[i][1])

quarters = { "Q1" : Q1, "Q2" : Q2, "Q3" : Q3, "Q4" : Q4}
print(quarters)