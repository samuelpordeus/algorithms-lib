# Biblioteca de otimização - APA 2016.1 - Python 3
##### Samuel Pordeus - Elcius Ferreira - Victor Franco
A biblioteca contém 15 algoritmos de otimização, 9 de programação dinâmica e 6 algoritmos gulosos. Abaixo podemos ver os algoritmos contidos e quem os implementou.

#### Guidelines
A biblioteca segue os padrões de código de **Python** da [**PEP8**](https://www.python.org/dev/peps/pep-0008/)

## Módulo principal - Programação dinâmica e algoritmos gulosos

### 1. Designação dos algoritmos
#### **_Samuel Pordeus_**
##### **Dinâmicos**
1. Mochila binária
2. Maior subsequência comum
3. Distância de edição

##### **Gulosos**
1. Caminho mais curto (Algoritmo de Dijkstra)
2. Coloração de grafos

#### **_Elcius Ferreira_**
##### **Dinâmicos**
1. Triângulo de Pascal
2. Soma de subconjunto
3. Multiplicação de matrizes

##### **Gulosos**
1. Seleção de atividades
2. Mochila fracionária

#### **_Victor Franco_**
##### **Dinâmicos**
1. Quebra de palavras
2. Troco em moedas
3. Empilhamento de caixas

##### **Gulosos**
1. Árvore geradora mínima (Algoritmo de Kruskal)
2. Árvore geradora mínima (Algoritmo de Prim)

### 2. Testes
Um conjunto de testes para cada algoritmo foi desenvolvido e é executado se você rodar o script do algoritmo em questão.
Para a criação dos testes automatizados, foi utilizado o módulo [**unittest**](https://docs.python.org/3/library/unittest.html).

Exemplo, algoritmo da Maior Subsequência Comum (LCS):
```python
import unittest
class TestLcs(unittest.TestCase):

    def test_example(self):
        self.assertEqual(lcs('ABC', 'AC', 3, 2), 2)
```

Para rodar toda a suíte de testes, use o seguinte comando no terminal no diretório raiz do projeto:

```
$ make test
```

### 3. Algoritmos
Os algoritmos estão implementados de forma que pode-se chamá-los por duas funções:
```python
import algorithms
# Se chamados pela funcao com 'call' antes, os algoritmos chamam a funcao original
# e printam a saída detalhadamente
algorithms.call_edit_distance(str1, str2)
# Podemos chamar as funcoes otimizadas diretamente utilizando seus parametros originais
algorithms.edit_distance(str1, str2, len(A), len(B))
```
#### 3.1 Programação dinâmica
###### Mochila binária
```python
import algorithms
# A entrada é a capacidade da mochila, o peso dos itens e o valor dos itens
# Se for mais de um item, deve-se colocá-los em listas de tamanhos iguais.
# n é a quantidade de valores inseridos, preferencialmente colocar len(value) ou len(weight)
algorithms.max_knapsack.py(cap, weight, value, n)
# A saída é o valor máximo da mochila
```
A algoritmo da mochila binária pega itens que contém pesos e valores e coloca o máximo de valor possível mediante a capacidade da mochila. Teve sua aplicação principal no algoritmo de **Criptografia de chave pública**.
* Complexidade O(2^n)

###### Maior subsequência comum
```python
import algorithms
# A entrada são as duas strings que serão comparadas e o tamanho respectivo destas
algorithms.lcs(str1, str2, A, B)
# A saída é o valor inteiro da maior subsequência comum
```
O algoritmo da maior subsequência comum analisa duas strings e visualiza qual o tamanho da maior sequencia comum entre elas. Entre as suas aplicações estão a _engine_ da **wiki** e **sistemas de controle de versão**.
* Complexidade O(2^n)

###### Distância de edição
```python
import algorithms
# A entrada são as duas strings que serão comparadas e o tamanho respectivo destas
algorithms.edit_distance(str1, str2, m, n)
# A saída é o valor inteiro do número de operações necessárias para convertar str1 em str2
```
O algoritmo da distância de edição pega duas strings e as compara para saber quantas operações seriam necessárias para que uma string se tornasse a outra.
* Complexidade O(m x n) - Sendo m o tamanho de uma string e n o de outra

###### Triângulo de pascal
```python
import algorithms
# A entrada são dois inteiros, n representa o número da linha e k o da coluna
algorithms.binomial_coefficient(n, k)
# A saída é o valor inteiro do coeficiente binomial do triângulo de pascal
```
O algoritmo pega o número de linhas e de colunas e cálcula pelo triângulo de pascal
o coeficiente binomial. Esse algoritmo é utilizado na matemática.
* Complexidade O(n x k)

###### Soma de subconjunto
```python
import algorithms
# A entrada é um array de números e a soma a ser analisada
algorithms.is_subset_sum(set, sum)
# A saída é um booleano dizendo se a soma está contida ou não.
```
O algoritmo confere se em um dado set de números, um número inteiro está contido na soma de números deste set.

* Complexidade O(sum * n)

###### Multiplicação de matrizes
```python
import algorithms
# A entrada é um array de números e o tamanho dela.
algorithms.matrix_chain_order(arr, n)
# A saída é a menor quantidade possível de múltiplicações das matrizes
```
O algoritmo dá a forma mais eficiente de multiplicar as matrizes de tamanho indicado

* Complexidade O(n³)

###### Quebra de palavras
```python
import algorithms
# Dado uma string de letras não espaçadas, o algoritmo determina se é possível separá-las em
# palavras de acordo com um dicionário
algorithms.word_break(string, dicionario)
# A saída é True caso seja possível separar as palavras
```
O algoritmo é usado em corretores de texto como forma de corrigir erros de digitação.

* Complexidade O(n * m), onde n é o tamanho da string e m é o tamanho do dicionário

###### Troco em moedas
```python
import algorithms
# A entrada é a quantidade de dinheiro a ser trocado e uma array com as moedas disponíveis para troco
algorithms.coin_change(quantidade, moedas_disponiveis)
# A saída é o menor número de moedas quando esse é possível determinar. Caso não seja, retorna False
```

O algoritmo pode ser usado para cálcular o troco de uma determinada transação.

* Complexidade O(n * m), onde n é o número de moedas e m é a quantidade de dinheiro a ser trocada

###### Empilhamento de caixas
```python
import algorithms
# A entrada é uma array de dimensões das caixas
algorithms.box_stack(dimensions)
# A saída é a maior altura que as caixas podem ser empilhadas sem violar as restrições de tamanho
```

O algoritmo pode ser usado para determinar a melhor forma de organizar objetos de dimensões fixas dentro
de um espaço.

* Complexidade O(n²)

#### 3.2 Algoritmos gulosos
###### Caminho mais curto (Algoritmo de Dijkstra)
```python
import algorithms
# A entrada é o grafo, que é representado por um dict e o vértice que será comparado aos outros
graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
algorithms.shortest_path(graph, start)
# A saída é uma lista com os valores sequenciais do caminho mais curto
# de cada vértice para o vértice indicado em start
```

O algoritmo do caminho mais curto de Dijkstra mede o caminho mais curto entre um ponto e outro, sua aplicação
é vastamente utilizada na programação, como em problemas de **Redes telefônicas** ou **Controle de aeronaves**
* Complexidade O(V²)

###### Coloração de Grafos
```python
import algorithms
# A entrada é o grafo, que é representado por um dicionário e as cores que serão dadas aos grafos
graph = {0: {1: 2, 3: 2}, 1: {0: 2, 2: 6}, 2: {1: 6}, 3: {0: 0}}
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
algorithms.colored_graphs(graphs, colors)
# A saída é a respectiva cor de cada vértice do grafo
```
O algoritmo da distância de edição pega duas strings e as compara para saber quantas operações seriam necessárias para que uma string se tornasse a outra.
* Complexidade O(V² + E)

###### Seleção de atividades
```python
import algorithms
# A entrada são as duas lista, start e finish
algorithms.max_activities(s, f)
# A saída é uma lista indicando quais atividades podem ser executadas por uma única pessoa
```
O algoritmo seleciona o máximo número de atividades possíveis, mediante o tempo de começo e fim destas,
que podem ser realizadas por uma única pessoa. Dentre as aplicações estão algoritmos para otimizar
rotinas.

###### Mochila fracionária
```python
import algorithms
# A entrada é a capacidade da mochila, uma listas do objeto item
# que contém peso e valor e o tamanho da lista
items_list = [algorithms.Item(60, 10), algorithms.Item(40, 10), algorithms.Item(50, 30)]
algorithms.fractional_knapsack(W, items_list, n)
# A saída é o valor máximo da mochila
```
A algoritmo da mochila binária pega itens que contém pesos e valores e coloca o máximo de valor possível mediante a capacidade da mochila. Ao contrário do algoritmo da Mochila Binária, aqui podemos quebrar os valores em várias partes, agilizando o algoritmo.

* Complexidade O(n x log n)

###### Árvore geradora mínima (Algoritmo de Kruskal)
```python
import algorithms
# A entrada são as duas lista, a primeira de vertices e a segunda de conexões (arestas)
algorithms.kruskal(vertices, edges)
# A saída é uma lista de conexões entre os vértices
```
O algoritmo seleciona o menor caminho percorrido para conextar todos os nós de um grafo com o menor custo possível. É usado, por exemplo, em problemas que envolvem percorrer um espaço (físico ou virtual) no menor tempo/percurso possível, como gerenciar a entrega de envelopes em uma cidade.

* Complexidade O(E log V), onde E é o número de conexões (arestas) e V é o número de vértices

###### Árvore geradora mínima (Algoritmo de Prim)
```python
import algorithms
# A entrada são as duas lista, a primeira de vertices e a segunda de arestas
algorithms.prim(vertices, edges)
# A saída é uma lista de conexões entre os vértices
```
Assim como o Alguritmo de Kruskal, o Algoritmo de Prim é usado para determinar o percurso menos custoso para percorrer
todos os nós de um grafo, porém é especializado em grafos mais densos, para o caso em que existem mais arestas que vértices, onde sua performance é melhor. Um exemplo seria o roteamento de pacotes via redes de computador, que é um grafo bastante denso onde quanto menor a latência mais rápido o pacote chegará a outro lado rede.

* Complexidade O(E + V log V) (Amortizada), onde E é o número de arestas e V é o número de vértices