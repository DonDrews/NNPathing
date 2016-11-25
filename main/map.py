import numpy
import random

#constants
FLOOR = 0
WALL = 1

class Map:

	def __init__(self, x, y)
		self.raster = numpy.zeros(x, y)
		self.obstacles = []
		
		#make obstacles
		for i in range(20):
			xPos = random.randint(1, x - 1)
			yPos = random.randint(1, y - 1)
			width = random.randint(1, int(x / 2))
			height = random.randint(1, int(y / 2))
			
			#check for fitting
			if xPos + width > x - 1:
				width = x - (xPos + 1)

			if yPos + height > y - 1:
				height = y - (yPos + 1)

			#add
			self.obstacles.append(Obstacle(xPos, yPos, width, height))

		for o in self.obstacles:
			o.addToRaster(self.raster)

		#pick goal and start
		self.start = self.pickSidePoint(False)
		self.goal = self.pickSidePoint(True)

	def pickSidePoint(self, isGoal):
		x = random(0, self.raster.shape[0])
		if isGoal:
			return (x, 0)
		else:
			return (x, self.raster.shape[1])

class Obstacle:

	def __init__(self, xPos, yPos, width, height):
		self.x = xPos
		self.y = yPos
		self.w = width
		self.h = height

	def addToRaster(raster):
		for xCoord in range(self.x, self.x + self.width):
			for yCoord in range(self.y, self.y + self.height):
				raster[xCoord][yCoord] = WALL
