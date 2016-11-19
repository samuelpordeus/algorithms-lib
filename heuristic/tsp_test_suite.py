import unittest, math, time
import tsplib_parser
from result import TSPResult

MAX = 10000
timeConstraint = 0.1 # Teto para cada resultado das metaheurísticas - 60s para o trabalho

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
        print("VNS START")
        from algorithms.vns import search
        # Configuração do algoritmo
        maxNoImprove = MAX # 50
        maxNoImproveLocal = MAX # 70
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
            print("result_list:", result_list)
            print("Media dos resultados:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))
            rpd_list = []
            result_list = []

    def testGreedyRandomizedAdaptiveSearch(self):
        print("GRASP START")
        from algorithms.grasp import search
        # Configuração do algoritmo
        maxNoImprove = MAX # 50
        maxIterations = MAX # 50
        greedinessFactor = 0.2

        # Execução do algoritmo
        result_list = []
        rpd_list = []
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = search(self.TSP[x][1], maxIterations, maxNoImprove, greedinessFactor, timeConstraint)
                result_list.append(result["cost"])
                tspResult = TSPResult(self.TSP[x][0], "GRASP Results", self.TSP[x][2], y)
                rpd_list.insert(0, tspResult.getRPD(result))
                print(tspResult.FormattedOutput(result))

            print('*' * 30)
            print("result_list:", result_list)
            print("Media do Tour Cost:", int(sum(result_list) / len(result_list)))
            print("Media do RPD:", sum(rpd_list) / len(rpd_list))
            rpd_list = []
            result_list = []

    def testTabuSearch(self):
        print("TABU SEARCH START")
        from algorithms.tabu_search import search
        # Configuração do algoritmo
        maxIterations = MAX # 50
        maxTabuCount = 150
        maxCandidates = 500

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
            print("result_list:", result_list)
            print("Media dos resultados:", int(sum(result_list) / 10))
            print("Media do RPD:", float(float(sum(rpd_list)) / 10))
            rpd_list = []
            result_list = []

if __name__ == "__main__":
    unittest.main()
