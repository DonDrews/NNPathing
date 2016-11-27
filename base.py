import MultiNEAT as NEAT
import gui.render as rn
import main.unit as un
import main.map as mp

window = rn.Window()
params = NEAT.Parameters()
params.PopulationSize = 100
#INPUTS:
#0-3 distance to walls in cardinal directions
#4 x distance to goal
#5 y distance to goal
#6 directrion to goal

#OUTPUTS
#0 x movement
#1 y movement

genome = NEAT.Genome(0, 8, 0, 2, False, NEAT.ActivationFunction.SIGNED_SIGMOID, NEAT.ActivationFunction.SIGNED_SIGMOID, 0, params)
pop = NEAT.Population(genome, params, True, 1.0)

def simGeneration():
	genomeList = NEAT.GetGenomeList(pop)

	#make graph
	graph = mp.Map(20, 20)

	for g in genomeList:
		net = NEAT.NeuralNetwork()
		g.BuildPhenotype(net)
		fitness = evaluate(net, graph)
		g.SetFitness(fitness)

	pop.Epoch()
	
def evaluate(net, graph):
	timeTaken = 0
	#make unit
	u = un.Unit(net, graph.start)

	while !u.simulate(graph):
		#todo: render window
		sleep(0.1)
		timeTaken += 1
		
		#keep simulation time to a minimum
		if timeTaken > 1000:
			return 0

	return (1 / timeTaken)
