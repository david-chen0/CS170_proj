import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob


def solve(G):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    #First find the best c cities to remove(if none helpful then move on)
    #then find best k edges to remove

    C = 1 #Number of cities to remove
    K = 15 #Number of edges to remove

    #Returns the modified graph and the cities removed
    G_prime, c = removeCities(G, C)


def removeCities(G, C):
	start = 0
	target = len(G.nodes())
	minima = nx.shortest_path(G, start, target)

	removedCities = []
	G_prime = G

	#Loops until C cities are deleted or the length can no longer decrease
	while C > 0:
		minima = nx.shortest_path(G_prime, start, target) #Current shortest distance
		min_vertex = None #Vertex to be removed, if there is one
		for vertex in G_prime.nodes():
			if vertex == start or vertex == target:
				continue
			G_test = G_prime.remove_node(vertex) #Check if this is destructive, if so make changes
			cur_distance = nx.shortest_path(G_test, start, target) #Find length of s-t path with a single vertex removed
			if cur_distance < minima:
				minima = cur_distance
				min_vertex = vertex
		if min_vertex == None:
			break
		else:
			G_prime = G_prime.remove_node(vertex)
			removedCities.append(min_vertex)

	return G_prime, removedCities



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
