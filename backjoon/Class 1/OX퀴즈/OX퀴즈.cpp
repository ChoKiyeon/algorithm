#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        string result;
        cin >> result;

        int idx = 0;
        int score = 0;
        while (1)
        {
            int cnt = 0;
            while (result[idx] == 'O')
            {
                cnt++;
                score += cnt;
                idx++;
            }

            idx = result.find('O', idx);

            if (idx == -1)
                break;
        }

        cout << score << '\n';
    }
}