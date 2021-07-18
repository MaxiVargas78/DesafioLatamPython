from sys import argv

def Mayor():
    x = float(argv[1])
    y = float(argv[2])
    z = float(argv[3])

    if x >= y and x >= z:
        print(int(x))
    elif y >= x and y >= z:
        print(int(y))
    elif z >= x and z >= y:
        print(int(z))
    else:
        print("variables incorrectas") 

Mayor()