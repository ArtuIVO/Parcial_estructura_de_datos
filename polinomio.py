from nudo import Node


class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo_termino = Node(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_termino
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_termino

        print("Polinomio actualizado:")
        self.mostrar_polinomio()

    def mostrar_polinomio(self):
        actual = self.cabeza
        polinomio_str = ""
        while actual:
            if actual.coeficiente != 0:
                if actual.coeficiente > 0 and len(polinomio_str) > 0:
                    polinomio_str += " + "
                polinomio_str += str(actual.coeficiente)
                if actual.exponente > 0:
                    polinomio_str += "x"
                    if actual.exponente > 1:
                        polinomio_str += "^" + str(actual.exponente)
            actual = actual.siguiente
        print(polinomio_str if polinomio_str else "0")

    def evaluar_polinomio(self, x):
        resultado = 0
        actual = self.cabeza
        while actual:
            resultado += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return resultado

    def sumar_polinomios(self, otro_polinomio):
        nuevo_polinomio = Polinomio()
        actual1 = self.cabeza
        actual2 = otro_polinomio.cabeza

        while actual1 and actual2:
            if actual1.exponente == actual2.exponente:
                nuevo_polinomio.agregar_termino(actual1.coeficiente + actual2.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
            elif actual1.exponente > actual2.exponente:
                nuevo_polinomio.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            else:
                nuevo_polinomio.agregar_termino(actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente

        while actual1:
            nuevo_polinomio.agregar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente

        while actual2:
            nuevo_polinomio.agregar_termino(actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente

        print("Polinomio suma:")
        nuevo_polinomio.mostrar_polinomio()
        return nuevo_polinomio

    def restar_polinomios(self, otro_polinomio):
        nuevo_polinomio = Polinomio()
        actual1 = self.cabeza
        actual2 = otro_polinomio.cabeza

        while actual1 and actual2:
            if actual1.exponente == actual2.exponente:
                nuevo_polinomio.agregar_termino(actual1.coeficiente - actual2.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
                actual2 = actual2.siguiente
            elif actual1.exponente > actual2.exponente:
                nuevo_polinomio.agregar_termino(actual1.coeficiente, actual1.exponente)
                actual1 = actual1.siguiente
            else:
                nuevo_polinomio.agregar_termino(-actual2.coeficiente, actual2.exponente)
                actual2 = actual2.siguiente

        while actual1:
            nuevo_polinomio.agregar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente

        while actual2:
            nuevo_polinomio.agregar_termino(-actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente

        print("Polinomio resta:")
        nuevo_polinomio.mostrar_polinomio()
        return nuevo_polinomio