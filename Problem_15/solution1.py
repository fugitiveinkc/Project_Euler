'''

Title: Problem 15 -- Lattice paths

Problem: Given a lattice path n x n, start at the north west corner and can only travel south or east, what are all the possible pathways to get to the south east corner?

Notes:
	-Works, but too slow.  Currently, depth first recursion. (Updated: Doesn't duplicate work anymore!  SUPAH FAST!)

Extra:
	-Figured out closed form of solution = (2n)! / 2(n!)
'''

from node import Node
import sys

#Set up lattice path

def setupLattice(n, m): #Uses node count, not block count (+1)
	lattice = []
	for x in range(n):
		lattice.append([])
		for y in range(m):
			lattice[x].append(Node())
	for x in range(n):
		for y in range(m):
			if x == n-1 and y == m-1:
				lattice[x][y].end = True
				lattice[x][y].value = 1
			elif x == n-1:
				lattice[x][y].east = lattice[x][y+1]
			elif y == m-1:
				lattice[x][y].south = lattice[x+1][y]
			else:
				lattice[x][y].east = lattice[x][y+1]
				lattice[x][y].south = lattice[x+1][y]
		lattice[0][0].start = True
	return lattice


def traverseLattice(node):
	#1) Select start node and mark as visited
	#2) Check if last node.  If so, add to count.
	#3) Otherwise, check east and south.
	#4) Traverse value that hasn't been visited and call traverse
	#5) Mark as unvisited
	if node.end == True:
		return node.value
	else:
		for p in node.east, node.south:
			if p != None:
				if p.visited == True:
					node.value += p.value
				else:
					node.value += traverseLattice(p)
		node.visited = True
		return node.value
		

if __name__ == '__main__':
	lattice = setupLattice(int(sys.argv[1]), int(sys.argv[2]))
	print traverseLattice(lattice[0][0])
			
			
		

			
