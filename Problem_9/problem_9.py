'''


Title: Problem 9 -- Special Pythagorean Triplet

Goal: Find a pythagorean triplet where a + b + c = 1000

Notes:
	-a, b and c must be less than 1000
	-a < b < c
	-First solution isn't too slow, but slower than I'd like.

'''

#--Solution 1 -- 11/25/2015--#


#Import necessary libraries

from itertools import combinations_with_replacement as combor


#Find the special pythagorean triplet

for a,b,c in ((x,y,z) for (x,y,z) in combor(range(1,999), 3) if x < y and y < z): #Used a generator!
	if a + b + c == 1000 and a**2 + b**2 == c**2:
		print "Special Pythagorean Triple: " + str((a,b,c))
		print "Product of triple: " + str(a*b*c)
		break
		
			

