import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
from solver import solve
import glob
import os.path as path


if __name__ == '__main__':
	inputs = glob.glob('inputs/small/*')

	#This is the part I added to use for sample testing, rest is needed to write out final file

	'''
	G = read_input_file(inputs)
	c, k = solve(G)
	print(c)
	print(k)
	print(calculate_score(G, c, k))
	'''

	'''
	for input_path in inputs:
		output_path = 'outputs/small/' + path.basename(path.normpath(input_path))[:-3] + '.out'
		G = read_input_file(input_path)
		c, k = solve(G)
		assert is_valid_solution(G, c, k)
		distance = calculate_score(G, c, k)
		write_output_file(G, c, k, output_path)
	'''

	'''
	for num in range(1):
		input_path = inputs[2 + num]
		print(input_path)
		output_path = 'outputs/small/' + path.basename(path.normpath(input_path))[:-3] + '.out'
		G = read_input_file(input_path)
		c, k = solve(G)
		assert is_valid_solution(G, c, k)
		distance = calculate_score(G, c, k)
		write_output_file(G, c, k, output_path)
	'''

	'''
	for num in range(len(inputs) - 157):
		input_path = inputs[157 + num]
		output_path = 'outputs/small/' + path.basename(path.normpath(input_path))[:-3] + '.out'
		G = read_input_file(input_path)
		c, k = solve(G)
		assert is_valid_solution(G, c, k)
		distance = calculate_score(G, c, k)
		write_output_file(G, c, k, output_path)
		print(num)
	'''

	print(inputs[157])