import getpass

password = getpass.getpass("Ingrese password: ").lower()
iterador = 0
n = len(password)

for i in range(n):
    for j in range(25):
        if (list(password)[i]==chr(97)):
            iterador += 1
            break
        else:
            iterador +=1
print (str(iterador)+" intentos")

