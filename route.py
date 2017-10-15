from routemanager import *

class Route:

    route = []
    fitness = 0
    distance = 0

    def __init__ (self, route = None):

        if route == None:
            for i in range(20):
                self.route.append(None)
        else:
            self.route = route

    def generateIndividual (self):
        for dindex in range(20):
            self.setDustbin(dindex, RouteManager.getDustbin(dindex))

        random.shuffle(self.route)

    def getDustbin(self, index):
        return self.route[index]

    def setDustbin(self, index, db):
        self.route.insert(index, db)
        self.fitness = 0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            fitness = 1/self.getDistance()

        return fitness

    def getDistance(self):
        if self.distance == 0:
            routeDistance = 0

            for dindex in range(self.routeSize()):
                fromDustbin = self.getDustbin(dindex)

                if dindex+1 < self.routeSize():
                    destinationDustbin = self.getDustbin(dindex + 1)

                else:
                    destinationDustbin = getDustbin(0)

                routeDistance += fromDustbin.distanceTo(destinationDustbin)

            distance =  routeDistance

        return routeDistance

    def routeSize(self):
        size = len(self.route)
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
