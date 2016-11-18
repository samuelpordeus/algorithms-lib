'''
Estratégia:
A estratégia para a Busca em Vizinhança Variável envolve exploração iterativa de vizinhanças cada vez maiores para um dado
local ideal até que uma melhora seja localizada depois de cada repetição que a busca percorre expandindo vizinhanças.

A estratégia é motivada por três princípos:
1) um mínimo local para uma estrutura de vizinhança pode não ser um mínimo local para estruturas de vizinhança diferentes,
2) um mínimo global é um mínimo local para todas as estruturas de vizinhança possíveis, e
3) mínimos locais são relativamente próximos aos mínimos globais para qualquer classe de problemas.

Heurísticas:
Métodos aproximativos (como escalada estocástica) são sugeridos para uso como procedimento de Busca Local para grandes 
instâncias de problema, com o objetivo de reduzir o tempo de execução.

Busca em Vizinhança Variável tem sido aplicado para uma ampla gama de problemas de otimização combinatória, assim como
clustering e problemas de otimização de funções contínuas.

A técnica de Busca Local utilizada deve ser específica para o tipo de problema e instância.

O Variable Neighborhood Descent (VND) pode ser utilizado no VNS como procedimento de Busca Local e tem se mostrado o 
mais efetivo.
'''
from algorithms.utilities import stochasticTwoOpt, tourCost, constructInitialSolution
import time

def localSearch(best, maxIter, neighborhood, timeLimit):
    count =0
    while count < maxIter and time.time() < timeLimit:
        candidate ={}
        candidate["permutation"]=best["permutation"]
        for index in range(0,neighborhood):# Envolve executar duas opções estocásticas por quantidade de vizinhos.
                # Obter a solução candidata de vizinhança.
                candidate["permutation"] = stochasticTwoOpt(candidate["permutation"])

        candidate["cost"] = tourCost(candidate["permutation"])
        if candidate["cost"] < best["cost"]:# A busca é reiniciada quando um ótimo local é encontrado. # We also restart the search when we find the local optima
            best,count = candidate, 0
        else:
            count +=1

    return best

def search(points,neighborhoods, maxNoImprove, maxNoImproveLocalSearch, timeLimit):
    t_end = time.time() + timeLimit
    # Permutação aleatória é usada para a construção da solução inicial.
    best ={}
    best["permutation"] = constructInitialSolution(points)
    best["cost"] = tourCost(best["permutation"])
    noImproveCount =0
    while noImproveCount<=maxNoImprove and time.time() < t_end:
        candidate ={}
        candidate["permutation"] = best["permutation"]
        # Para cada vizinhança em vizinhanças.
        for neighborhood in neighborhoods:
            # Calcular vizinhança: Envolve executar duas opções estocásticas por quantidade de vizinhanças.
            for index in range(0,neighborhood):
                # Obter solução canditada de vizinhança.
                candidate["permutation"] = stochasticTwoOpt(candidate["permutation"])

            # Calcular o custo da vizinhança final.
            candidate["cost"] = tourCost(candidate["permutation"])
            # Refinar a solução candidata final usando a busca local e a vizinhança.
            candidate = localSearch(candidate,maxNoImproveLocalSearch, neighborhood, t_end)
            # Se o custo da candidata é menor que o custo da melhor solução atual, então substitua a melhor pela candidata.
            if candidate["cost"] < best["cost"]:
                best, noImproveCount = candidate, 0 # Quando um ótimo local é encontrado a busca é reiniciada. 
                # Interrupção da iteração das vizinhanças.
                break
            else: # Incremento do contador para informar que um ótimo local não foi encontrado. 
                noImproveCount +=1

    return best


