#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    int dat[26] = { 0 };

    string str;
    cin >> str;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] >= 'a' && str[i] <= 'z')
            dat[str[i] - 'a']++;
        else
            dat[str[i] - 'A']++;
    }

    int max_idx = 0;
    for (int i = 0; i < 26; i++)
    {
        if (dat[max_idx] < dat[i])
            max_idx = i;
    }

    for (int i = 0; i < 26; i++)
    {
        if (dat[max_idx] == dat[i] && i != max_idx)
        {
            cout << '?';
            return 0;
        }
    }

    cout << (char)(max_idx + 'A');

    return 0;
}