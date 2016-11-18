#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w

def fractional_knapsack(W, items_list, n):

    # Sorting Item on basis of ration
    new_items_list = sorted(items_list, key=lambda item: item.weight)

    cur_weight = 0   # Current weight in knapsack
    final_value = 0.0    # Result

    for i in range(n):  # Looping through all Items

        # If adding Item won't overflow, add it completely
        if(cur_weight + new_items_list[i].weight <= W):
            cur_weight += new_items_list[i].weight
            final_value += new_items_list[i].value

        # If we can't add current Item, add fractional part of it
        else:
            remain = W - cur_weight
            final_value += new_items_list[i].value * \
                (remain / new_items_list[i].weight)
            break

    return final_value


class TestFractionalKnapsack(unittest.TestCase):

    def test_one(self):
        items_list = [Item(60, 10), Item(40, 10), Item(50, 30)]
        self.assertEqual(fractional_knapsack(50, items_list, 3), 150)

    def test_two(self):
        items_list = [Item(60, 10), Item(40, 10), Item(50, 30), Item(90, 20), Item(30, 50)]
        self.assertEqual(fractional_knapsack(100, items_list, 5), 258)

    def test_big_bag(self):
        items_list = [Item(30, 10), Item(90, 6), Item(50, 3), Item(90, 2), Item(30, 5)]
        self.assertEqual(fractional_knapsack(1000, items_list, 5), 290)

    def test_no_space(self):
        items_list = [Item(30, 20), Item(40, 50)]
        self.assertEqual(fractional_knapsack(10, items_list, 2), 15.0)



# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
