from routemanager import *

class Route:



    def __init__ (self, route = None):
        self.route = []
        self.fitness = 0
        self.distance = 0

        if route == None:
            for i in range(RouteManager.numberOfDustbins()):
                self.route.append(Dustbin(-1,-1))

        else:
            self.route = route

    def generateIndividual (self):
        for dindex in range(RouteManager.numberOfDustbins()):
            self.setDustbin(dindex, RouteManager.getDustbin(dindex))

        random.shuffle(self.route)

    def getDustbin(self, index):
        return self.route[index]

    def setDustbin(self, index, db):
        self.route[index] = db
        #self.route.insert(index, db)
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
                    destinationDustbin = self.getDustbin(0)

                routeDistance += fromDustbin.distanceTo(destinationDustbin)

            distance =  routeDistance

        return routeDistance

    def routeSize(self):
        size = len(self.route)
        return size

    def containsDustbin(self, db):
        if db in self.route:
            return True
        else:
            return False

    def toString (self):
        geneString = '|'

        for i in range(self.routeSize()):
            geneString += self.getDustbin(i).toString() + '|'

        return geneString
