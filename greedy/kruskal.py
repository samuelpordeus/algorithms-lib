#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


def find(vertice, parents):
    if parents[vertice] != vertice:
        parents[vertice] = find(parents[vertice], parents)
    return parents[vertice]


def union(a, b, parents, ranks):
    rootA = find(a, parents)
    rootB = find(b, parents)
    if rootA != rootB:
        if ranks[rootA] > ranks[rootB]:
            parents[rootB] = rootA
        else:
            parents[rootA] = rootB
            if ranks[rootA] == ranks[rootB]:
                ranks[rootB] += 1


def kruskal(vertices, edges):
    parents = {}
    ranks = {}

    for vertice in vertices:
        parents[vertice] = vertice
        ranks[vertice] = 0

    # Realiza sort das ligações entre os vertices usando o peso delas como
    # atributo
    edges.sort(key=lambda edge: edge[2])

    mst = set()
    for edge in edges:
        a, b, weight = edge
        if find(a, parents) != find(b, parents):
            union(a, b, parents, ranks)
            mst.add(edge)

    return mst


class TestKruskal(unittest.TestCase):
    def test_1(self):
        result = kruskal(['A', 'B', 'C', 'D'], [
            ('A', 'B', 2),
            ('A', 'C', 1),
            ('C', 'D', 2),
            ('B', 'D', 4)
        ])

        self.assertEqual(result, set([
            ('A', 'B', 2),
            ('A', 'C', 1),
            ('C', 'D', 2)
        ]))

    def test_2(self):
        result = kruskal(['A', 'B', 'C', 'D', 'E', 'F'], [
            ('A', 'B', 1),
            ('A', 'C', 5),
            ('A', 'D', 3),
            ('B', 'C', 4),
            ('B', 'D', 2),
            ('C', 'D', 1)
        ])

        self.assertEqual(result, set([
            ('B', 'D', 2),
            ('A', 'B', 1),
            ('C', 'D', 1)
        ]))

    def test_3(self):
        result = kruskal(['A', 'B', 'C', 'D', 'E', 'F'], [
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

        self.assertEqual(result, set([
            ('A', 'B', 1),
            ('A', 'C', 2),
            ('B', 'D', 4),
            ('D', 'F', 5),
            ('E', 'F', 1),
        ]))

    def test_4(self):
        result = kruskal(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [
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

        self.assertEqual(result, set([
            ('B', 'F', 6),
            ('E', 'I', 7),
            ('A', 'C', 6),
            ('E', 'F', 7),
            ('C', 'D', 8),
            ('A', 'B', 1),
            ('G', 'I', 6),
            ('H', 'I', 7),
        ]))

# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
