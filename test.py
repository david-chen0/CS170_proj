import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
from solver import solve

G_30 = read_input_file('30.in')
c, k = solve(G_30)
print(c)
print(k)
print(calculate_score(G_30, c, k))

#write_output_file(G_30, c, k, '30.out')