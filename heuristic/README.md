# Módulo adicional - Otimização heurística

## TODO

Configurem os algoritmos de maneira que eu possa executá-los de forma ideal. Os parâmetros estão localizados na parte de configuração da suíte de testes

Reorganizar o módulo

Se sobrar tempo, testaremos com: 25, 50, 100, 250 iterações





#### Samuel Pordeus - Elcius Ferreira - Victor Franco

A biblioteca contém 3 abordagens metaheurísticas para resolução do **Problema do Caixeiro Viajante**

#### Guidelines
A biblioteca segue os padrões de código de **Python** da [**PEP8**](https://www.python.org/dev/peps/pep-0008/)

### 1. Designação das metaheurísticas
### **Samuel Pordeus**
GRASP

### **Elcius Ferreira**
Variable Neighborhood Search

### **Victor Franco**
Tabu Search

### 2. Testes
Dois conjuntos de testes foram realizados, um para testar a eficiência dos algoritmos e outro para testar a evolução dos algoritmos mediante iterações
Para a criação dos testes automatizados, utilizamos o módulo [**unittest**](https://docs.python.org/3/library/unittest.html).

```python
import unittest
class SearchTests(unittest.TestCase):

    def setUp(self):
        self.Vector = [1, 2]
        self.TSP = []
        self.TSP.insert(0, [7542, readtsplib.readData('TSPLIB/berlin52.tsp')])
        self.TSP.insert(1, [26524, readtsplib.readData('TSPLIB/kroa150.tsp')])
        self.TSP.insert(2, [22141, readtsplib.readData('TSPLIB/krob100.tsp')])
        self.TSP.insert(3, [44303, readtsplib.readData('TSPLIB/pr107.tsp')])
        self.TSP.insert(4, [108159, readtsplib.readData('TSPLIB/pr76.tsp')])

```
Cada teste das três metaheurísticas roda o algoritmo **10** vezes. Algumas configurações do setup podem ser alteradas nos testes.

Existem dois testes:

*tsp_test_suite.py*: testa a eficiência do algoritmo, configurado de forma a maximizar a performance em 60s de execução.

*tsp_test_iteration.py*: tem o objetivo de testar a evolução do algoritmo a cada iteração durante 60s de execução.

É interessante que o script da suíte de testes seja rodado com um timeConstraint de 0.1 se o usuário desejar testar apenas o funcionamentos dos algoritmos.

Script no terminal:
```
$ python3 tsp_test_suite.py
```

O script de teste de iteração pode ser rodado com:

```
$ python3 tsp_test_iteration.py
```

Os outputs estão formatados para uma análise de dados utilizando a biblioteca *Pandas*.
---

---
### 3. Arquivos de entrada
Utilizamos as entradas da TSPLib e fizemos uma função para adaptar os arquivòs da biblioteca para uma estrutura de dados adequada. Optamos por utilizar listas.

**berlin52.tsp**
- distância ideal: 7542 passos

**kroa150.tsp**
- distância ideal: 26524 passos

**krob100.tsp**
- distância ideal: 22141 passos

**pr107.tsp**
- distância ideal: 44303 passos

**pr76.tsp**
- distância ideal: 108159 passos

### 4. Algoritmos

##### GRASP
```python
from algorithms import grasp
# A entrada tem como parâmetros:
# - A instância da TSPLIB em forma de lista
# - O número máximo de iterações
# - O número máximo de melhorias locais a serem feitas
# - O threshold que determina o quão guloso o algoritmo é
# - O fator que delimita o tempo máximo
result = search(self.TSP[x][1], maxIterations, maxNoImprove, greedinessFactor, timeConstraint)
# A saída pode ser obtida utilizando a função auxiliar do result.py TSPResult
# Pois a saída do algoritmo contém muitas informações que são tratadas utilizando a TSPResult
tspResult = TSPResult(self.TSP[x][0], "GRASP Results", self.TSP[x][2], y)
```
**Estrategia**

Iterativamente fazer soluções gulosas aleatórias e depois usar uma heurística de busca local para refiná-las.
Construindo uma Lista Restrita de Candidatos (RCL) que delimita as features da solução a ser escolhida a cada ciclo.

##### Setup dos testes de eficiência
```python
maxNoImprove = 10000
maxIterations = MAX
greedinessFactor = 0.2
```
###### Setup dos testes de iteração
```python
maxNoImprove = 500
maxIterations = MAX
greedinessFactor = 0.2
```

##### VNS
```python
from algorithms.vns import search
# A entrada tem como parâmetros:
# - A instância da TSPLIB em forma de lista
# - O ciclo de vizinhanças
# - O número máximo de melhorias locais a serem feitas
# - O número máximo de melhorias locais a serem feitas na busca local do VNS
# - O fator que delimita o tempo máximo
result = search(self.TSP[x][1], neighborhoods, maxNoImprove, maxNoImproveLocal, timeConstraint)
# A saída pode ser novamente obtida utilizando a função auxiliar do result.py TSPResult
# As informações que contidas na saída serão mais uma vez tratadas utilizando esta função auxiliar
tspResult = TSPResult(self.TSP[x][0], "VNS Results", self.TSP[x][2], y)
```
**Estratégia**

A estratégia para a Busca em Vizinhança Variável envolve exploração iterativa de vizinhanças cada vez maiores para um dado
local ideal até que uma melhora seja localizada depois de cada repetição que a busca percorre expandindo vizinhanças.

A estratégia é motivada por três princípos:
- 1) um mínimo local para uma estrutura de vizinhança pode não ser um mínimo local para estruturas de vizinhança diferentes,
- 2) um mínimo global é um mínimo local para todas as estruturas de vizinhança possíveis, e
- 3) mínimos locais são relativamente próximos aos mínimos globais para qualquer classe de problemas.

##### Setup dos testes de eficiência
```python
maxNoImprove = MAX
maxNoImproveLocal = MAX
neighborhoods = range(1, 21)
```
###### Setup dos testes de iteração
```python
maxNoImprove = MAX
maxNoImproveLocal = 700 
neighborhoods = range(1, 21)
```