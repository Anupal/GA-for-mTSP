import random
import math

xMax = 200
yMax = 200

class Dustbin:

	def __init__ (self, x = None, y = None):
		if x == None and y == None:
			self.x = random.randint(0, xMax)
			self.y = random.randint(0, yMax)
		else:
			self.x = x
			self.y = y

	def getX (self):
		return this.x

	def getY (self):
		return this.y

	def distanceTo (self, db):
		xDis = abs(self.getX() - db.getX())
		yDis = abs(self.getY() - db.getY())
		dis = math.sqrt((xDis*xDis), (yDis*yDis))
		return dis

	def toString (self):
		s =  '(' + str(getX()) + ',' + str(getY) + ')'
		return s
