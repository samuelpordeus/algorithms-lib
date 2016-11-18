import math, random


# Função que calcula a distancia euclidiana entre dois pontos
def euclideanDistance(v1, v2):
    sum =0.0
    for coord1,coord2 in zip(v1,v2):
        sum += pow((coord1-coord2), 2)

    return math.sqrt(sum)

# Função que calcula o custo total do passeio
def tourCost(perm):
    totalDistance =0.0
    size = len(perm)
    for index in range(size):
        if index == size-1 :
            point2 = perm[0]
        else:
            point2 = perm[index+1]

        totalDistance +=  euclideanDistance(perm[index], point2)

    return totalDistance

# Função que deleta duas arestas e inverte a sequecia entre elas
def stochasticTwoOpt(perm):
    result = perm[:] # Cópia da lista
    size = len(result)
    p1, p2 = random.randrange(0,size), random.randrange(0,size)
    exclude = set([p1])
    if p1 == 0:
        exclude.add(size-1)
    else:
        exclude.add(p1-1)

    if p1 == size-1:
        exclude.add(0)
    else:
        exclude.add(p1+1)

    while p2 in exclude:
        p2 = random.randrange(0,size)

    if p2<p1:
        p1, p2 = p2, p1

    result[p1:p2] = reversed(result[p1:p2])

    return result

def stochasticTwoOptWithEdges(perm):
    result = perm[:] # Cópia da lista
    size = len(result)
    p1, p2 = random.randrange(0,size), random.randrange(0,size)
    exclude = set([p1])
    if p1 == 0:
        exclude.add(size-1)
    else:
        exclude.add(p1-1)

    if p1 == size-1:
        exclude.add(0)
    else:
        exclude.add(p1+1)

    while p2 in exclude:
        p2 = random.randrange(0,size)

    if p2<p1:
        p1, p2 = p2, p1

    result[p1:p2] = reversed(result[p1:p2])

    return result, [[perm[p1-1],perm[p1]],[perm[p2-1],perm[p2]]]

# Função que cria uma permutação aleatória de uma permutação inicial misturando seus elementos para uma ordem aleatória
def constructInitialSolution(initPerm):
    permutation = initPerm[:] # Cópia da lista
    size = len(permutation)
    for index in range(size):
        shuffleIndex = random.randrange(index,size)
        permutation[shuffleIndex], permutation[index]= permutation[index], permutation[shuffleIndex]

    return permutation

