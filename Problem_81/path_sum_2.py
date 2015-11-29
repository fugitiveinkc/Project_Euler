'''


Title: Problem 81 -- Path sum: two ways

Purpose: Only moving right and down and starting from the left top corner of a matrix, find the minimal path sum.

Note:
	-Problem with function (misread problem!)
	-Need to addred what happens when you get to second to last column.
	-New idea: Test every permutation of right and down
	
'''

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





#Read in matrix file

matrix = open('test_matrix.txt','r')
matrix = [row.strip('\n').split(',') for row in matrix]
for row_index, row in enumerate(matrix):
	for col_index, col in enumerate(row):
		matrix[row_index][col_index] = int(col)
print min_path_sum(0, 0)
