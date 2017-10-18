from galogic import *

#routeManager = RouteManager()

dustbin = Dustbin(60, 200);
RouteManager.addDustbin(dustbin);

dustbin2 = Dustbin(180, 200);
RouteManager.addDustbin(dustbin2);

dustbin3 = Dustbin(80, 180);
RouteManager.addDustbin(dustbin3);
dustbin4 = Dustbin(140, 180);
RouteManager.addDustbin(dustbin4);

dustbin5 = Dustbin(20, 160);
RouteManager.addDustbin(dustbin5);

dustbin6 = Dustbin(100, 160);
RouteManager.addDustbin(dustbin6);

dustbin7 = Dustbin(200, 160);
RouteManager.addDustbin(dustbin7);

dustbin8 = Dustbin(140, 140);
RouteManager.addDustbin(dustbin8);

dustbin9 = Dustbin(40, 120);
RouteManager.addDustbin(dustbin9);

dustbin10 = Dustbin(100, 120);
RouteManager.addDustbin(dustbin10);

dustbin11 = Dustbin(180, 100);
RouteManager.addDustbin(dustbin11);

dustbin12 = Dustbin(60, 80);
RouteManager.addDustbin(dustbin12);

dustbin13 = Dustbin(120, 80);
RouteManager.addDustbin(dustbin13);

dustbin14 = Dustbin(180, 60);
RouteManager.addDustbin(dustbin14);

dustbin15 = Dustbin(20, 40);
RouteManager.addDustbin(dustbin15);

dustbin16 = Dustbin(100, 40);
RouteManager.addDustbin(dustbin16);

dustbin17 = Dustbin(200, 40);
RouteManager.addDustbin(dustbin17);

dustbin18 = Dustbin(20, 20);
RouteManager.addDustbin(dustbin18);

dustbin19 = Dustbin(60, 20);
RouteManager.addDustbin(dustbin19);

dustbin20 = Dustbin(160, 20);
RouteManager.addDustbin(dustbin20);

pop = Population(50, True)
print ('Initial distance: ' + str(pop.getFittest().getDistance())

#pop = GA.evolvePopulation(pop)
for i in range(100):
    pop = GA.evolvePopulation(pop)
print ('Finished')
print ('Final distance: ' + pop.getFittest().getDistance())
print ('Solution: ')
print (pop.getFittest())
