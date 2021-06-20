#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str;
    getline(cin, str);

    int cnt = 0;
    int n = str.length();
    for (int i = 0; i < n; i++)
    {
        if (n == 1 && str[i] == ' ')
        {
            cout << 0;
            return 0;
        }

        if ((i == 0 || i == n - 1) && str[i] == ' ')
            continue;

        if (str[i] == ' ')
            cnt++;
    }

    cout << cnt + 1;

    return 0;
}