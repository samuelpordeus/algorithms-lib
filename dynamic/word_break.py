#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def word_break(string, dicionario, cache=None):
    """Responsável por dividir uma string onde todas as palavras estão coladas
    sem espaço em uma frase usando uma lista de palavras conhecidas"""

    # Cria o cache caso não exista
    if not cache:
        cache = []

    # Caso não tenha string (o tamanho da string seja zero) então retorna falso
    if not string:
        return True

    if string in cache:
        return False

    # Para dada string processa várias substrings na procura por uma palavra
    # Ex.: string "testesistema" e dicionário [ "teste" ]
    # t -> False
    # te -> False
    # tes -> False
    # test -> False
    # teste -> True
    for i in range(0, len(string) + 1):
        # Caso funcione, continuamos de onde paramos
        if string[:i] in dicionario:
            resultado = word_break(string[i:], dicionario, cache)
            if resultado:
                return True

    cache.append(string)
    return False


class TestWordBreak(unittest.TestCase):
    dicionario = ["muito", "mui", "test", "and", "algo", "ritmo", "algoritmos",
                  "sistema", "word", "break", "palavra", "testando", "paladar", "erro",
                  "proposital"]

    def test_0(self):
        self.assertEqual(word_break("algoritmos", self.dicionario), True)

    def test_1(self):
        self.assertEqual(word_break(
            "testandoalgoritmos", self.dicionario), True)

    def test_2(self):
        self.assertEqual(word_break("sistemawordbreak", self.dicionario), True)

    def test_3(self):
        self.assertEqual(word_break(
            "testandoalgoritmo", self.dicionario), True)

    def test_4(self):
        self.assertEqual(word_break("testandoalgo", self.dicionario), True)

    def test_5(self):
        self.assertEqual(word_break("muitoritmofail", self.dicionario), False)

    def test_6(self):
        self.assertEqual(word_break("alpaladar", self.dicionario), False)

    def test_7(self):
        self.assertEqual(word_break("erropropozital", self.dicionario), False)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
