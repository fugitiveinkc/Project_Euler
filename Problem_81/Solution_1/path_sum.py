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


