'''

Title: Problem 16 -- Power digit sum

Problem: Sum the digits of the result of 2^1000

Note: Trivial since python handles such large numbers

'''

large_number = str(2**1000)
result = sum(int(x) for x in large_number)
print result
