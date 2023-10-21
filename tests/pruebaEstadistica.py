import math
import unittest

from src.Estadistica import Estadistica, ExceptionDatos


class PruebaEstadistica(unittest.TestCase):
    def setUp(self):
        self.estadistica = Estadistica([])

    def tearDown(self):
        self.estadistica = None

    def test_media_vacio_retornaExcepcion(self):
        self.estadistica.numeros = []
        with self.assertRaises(ExceptionDatos):
            self.estadistica.calcular_media()

    def test_media_noNumero_retornaExcepcion(self):
        self.estadistica.numeros = [4, 5, "a", 10]
        with self.assertRaises(ExceptionDatos):
            self.estadistica.calcular_media()

    def test_media_nNumeros_retornaMedia(self):
        # Arrange
        self.estadistica.numeros = [15.62, 15.9, 14.5]
        resultadoEsperado = 15.340

        # Do
        resultadoActual = self.estadistica.calcular_media()

        # Assert
        self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=5)

    def test_media_nCasosNumeros_retornaMedia(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "datos": [15.82], "media": 15.820, "desvstd": 0.000},
            {"Case": "Caso 02", "datos": [15.62, 15.9], "media": 15.760, "desvstd": 0.140},
            {"Case": "Caso 03", "datos": [15.62, 15.9, 14.5], "media": 15.340, "desvstd": 0.605},
            {"Case": "Caso 04", "datos": [15, 16.06, 15.14, -20, 17.25, 14.37, 14.28], "media": 10.300,
             "desvstd": 12.407},
            {"Case": "Caso 05", "datos": [0, 0, 0, 0, 0, 0, 0], "media": 0.000, "desvstd": 0.000},
            {"Case": "Caso 06", "datos": [-15, 16.06, 15.14, -20, -17.25, 14.37, 14.28], "media": 1.086,
             "desvstd": 16.088},
        )
        for item in items:
            with self.subTest(item["Case"]):
                self.estadistica.numeros = item["datos"]
                resultadoEsperado = item["media"]

                # Do
                resultadoActual = self.estadistica.calcular_media()

                # Assert
                self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=3)

    def test_desviacion_estandar_nCasosNumeros_retornaDesviacionEstandar(self):
        # Arrange
        items = (
            {"Case": "Caso 01", "datos": [15.82], "media": 15.820, "desvstd": 0.000},
            {"Case": "Caso 02", "datos": [15.62, 15.9], "media": 15.760, "desvstd": 0.140},
            {"Case": "Caso 03", "datos": [15.62, 15.9, 14.5], "media": 15.340, "desvstd": 0.605},
            {"Case": "Caso 04", "datos": [15, 16.06, 15.14, -20, 17.25, 14.37, 14.28], "media": 10.300,
             "desvstd": 12.407},
            {"Case": "Caso 05", "datos": [0, 0, 0, 0, 0, 0, 0], "media": 0.000, "desvstd": 0.000},
            {"Case": "Caso 06", "datos": [-15, 16.06, 15.14, -20, -17.25, 14.37, 14.28], "media": 1.086,
             "desvstd": 16.088},
        )
        for item in items:
            with self.subTest(item["Case"]):
                self.estadistica.numeros = item["datos"]
                resultadoEsperado = item["desvstd"]

                # Do
                resultadoActual = self.estadistica.desviacion_estandar()

                # Assert
                self.assertAlmostEqual(resultadoActual, resultadoEsperado, places=3)
