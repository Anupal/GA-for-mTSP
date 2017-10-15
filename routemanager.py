from dustbin import *

class RouteManager:
    destinationDustbins = []

    def addDustbin (self, db):
        destinationDustbins.append(db)

    def getDustbin (self, index):
        return destinationDustbins[index]

    def numberOfDustbins():
        return len(destinationDustbins)
