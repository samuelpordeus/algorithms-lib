import unittest, math
import tsplib_parser
from result import TSPResult

MAX = 1000
timeConstraint = 60 # Teto para cada resultado das metaheurísticas - 60s para o trabalho

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.Vector = [1, 2]
        self.TSP = []
        self.TSP.insert(0, [7542, tsplib_parser.readData('TSPLIB/berlin52.tsp'), 'Berlin52'])
        self.TSP.insert(1, [26524, tsplib_parser.readData('TSPLIB/kroa150.tsp'), 'Kroa150'])
        self.TSP.insert(2, [22141, tsplib_parser.readData('TSPLIB/krob100.tsp'), 'Krob100'])
        self.TSP.insert(3, [44303, tsplib_parser.readData('TSPLIB/pr107.tsp'), 'Pr107'])
        self.TSP.insert(4, [108159, tsplib_parser.readData('TSPLIB/pr76.tsp'), 'Pr76'])

    def tearDown(self):
        self.Vector = []

    def testVariableNeighborhoodSearch(self):
        from algorithms.vns import search
        # Configuração do algoritmo
        maxNoImprove = MAX # 50
        maxNoImproveLocal = 70 # 70
        neighborhoods = range(1, 21)  # 20 ciclos de neighborhoods

        # Execução do algoritmo
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], neighborhoods, maxNoImprove, maxNoImproveLocal, timeConstraint)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "VNS Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))
                print(tspResult.FormattedOutput(result))

            print('#' * 30)
            print("Media dos resultados:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))

    def testGreedyRandomizedAdaptiveSearch(self):
        from algorithms.grasp import search
        # Configuração do algoritmo
        maxNoImprove = 500 # 50
        maxIterations = MAX # 50
        greedinessFactor = 0.2

        # Execução do algoritmo
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], maxIterations, maxNoImprove, greedinessFactor, timeConstraint)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "GRASP Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))
                print(tspResult.FormattedOutput(result))

            print('*' * 30)
            print("Media do Tour Cost:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))

    def testTabuSearch(self):
        from algorithms.tabu_search import search
        # Configuração do algoritmo
        maxIterations = MAX # 50
        maxTabuCount = 15
        maxCandidates = 50

        # Execução do algoritmo
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], maxIterations, maxTabuCount, maxCandidates, timeConstraint)
                result_list.insert(0, result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "Tabu Search Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))

                print(tspResult.FormattedOutput(result))
            print('@' * 30)
            print("Media dos resultados:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))


if __name__ == "__main__":
    unittest.main()
