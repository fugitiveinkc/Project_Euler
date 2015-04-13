# coding=utf-8

'''

Title: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 � 99.

Find the largest palindrome made from the product of two 3-digit numbers.

--Pseudocode--
function palindrome(the number):
    identifies if number is a palindrome


result = place to save palindrome
cycle through first multiplier "x"
    cycle through second multiplier "y"
        determine product, if product is a palindrome and store result if highest palindrome

'''

def palindrome(int_number): #Checks to see if number is a palindrome
    str_number = str(int_number)
    for x in range(len(str_number)):
        if str_number[x] != str_number[len(str_number)-1-x]:
            return False
    return True

result = 0 #Stores current palindrome
for x in range(100,1000):
    for y in range(100,1000):
        product = x * y
        if palindrome(product) and (product >= result):
            result = product

print(result)
