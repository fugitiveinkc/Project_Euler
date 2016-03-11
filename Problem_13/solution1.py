'''

Title: Large sum

Objective: Given a list of one-hundred 50-digit numbers, sum them and print out the first 10 digits.

Notes:
	-Python handles really large numbers, so this is a lot easier than expected.
	-What if Python couldn't handle such large numebrs?  What then?

'''

numbers = open('numbers.txt')
numbers = numbers.readlines()
numbers = [int(x.strip('\n')) for x in numbers]
summation = sum(x for x in numbers)
print str(summation)[1:11]
