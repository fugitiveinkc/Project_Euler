'''

Problem title: Largest prime factor
Problem summary: What is the largest prime factor of the number 6008511475143

'''

from math import ceil,sqrt

def factors(a):
	factors=[]
	for x in xrange(1,int(sqrt(a+1))):
		if a%x==0:
			factors.append(x)
	return factors	

def prime(b):
	for x in range(2,int(sqrt(b))):
		if b%x==0:
			return False
	return True

testing_value=600851475143
factors=factors(testing_value)
highest_prime_factor=0
for x in factors:
	if prime(x):
		highest_prime_factor=x
print(highest_prime_factor)
