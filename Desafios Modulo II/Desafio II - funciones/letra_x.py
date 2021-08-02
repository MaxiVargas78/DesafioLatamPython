
def letra_x(n):
    if n % 2 == 0:
        for i in range(n):
            for j in range(n + 1):
                if i == j or i+j == n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    else:
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        

letra_x(6) # Ingresar el valor dentro de los parentesis