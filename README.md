# CS 170 Project Spring 2021

This is David Chen's CS 170 Project for Spring 2021.

How to run solve() on input files stored in input/:

  Create a pointer to the inputs(inputs = glob.glob(inputs/*)

  Mark the specific input file you want(ex: for input file at index i, file = inputs[i])
  
  Create the graph from the input file(G = read_input_file(file))
  
  Run solve on the graph(c, k = solve(G))
  
  Write the output file with these results to any specified output_path(write_output_file(G, c, k, output_path))


Take a look at test.py for examples on how to run solve() on input files and create corresponding output files.
