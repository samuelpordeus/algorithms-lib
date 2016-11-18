class TSPResult(object):

    def __init__(self, optimalTourCost, searchAlgorithm, FileName, iteration):
        '''
        Constructor
        '''
        self.OptimalTourCost = optimalTourCost
        self.Algorithm = searchAlgorithm
        self.FileName = FileName
        self.iteration = iteration
    def FormattedOutput(self, result):
        '''
        Calcula o RDP do resultado
        Se a distancia ideal do passeio for de 7542 unidades, o RDP será definido por quão longe está do ideal.
        RPD = (Custo do passeio - Ideal) / Ideal
        RPD de 0 é o melhor.
        '''
        name = self.Algorithm + " - " + self.FileName +" - " + str(self.iteration)
        divider = "-" * 30
        tourCostHeader = "Tour Cost"
        tourCost = round(result["cost"], 2)

        RPDHeader = "RPD"
        RPD = round(float((result["cost"] - self.OptimalTourCost) / self.OptimalTourCost), 2)

        final = divider + "\n"\
            + name + "\n"\
            + divider + "\n"\
            + tourCostHeader + " " + str(tourCost) + "\n"\
            + divider + "\n"\
            + RPDHeader + " " + str(RPD) + "\n"\
            + divider + "\n"\

        return final

    def getRPD(self, result):
        return round(float((result["cost"] - self.OptimalTourCost) / self.OptimalTourCost), 2)
