#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest


def coin_change_internal(quantidade, moedas, cache):
    """Função interna para calculo de troco"""
    # Caso a quantidade seja zero, retorna zero, terminando a recursão
    if quantidade == 0:
        return 0

    # Pega o resultado do cache caso ele exista
    if quantidade in cache:
        return cache[quantidade]

    # O número inicial de possibilidade é o maior valor que um inteiro suporta
    possibilidade = sys.maxsize

    # Procura moedas menores que a quantidade
    for moeda in moedas:
        if moeda <= quantidade:
            # Caso o resultado seja válido (não seja sys.maxsize), então
            # verifica se ele ainda é menor que o último resultado obtido para
            # esse problelam
            resultado = coin_change_internal(quantidade - moeda, moedas, cache)
            if resultado != sys.maxsize and (resultado + 1) < possibilidade:
                possibilidade = resultado + 1

    # Retorna o número de posibilidades
    cache[quantidade] = possibilidade
    return possibilidade


def coin_change(quantidade, moedas):
    """Calcula um troco para dada quantidade utilizando as moedas fornecidas"""
    cache = {}

    # Pega o resultado e verifica se ele é válido
    resultado = coin_change_internal(quantidade, moedas, cache)
    if resultado == sys.maxsize:
        return False

    # Retorna o resultado
    return resultado


class TestCoinCharge(unittest.TestCase):

    def test_50(self):
        self.assertEqual(coin_change(50, [5, 10, 50]), 1)

    def test_100(self):
        self.assertEqual(coin_change(50, [5, 10, 50]), 2)

    def test_75(self):
        self.assertEqual(coin_change(75, [5, 10, 50]), 4)

    def test_100(self):
        self.assertEqual(coin_change(100, [3, 7]), 16)

    def test_1000(self):
        self.assertEqual(coin_change(1000, [9, 1]), 112)

    def test_789(self):
        self.assertEqual(coin_change(789, [8, 5, 3]), 99)

    def test_failue(self):
        self.assertEqual(coin_change(789, [2, 4, 8]), False)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
