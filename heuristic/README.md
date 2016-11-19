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
Cada função de teste das três metaheurísticas roda o algoritmo **10** vezes. Algumas configurações do setup podem ser alteradas na suíte de testes

É interessante que o script da suíte de testes seja rodado com um timeConstraint de 0.1 se o usuário desejar testar apenas o funcionamentos dos algoritmos.

Sscript no terminal:
```
$ python3 tsp_test_suite.py
```

O teste de iterações pode ser rodado com

```
$ python3 tsp_test_iteration.py
```
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

###### GRASP
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
Construindo uma Lista Restrita de Candidatos (RCL) que delimita as features da solução a ser escolhida a cada ciclo