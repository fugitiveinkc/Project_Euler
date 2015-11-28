'''


Title: Problem 81 -- Path sum: two ways

Purpose: Only moving right and down and starting from the left top corner of a matrix, find the minimal path sum.


'''

#--Solution 1 -- 11/28/2015--#


#Path sum traversal function (Recursive)

#def min_path_sum(matrix):
	

#Read in matrix file

matrix = open('p081_matrix.txt','r')
matrix = [row.strip('\n').split(',') for row in matrix]
for r, row in enumerate(matrix):
	for c, col in enumerate(row):
		matrix[r][c] = int(col)

		
