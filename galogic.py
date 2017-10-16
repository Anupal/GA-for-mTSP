from population import *

class GA:
    mutationRate = 0.015
    tournamentSize = 5
    elitism = True

    @classmethod
    def evolvePopulation(cls, pop):
        #print (RouteManager.getDustbin(3).toString())

        newPopulation = Population(pop.populationSize, False)

        elitismOffset = 0
        if cls.elitism:
            newPopulation.saveRoute(0, pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize):
            parent1 = cls.tournamentSelection(pop)
            parent2 = cls.tournamentSelection(pop)
            child = cls.crossover(parent1, parent2)
            newPopulation.saveRoute(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            cls.mutate(newPopulation.getRoute(i))

        return newPopulation

    @classmethod
    def crossover(cls, parent1, parent2):
        child = Route()
        startPos = random.randint(0, parent1.routeSize()-1)
        endPos = random.randint(0, parent2.routeSize()-1)

        for i in range(child.routeSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setDustbin(i, parent1.getDustbin(i))

            elif startPos > endPos:
                if not(i < startPos and i > endPos):
                    child.setDustbin(i, parent1.getDustbin(i))
        print ('P1: ' + parent1.toString())
        print ('P2: ' + parent2.toString())
        #print('P2 rs:' + str(parent2.routeSize()))
        for i in range(parent2.routeSize()):
            if not(child.containsDustbin(parent2.getDustbin(i))):
                for i1 in range(child.routeSize()):
                    if child.getDustbin(i1) == None:
                        child.setDustbin(i1, parent2.getDustbin(i))
                        break

        print ('C: ' + child.toString())
        return child

    @classmethod
    def mutate (cls, route):
        for routePos in range(route.routeSize()):
            if random.randrange(1) < cls.mutationRate:
                routePos2 = random.randint(0, route.routeSize()-1)

                dustbin1 = route.getDustbin(routePos)
                dustbin2 = route.getDustbin(routePos2)

                route.setDustbin(routePos2, dustbin1)
                route.setDustbin(routePos, dustbin2)

    @classmethod
    def tournamentSelection (cls, pop):
        tournament = Population(cls.tournamentSize, False)

        for i in range(cls.tournamentSize):
            randomInt = random.randint(0, pop.populationSize-1)
            tournament.saveRoute(i, pop.getRoute(randomInt))

        fittest = tournament.getFittest()
        return fittest
