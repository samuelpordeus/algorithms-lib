#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def lcs(str1, str2, A, B):
    if A == 0 or B == 0:
        return 0
    elif str1[A - 1] == str2[B - 1]:
        return 1 + lcs(str1, str2, A - 1, B - 1)
    else:
        return max(lcs(str1, str2, A, B - 1), lcs(str1, str2, A - 1, B))


class TestLcs(unittest.TestCase):

    def test_small(self):
        self.assertEqual(lcs('ABC', 'AC', 3, 2), 2)

    def test_medium(self):
        self.assertEqual(lcs('AAAAACDHEFA', 'AKJFHAEJFHAAOFH', 11, 15), 5)

    def test_medium2(self):
        self.assertEqual(lcs('AAAACBABAJKCAB', 'CABCABCABA', 14, 10), 7)

    def test_diff(self):
        self.assertEqual(lcs('AAAAAAAAA', 'BBBBBBBBB', 9, 9), 0)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
