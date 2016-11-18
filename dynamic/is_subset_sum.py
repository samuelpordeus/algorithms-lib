#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def is_subset_sum(set, total_sum):

    length_set = len(set)

    subset = [[x for x in range(length_set + 1)]
              for y in range(total_sum + 1)]        # Two-dimensional array

    for numb in range(0, length_set + 1):  # if sum is 0, true is returned
        subset[0][numb] = True

    # If sum isn't 0 and set is empty, the answer is false
    for numb in range(1, total_sum + 1):
        subset[numb][0] = False

    # Fill the table in botton up manner
    for i in range(1, total_sum + 1):
        for j in range(1, length_set + 1):
            subset[i][j] = subset[i][j - 1]

            if(i >= set[j - 1]):
                # Divide in two subproblems.
                subset[i][j] = subset[i][j] or subset[i - set[j - 1]][j - 1]

    return subset[total_sum][length_set]


class TestIsSubsetSum(unittest.TestCase):

    def test_selfnumber(self):
        self.assertEqual(is_subset_sum([3, 34, 4, 12, 5, 2], 12), True)

    def test_medium(self):
        self.assertEqual(is_subset_sum(
            [10, 300, 9080, 34, 704, 209, 340, 92], 10769), True)

    def test_big_small_numbers(self):
        self.assertEqual(is_subset_sum(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 200), True)

    def test_big_false(self):
        self.assertEqual(is_subset_sum(
            [30, 92, 41, 62, 555, 927, 39, 40, 93], 99999), False)

    def test_zero(self):
        self.assertEqual(is_subset_sum([0], 0), True)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
