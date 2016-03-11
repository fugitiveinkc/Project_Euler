'''

Supplement to solution 2.

Counting factors here is designed with prime factorization which relies on determination of primeness

'''

from math import sqrt
from itertools import count

def prime(number): #Self explanatory.  Only checks up to sqrt of the number factors.
	if number <= 1:
		return False
	else:
		for x in range(2, int(sqrt(number))+1):
			if number%x == 0:
				return False
		return True

def prime_factorization(number):
	'''
	1) Checks to see if number is prime first
	2) Uses a prime generator and divides until it can't anymore
	3) Keeps track of number of primes in a dictionary and returns this
	'''
	prime_gen = (x for x in count(1) if prime(x))
	powers_dict = dict()
	next_value = number
	if prime(number):
		powers_dict[number] = 1
		return powers_dict
	for p in prime_gen:
		while True:
			if not p in powers_dict:
				powers_dict[p] = 0
			if next_value%p == 0:
				next_value = next_value/p
				powers_dict[p] += 1
				if prime(next_value): #Determination if we finally made it to last prime
					if not next_value in powers_dict:
						powers_dict[next_value] = 1
					else:
						powers_dict[next_value] += 1
					return powers_dict
			else:
				break

def factor_count(number):
	powers_dict = prime_factorization(number)
	product = 1
	for p in powers_dict:
		if powers_dict[p] > 0:
			product *= powers_dict[p]+1	
	return product

				
