diccionario1 = {}
def filter_dict(diccionario, parametro):
    for i in diccionario:
        if (diccionario[i] > parametro):
            diccionario1[i] = diccionario[i]
        else:
            None
    print(diccionario1)

filter_dict() #ingresar valores aqui de la forma (algo, algo1) 