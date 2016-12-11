from . import dir
import math

#utility function
def convertToNet(x):
        if x < 0.5:
                return 1
        else:
                return (1 / x)

#each net tested is converted into a unit for evaluation
class Unit:

	def __init__(self, nn, pos):
		self.net = nn
		self.x = pos[0]
		self.y = pos[1]

	def simulate(self, graph):
		distances = [0, 0, 0, 0]
		#find distances to walls
		for i in range(4):
			dist = 0
			while True:
				if dir.getPosDir((self.x, self.y), i, dist) != 0:
					break
				dist += 1
			distances[i] = convertToNet(dist)

		#find goal x and y relative to unit
		diffX = graph.goal[0] - self.x
		diffY = graph.goal[1] - self.y

		#find direction to goal
		direction = math.atan2(diffY, diffX)

		#combine inputs
		inputs = distances
		inputs.append(diffX)
		inputs.append(diffY)
		inputs.append(direction)
		inputs.append(1.0) #bias

		#simulate in neural net
		self.net.Input(inputs)
		self.net.Activate()
		outputs = self.net.Output()

		#move if necessary
		movement = dir.getDirection(outputs[0], outputs[1])
		if movement != -1:
			self.move(graph, movement)

		#check for completion
		if (self.x, self.y) == graph.goal:
			return True
		else:
			return False


	def move(self, graph, move):
		newPos = dir.getPosAdjacent((self.x, self.y), move)

		#check for moving out of bounds
		if newPos[0] < 0 or newPos[1] < 0:
			return False

		if newPos[0] >= graph.raster.shape[0] or newPos[1] >= graph.raster.shape[1]:
			return False

		#check if moving into wall
		if graph.raster[newPos[0]][newPos[1]] != graph.FLOOR:
			return False

		self.x = newPos[0]
		self.y = newPos[1]
		return True

