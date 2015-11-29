'''


Title: Problem 81 -- Path sum: two ways

Purpose: Only moving right and down and starting from the left top corner of a matrix, find the minimal path sum.

Note:
	-Problem with function

'''

#--Solution 1 -- 11/28/2015--#


#Path sum traversal function (Recursive)

def min_path_sum(row_index = 0, col_index = 0):
	
	try:
		rightward = matrix[row_index][col_index + 1]

	except IndexError:
		rightward = None

	try: 
		downward = matrix[row_index + 1][col_index]

	except IndexError:
		downward = None

	try:
		current_position = matrix[row_index][col_index]
	
	except IndexError:
		current_position = 0	

	if rightward == None and downward == None:
		return current_position

	elif rightward > downward:
		return current_position + min_path_sum(row_index + 1, col_index)

	elif downward > rightward:
		return current_position + min_path_sum(row_index, col_index + 1)

	else:
		return max([current_position + min_path_sum(row_index + 1, col_index), current_position + min_path_sum(row_index, col_index + 1)])
	
	


#Read in matrix file

matrix = open('p081_matrix.txt','r')
matrix = [row.strip('\n').split(',') for row in matrix]
for row_index, row in enumerate(matrix):
	for col_index, col in enumerate(row):
		matrix[row_index][col_index] = int(col)
solution = min_path_sum(0,0)		
print solution
