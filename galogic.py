from population import *

class GA:
    mutationRate = 0.015
    tournamentSize = 5
    elitism = True

    def evolvePopulation(self, pop):
        newPopulation = Population(pop.populationSize(), false)

        elitismOffset = 0
        if elitism:
            newPopulation.saveRoute(0, pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = tournamentSelection(pop)
            parent2 = tournamentSelection(pop)
            child = crossover(parent1, parent2)
            newPopulation.saveRoute(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            mutate(newPopulation.getRoute(i))

        return newPopulation

    def crossover(self, parent1, parent2):
        child = Route()
        startPos = random.randint(0, parent1.routeSize())
        endPos = random.randint(0, parent2.routeSize())

        for i in range(child.routeSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setDustbin(i, parent1.getDustbin(i))

            elif startPos > endPos:
                if not(i < startPos and i > endPos):
                    child.setDustbin(i, parent1.getDustbin(i))

        for i in range(parent2.routeSize()):
            if not(child.containsDustbin(parent2.getDustbin(i))):
                for i1 in range(child.routeSize()):
                    if child.getDustbin(i1) == None:
                        child.setDustbin(i1, parent2.getDustbin(i))
                        break


        return child

    def mutate (self, route):
        for routePos in range(route.routeSize()):
            if random.randrange(1) < mutationRate:
                routePos2 = random.randint(0, route.routeSize())

                dustbin1 = route.getDustbin(routePos)
                dustbin2 = route.getDustbin(routePos2)

                route.setDustbin(routePos2, dustbin1)
                route.setDustbin(routePos, dustbin2)

    def tournamentSelection (self, pop):
        tournament = Population(tournamentSize, false)

        for i in range(tournamentSize):
            randomInt = random.randint(pop.populationSize())
            tournament.saveRoute(i, pop.getRoute(randomInt))

        fittest = tournament.getFittest()
        return fittest
