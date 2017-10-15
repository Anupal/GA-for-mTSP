from routemanager import *

class Route:

    route = []
    fitness = 0
    distance = 0

    def __init__ (self):
        for i in range(RouteManager.numberOfDustbins()):
            route.append(None)

    def __init__ (self, route):
        this.route = route

    def generateIndividual (self):
        for dindex in range(RouteManager.numberOfDustbins()):
            setDustbin (dindex, RouteManager.getDustbin(dindex))

        random.shuffle(route)

    def getDustbin(self, index):
        return tour[index]

    def setDustbin(self, index, db):
        tour.insert(index, db)
        fitness = 0
        distance = 0

    def getFitness(self):
        if fitness == 0:
            fitness = 1/getDistance()

        return fitness

    def getDistance(self):
        if distance == 0:
            routeDistance = 0

            for dindex in range(routeSize()):
                fromDustbin = getDustbin(dindex)

                if dindex+1 < routeSize():
                    destinationDustbin = getDustbin(dindex + 1)

                else:
                    destinationDustbin = getDustbin(0)

                routeDistance += fromDustbin.distanceTo(destinationDustbin)

            distance =  routeDistance

        return routeDistance

    def routeSize(self):
        size = len(route)
        return size

    def containsDustbin(self, db):
        if db in route:
            return true
        else:
            return false

    def toString (self):
        geneString = '|'

        for i in range(routeSize()):
            geneString += getDustbin(i) + '|'

        return geneString
