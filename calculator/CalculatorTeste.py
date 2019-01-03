"""
Problema: http://osherove.com/tdd-kata-1/
"""

from unittest import TestCase

from Calculator import Calculator

calculator = Calculator()


class CalculatorTeste(TestCase):

    def testeAddComNenhumNumero(self):
        self.assertEqual(0, calculator.add(""))

    def testeAddComUmNumero(self):
        self.assertEqual(0, calculator.add("0"))
        self.assertEqual(5, calculator.add("5"))

    def testeAddComDoisNumeros(self):
        self.assertEqual(2, calculator.add("0,2"))
        self.assertEqual(5, calculator.add("3,2"))

    def testeAddComVariosNumeros(self):
        self.assertEqual(10, calculator.add("0,2,2,2,4"))
        self.assertEqual(11, calculator.add("0,2,5,4"))

    def testeAddComVariosNumerosEPulandoLinha(self):
        self.assertEqual(10, calculator.add("0\n2,2,2,4"))
