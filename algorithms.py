#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, 'greedy')

# Algoritmos gulosos
# Samuel
from shortest_path import shortest_path
from colored_graphs import colored_graphs
# Elcius
from max_activities import max_activities
from fractional_knapsack import Item, fractional_knapsack
# Victor
from kruskal import kruskal
from prim import prim

sys.path.insert(0, 'dynamic')

# Algoritmos dinâmicos
# Samuel
from lcs import lcs
from max_knapsack import max_knapsack
from edit_distance import edit_distance
# Elcius
from is_subset_sum import is_subset_sum
from matrix_chain_order import matrix_chain_order
from binomial_coefficient import binomial_coefficient
# Victor
from word_break import word_break
from box_stacking import box_stack
from coin_change import coin_change

sys.path.insert(0, 'heuristic/algorithms')

#Metaheuristicas
#Samuel
import grasp

# Victor
import tabu_search

#Elcius
import vns