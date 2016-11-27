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
        result_master_list = []
        result_list = []
        print("VNS START")
        from algorithms.vns import searchIteration
        # Configuração do algoritmo
        maxNoImprove = MAX # 50
        maxNoImproveLocal = 700 # 70
        neighborhoods = range(1, 21)  # 20 ciclos de neighborhoods

        # Execução do algoritmo
        for x in range(len(self.TSP)):
            for y in range(1, 11):
                result = searchIteration(self.TSP[x][1], neighborhoods, maxNoImprove, maxNoImproveLocal, timeConstraint)
                for z in range(len(result)):
                    result[z] = (result[z] - self.TSP[x][0]) / self.TSP[x][0]
                    result_list.append(result[z])
                result_master_list.append(result_list)
            print(result_master_list)
            print('*' * 30)

    # def testGreedyRandomizedAdaptiveSearch(self):
    #     print("GRASP START")
    #     from algorithms.grasp import searchIteration
    #     # Configuração do algoritmo
    #     maxNoImprove = 500 # 50
    #     maxIterations = MAX # 50
    #     greedinessFactor = 0.2

    #     # Execução do algoritmo
    #     # rpd_list = []
    #     for x in range(len(self.TSP)):
    #         for y in range(1, 11):
    #             result = searchIteration(self.TSP[x][1], maxIterations, maxNoImprove, greedinessFactor, timeConstraint)
    #             for z in range(len(result)):
    #                 rpd = (result[z] - self.TSP[x][0]) / self.TSP[x][0]
    #                 result[z] = rpd
    #             print((self.TSP[x][2] + str(y)), "=", str(result))
    #             print(('G_' + self.TSP[x][2] + str(y)), "=", "Series(" + (self.TSP[x][2] + str(y)) + ")")
    #         # print("Media do RPD:", sum(rpd_list) / len(rpd_list))
    #         print('*' * 30)


    # def testTabuSearch(self):
    #     print("TABU SEARCH START")
    #     from algorithms.tabu_search import searchIteration
    #     # Configuração do algoritmo
    #     maxIterations = MAX # 50
    #     maxTabuCount = 150
    #     maxCandidates = 500

    #     # Execução do algoritmo
    #     result_list = []
    #     rpd_list = []
    #     for x in range(len(self.TSP)):
    #         for y in range(1, 11):
    #             result = searchIteration(self.TSP[x][1], maxIterations, maxTabuCount, maxCandidates, timeConstraint)
    #             for z in range(len(result)):
    #                 result[z] = (result[z] - self.TSP[x][0]) / self.TSP[x][0]
    #             print((self.TSP[x][2] + str(y)), "=", str(result))
    #             print(('T_' + self.TSP[x][2] + str(y)), "=", "Series(" + (self.TSP[x][2] + str(y)) + ")")

    #         print('*' * 30)

if __name__ == "__main__":
    unittest.main()
