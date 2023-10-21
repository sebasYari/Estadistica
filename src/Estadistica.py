from math import sqrt


class ExceptionDatos(Exception):
    pass


class Estadistica:

    def __init__(self, numeros=None):
        if numeros is not None:
            self.__numeros = self.validarNumeros(numeros)
        else:
            self.__numeros = []

    def validarNumeros(self, numeros):
        if numeros is not None:
            for numero in numeros:
                if not isinstance(numero, int) and not isinstance(numero, float):
                    raise ValueError
            return numeros
        else:
            raise ExceptionDatos

    @property
    def numeros(self):
        return self.__numeros

    @numeros.setter
    def numeros(self, numeros):
        try:
            self.__numeros = self.validarNumeros(numeros)
        except ValueError as e:
            self.__numeros = []

    def desviacion_estandar(self):
        media = self.calcular_media()
        suma = 0
        for valor in self.__numeros:
            suma += (valor - media) ** 2
        radicando = suma / (len(self.__numeros) - 1)
        return sqrt(radicando)

    def calcular_media(self):
        if len(self.__numeros) > 0:
            suma = 0
            for valor in self.__numeros:
                suma += valor
            return suma / len(self.__numeros)
        else:
            raise ExceptionDatos

    def __str__(self):
        return self.__numeros

if __name__ == "__main__":
    try:
        datos = [7, 3, 13, 17, 10, 8, 12, 9]
        estadistica = Estadistica(datos)
        print(estadistica.numeros)
        estadistica.numeros = [7, 3, 13]
        print(estadistica.numeros)
        print(estadistica.desviacion_estandar())
    except ExceptionDatos:
        print("Sin datos")





