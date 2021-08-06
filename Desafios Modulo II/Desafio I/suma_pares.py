sumar = int(input("ingresa un valor para sumatoria: "))
sumador = 0
for i in range(sumar + 1):
    if i%2==0 and i!=0:
        sumador += i
        i +=1
    else:
        None
print("La sumatoria tiene un valor de: "+str(sumador))