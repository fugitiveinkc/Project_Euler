# coding=utf-8

'''

Title: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
divisors = [20,19,18,17,16,15,14,13,12,11,9,7] #Reduce redundancies
def smallest_multiple(number): #Sees if number is divisible by 1-20
    for x in divisors:
        if number%x != 0:
            return False
    return True

x = 20
while True: #Loop to find smallest number evenly divisible by 1-20
    if smallest_multiple(x):
        print(x)
        break
    x+=20

#Other possible methods: LCM
