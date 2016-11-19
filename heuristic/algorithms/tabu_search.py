'''
Estratégia
A estratégia é restringir o retorno a áreas recentemente visitadas do espaço
de busca através de uma heurística incorporada ao algoritmo (ciclicamente).
O algoritmo mantém uma pequena memória de passos recentes e impede passos
futuros de desfazer essas alterações. Esta estratégia pode ser estendida
adicionando estruturas de memória intermediárias para servir de 'bias' nos
passos próximos à áreas promissoras (intensificação), bem como estruturas de
memória de longo prazo para promover a diversidade.

Heurística
A Pesquisa Tabu foi projetado para gerenciar uma escalada heurística, embora
pode ser adaptado para gerenciar qualquer exploração heurística de vizinhança.

Tem sido predominantemente aplicada a domínios discretos, tais como problemas
de optimização combinatória.

Os candidatos para passos vizinhos podem ser gerados deterministicamente para
toda uma vizinhança, ou a vizinhança pode ser amostrada estocásticamente a um
tamanho fixo, trocando eficiência por exatidão.
'''
from algorithms.utilities import constructInitialSolution, tourCost, stochasticTwoOptWithEdges
import time

# Função que retorna o melhor candidato, ordenada pelo custo
def locateBestCandidate(candidates):
    candidates.sort(key=lambda c: c["candidate"]["cost"])
    best, edges = candidates[0]["candidate"], candidates[0]["edges"]
    return best, edges


def isTabu(perm, tabuList, timeLimit):
    if time.time() > timeLimit:
        return False
    count = 0
    count += 1
    result = False
    size = len(perm)
    for index, edge in enumerate(perm):
        if index == size - 1:
            edge2 = perm[0]
        else:
            edge2 = perm[index + 1]
        if [edge, edge2] in tabuList:
            result = True
            break

    return result


def generateCandidates(best, tabuList, points, timeLimit):
    permutation, edges, result = None, None, {}
    while permutation == None or isTabu(best["permutation"], tabuList, timeLimit):
        permutation, edges = stochasticTwoOptWithEdges(best["permutation"])
    candidate = {}
    candidate["permutation"] = permutation
    candidate["cost"] = tourCost(candidate["permutation"])
    result["candidate"] = candidate
    result["edges"] = edges
    return result


def search(points, maxIterations, maxTabu, maxCandidates, timeLimit):
    t_end = time.time() + timeLimit
    # construct a random tour
    best = {}
    best["permutation"] = constructInitialSolution(points)
    best["cost"] = tourCost(best["permutation"])
    tabuList = []
    while maxIterations > 0 and time.time() < t_end:
        # Gera candicdatos usando o algoritmo 2-opt de busca local
        # estocásticamente, perto do melhor candidato dessa iteração.
        # Usa a lista tabu para não visitar vértices mais de uma vez
        candidates = []
        for index in range(0, maxCandidates):
            candidates.append(generateCandidates(best, tabuList, points, t_end))
        # Procura o melhor candidasto
        # ordena a lista de cnadicados pelo custo
        bestCandidate, bestCandidateEdges = locateBestCandidate(candidates)
        # compara com o melhor candidato e o atualiza se necessário
        if bestCandidate["cost"] < best["cost"]:
            # define o candidato atual como melhor
            best = bestCandidate
            # atuliza a lista tabu
            for edge in bestCandidateEdges:
                if len(tabuList) < maxTabu:
                    tabuList.append(edge)
        maxIterations -= 1

def searchIteration(points, maxIterations, maxTabu, maxCandidates, timeLimit):
    t_end = time.time() + timeLimit
    best_list = []
    # constrói a solução inical
    best = {}
    best["permutation"] = constructInitialSolution(points)
    best["cost"] = tourCost(best["permutation"])
    tabuList = []
    while maxIterations > 0 and time.time() < t_end:
        # Gera candicdatos usando o algoritmo 2-opt de busca local
        # estocásticamente, perto do melhor candidato dessa iteração.
        # Usa a lista tabu para não visitar vértices mais de uma vez
        candidates = []
        for index in range(0, maxCandidates):
            candidates.append(generateCandidates(best, tabuList, points, t_end))
        # Procura o melhor candidasto
        # ordena a lista de cnadicados pelo custo
        bestCandidate, bestCandidateEdges = locateBestCandidate(candidates)
        # compara com o melhor candidato e o atualiza se necessário
        if bestCandidate["cost"] < best["cost"]:
            # define o candidato atual como melhor
            best = bestCandidate
            # atuliza a lista tabu
            for edge in bestCandidateEdges:
                if len(tabuList) < maxTabu:
                    tabuList.append(edge)
        maxIterations -= 1
        best_list.append(best["cost"])

    return best_list
