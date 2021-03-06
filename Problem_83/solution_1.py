#--Solution 1 -- 12/2/2015--#

from node import Node


#Function used to import matrix

def read_matrix(filename):
	matrix = open(filename, 'r')
	matrix = [row.strip('\n').split(',') for row in matrix]
	for row_index, row in enumerate(matrix):
		for col_index, col in enumerate(row):
			matrix[row_index][col_index] = int(col)
	return matrix


#Function used to generate graph

def graph_generator(matrix):
	#Generate map
	graph = []
	for r_i, row in enumerate(matrix):
		graph.append([])
		for c_i, col_value in enumerate(row):
			graph[r_i].append(Node(col_value))	
	#Update neighbors between each node
	for r_i, row in enumerate(graph):
		for c_i, vertex in enumerate(row): #Below is all edge cases (Better way to do this?)
			if  r_i == 0 and c_i == 0:
				vertex.neighbors = [graph[r_i+1][c_i], graph[r_i][c_i+1]]
 			elif r_i == len(matrix)-1 and c_i == 0:
				vertex.neighbors = [graph[r_i-1][c_i], graph[r_i][c_i+1]]
			elif r_i == len(matrix)-1 and c_i == len(row)-1:
				vertex.neighbors = [graph[r_i-1][c_i], graph[r_i][c_i-1]]
			elif r_i == 0 and c_i == len(row)-1:
				vertex.neighbors = [graph[r_i+1][c_i], graph[r_i][c_i-1]]
			elif r_i == 0:
				vertex.neighbors = [graph[r_i][c_i-1], graph[r_i+1][c_i], graph[r_i][c_i+1]]
			elif c_i == len(row)-1:
				vertex.neighbors = [graph[r_i+1][c_i], graph[r_i][c_i-1], graph[r_i-1][c_i]]
			elif r_i == len(matrix)-1:
				vertex.neighbors = [graph[r_i][c_i-1], graph[r_i-1][c_i], graph[r_i][c_i+1]]
			elif c_i == 0:
				vertex.neighbors = [graph[r_i+1][c_i], graph[r_i][c_i+1], graph[r_i-1][c_i]]
			else:
				vertex.neighbors = [graph[r_i][c_i-1], graph[r_i+1][c_i], graph[r_i][c_i+1], graph[r_i-1][c_i]]


	graph[0][0].dist_source = 0 #This is the source
	return graph


#Function to execute dijkstra's algorithm

def d_algorithm(graph):
	unvisited = [vertex for row in graph for vertex in row]
	current = graph[0][0]
	while True:
		if current == graph[-1][-1] or len(unvisited) == 0:
			break
		for vertex in current.neighbors: 
			if vertex.visited == True:
				continue
			else:
				distance = vertex.value + current.value + current.dist_source
				if distance <= vertex.dist_source:
					vertex.dist_source = distance
					vertex.previous = current
		unvisited.remove(current)
		current.visited = True
		current = min(unvisited, key = lambda x: x.dist_source)

#Function to print shortest path sum

def shortest_path_sum(graph):
	current = graph[-1][-1]
	path_sum = 0
	while True:
		path_sum += current.value
		if not current.previous:
			break
		current = current.previous
	return path_sum	


matrix = read_matrix('p081_matrix.txt')
graph = graph_generator(matrix)
d_algorithm(graph)
solution = shortest_path_sum(graph)
print solution
