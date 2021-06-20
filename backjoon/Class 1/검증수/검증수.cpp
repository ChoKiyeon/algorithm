#include <iostream>
using namespace std;

int main()
{
	int n[5];
	int num = 0;
	for (int i = 0; i < 5; i++)
	{
		cin >> n[i];
		n[i] *= n[i];
		num += n[i];
	}

	cout << num % 10;

	return 0;
}