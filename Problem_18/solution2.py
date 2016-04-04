'''

Title: Solution 2 to Problem 18 -- Maximum Path Sum I

Revision: Used pyramid simplification as algorithm
	-How it works: Starts at the base and simplifies the next row by adding only feasible numbers from the row below it.  The pyramid becomes reduced by one row each iteration.

'''
import sys

#Read in pyramid

pyramid = open(sys.argv[1])
pyramid = [line.strip('\n').split(' ') for line in pyramid]
pyramid = pyramid[::-1] #upside-down pyramid
pyramid_int = []
for r, row in enumerate(pyramid):
	pyramid_int.append([])
	for x in row:
		pyramid_int[r].append(int(x))


#Go through pyramid and simplify (start from bottom row and add top row based on only feasible solutions) -- pyramid has been inverted to make this easier

for r, row in enumerate(pyramid_int[:len(pyramid_int)-1]):
	for i in range(0,len(row)-1):
		if row[i] > row[i+1]:
			pyramid_int[r+1][i] += row[i]
		else:
			pyramid_int[r+1][i] += row[i+1]

print 'Maximum path sum: ' + str(pyramid_int[::-1][0][0]) #Re-invert pyramid and top element should be solution
