#--Solution 2 -- 12/4/2015--#


#Necessary libraries

import sys


#Solution based on recursive algorithm and dynamic programming

partition_table = {} #Cache for already computed values
def p(n = int(sys.argv[1]), m = int(sys.argv[2])):
	if n <= 1:
		return 1

	elif m > n: #When m > n, p(n, m) = p(n, n)
		try:
			return partition_table[(n, m)]
		except:
			partition_table[(n, m)] = p(n, n)
			return partition_table[(n, m)]

	try:
			return partition_table[(n, m)]
	except:
		total = 0
		for x in range(1,m+1):
			if (n-x, x) in partition_table:
				total += partition_table[(n-x, x)]
			else:
				partition_table[(n-x, x)] = p(n-x, x)
				total += partition_table[(n-x, x)]
		return total

print(p())
