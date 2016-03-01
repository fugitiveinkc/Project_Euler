'''

Title: Largest product in a grid

Problem: Given a grid, fine the greatest product of four adjacent numbers (up, down, left, right or diagonally).

Notes: Problem asks for solution for a 20x20 grid, but can this be easily generalize?
    Update: I've generalize the code so that a person can input how large of cluster they want to find products for.

Status: grid_gen is complete. grid_largest_prod is complete.  

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


#Algorithm for parsing through grid (keep track of largest prod, function)

def grid_largest_prod(grid, cluster_num):
        #1) Pick the first row
        #2) Go through the elements of the row
        #3) Three prods to check. Must be distance of 3 away to apply
        largest_prod = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                #Proceed to calculating possible right, down, SW and NW diagonals
                if c <= len(grid[0])-cluster_num: #Right
                    temp = reduce(lambda x,y:x*y, [grid[r][c+i] for i in range(cluster_num)])
                    if temp > largest_prod:
                        largest_prod = temp
                if r <= len(grid)-cluster_num: #Down
                    temp = reduce(lambda x,y:x*y, [grid[r+i][c] for i in range(cluster_num)])
                    if temp > largest_prod:
                        largest_prod = temp
                if c <= len(grid[0])-cluster_num and r <= len(grid)-cluster_num: #SW Diag
                    temp = reduce(lambda x,y:x*y, [grid[r+i][c+i] for i in range(cluster_num)])
                    if temp > largest_prod:
                        largest_prod = temp
                if r >= cluster_num-1 and c <= len(grid[0])-cluster_num: #NW Diag
                    temp = reduce(lambda x,y:x*y, [grid[r-i][c+i] for i in range(cluster_num)])
                    if temp > largest_prod:
                        largest_prod = temp
	return largest_prod

grid = grid_gen()
print grid_largest_prod(grid, 4) #Cluster number is 4 since question asks for highest product with 4 adjacent numbers

	


