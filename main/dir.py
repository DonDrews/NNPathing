NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def getPosAdjacent(pos, dir):
	if dir == NORTH:
		return(pos[0], pos[1] + 1)
	elif dir == EAST:
		return(pos[0] + 1, pos[1])
	elif dir == SOUTH:
		return(pos[0], pos[1] - 1)
	elif dir == WEST:
		return(pos[0] - 1, pos[1])

def getPosDir(pos, dir, magnitude):
	if dir == NORTH:
		return(pos[0], pos[1] + magnitude)
	elif dir == EAST:
		return(pos[0] + magnitude, pos[1])
	elif dir == SOUTH:
		return(pos[0], pos[1] - magnitude)
	elif dir == WEST:
		return(pos[0] - magnitude, pos[1])

def getDist(pos1, pos2):
	return (abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]))

