#include <iostream>
using namespace std;

int main(void)
{
	string str = "";
	for (int i = 0; i < 8; i++)
	{
		char ch;
		cin >> ch;

		str += ch;
	}

	if (str == "12345678")
		cout << "ascending";
	else if (str == "87654321")
		cout << "descending";
	else
		cout << "mixed";

	return 0;
}