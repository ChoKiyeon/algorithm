#include <iostream>
using namespace std;

int main(void)
{
	int h, m;
	cin >> h >> m;

	int cvt_M = 60 * h + m - 45;
	int H = cvt_M / 60;
	int M = abs(cvt_M % 60);

	if (cvt_M + 45 < 45)
	{
		H = 23;
		M = 60 - M;
	}
	
	cout << H << ' ' << M;

	return 0;
}