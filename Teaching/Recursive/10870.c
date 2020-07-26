#include <stdio.h>

int fibonacci(int n);

int main() {
	int n = 0;
	scanf("%d", &n);

	printf("%d\n", fibonacci(n));
}

int fibonacci(int n) {
	if (n == 1) {
		return 1;
	} else if (n == 0) {
		return 0;
	}

	return fibonacci(n - 1) + fibonacci(n - 2);
}