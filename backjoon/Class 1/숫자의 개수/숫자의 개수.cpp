#include <iostream>
using namespace std;

int main(void)
{
	int a, b, c;
	cin >> a >> b >> c;

	int n = a * b * c;
	int dat[10] = { 0 };
	while (n != 0)
	{
		dat[n % 10]++;
		n /= 10;
	}

	for (int i = 0; i < 10; i++)
	{
		cout << dat[i] << '\n';
	}

	return 0;
}