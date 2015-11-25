'''

Title: Problem 7 -- 10001st Prime

Goal: In title

'''

#Solution 1 -- 11/24/2015

#Necessary libraries

from math import sqrt, ceil
from itertools import count

#Function for testing primality

def prime_testing(number):
	for x in range(2, int(ceil(sqrt(number))+1)): #Only need to test between 2 and sqrt of number	
		if number%x == 0:
			return False
	return True

#Calculate 10001st prime

while True:
	prime_counter = 2
	for y in count(4):
		if prime_testing(y):
			prime_counter += 1
		if prime_counter == 10001:
			print y
			break
	break


'''

Notes:
-In prime_testing, perhaps I can use a more efficient generator?
-When I calculate 10001st prime, it looks a bit messy

'''
