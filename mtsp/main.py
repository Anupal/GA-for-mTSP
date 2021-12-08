from galogic import *
import matplotlib.pyplot as plt
import progressbar
import pandas as pd
import time
pbar = progressbar.ProgressBar()

tic = time.time()
# Add Dustbins
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin(X[i],Y[i]))

random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)
toc = time.time()
print("Time cost:",round(toc-tic,2))

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route:\n' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()
