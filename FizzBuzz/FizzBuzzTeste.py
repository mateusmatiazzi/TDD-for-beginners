"""
Problema: http://codingdojo.org/kata/FizzBuzz/
"""
from unittest import TestCase

from PreditorFizzBuzz import PreditorFizzBuzz

preditorFizzBuzz = PreditorFizzBuzz()


class FizzBuzzTeste(TestCase):

    def testePreditorFizzBuzzPara1NumeroMultiplo(self):
        self.assertEqual("1", preditorFizzBuzz.predizPara(1))
        self.assertEqual("2", preditorFizzBuzz.predizPara(2))
        self.assertEqual("Fizz", preditorFizzBuzz.predizPara(3))
        self.assertEqual("Buzz", preditorFizzBuzz.predizPara(20))
        self.assertEqual("FizzBuzz", preditorFizzBuzz.predizPara(15))

    def testePreditorParaNumerosInseridosNoNumeroASerPredito(self):
        self.assertEqual("Fizz", preditorFizzBuzz.predizPara(31))
        self.assertEqual("Fizz", preditorFizzBuzz.predizPara(83))
        self.assertEqual("Fizz", preditorFizzBuzz.predizPara(37))
        self.assertEqual("Buzz", preditorFizzBuzz.predizPara(50))
