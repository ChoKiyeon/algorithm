#include <iostream>
using namespace std;

int is_LeapYear(int year)
{
    if (year % 4 != 0)
        return 0;

    if (year % 100 != 0)
        return 1;

    if (year % 400 == 0)
        return 1;

    return 0;
}

int main()
{
    int year;
    cin >> year;

    cout << is_LeapYear(year);
}