import random
import math
'''
Contains all global variables specific to simulation
'''
# Defines range for coordinates when dustbins are randomly scattered
xMax = 500
yMax = 500

numNodes = 20
numGenerations = 100
# size of population
populationSize = 200
mutationRate = 0.02
tournamentSize = 10
elitism = True
# number of trucks
numTrucks = 4

def random_range(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]

def route_lengths():
    upper = (numNodes + numTrucks - 1)
    fa = upper/numTrucks*1.6
    fb = upper/numTrucks*0.6
    a = random_range(numTrucks, upper)
    while 1:
        if all( i < fa and i > fb  for i in a):
                break
        else:
                a = random_range(numTrucks, upper)
    return a
