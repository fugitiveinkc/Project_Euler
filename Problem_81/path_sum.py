'''


Title: Problem 81 -- Path sum: two ways

Purpose: Only moving right and down and starting from the left top corner of a matrix, find the minimal path sum.

Note:
	-Dijkstra's algorithm would work here
	
'''
#Function used in every solution

def read_matrix(filename):
	matrix = open(filename, 'r')
	matrix = [row.strip('\n').split(',') for row in matrix]
	for row_index, row in enumerate(matrix):
		for col_index, col in enumerate(row):
			matrix[row_index][col_index] = int(col)
	return matrix


#--Solution 1 -- 11/28/2015--#


#Minimal path sum (recrusive -- breadth first)

def min_path_sum(row_index, col_index):
		
	current = matrix[row_index][col_index]
	
	try:
		right = matrix[row_index][col_index + 1]
	except:
		right = None
	try: 
		down = matrix[row_index + 1][col_index]
	except:
		down = None
	
	if right == None and down == None and current == matrix[len(matrix)-1][len(matrix[0])-1]:
		return current
	elif right == None and down == None:
		return float('inf')
	elif right == None:
		return current + min_path_sum(row_index+1, col_index)
	elif down == None:
		return current + min_path_sum(row_index, col_index+1)
	else:
		return min([current + min_path_sum(row_index+1, col_index), current + min_path_sum(row_index, col_index+1)])


#--Solution 2 -- 11/29/2015--#


#Use dijkstra's algorithm

from Node import node #node(value, index, neighbors) 

def generate_map(matrix): #Generates a list with every matrix value as a node.  Neighbors part is incomplete.
	generated_map = []
	for row_index, row in enumerate(matrix):
		generated_map.append([])
		for col_index, element in enumerate(row):
			current_node = node()
			current_node.value = element
			current_node.index = (row_index, col_index)
			generated_map[row_index].append(current_node)

	#Now update all the neighbors
	for row_index, row in enumerate(generated_map):
		for col_index, _ in enumerate(row):
			if col_index != len(row)-1 and row_index != len(generated_map)-1:
				generated_map[row_index][col_index].neighbors = [generated_map[row_index+1][col_index], generated_map[row_index][col_index+1]]	
			elif col_index == len(row)-1 and row_index == len(generated_map)-1:
				continue
			
			elif col_index == len(row)-1:
				generated_map[row_index][col_index].neighbors = [generated_map[row_index+1][col_index]]	

			elif row_index == len(row)-1:
				generated_map[row_index][col_index].neighbors = [generated_map[row_index][col_index+1]]	

	return generated_map

