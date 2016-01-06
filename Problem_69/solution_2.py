from math import sqrt, ceil

def prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	else:
		for x in range(2,int(ceil(sqrt(n+1)))):
			if n%x == 0:
				return False
		return True

def totient(n):
	result = n
	primes = (x for x in range(1,1000001) if prime(x))
	for x in primes:
		if x > n:
			break
		elif n%x == 0:
			result *= (1-(1.0/x))
	return result


current_max = 0
for n in range(2,11):
	#if n/totient(n) > current_max:
	#current_max = n
	print n/totient(n)
#print current_max

	
