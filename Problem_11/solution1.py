'''

Title: Largest product in a grid

Problem: Given a grid, fine the greatest product of four adjacent numbers (up, down, left, right or diagonally).

Notes: Problem asks for solution for a 20x20 grid, but can this be easily generalize?

Status: grid_gen is complete. grid_largest_sum in progress.  

'''

#Read in grid (function)

def grid_gen(filename = 'grid.txt'):
	grid_file = open(filename)
	grid_str = []
	for line in grid_file:
		grid_str.append(line.strip('\n').split(' '))
	grid = []
	for r_i, row in enumerate(grid_str):
		grid.append([])
		for string in row:
			grid[r_i].append(int(string))
	return grid


#Algorithm for parsing through grid (keep track of largest sum, function)

'''


def grid_largest_sum(grid)
        #1) Pick the first row
        #2) Go through the elements of the row
        #3) Three sums to check. Must be distance of 3 away to apply
        largest_sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
               """go through grid and do some MATH""" 
                
                
	return largest_sum

'''

	


