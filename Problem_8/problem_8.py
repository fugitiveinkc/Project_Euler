'''

Title: Problem 8 -- Largest Product in a series

Goal: In a 1000-digit number, find thirteen adjacent digits that have the greatest product.

Notes:
	-How can this be written with generators?

'''

#--Solution 1 -- 11/25/2015--#

#Read in number from file

raw_number = open('number.txt','r+')
raw_number = raw_number.read().split('\n')
raw_number = ''.join(raw_number)
thousand_digit_number = raw_number.strip('\n')


#Find largest thirteen adjacent digit product

stretch_number = 13
largest_product = 0

for i in range(len(thousand_digit_number)-stretch_number):
	current_product = 1
	for j in range(i,i+stretch_number):
		current_product *= int(thousand_digit_number[j])
	if current_product >= largest_product:
		largest_product = current_product

print largest_product
	
