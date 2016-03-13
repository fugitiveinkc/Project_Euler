'''

Title: Longest Collatz Sequence

Problem: Given n, if n is even then the next number is n/2 and if n is odd the next number is 3n+1, complete this until you get to one.  Which starting number under a million produces the longest chain.

Notes:
	-Based on truth of collatz conjecture for numbers under 1 million.
	-Runs slightly under a minute, but how can I speed up?  Dynamic programming?

'''

def collatz_generator(n):
	while n != 1:
		if n%2 == 0:
			yield n/2
			n = n/2
		else:
			yield (3*n)+1
			n = (3*n)+1

largest_chain = 0
starting_number = 0
for x in range(1, 1000000):
	current_chain = sum(1 for x in collatz_generator(x))
	if current_chain >= largest_chain:
		largest_chain = current_chain
		starting_number = x
print "Largest chain (not including starting number): " + str(largest_chain)
print "Starting number of largest chain: " + str(starting_number)

