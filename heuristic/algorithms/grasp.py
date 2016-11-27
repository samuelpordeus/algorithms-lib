'''
Estrategia
Iterativamente fazer soluções gulosas aleatórias e depois usar uma heurística de busca local para refiná-las.
Construindo uma Lista Restrita de Candidatos (RCL) que delimita as features da solução a ser escolhida a cada ciclo

Threshold define o quão guloso o mecanismo de construção é, sendo 0 guloso e 1 generalizado.

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
        # Calcula o custo de adicionar uma característica à solução
        # A 'feature' ou característica é definida por quão longe os outros pontos estão do último elemento da lista de candidatos
        costs = []
        candidateSize = len(candidate["permutation"])
        for item in candidates:
            costs.append(euclideanDistance(candidate["permutation"][candidateSize - 1], item))
        # Determina o menor e o maior custo do determinado set
        rcl, maxCost, minCost = [], max(costs), min(costs)
        # Construimos o RCL da seguinte maneira:
        # Adicionamos o que for menor ou igual ao mínimo + o custo da característica pela fórmula da RCL
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
    count = 0
    while count < maxIter and time.time() < timeLimit:
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
        candidate = localSearch(candidate, maxNoImprove, t_end)
        if best == None or candidate["cost"] < best["cost"]:
            best = candidate
        maxIterations -= 1
    return best

def searchIteration(points, maxIterations, maxNoImprove, threshold, timeLimit):
    best_list = []
    t_end = time.time() + timeLimit
    best = None
    while maxIterations > 0 and time.time() < t_end:
        # Constroi a solução gulosa
        candidate = constructGreedySolution(points, threshold)
        # Refina usando a busca local
        candidate = localSearch(candidate, maxNoImprove, t_end)
        if best == None or candidate["cost"] < best["cost"]:
            best = candidate
        maxIterations -= 1
        # print(best["cost"])
        best_list.append(best["cost"])
    return best_list