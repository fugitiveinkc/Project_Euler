class Node:

	def __init__(self, value = 0, previous = None, dist_source = float('inf'), neighbors = []):
		self.value = value
		self.previous = previous
		self.dist_source = float('inf')
		self.neighbors = neighbors
