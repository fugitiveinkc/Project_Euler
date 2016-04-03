'''

Title: Problem 18 Maximum Path Sum

Problem: Given a pyramid of numbers, find the maximumpath sum from top to bottom.

Current State: Gives wrong answer (algorithm logic is wrong)
	-Not using brute force.  (Using dijkstra's algorithm reverse)
	-Reason why not working: Dijkstra's algorithm cannot handle negative weights.  Try bellman-ford or find some other way.	

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
				graph[r].append(node(-int(element[1:])))
			else:
				graph[r].append(node(-int(element)))
	
	for r in range(0, len(graph)-1): #Updates neighbors
		for e in range(0, len(graph[r])):
			graph[r][e].neighbors = [graph[r+1][e], graph[r+1][e+1]]

	graph[0][0].distance = graph[0][0].value

	return graph


#Traverse graph for max path

def traverse_max(first_node):
	visited = [first_node]
	while True:
		current_sum = 0	
		for a_node in visited: #Main traversal algorithm
			#print a_node.value
			for b_node in a_node.neighbors:
				#print b_node.value
				if a_node.distance + b_node.value < b_node.distance:
					b_node.distance = a_node.distance + b_node.value
					if b_node.distance < current_sum:
						current_sum = b_node.distance
						current_node = a_node
						next_node = b_node			
		current_node.neighbors.remove(next_node)
		next_node.previous = current_node
		visited.append(next_node)
		if not next_node.neighbors:
			break
	return next_node.distance*-1

if __name__ == '__main__':
	graph = graph_generator('pyramid2.txt')
	print 'Maximum path sum: ' + str(traverse_max(graph[0][0]))

			
