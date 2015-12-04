'''


Title: Problem 76 -- Counting summations

Objective: Every number can be written as a summation of smaller numbers.  How many different ways can one hundred be written as a sum of at least two positive integers?

Note: Feels like recursion, but unsure at the moment.  Could also use combinations with repetition?
	-Currently doesn't work for 100.  Too slow


'''

#--Solution 1 -- 12/3/2015--#

#Import necessary libraries

from itertools import combinations_with_replacement
from sys import argv


#Brute force!

def partition_sum_count(number): #Slow because produces useless combinations
	total_sums = 0
	for choose in range(2,number+1):
		for numbers in combinations_with_replacement(range(1,number), choose): 
			if sum(numbers) == number:
				#print numbers
				total_sums += 1
	return total_sums

print(partition_sum_count(int(argv[1])))



