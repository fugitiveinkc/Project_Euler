'''


Title: Problem 81 -- Path sum: two ways

Purpose: Only moving right and down and starting from the left top corner of a matrix, find the minimal path sum.

Note:
	-Problem with function (misread problem!)
	-Need to addred what happens when you get to second to last column.
	-New idea: Test every permutation of right and down
	
'''

#--Solution 1 -- 11/28/2015--#


#Path sum traversal function (Recursive)



#Read in matrix file

matrix = open('test_matrix.txt','r')
matrix = [row.strip('\n').split(',') for row in matrix]
for row_index, row in enumerate(matrix):
	for col_index, col in enumerate(row):
		matrix[row_index][col_index] = int(col)
