#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def max_knapsack(cap, weight, value, n):
    if n == 0 or cap == 0:
        return 0
    if (weight[n - 1] > cap):
        return max_knapsack(cap, weight, value, n - 1)
    else:
        return max(value[n - 1] + max_knapsack(cap - weight[n - 1], weight, value, n - 1),
                   max_knapsack(cap, weight, value, n - 1))


class TestMaxKnapsack(unittest.TestCase):

    def test_one(self):
        self.assertEqual(max_knapsack(
            50, [10, 20, 30], [60, 100, 120], 3), 220)

    def test_two(self):
        self.assertEqual(max_knapsack(
            10, [5, 4, 6, 3], [10, 40, 30, 50], 4), 90)

    def test_zero(self):
        self.assertEqual(max_knapsack(100, 0, 0, 0), 0)

    def test_heavy(self):
        self.assertEqual(max_knapsack(
            100, [500, 300, 200, 900], [10, 20, 30, 40], 4), 0)

# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
