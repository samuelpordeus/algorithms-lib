#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from heapq import heappush, heappop


def shortest_path(graph, start):
    if start not in graph:
        return "Bad input!"
    # Create answer's list
    answer_list = [None] * len(graph)
    queue = [(0, start)]
    # Use heap queue to check the unvisited graphs
    while queue:
        path_len, v = heappop(queue)
        if answer_list[v] is None:
            answer_list[v] = path_len
            for weight, edge_len in graph[v].items():
                if answer_list[weight] is None:
                    heappush(queue, (path_len + edge_len, weight))
    return [0 if not x else x for x in answer_list]


class TestShortestPath(unittest.TestCase):

    def test_one(self):
        graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
        self.assertEqual(shortest_path(graph, 2), [8, 6, 0, 10])

    def test_one_vertix(self):
        graph = {0: {1: 100}, 1: {0: 100}}
        self.assertEqual(shortest_path(graph, 0), [0, 100])

    def test_triangle(self):
        graph = {0: {1: 100, 2: 100}, 1: {0: 100, 2: 100}, 2: {0: 100, 1: 100}}
        self.assertEqual(shortest_path(graph, 0), [0, 100, 100])

    def test_empty_graph(self):
        graph = {}
        self.assertEqual(shortest_path(graph, None), 'Bad input!')


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
