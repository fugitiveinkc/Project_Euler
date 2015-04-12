/*
Problem title:  Multiples of 3 and 5
Summary: Find sum of all the multiples of 3 or 5 below 1000
*/


#include <iostream>

using namespace std;

int main()
{
	int running_sum = 0;
	for (int x = 1; x < 1000; x++)
	{
		if (x%3 == 0)
		{
			running_sum += x;
		}
		else if (x%5 == 0)
		{
			running_sum += x;
		}
	}
	cout << "Final sum is: " << running_sum << "\n";
}
