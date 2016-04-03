'''

Title: Problem 18 Maximum Path Sum

Problem: Given a pyramid of numbers, find the maximumpath sum from top to bottom.

Current State: Gives wrong answer (algorithm logic is wrong)
	-Not using brute force.  

'''

from Node import node

#Read in pyramid and create graph

def graph_generator(filename):
	pyramid = open(filename)
	pyramid = [line.strip('\n').split(' ') for line in pyramid]
	#print pyramid
	graph = []
	for r, row in enumerate(pyramid): #Creates nodes
		graph.append([])
		for element in row:
			if element[0] == '0':
				graph[r].append(node(int(element[1:])))
			else:
				graph[r].append(node(int(element)))
	
	for r in range(0, len(graph)-1): #Updates neighbors
		for e in range(0, len(graph[r])):
			graph[r][e].neighbors = [graph[r+1][e], graph[r+1][e+1]]
	return graph


#Traverse graph for max path

def traverse_max(first_node):
	visited = [first_node]
	while True:
		current_sum = 0	
		for a_node in visited: #Main traversal algorithm
			#print a_node.value
			for b_node in a_node.neighbors:
				if a_node.value + b_node.value > current_sum: #Problem here?
					current_sum = a_node.value + b_node.value
					current_node = a_node
					next_node = b_node
		current_node.neighbors.remove(next_node)
		next_node.previous = current_node
		visited.append(next_node)
		if not next_node.neighbors:
			break
	values = [visited[len(visited)-1].value]
	previous = visited[len(visited)-1].previous
	while previous != None: #Traverses maximum path and creates list of values
		#print previous.value
		values.append(previous.value)
		previous = previous.previous	
	return sum(values)

graph = graph_generator('pyramid.txt')
print 'Maximum path sum: ' + str(traverse_max(graph[0][0]))

			
