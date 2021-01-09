#include <stdio.h>16

int n;
int w[5][5];
int d[1 << 5][5] = { 0 };
int p[1 << 5][5] = { 0 };

int salesperson(int check, int nc)
{
	for(i = 2; i <= 5; i++) {
		d[i][0] = w[i][1]
	}

	check |= (1 << nc);
	
	//모든 도시를 지난 경우
	if (check == (1 << n) - 1)
	{
		if (w[nc][0] > 0)
		{
			return w[nc][0]; //가중치
		}
		return 10000;//불가능한 경우 MAX 반환
	}

	int& ret = d[check][nc];
	//memorization
	if (ret > 0)
		return ret;
	ret = 10000;
	for (int i = 0; i < n; i++)
	{
		//now -> 아직 방문하지 않은 i번 도시 가는 경로가 있는 경우 
		if (i != nc && (check&(1<<i))==0 && w[nc][i] > 0)
		{
			//최소 비용 갱신
			int temp = salesperson(check, i) + w[nc][i];
			if (ret > temp)
				ret = temp;
		}
	}
	return ret;
}

int main()
{
	n = 5
	w = 
	
	result = TSP(0, 0);
	printf("%d\n", ans);

	return 0;
}
