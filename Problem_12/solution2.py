'''

Title: Solution 2 to Problem 12

Method: Prime factorization d(x) = (v1 + 1)(v2 + 2) ...

Notes:
	-Works but code could be cleaned up in prime_factorization.py
	-Relatively fast!

'''

from solution1 import tri_num_gen
from prime_factorization import *

for x in count(2):
	temp = tri_num_gen(x)
	if factor_count(temp) > 500:
		print temp
		break

