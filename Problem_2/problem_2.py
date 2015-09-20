'''

Problem title: Even Fibonacci Numbers
Summary: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

'''

fib_sum = 0
fib_elem = 2
fib_prev = 1
while fib_elem <= 4000000:
	if fib_elem%2==0:
		fib_sum = fib_elem + fib_sum
	temp = fib_elem
	fib_elem = fib_elem + fib_prev
	fib_prev = temp
print("The answer is: " + str(fib_sum) + ".")

#Solution using Generator

#Solution using Iterator		
