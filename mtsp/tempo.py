from galogic import *

for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())

a = Route()
b = Route()
a.generateIndividual()
b.generateIndividual()

c = GA.crossover(a, b)
d = GA.crossover(a, c)
