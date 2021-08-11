from velocidad import *

matrix = []
for lista in zip(vel, distancia):
    matrix.append(lista)

matrix1 = []
for j in matrix:
    matrix1.append(j[0])

matrix2 = []
for k in matrix:
    matrix2.append(k[1])

a = promedio(matrix1)
b = promedio(matrix2)

count = 0
for i in range(len(matrix1)):
    if (matrix1[i] < a):
        count += 1
    else:
        None

count2 = 0
for i in range(len(matrix1)):
    if (matrix1[i] < a and matrix2[i] > b):
        count2 += 1
    else:
        None

count3 = 0
for i in range(len(matrix1)):
    if (matrix1[i] > a):
        count3 += 1
    else:
        None

count4 = 0
for i in range(len(matrix1)):
    if (matrix1[i] > a and matrix2[i] < b):
        count4 += 1
    else:
        None

print("Velocidad bajo el promedio: "+str(count))
print("Velocidad bajo el promedio y distancia sobre el promedio: "+str(count2))
print("Velocidad sobre el promedio: "+str(count3))
print("Velocidad sobre el promedio y distancia bajo el promedio: "+str(count4))