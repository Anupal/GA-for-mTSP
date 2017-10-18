from galogic import *
'''
RouteManager.addDustbin(Dustbin(0,0))
RouteManager.addDustbin(Dustbin(0,100))
RouteManager.addDustbin(Dustbin(150,200))
RouteManager.addDustbin(Dustbin(100,100))
RouteManager.addDustbin(Dustbin(200,200))
RouteManager.addDustbin(Dustbin(0,200))
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

p1 = Route()
p1.generateIndividual()
print(p1.toString())
print(p1.getDistance())
print(p1.getFitness())

#p2 = Route()
#p2.generateIndividual()
#print(p2.toString())

#child = GA.crossover(p1, p2)
#print (child.toString())
#GA.mutate(child)
#print (child.toString())
