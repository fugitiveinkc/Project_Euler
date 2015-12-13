'''

Title: Problem 99 -- Largest exponential

Objective: Find the line number with the greatest exponential value

Note:
	-Waaaay too slow.  Needs to optimize how I find the exponential
'''

#Read in file

text = open('p099_base_exp.txt')
file_lines = [line.strip('\n').split(',') for line in text]
exponentials = [(int(line[0]), int(line[1])) for line in file_lines]


#Find largest exponential and line number

largest_exponential = 0
largest_line_number = 0
for line_number in range(len(exponentials)):
		a, b = exponentials[line_number]
		print a
		if a**b > largest_exponential:
			largest_line_number = line_number+1
print largest_line_number
			
