from galogic import *

RouteManager.addDustbin(Dustbin(0,0))
RouteManager.addDustbin(Dustbin(0,100))
RouteManager.addDustbin(Dustbin(150,200))
RouteManager.addDustbin(Dustbin(100,100))
RouteManager.addDustbin(Dustbin(200,200))
RouteManager.addDustbin(Dustbin(0,200))

p1 = Route()
p1.generateIndividual()
print(p1.toString())

p2 = Route()
p2.generateIndividual()
print(p2.toString())

child = GA.crossover(p1, p2)
GA.mutate(child)
print (child.toString())
