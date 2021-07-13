#include <iostream>
using namespace std;

int main(void)
{
	int x, y, w, h;
	cin >> x >> y >> w >> h;

	int left_DX = x;
	int right_DX = w - x;
	int up_DX = h - y;
	int down_DX = y;
	
	int DX[4] = { left_DX, right_DX, up_DX, down_DX };
	int min_idx = 0;
	for (int i = 0; i < 4; i++)
	{
		if (DX[min_idx] > DX[i])
			min_idx = i;
	}

	cout << DX[min_idx];

	return 0;
}