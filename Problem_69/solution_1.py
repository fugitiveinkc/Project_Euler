'''

Title: Problem 69 -- Totient Maximum

Purpose: for n <= 1,000,000, find where n/totient(n) is a maximum

'''

#--Solution 1 -- 01/05/2015--#

from math import sqrt

def totient(n):
	count = 1
	for x in range(2,n):
		if coprime(n,x):
			count += 1
	return count

def coprime(n,m):
	Min = min(n,m)
	Max = max(n,m)
	#print "Min: " + str(Min)
	#print "Max: " + str(Max)
	for x in (y for y in range(2,Min+1) if Min%y==0):
		if Max%x == 0:
			return False
	#print "Coprime!"
	return True


current_max = 0
for n in range(11):
	if float(n)/totient(n) > current_max:
		current_max = n
print current_max 
