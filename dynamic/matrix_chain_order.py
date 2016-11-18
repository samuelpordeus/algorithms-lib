#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import unittest


def matrix_chain_order(arr, n):

    # One extra row and one extra column are allocated in matrix
    matrix = [[0 for x in range(n)] for x in range(n)]

    # Cost is zero when multiplying one matrix.
    for i in range(1, n):
        matrix[i][i] = 0

    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            matrix[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost/scalar multiplications
                q = matrix[i][k] + matrix[k + 1][j] + \
                    arr[i - 1] * arr[k] * arr[j]
                if q < matrix[i][j]:
                    matrix[i][j] = q

    return matrix[1][n - 1]


class TestMatrixChainOrder(unittest.TestCase):

    def test_small(self):
        self.assertEqual(matrix_chain_order([1, 2, 3, 4], 4), 18)

    def test_medium(self):
        self.assertEqual(matrix_chain_order([40, 20, 30, 10, 30], 5), 26000)

    def test_medium2(self):
        self.assertEqual(matrix_chain_order([10, 20, 30, 40, 30], 5), 30000)

    def test_medium3(self):
        self.assertEqual(matrix_chain_order([10, 20, 30], 3), 6000)

# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
