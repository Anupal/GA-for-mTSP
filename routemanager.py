from dustbin import *

class RouteManager:
    destinationDustbins = []

    @classmethod
    def addDustbin (cls, db):
        cls.destinationDustbins.append(db)

    @classmethod
    def getDustbin (cls, index):
        return cls.destinationDustbins[index]

    @classmethod
    def numberOfDustbins(cls, self):
        return len(cls.destinationDustbins)
