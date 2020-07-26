#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
	int n = 0, m = 0;
	scanf("%d %d", &n, &m);

	int** arr = (int**)malloc(sizeof(int*) * (n + 1));
	for (int i = 0; i < n + 1; i++) {
		arr[i] = (int*)malloc(sizeof(int) * (m + 1));
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int t = 0;
			scanf("%d", &t);
			arr[i][j] = t;
			//printf("%d", arr[i][j]);
		}
	}

	int k = 0;
	scanf("%d", &k);
	for (int i = 0; i < k; i++) {
		int a = 0, b = 0, c = 0, d = 0;
		scanf("%d %d %d %d", &a, &b, &c, &d);
		//printf("%d %d %d %d", a, b, c, d);
		int ans = 0;
		for (int y = a - 1; y < c; y++) {
			for (int x = b - 1; x < d; x++) {
				ans += arr[y][x];
			}
		}

		printf("%d\n", ans);
	}

	return 0;
}