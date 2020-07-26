#include <stdio.h>
#include <stdlib.h>

int main() {
	int n = 0, m = 0, r = 0;
	scanf("%d %d %d", &n, &m, &r);

	int** num = (int**)malloc(sizeof(int*) * n);
	for (int i = 0; i < m; i++) {
		num[i] = (int*)malloc(sizeof(int) * m);
	}

	int t = 0;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%d", &t);
			num[i][j] = t;
			printf("%d ", t);
		}
	}
}