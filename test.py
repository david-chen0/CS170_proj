import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
from solver import solve, removeCities, removeEdges
import glob
import os.path as path


if __name__ == '__main__':
	inputs = glob.glob('inputs/large/*')

	'''
	G = read_input_file(inputs[157])
	c, k = solve(G)
	print(c)
	print(k)
	G, city = removeCities(G, 1, 29)
	G, edge = removeEdges(G, 15, 29)
	print(city)
	print(nx.has_path(G, 0, 29))
	print(calculate_score(G, c, k))
	'''

	
	for input_path in inputs:
		output_path = 'outputs/large/' + path.basename(path.normpath(input_path))[:-3] + '.out'
		G = read_input_file(input_path)
		c, k = solve(G)
		assert is_valid_solution(G, c, k)
		distance = calculate_score(G, c, k)
		write_output_file(G, c, k, output_path)
	

	'''	
	endedOn = 125
	for num in range(len(inputs) - endedOn):
		input_path = inputs[endedOn + num]
		output_path = 'outputs/small/' + path.basename(path.normpath(input_path))[:-3] + '.out'
		G = read_input_file(input_path)
		c, k = solve(G)
		assert is_valid_solution(G, c, k)
		distance = calculate_score(G, c, k)
		write_output_file(G, c, k, output_path)
	'''