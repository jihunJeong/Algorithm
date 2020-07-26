#include <stdio.h>

int main() {
	int arr[4];
	int max = 0;
	int max_i = 1;
	int sum = 0;

	for (int i = 0; i < 5; i++) {
		scanf("%d %d %d %d", &(arr[0]), &(arr[1]), &(arr[2]), &(arr[3]));
		for(int j = 0; j < 4; j++) {
			sum += arr[j];
		}

		if (max < sum) {
			max = sum;
			max_i = i + 1;
		}
		sum = 0;
	}

	printf("%d %d\n", max_i, max);
}