from galogic import *

#routeManager = RouteManager()
#TODO: Add provision for multiple salesmen
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

pop = Population(50, True)
print ('Initial distance: ' + str(pop.getFittest().getDistance()))

for i in range(101):
    pop = GA.evolvePopulation(pop)
    fittest = pop.getFittest().getDistance()
    if fittest < 1050:
        break
print ('Final distance: ' + str(fittest))
print ('Final Route: ' + pop.getFittest().toString())
