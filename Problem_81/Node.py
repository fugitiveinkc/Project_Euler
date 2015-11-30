class node:

	'''
	This class will be useful to convert the matrix into
	a map of vertices.  Each value in the matrix will be
	a node.
	'''

	def __init__(self, value = 0, index = (None, None), neighbors = []):
		self.value = value
		self.index = index
		self.neighbors = neighbors
		self.visited = False
		self.next_node = None
