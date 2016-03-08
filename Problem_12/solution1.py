'''

Title: Highly Divisible Triangular Number

Problem: What is the value of the first triangle number to have over five hundred divisors?

Notes: 
	-The nth triangle number is the sum of te first n natural numbers.
	-Currently too slow.  Need to optimize or use different algorithm.
		-Factoring here is too slow I believe (use prime factorization to speed up?)
'''

from itertools import count


#Functions: triangle number generator, factor counter

def tri_num_gen(index):
	return sum([x for x in range(1,index+1)])

def factor_count(number):
	count = 0
	for x in range(1,number+1):
		if number%x == 0:
			count += 1
	return count


#Main operations

for x in count(1):
	temp = tri_num_gen(x)
	if factor_count(temp) > 5:
		print temp
		break

