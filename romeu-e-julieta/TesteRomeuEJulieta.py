"""
Problema:
    Receber um numero como entrada
    caso:
        X % 3 -> Queijo
        X % 5 -> Goiabada
        X % 3 and X % 5 -> Romeu e Julieta
"""
from unittest import TestCase

from app import romeu_julieta


class TesteRomeuEJulieta(TestCase):

    def teste_retorna_queijo_quando_input_for_mult_3(self):
        valores_de_entrada = [3, 12, 18]
        for valor in valores_de_entrada:
            self.assertEqual(romeu_julieta(valor), "Queijo")

    def teste_retorna_goiabada_quando_input_for_mult_5(self):
        valores_de_entrada = [5, 20, 25, 40]
        for valor in valores_de_entrada:
            self.assertEqual(romeu_julieta(valor), "Goiabada")

    def teste_retorna_romeu_e_julieta_quando_input_for_mult_15(self):
        valores_de_entrada = [15, 30, 45, 90]
        for valor in valores_de_entrada:
            self.assertEqual(romeu_julieta(valor), "Romeu e Julieta")
