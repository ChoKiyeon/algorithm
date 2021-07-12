#include <iostream>
using namespace std;

int main()
{
    int dat[26];
    fill(dat, dat + 26, -1);

    string str;
    cin >> str;

    for (int i = 0; i < str.length(); i++)
    {
        if (dat[str[i] - 'a'] != -1)
            continue;

        dat[str[i] - 'a'] = i;
    }

    for (int i = 0; i < 26; i++)
    {
        cout << dat[i] << ' ';
    }

    return 0;
}