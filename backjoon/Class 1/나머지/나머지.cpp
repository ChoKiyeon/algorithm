#include <iostream>
using namespace std;

int main()
{
    int dat[42] = { 0 };
    for (int i = 0; i < 10; i++)
    {
        int n;
        cin >> n;

        dat[n % 42]++;
    }

    int cnt = 0;
    for(int i = 0; i < 42; i++)
    {
        if (dat[i])
            cnt++;
    }

    cout << cnt;

    return 0;
}