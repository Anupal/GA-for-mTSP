import random
import math

xMax = 200
yMax = 200

class Dustbin:

	def __init__ (self):
		self.x = random.randint(0, xMax)
		self.y = random.randint(0, yMax)

	def __init__ (self, x, y):
		self.x = x
		self.y = y

	def getX (self):
		return this.x

	def getY (self):
		return this.y

	def distanceTo (self, db):
		xDis = abs(getX() - db.getX())
		yDis = abs(getY() - db.getY())
		dis = math.sqrt((xDis*xDis), (yDis*yDis))
		return dis

	def toString (self):
		s =  '(' + str(getX()) + ',' + str(getY) + ')'
		return s
