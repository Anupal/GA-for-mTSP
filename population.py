from route import *

class Population:
    routes = []

    def __init__ (self, populationSize, initialise):
        if initialise:
            for i in range(populationSize):
                newRoute = Route()
                newRoute.generateIndividual()
                self.routes.append(newRoute)
                #self.saveRoute(i, newRoute)

    def saveRoute (self, index, route):
        self.routes[index] = route

    def getRoute (self, index):
        return routes[index]

    def getFittest (self):
        fittest = self.routes[0]

        for i in range(1, self.populationSize()):
            if fittest.getFitness() <= getRoute(i).getFitness():
                fittest = getRoute(i)

        return fittest

    def populationSize(self):
        size = len(self.routes)
        return size
