#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    string sn;
    cin >> sn;

    int result = 0;
    for (int i = 0; i < n; i++)
    {
        result += sn[i] - '0';
    }

    cout << result;
}