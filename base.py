import MultiNEAT as NEAT
import gui.render as rn

window = rn.Window()
params = NEAT.Parameters()
params.PopulationSize = 100
#INPUTS:
#0 bias
#1-4 distance to walls in cardinal directions
#5 x distance to goal
#6 y distance to goal
#7 directrion to goal

#OUTPUTS
#0 x movement
#1 y movement

genome = NEAT.Genome(0, 8, 0, 2, False, NEAT.ActivationFunction.SIGNED_SIGMOID, NEAT.ActivationFunction.SIGNED_SIGMOID, 0, params)
pop = NEAT.Population(genome, params, True, 1.0)

def simGeneration():
	genomeList = NEAT.GetGenomeList(pop)

	for g in genomeList:
		fitness = evaluate(g)
		g.SetFitness(fitness)

	pop.Epoch()
	
