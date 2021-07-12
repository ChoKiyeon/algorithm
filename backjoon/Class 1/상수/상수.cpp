#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n1, n2;
    cin >> n1 >> n2;

    int r1 = 0, r2 = 0;
    for (int i = 0; i < 3; i++)
    {
        r1 += n1 % 10;
        r2 += n2 % 10;

        if (i == 2)
            continue;

        n1 /= 10;
        n2 /= 10;

        r1 *= 10;
        r2 *= 10;
    }

    if (r1 > r2)
        cout << r1;
    else
        cout << r2;

    return 0;
}