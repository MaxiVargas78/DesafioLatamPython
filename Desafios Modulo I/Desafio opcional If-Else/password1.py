password = input("Ingrese una clave de al menos seis digitos:")
if(len(password) < 6):
    if (password == "12345"):
        print("Su clave es incorrecta")
    else:
        print("Su clave debe ser mayor a seis digitos")
else:
    pass