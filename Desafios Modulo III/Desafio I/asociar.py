from velocidad import *

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
 17, 28, 14, 20, 24, 28, 26, 34, 34,
 46, 26, 36, 60, 80, 20, 26, 54, 32,
 40, 32, 40, 50, 42, 56, 76, 84, 36,
 46, 68, 32, 48, 52, 56, 64, 66, 54,
 70, 92, 93, 120, 85]

matrix = []
for lista in zip(velocidad, distancia):
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