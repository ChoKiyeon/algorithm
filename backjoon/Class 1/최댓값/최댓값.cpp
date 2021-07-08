#include <iostream>
using namespace std;

int main(void)
{
	int n;
	int max = 0, max_idx = 0;
	for (int i = 0; i < 9; i++)
	{
		cin >> n;
		if (n > max)
		{
			max = n;
			max_idx = i + 1;
		}
	}

	cout << max << '\n' << max_idx;

	return 0;
}