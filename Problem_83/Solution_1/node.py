class Node:

	def __init__(self, value):
		self.value = value
		self.previous = None
		self.dist_source = float('inf')
		self.neighbors = []
		self.visited = False
