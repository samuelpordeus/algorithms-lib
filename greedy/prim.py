#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import collections
import heapq


def prim(vertices, edges):
        # Cria uma hash com listas dentro
    conections = collections.defaultdict(list)
    for edge in edges:
        # Adiciona as conexões de ida e de volta
        a, b, weight = edge
        conections[a].append((weight, a, b))
        conections[b].append((weight, b, a))

    mst = []
    used = set(vertices[0])
    usable = conections[vertices[0]][:]
    heapq.heapify(usable)

    while usable:
        weight, a, b = heapq.heappop(usable)
        if b not in used:
            used.add(b)
            mst.append((a, b, weight))

            for edge in conections[b]:
                if edge[2] not in used:
                    heapq.heappush(usable, edge)
    return mst


class TestPrim(unittest.TestCase):
    def test_1(self):
        result = prim(['A', 'B', 'C', 'D'], [
            ('A', 'B', 2),
            ('A', 'C', 1),
            ('C', 'D', 2),
            ('B', 'D', 4)
        ])

        self.assertEqual(result, [
            ('A', 'C', 1),
            ('A', 'B', 2),
            ('C', 'D', 2)])

    def test_2(self):
        result = prim(['A', 'B', 'C', 'D', 'E', 'F'], [
            ('A', 'B', 1),
            ('A', 'C', 5),
            ('A', 'D', 3),
            ('B', 'C', 4),
            ('B', 'D', 2),
            ('C', 'D', 1)
        ])

        self.assertEqual(result, [
            ('A', 'B', 1),
            ('B', 'D', 2),
            ('D', 'C', 1)])

    def test_3(self):
        result = prim(['A', 'B', 'C', 'D', 'E', 'F'], [
            ('A', 'B', 1),
            ('A', 'C', 2),
            ('A', 'D', 6),
            ('B', 'D', 4),
            ('B', 'F', 10),
            ('C', 'E', 7),
            ('D', 'F', 5),
            ('D', 'E', 6),
            ('E', 'F', 1),
        ])

        self.assertEqual(result, [
            ('A', 'B', 1),
            ('A', 'C', 2),
            ('B', 'D', 4),
            ('D', 'F', 5),
            ('F', 'E', 1)])

    def test_4(self):
        result = prim(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [
            ('A', 'B', 1),
            ('A', 'C', 6),
            ('B', 'E', 10),
            ('B', 'F', 6),
            ('C', 'E', 15),
            ('C', 'D', 8),
            ('D', 'E', 16),
            ('D', 'H', 20),
            ('E', 'F', 7),
            ('E', 'H', 10),
            ('E', 'G', 9),
            ('E', 'I', 7),
            ('F', 'G', 20),
            ('G', 'I', 6),
            ('H', 'I', 7),
        ])

        self.assertEqual(result, [
            ('A', 'B', 1),
            ('A', 'C', 6),
            ('B', 'F', 6),
            ('F', 'E', 7),
            ('E', 'I', 7),
            ('I', 'G', 6),
            ('I', 'H', 7),
            ('C', 'D', 8)])

# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
