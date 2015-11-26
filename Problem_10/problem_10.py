'''


Title: Problem 10 -- Summation of primes

Goal: Find the sum of all the primes below two million

Notes:
	-A bit slow for my tastes.  Find ways to speed up.


'''

#--Solution 1 -- 11/25/2015--#


#Import necessary libraries

from math import sqrt


#Function for determining primality

def primality(number):
	if number < 2:
		return False
	else:
		for x in range(2,int(sqrt(number))+1):
			if number%x == 0:
				return False
		return True


#Sum of all primes below two million

sum_primes = sum((x for x in range(2000000) if primality(x)))
print sum_primes 



