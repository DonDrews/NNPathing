#each net tested is converted into a unit for evaluation
class Unit:

	def __init__(self, nn, xPos, yPos):
		self.net = nn
		self.x = xPos
		self.y = yPos
