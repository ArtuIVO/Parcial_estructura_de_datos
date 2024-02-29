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
        polinomio = input("Ingrese el nombre del polinomio (a o b): ").strip().lower()
        coeficiente = float(input("Ingrese el coeficiente del término: "))
        exponente = int(input("Ingrese el exponente del término: "))
        if polinomio == "a":
            polinomio_a.agregar_termino(coeficiente, exponente)
            print(polinomio_a)
        elif polinomio == "b":
            polinomio_b.agregar_termino(coeficiente, exponente)
            print(polinomio_b)
        else:
            print("Polinomio no válido.")
    elif datop == 2:
        print("Que desea hacer, sumar (s) o restar (r)")
        b = input().lower()

        if b == "s":
            print("Sumar polinomios:")
            print("Polinomio A:")
            polinomio_a.mostrar_polinomio()
            print("Polinomio B:")
            polinomio_b.mostrar_polinomio()

            resultado_suma = polinomio_a.sumar_polinomios(polinomio_b)
            print("Resultado de la suma:")
            resultado_suma.mostrar_polinomio()
        elif b == "r":

            print("Restar polinomios:")
            resultado_resta = polinomio_a.restar_polinomios(polinomio_b)
            print("Resultado de la resta:")
            resultado_resta.mostrar_polinomio()
        else:
            print("Dato incorrecto")
    elif datop == 3:
        polinomio = input("Ingrese el nombre del polinomio (a o b) que desea evaluar: ").strip().lower()
        valor_x = float(input("Ingrese el valor de x: "))
        if polinomio == "a":
            resultado = polinomio_a.evaluar_polinomio(valor_x)
            print(f"Resultado de evaluar polinomio 'a': {resultado}")
        elif polinomio == "b":
            resultado = polinomio_b.evaluar_polinomio(valor_x)
            print(f"Resultado de evaluar polinomio 'b': {resultado}")
        else:
            print("Polinomio no válido.")
    elif datop == 4:
        print("\n")
        print(" Gracias por usar el programa ")
        break
    else:
        print(" Número del menú no existente, vuelva a intentarlo ")
        print("\n")
