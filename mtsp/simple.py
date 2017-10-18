from galogic import *
import matplotlib.pyplot as plt
import progressbar
pbar = progressbar.ProgressBar()
'''
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin())
'''
RouteManager.addDustbin(Dustbin(60, 200))

RouteManager.addDustbin(Dustbin(180, 200))

RouteManager.addDustbin(Dustbin(80, 180))

RouteManager.addDustbin(Dustbin(140, 180))

RouteManager.addDustbin(Dustbin(20, 160))

RouteManager.addDustbin(Dustbin(100, 160))

RouteManager.addDustbin(Dustbin(200, 160))

RouteManager.addDustbin(Dustbin(140, 140));

RouteManager.addDustbin(Dustbin(40, 120));

RouteManager.addDustbin(Dustbin(100, 120));

RouteManager.addDustbin(Dustbin(180, 100));

RouteManager.addDustbin(Dustbin(60, 80));

RouteManager.addDustbin(Dustbin(120, 80));

RouteManager.addDustbin(Dustbin(180, 60));

RouteManager.addDustbin(Dustbin(20, 40));

RouteManager.addDustbin(Dustbin(100, 40));

RouteManager.addDustbin(Dustbin(200, 40));

RouteManager.addDustbin(Dustbin(20, 20));

RouteManager.addDustbin(Dustbin(60, 20));

RouteManager.addDustbin(Dustbin(160, 20));
random.seed(1)
yaxis = []
xaxis = []
pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    #print(fittest)
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: ' + globalRoute.toString())

fig = plt.figure()
#plt.ylim(0, 80000)
plt.plot(xaxis, yaxis, 'r-')
plt.show()
'''
pop = Population(populationSize, True)

for i in range(populationSize):
    print(pop.getRoute(i).toString())
    print(pop.getRoute(i).getDistance())
    print(pop.getRoute(i).getFitness())
'''

#p2 = Route()
#p2.generateIndividual()
#print(p2.toString())

#child = GA.crossover(p1, p2)
#print (child.toString())
#GA.mutate(child)
#print (child.toString())
