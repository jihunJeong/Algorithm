#include <stdio.h>

int main() {
	int n = 0;
	// 변수 앞에 &의 의미는 주소값을 나타낸다
	scanf("%d", &n);

	int j = 0;

	for (int i = 1; i < 2 * n; i++) {
		if (i > n) {
			j--;
		}
		else {
			j++;
		}

		for (int k = 0; k < j; k++) {
			printf("*");
		}
		printf("\n");
	}
}