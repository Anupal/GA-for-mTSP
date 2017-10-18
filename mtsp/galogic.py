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

        # tournament selection
        for i in range(elitismOffset, newPopulation.populationSize):
            newPopulation.saveRoute(i, cls.tournamentSelection(pop))

        # mutate here
        for i in range(elitismOffset, newPopulation.populationSize):
            cls.mutate(newPopulation.getRoute(i))

        return newPopulation

    #TODO: Implement cross route mutation
    @classmethod
    def mutate (cls, route):
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = random.randint(0, numTrucks - 1)
            index2 = random.randint(0, numTrucks - 1)
        #print ('Indexes selected: ' + str(index1) + ',' + str(index2))

        #generate replacement range for 1
        route1startPos = 0
        route1lastPos = 0
        while route1startPos >= route1lastPos or route1startPos == 1:
            route1startPos = random.randint(1, route.routeLengths[index1] - 1)
            route1lastPos = random.randint(1, route.routeLengths[index1] - 1)

        #generate replacement range for 2
        route2startPos = 0
        route2lastPos = 0
        while route2startPos >= route2lastPos or route2startPos == 1:
            route2startPos = random.randint(1, route.routeLengths[index2] - 1)
            route2lastPos= random.randint(1, route.routeLengths[index2] - 1)

        #print ('startPos, lastPos: ' + str(route1startPos) + ',' + str(route1lastPos) + ',' + str(route2startPos) + ',' + str(route2lastPos))
        swap1 = [] # values from 1
        swap2 = [] # values from 2

        if random.randrange(1) < cls.mutationRate:
            # pop all the values to be replaced
            for i in range(route1startPos, route1lastPos + 1):
                swap1.append(route.route[index1].pop(route1startPos))

            for i in range(route2startPos, route2lastPos + 1):
                swap2.append(route.route[index2].pop(route2startPos))

            del1 = (route1lastPos - route1startPos + 1)
            del2 = (route2lastPos - route2startPos + 1)
            '''
            print('After removal: \n' + route.toString())
            print('swap1')
            for i in swap1:
                print(i.toString())
            print('swap2')
            for i in swap2:
                print(i.toString())
            '''
            # add to new location by pushing
            route.route[index1][route1startPos:route1startPos] = swap2
            route.route[index2][route2startPos:route2startPos] = swap1

            route.routeLengths[index1] = len(route.route[index1])
            route.routeLengths[index2] = len(route.route[index2])

    @classmethod
    def tournamentSelection (cls, pop):
        tournament = Population(cls.tournamentSize, False)

        for i in range(cls.tournamentSize):
            randomInt = random.randint(0, pop.populationSize-1)
            tournament.saveRoute(i, pop.getRoute(randomInt))

        fittest = tournament.getFittest()
        return fittest
