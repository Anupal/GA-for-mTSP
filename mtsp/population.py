from route import *

class Population:
    routes = []

    def __init__ (self, populationSize, initialise):
        self.populationSize = populationSize
        if initialise:
            for i in range(populationSize):
                newRoute = Route()
                newRoute.generateIndividual()
                self.routes.append(newRoute)

    def saveRoute (self, index, route):
        self.routes[index] = route

    def getRoute (self, index):
        return self.routes[index]

    def getFittest (self):
        fittest = self.routes[0]

        for i in range(1, self.populationSize):
            if fittest.getFitness() <= self.getRoute(i).getFitness():
                fittest = self.getRoute(i)

        return fittest

    def populationSize(self):
        return int(self.populationSize)

    def equals(self, pop):
        self.routes = pop.routes
