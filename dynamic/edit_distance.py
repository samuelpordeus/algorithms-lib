#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def edit_distance(str1, str2, m, n):

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(edit_distance(str1, str2, m, n - 1),    # Insert
                   edit_distance(str1, str2, m - 1, n),    # Remove
                   edit_distance(str1, str2, m - 1, n - 1)    # Replace
                   )


class TestEditDistance(unittest.TestCase):

    def test_blabla(self):
        self.assertEqual(edit_distance('blabla', 'blablabla', 6, 9), 3)

    def test_null(self):
        self.assertEqual(edit_distance('blabla', '', 6, 0), 6)

    def test_diff(self):
        self.assertEqual(edit_distance('blablabla', 'kekkekkek', 9, 9), 9)

# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
