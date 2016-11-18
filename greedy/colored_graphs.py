#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

colors_of_graphs = {}


def picking_color(graph_dict, graph, color):
    for graph in graph_dict.get(graph):
        color_of_neighbor = colors_of_graphs.get(graph)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_graph(graphs, graph, colors):
    for color in colors:
        if picking_color(graphs, graph, color):
            return color


def colored_graphs(graphs, colors):
    graphs_list = []
    for graph in graphs:
        colors_of_graphs[graph] = get_color_for_graph(graphs, graph, colors)
    for graph in graphs:
        graphs_list.append(colors_of_graphs[graph])
    return graphs_list


class TestColorOfGraphs(unittest.TestCase):

    def test_normal(self):
        colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
        graph_dict = {0: [1, 2, 5], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [1, 2], 4: [1, 2], 5: [0]}
        self.assertEqual(colored_graphs(graph_dict, colors), ['Red', 'Blue', 'Green', 'Red', 'Red', 'Blue'])
    def test_one_color(self):
        colors = ['Red']
        graph_dict = {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4, 5], 3: [1, 2], 4: [1, 2], 5: [2]}
        self.assertEqual(colored_graphs(graph_dict, colors), ['Red', None, None, 'Red', 'Red', 'Red'])
    def test_no_color_broke_graph(self):
        colors = []
        graph_dict = {0: [1, 2, 5, 3], 1: [0, 2], 2: 4, 3: 1, 4: 1, 5: [0]}
        self.assertEqual(colored_graphs(graph_dict, colors), [None, None, None, None, None, None])


# Executa a suite de teste
if __name__ == '__main__':
    unittest.main()
