#include <iostream>
using namespace std;

int main(void)
{
	int n;
	cin >> n;

	int min = 1000000;
	int max = -1000000;
	for (int i = 0; i < n; i++)
	{
		int num;
		cin >> num;

		if (num > max)
			max = num;

		if (num < min)
			min = num;
	}

	cout << min << ' ' << max;

	return 0;
}