#include <iostream>
using namespace std;

int main(void)
{
	double grade[1000];

	double n;
	cin >> n;

	int max_idx = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> grade[i];

		if (grade[max_idx] < grade[i])
			max_idx = i;
	}

	double sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += grade[i] / grade[max_idx] * 100.0;
	}

	cout << fixed;
	cout.precision(6);
	cout << sum / n;

	return 0;
}