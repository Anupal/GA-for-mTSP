from routemanager import *

class Route:



    def __init__ (self, route = None):
        self.route = []
        self.base = []

        self.routeLengths = route_lengths()

        for i in range(numTrucks):
            self.route.append([])
        self.fitness = 0
        self.distance = 0

        if route == None:
            for i in range(RouteManager.numberOfDustbins()-1):
                self.base.append(Dustbin(-1,-1))

        else:
            self.route = route

    def generateIndividual (self):
        k=0
        # put 1st member of RouteManager as it is and shuffle the rest before adding
        for dindex in range(1, RouteManager.numberOfDustbins()):
            self.base[dindex-1] = RouteManager.getDustbin(dindex)

        random.shuffle(self.base)
        for i in range(numTrucks):
            self.route[i].append(RouteManager.getDustbin(0)) # add same first node for each route
            for j in range(self.routeLengths[i]-1):
                self.route[i].append(self.base[k]) # add shuffled values for rest
                k+=1


    def getDustbin(self, i, j):
        return self.route[i][j]

    def setDustbin(self, i, j, db):
        self.route[i][j] = db
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

            for i in range(numTrucks):
                for j in range(self.routeLengths[i]):
                    fromDustbin = self.getDustbin(i, j)

                    if j+1 < self.routeLengths[i]:
                        destinationDustbin = self.getDustbin(i, j + 1)

                    else:
                        destinationDustbin = self.getDustbin(i, 0)

                    routeDistance += fromDustbin.distanceTo(destinationDustbin)

        distance =  routeDistance
        return routeDistance

    def containsDustbin(self, db):
        if db in self.base: #base <-> route
            return True
        else:
            return False

    def toString (self):
        geneString = '|'
        print (self.routeLengths)
        #for k in range(RouteManager.numberOfDustbins()-1):
        #    print (self.base[k].toString())
        for i in range(numTrucks):
            for j in range(self.routeLengths[i]):
                geneString += self.getDustbin(i,j).toString() + '|'
            geneString += '\n'

        return geneString
