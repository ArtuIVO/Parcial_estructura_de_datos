from polinomio import Polinomio
polinomio_a = Polinomio()
polinomio_b = Polinomio()
cons = 0

print("Bienvenido al programa de polinomios hecho por Arturo Alva 1525123")
while True:
    print("\n")
    print("Que desea hacer ?")
    print("1. Ingresar componentes a un polinomio ")
    print("2. Adición y sustraccion de un polinomio ")
    print("3. Evaluar polinomio ")
    print("4. Salir ")
    print("\n")

    datop = int(input())

    if datop == 1:
        print("De que grado sera su polinomio ?")
        a = int(input("Ingrese el gardo: "))


    elif datop == 2:
        pass
    elif datop == 3:
        pass
    elif datop == 4:
        print("\n")
        print(" Gracias por usar el programa ")
        break
    else:
        print(" Número del menú no existente, vuelva a intentarlo ")
        print("\n")
