#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from collections import namedtuple
from itertools import permutations


dimension = namedtuple("Dimension", "height length width")

# Gera dimensões usando como base permutações das
# dimensões com comprimento maior que altura


def rotations(dimensions):
    rotations = []
    for dim in dimensions:
        # Permuta
        for (height, length, width) in permutations((dim.height, dim.length, dim.width)):
            if length >= width:
                rotations.append(dimension(height, length, width))
    return rotations


def box_stack(dimensions):
    # Ordena as caixas com base nas dimensões
    boxes = sorted(
        rotations(dimensions),
        key=lambda dim: dim.length * dim.width,
        reverse=True)

    T = [rotation.height for rotation in boxes]
    R = [i for i in range(len(boxes))]

    for i in range(1, len(boxes)):
        for j in range(0, i):
            if (boxes[i].length < boxes[j].length
                    and boxes[i].width < boxes[j].width):
                height = T[j] + boxes[i].height
                if height > T[i]:
                    T[i] = height
                    R[i] = j

    return max(T)


class TestBoxStack(unittest.TestCase):
    def test_1(self):
        self.assertEqual(box_stack([
            dimension(5, 3, 5),
            dimension(8, 2, 6),
            dimension(7, 6, 8),
            dimension(5, 8, 4),
            dimension(5, 7, 5),
        ]), 22)

    def test_2(self):
        self.assertEqual(box_stack([
            dimension(5, 5, 1),
            dimension(8, 8, 2),
            dimension(7, 4, 8),
            dimension(1, 8, 3),
            dimension(8, 2, 10),
        ]), 22)

    def test_3(self):
        self.assertEqual(box_stack([
            dimension(2, 1, 4),
            dimension(7, 2, 7),
            dimension(5, 2, 8),
            dimension(3, 6, 3),
            dimension(3, 3, 3),
        ]), 17)

    def test_4(self):
        self.assertEqual(box_stack([
            dimension(9, 3, 3),
            dimension(8, 8, 6),
            dimension(5, 7, 1),
            dimension(9, 9, 9),
            dimension(2, 7, 1),
        ]), 34)

    def test_5(self):
        self.assertEqual(box_stack([
            dimension(1, 1, 1),
            dimension(8, 2, 1),
            dimension(6, 4, 2),
            dimension(5, 5, 5),
            dimension(3, 1, 5),
        ]), 19)


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
