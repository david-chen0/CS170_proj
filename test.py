import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_score
from solver import solve, removeCities, removeEdges
import glob
import os.path as path


if __name__ == '__main__':
	inputs = glob.glob('inputs/small/*')

	locations = ['small/', 'medium/', 'large/']

	'''
	G = read_input_file(inputs[1])
	c, k = solve(G)
	output_path = 'outputs/small/' + path.basename(path.normpath(inputs[1]))[:-3] + '.out'
	write_output_file(G, c, k, output_path)
	'''

	
	for location in locations:
		inputs = glob.glob('inputs/' + location + '*')
		i = 1
		for input_path in inputs:
			output_path = 'outputs/' + location + path.basename(path.normpath(input_path))[:-3] + '.out'
			G = read_input_file(input_path)
			curScore = read_output_file(G, output_path)
			c, k = solve(G)
			distance = calculate_score(G, c, k)
			if distance < curScore:
				write_output_file(G, c, k, output_path)
			print("Finished " + location + i)
			i += 1
	

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