/*

Problem title: Even Fibonacci Numbers
Summary: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

*/

#include <iostream>

using namespace std;

int main()
{
	int fib_sum = 0;
	int fib_elem = 2;
	int fib_prev = 1;
	while (fib_elem < 4000000)
	{

		if (fib_elem%2 == 0)
		{
			fib_sum += fib_elem;
		}
		int temp = fib_elem;
		fib_elem = fib_elem+fib_prev;
		fib_prev = temp;
	}
	cout << "The answer is: " << fib_sum << ".\n";
}
