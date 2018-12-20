"""
Problema: https://github.com/testdouble/contributing-tests/wiki/Greeting-Kata
"""

from unittest import TestCase

from Greeting import Greeting

greeting = Greeting()


class AnalisadorDeString(TestCase):

    def testeGreetParaUmNome(self):
        self.assertEqual("Hello, Bob.", greeting.greet("Bob"))
        self.assertEqual("Hello, Kevin.", greeting.greet("Kevin"))

    def testeGreetParaUmaStringNull(self):
        self.assertEqual("Hello, my friend.", greeting.greet(None))
        self.assertEqual("Hello, my friend.", greeting.greet(""))

    def testeGreetParaTodasAsLetrasMaiusculas(self):
        self.assertEqual("HELLO JERRY!", greeting.greet("JERRY"))
        self.assertEqual("HELLO MARY!", greeting.greet("MARY"))

    def testeGreetParaEntradaDeDoisNomes(self):
        self.assertEqual("Hello, Jill and Jane.", greeting.greet(["Jill", "Jane"]))
        self.assertEqual("Hello, Mary and Jane.", greeting.greet(["Mary", "Jane"]))

    def testeGreetParaEntradaDeVariosNomes(self):
        self.assertEqual("Hello, Amy, Brian, and Charlotte.", greeting.greet(["Amy", "Brian", "Charlotte"]))
        self.assertEqual("Hello, Mary, Brian, and Charlotte.", greeting.greet(["Mary", "Brian", "Charlotte"]))

    def testeGreetParaEntradaDeVariosNomesVariados(self):
        self.assertEqual("Hello, Amy and Charlotte. AND HELLO BRIAN!", greeting.greet(["Amy", "BRIAN", "Charlotte"]))

    def testeGreetParaEntradaComVirgulaNosNomes(self):
        self.assertEqual("Hello, Bob, Charlie, and Dianne.", greeting.greet(["Bob", "Charlie, Dianne"]))
