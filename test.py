import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
from solver import solve

G = read_input_file('50.in')
c, k = solve(G)
print(c)
print(k)
print(calculate_score(G, c, k))

#write_output_file(G_30, c, k, '30.out')