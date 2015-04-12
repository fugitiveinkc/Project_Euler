'''

Problem title:  Multiples of 3 and 5
Summary: Find sum of all the multiples of 3 or 5 below 1000

'''


def problem_1(number):
	summation=0
	for x in range(1,number):
		if x%3==0:
			summation+=x
		elif x%5==0:
			summation+=x
	print("The sum is: " + str(summation))

		
