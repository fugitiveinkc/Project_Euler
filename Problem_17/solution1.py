'''

Title: Problem 17 -- Number letter counts

Problem: Convert 1 to 1000 into english and count letters

Approach: Convert using dictionary and patterns in language and then count

Notes:
	-What does it mean to program this elegantly?  Fewest conditions for each number to string conversion?
	-Any way to make this code as short as possible?  Maybe that is what is elegant here?

'''

#Create a dictionary and function to convert numbers to strings

n_dict = {
		0 : '',
		1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
		10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
		20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eigthy', 90: 'ninety'
}


def number_to_string(number):
	'''
	Converts number to string.  Only works for numbers
	1 through 1000 and has no spaces or hyphens.  Serves to count
	number of digits per number.
	'''
	number_str = str(number) #String version of number
	if len(number_str) == 1: #Units digits
		return n_dict[number]
	elif len(number_str) == 2 and number < 20: #Double digits less than 20
		return n_dict[number]
	elif len(number_str) == 2: #Rest of double digits and save number to dict
		n_dict[number] =  n_dict[int(number_str[0]+'0')] + n_dict[int(number_str[1])]
		return n_dict[number]
	elif len(number_str) == 3: #Triple digits
		if number_str[1:3] == '00': #Hundreds with no teens or units
			return n_dict[int(number_str[0])] + 'hundred'
		elif int(number_str[1:3]) < 10: #Hundreds digits with teens/units below 10
			return n_dict[int(number_str[0])] + 'hundredand' + n_dict[int(number_str[2])]
		else: #Every other hundreds number
			return n_dict[int(number_str[0])] + 'hundredand' + n_dict[int(number_str[1:3])]
	else: #1000!
		return "onethousand"
			
	
#Go from 1 to 1000 and count letters

if __name__ == "__main__":
	print 'Total letter count for 1 through 1000 is: ' + str(sum(len(number_to_string(x)) for x in range(1,1001)))
