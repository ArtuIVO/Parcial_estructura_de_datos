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
