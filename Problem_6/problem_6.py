'''

Title: Problem 6 -- Sum Square difference

Goal: Find difference between sum of the square and square of the sum of the first 100 natural numbers

'''

#Solution 1 -- 11/24/2015

sum_of_squares = 0
summation = 0

for i in range(1,101):
	sum_of_squares += i**2
	summation += i

difference = abs(sum_of_squares - summation**2)
print difference

#Solution 2 -- Unknown right now


