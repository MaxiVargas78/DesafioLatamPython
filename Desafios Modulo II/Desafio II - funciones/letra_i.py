def letra_i(n):
    if n % 2 == 0:
        for i in range(1):
                for j in range(n + 1):
                    print("* ", end="")
                print()

        for i in range(n - 1):
            for j in range((n) // 2):
                print("  ", end="")
            for j in range(1):
                print("* ", end="")
            print()

        for i in range(1):
                for j in range(n +1):
                    print("* ", end="")
                print()
    else:
        for i in range(1):
            for j in range(n):
                    print("* ", end="")
            print()

        for i in range(n - 1):
            for j in range((n - 1) // 2):
                print("  ", end="")
            for j in range(1):
                print("* ", end="")
            print()

        for i in range(1):
                for j in range(n):
                    print("* ", end="")
                print()
        
letra_i() # Ingresar el valor dentro de los parentesis