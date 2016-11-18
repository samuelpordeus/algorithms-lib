#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def binomial_coefficient(n, k):

    # Declaring an empty array
    C = [0 for i in range(k + 1)]
    C[0] = 1

    for i in range(1, n + 1):

        # Compute next row of pascal triangle using the previous row
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j - 1]
            j -= 1

    return C[k]


def call_binomial_coefficient(n, k):
    print("Value of C(%d,%d) is %d" % (n, k, binomial_coefficient(n, k)))


class TestBinomialCoefficient(unittest.TestCase):

    def test_52(self):
        self.assertEqual(binomial_coefficient(5, 2), 10)

    def test_106(self):
        self.assertEqual(binomial_coefficient(10, 6), 210)

    def test_137(self):
        self.assertEqual(binomial_coefficient(13, 7), 1716)

    def test_99(self):
        self.assertEqual(binomial_coefficient(9, 9), 1)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
