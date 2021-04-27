import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob
import random


def solve(G):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    start = 0
    target = len(G) - 1

    if len(G) >= 20 and len(G) <= 30:
        C = 1 #Number of cities to remove
        K = 15 #Number of edges to remove
    elif len(G) > 30 and len(G) <= 50:
        C = 3
        K = 50
    elif len(G) > 50 and len(G) <= 100:
        C = 5
        K = 100

    CK_list = [] #List of edges and cities to remove
    numIterations = len(G) #Number of iterations for later randomization


    #All nodes then all edges strategy
    G_prime, c0 = removeCities(G, C, target)
    G_prime, k0 = removeEdges(G_prime, K, target)
    CK_list.append([c0, k0])

    #All edges then all nodes strategy
    G_prime, k1 = removeEdges(G, K, target)
    G_prime, c1 = removeCities(G_prime, C, target)
    CK_list.append([c1, k1])

    #Chooses cities and edges to remove randomly one at a time
    #Probability is the probability of removing a city
    def randomChoice(probability = 50, skipChance = 0):
	    G_prime = G.copy()
	    C_prime = C
	    K_prime = K
	    c2, k2 = [], []
	    while C_prime > 0 and K_prime > 0:
	    	if random.randint(0, 100) < probability:
	    		G_prime, lst = removeCities(G_prime, 1, target)
	    		c2 += (lst)
	    		C_prime -= 1
	    	else:
	    		G_prime, lst = removeEdges(G_prime, 1, target)
	    		k2 += (lst)
	    		K_prime -= 1
	    G_prime, lst = removeCities(G_prime, C_prime, target)
	    c2 += (lst)
	    G_prime, lst = removeEdges(G_prime, K_prime, target)
	    k2 += (lst)
	    CK_list.append([c2, k2])


	#Random choice at every step strategy
    for __ in range(numIterations):
    	randomChoice()

    #Random choice favoring edges strategy
    for __ in range(numIterations):
    	randomChoice(20)

    #Random choice with a 5% chance to skip strategy
    for __ in range(numIterations):
    	randomChoice(50, 5)


    #Finds the maximal strategy and returns it
    CK_list_evaluated = list(map(lambda lst: calculate_score(G, lst[0], lst[1]), CK_list))
    max_index = CK_list_evaluated.index(max(CK_list_evaluated))
    print(max_index)
    return CK_list[max_index][0], CK_list[max_index][1]


#Removes up to C cities from graph G non-destructively and returns the new graph with C cities
#removed and a list of the C cities removed
def removeCities(G, C, target, skipChance = 0):
	if C == 0:
		return G, []

	start = 0

	shortestPath = nx.shortest_path(G, start, target)
	maxima = nx.dijkstra_path_length(G, start, target)

	removedCities = []
	G_prime = G.copy()

	#Loops until C cities are deleted or the shortest path length can no longer be increased
	while C > 0:

		#Vertex to be removed, if there is a suitable one
		max_vertex = None

		#Only removing nodes in the current shortest path will affect the SP length
		for vertex in shortestPath:

			#Skips over start and target nodes so that they are not deleted
			if vertex == start or vertex == target:
				continue

			G_test = G_prime.copy()
			G_test.remove_node(vertex)

			#Checks if start and target are still connected
			if not nx.has_path(G_test, start, target):
				continue

			#Find length of shortest s-t path with a single vertex removed
			cur_distance = nx.dijkstra_path_length(G_test, start, target)

			#Sets max_vertex to current vertex if this vertex produces a better result
			#If equal result, add with probability 1 - 0.01 * skipChance
			if cur_distance > maxima or (cur_distance == maxima and random.randint(1, 100) > skipChance):
				maxima = cur_distance
				max_vertex = vertex
		
		#Adds a vertex to be removed if beneficial, otherwise breaks out of the loop
		if max_vertex == None:
			break
		else:
			G_prime.remove_node(max_vertex)
			removedCities.append(max_vertex)
		
		shortestPath = nx.shortest_path(G_prime, start, target)
		C -= 1

	return G_prime, removedCities


#Removes up to K edges and returns the modified graph and a list of the K edges removed
def removeEdges(G, K, target, skipChance = 0):
	if K == 0:
		return G, []

	start = 0

	shortestPath = nx.shortest_path(G, start, target)
	maxima = nx.dijkstra_path_length(G, start, target)

	removedEdges = []
	G_prime = G.copy()

	#Loops until K edges are deleted or the shortest path length can no longer be increased
	while K > 0:

		#Edge to be removed
		max_edge = None

		#Temporary graph containing only the current shortest path
		pathGraph = nx.path_graph(shortestPath)

		#Only removing edges along the current shortest path can increase shortest path length
		for edge in pathGraph.edges():

			G_test = G_prime.copy()
			G_test.remove_edge(edge[0], edge[1])

			#Checks if start and target are still connected
			if not nx.has_path(G_test, start, target):
				continue

			#Find length of shortest s-t path with a single edge removed
			cur_distance = nx.dijkstra_path_length(G_test, start, target)

			#Sets max_edge to current edge if this edge produces a better result
			#If equal result, add with probability 1 - 0.01 * skipChance
			if cur_distance > maxima or (cur_distance == maxima and random.randint(1, 100) > skipChance):
				maxima = cur_distance
				max_edge = edge

		#Adds an edge to be removed if beneficial, otherwise breaks out of the loop
		if max_edge == None:
			break
		else:
			G_prime.remove_edge(max_edge[0], max_edge[1])
			removedEdges.append(max_edge)
			
		shortestPath = nx.shortest_path(G_prime, start, target)
		K -= 1

	return G_prime, removedEdges





# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     c, k = solve(G)
#     assert is_valid_solution(G, c, k)
#     print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
#     write_output_file(G, c, k, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('inputs/*')
#     for input_path in inputs:
#         output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G = read_input_file(input_path)
#         c, k = solve(G)
#         assert is_valid_solution(G, c, k)
#         distance = calculate_score(G, c, k)
#         write_output_file(G, c, k, output_path)
