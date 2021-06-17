#include <iostream>
using namespace std;

int main(void) 
{
	double a, b;
	while (1)
	{
		cin >> a >> b;
	
		if (a > 0 && a < 10 && b > 0 && b < 10)
			break;
	}

	cout << fixed;
	cout.precision(9);
	
	cout << a / b;

	return 0;
}