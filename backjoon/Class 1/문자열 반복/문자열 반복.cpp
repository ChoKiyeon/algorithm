#include <iostream>
using namespace std;

int main(void)
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++)
	{
		int r;
		string str;
		cin >> r >> str;

		for (int i = 0; i < str.size(); i++)
		{
			for (int j = 0; j < r; j++)
			{
				cout << str[i];
			}
		}
		cout << '\n';
	}

	return 0;
}