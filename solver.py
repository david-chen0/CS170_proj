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

    print('refer to ideas.txt line 12')

    #Returns the modified graph and the cities removed
    G_prime, c = removeCities(G, C)

    #Returns the modified graph and the edges removed
    G_prime, k = removeEdges(G, C, len(G) - 1)


#Removes up to C cities from graph G non-destructively and returns the new graph with C cities
#removed and a list of the C cities removed
def removeCities(G, C):
	start = 0
	target = len(G.nodes()) - 1

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

			#Sets max_vertex to current vertex if this vertex produces a better or equal result
			if cur_distance >= maxima:
				maxima = cur_distance
				max_vertex = vertex
		
		#Adds a vertex to be removed if beneficial, otherwise breaks out of the loop
		if max_vertex == None:
			break
			print('refer to ideas.txt line 12')
		else:
			G_prime.remove_node(max_vertex)
			removedCities.append(max_vertex)
			C -= 1

	return G_prime, removedCities


#Removes up to K edges and returns the modified graph and a list of the K edges removed
def removeEdges(G, K, target):
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
			G_test.remove_edge(edge)

			#Checks if start and target are still connected
			if not nx.has_path(G_test, start, target):
				continue

			#Find length of shortest s-t path with a single edge removed
			cur_distance = G_test.dijkstra_path_length(G_test, start, target)

			#Sets new max_edge to current edge if current edge produces a better or equal result
			if cur_distance >= maxima:
				maxima = cur_distance
				max_edge = edge

		#Adds an edge to be removed if beneficial, otherwise breaks out of the loop
		if max_edge == None:
			break
			print('Refer to ideas.txt line 12')
		else:
			G_prime.remove_edge(max_edge)
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
