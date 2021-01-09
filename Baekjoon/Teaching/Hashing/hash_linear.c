#include <stdio.h>


int hash_func(int key) {
	int hash_value = key % 13;

	return hash_value;
}

int main() {
	int array[13] = { 0 };

	int input = 0;
	int input_cnt = 8;
	while (input_cnt > 0) {
		scanf("%d", &input);

		for (int i = 0; i < 13; i++) {
			int index = hash_func(input + i);

			if (array[index] == 0) {
				array[index] = input;
				break;
			}
		}

		printf("Answer : [");
		for (int i = 0; i < 12; i++) {
			printf("%d, ", array[i]);
		}
		printf("%d]\n", array[12]);

		input_cnt--;
	}
}