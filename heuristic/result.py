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
        Calculates the RPD of the search from the passed in result object,
        which contains the tour cost of the final solution
        The optimal tour distance for e.g. berlin52 is 7542 units
        Search RPD is defined as how far we are away from the optimal
        RPD = (tourCost - optimal)/optimal
        an RPD of 0 is best
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
