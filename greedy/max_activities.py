#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest


def max_activities(s, f):
    n = len(f)
    answer = []

    # The first activity is always selected
    i = 0
    answer.append(i),

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            answer.append(j),
            i = j
    return answer


class TestMaxActivities(unittest.TestCase):

    def test_one(self):
        s = [1, 3, 0, 5, 8, 5]
        f = [2, 4, 6, 7, 9, 9]
        self.assertEqual(max_activities(s, f), [0, 1, 3, 4])

    def test_two(self):
        s = [3, 1, 5, 3, 8, 3, 9, 10, 20, 3]
        f = [2, 2, 9, 2, 9, 3, 5, 6, 7, 2]
        self.assertEqual(max_activities(s, f), [0, 0, 2, 6, 7, 8])

    def test_steps(self):
        s = [3, 1, 5, 3]
        f = [0, 10, 5, 10]
        self.assertEqual(max_activities(s, f), [0, 0, 1])


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
