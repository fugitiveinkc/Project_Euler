def dijkstra(start, end, graph):
	"""

	Input: start node, end (list of nodes) and graph
	Graph: 2D list with node objects
	Node: value, previous, dist_source, neighbors, visited
	Returns: Nothing, just modified previous in nodes so that shortest path can be found from end.
	Note: Meant for matrices

	"""
	unvisited = [vertex for row in graph for vertex in row]
	current = start
	while True:
		if current in end or len(unvisited) == 0:
			break
		for vertex in current.neighbors: #I think this checks neighbors that are visited as well.
			if vertex.visited == True:
				continue
			else:
				distance = vertex.value + current.value + current.dist_source
				if distance < vertex.dist_source:
					vertex.dist_source = distance
					vertex.previous = current
		unvisited.remove(current)
		current.visited = True
		current = min(unvisited, key = lambda x: x.dist_source)


def path_sum(last_point, graph):
	"""
	
	Input: last point (starting here), graph
	Graph: 2D list with node objects
	Node: value, previous, dist_source, neighbors, visited
	Returns: The sum of the values in the shortest path (or any path)
	Note: Meant for matrices

	"""
	current = last_point
	path_sum = 0
	while True:
		#print current.value
		path_sum += current.value
		if not current.previous:
			break
		current = current.previous
	return path_sum	
