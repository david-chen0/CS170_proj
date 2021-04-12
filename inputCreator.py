import random

def createInput(V, k, c):

	#Check for valid arguments
	assert isinstance(V, int), "Please enter an integer value for V."
	assert isinstance(k, int), "Please enter an integer value for k."
	assert isinstance(c, int), "Please enter an integer value for c."

	#Begin printing
	print(V)

	#First make sure that every edge has a degree of at least 2
	for num in range(V):
		i = 0
		while i < 2:
			end = randint(0, V - 1)
			if end != num:
				print(num + " " + end + " " + randint(1, 100))
				i++

	#Now add some extra edges
	numEdges = randint(1, 20)

	i = 0
	while i < numEdges:
		start = randint(0, V - 1)
		end = randint(0, V - 1)
		if start != end:
			print(start + " " + end + " " + randint(1, 100))
			i++