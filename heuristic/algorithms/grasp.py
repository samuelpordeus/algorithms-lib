'''
Strategy
The strategy is to iteratively sample stochastically greedy solutions and then use a local search heuristic to refine them
to a local optima. It builds a Restricted Candidate List (RCL) that constrains the features of a solution that may be selected from each
cycle.

Heuristics
The RCL may be constrained by an explicit size, or by using a threshold [0, 1] on the cost of adding each feature
to the current candidate solution.

The threshold defines the amount of greediness of the construction mechanism, where values close to 0 may be too greedy, and values
close to 1 may be too generalized.

As an alternative to using a threshold, the RCL can be constrained to the top n% of candidate features that may be
selected from each construction cycle.

'''
from algorithms.utilities import stochasticTwoOpt, tourCost, euclideanDistance
import random
import time

def constructGreedySolution(perm, alpha):
    candidate = {}
    # Seleciona um ponto da lista aleatoriamente
    problemSize = len(perm)
    candidate["permutation"] = [perm[random.randrange(0, problemSize)]]
    # Enquanto o tamanho do candidato não for igual ao tamanho da permutação
    while len(candidate["permutation"]) < problemSize:
        # Pega todos os pontos, exceto os já presentes na solução candidata
        candidates = [item for item in perm if item not in candidate["permutation"]]
        # Calcula o custo de adicionar uma feature à solução
        # A 'feature' é definida por quão longe os outros pontos estão do último elemento da lista de candidatos
        costs = []
        candidateSize = len(candidate["permutation"])
        for item in candidates:
            costs.append(euclideanDistance(candidate["permutation"][candidateSize - 1], item))
        # Determina o menor e o maior custo do determinado set
        rcl, maxCost, minCost = [], max(costs), min(costs)
        # Construimos o RCL da seguinte maneira:
        # Adicionamos o que for menor ou igual ao mínimo + o custo da feature pela fórmula da RCL
        # Quanto menor a distância aqui, menor o custo final do algoritmo
        # Custo de cada Feature:
        for index, cost in enumerate(costs):  # Para conseguir o index e o item enquanto faz o loop
            # IF Fcurrent <= Fmin + alpha * (Fmax-Fmin) THEN
            if (cost <= minCost + alpha * (maxCost - minCost)):
                # Adiciona ao RCL
                rcl.append(candidates[index])
        # Seleciona feature aleatório do RCL e adiciona à solução
        candidate["permutation"].append(rcl[random.randrange(0, len(rcl))])

    # Calcula o custo final antes de retornar a solução candidata
    candidate["cost"] = tourCost(candidate["permutation"])
    return candidate


def localSearch(best, maxIter, timeLimit):
    t_end = time.time() + timeLimit
    count = 0
    while count < maxIter and time.time() < t_end:
        candidate = {}
        candidate["permutation"] = stochasticTwoOpt(best["permutation"])
        candidate["cost"] = tourCost(candidate["permutation"])
        if candidate["cost"] < best["cost"]:
            best, count = candidate, 0
        else:
            count += 1

    return best


def search(points, maxIterations, maxNoImprove, threshold, timeLimit):
    t_end = time.time() + timeLimit
    best = None
    while maxIterations > 0 and time.time() < t_end:
        # Constroi a solução gulosa
        candidate = constructGreedySolution(points, threshold)
        # Refina usando a busca local
        candidate = localSearch(candidate, maxNoImprove, timeLimit)
        if best == None or candidate["cost"] < best["cost"]:
            best = candidate
        maxIterations -= 1
    return best
