#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int search(char* arr, int idx, int mid) {
	if (arr[mid + idx] == arr[mid - idx]) {
		return -1;
	}
	if (idx >= mid) {
		return 1;
	}

	return search(arr, idx + 1, mid);
}

int main() {
	int t = 0;
	scanf("%d", &t);
	while (t--) {
		char s[3001];
		scanf("%s", s);
		int mid = strlen(s) / 2;
		if (strlen(s) == 1 || search(s, 1, mid) == 1) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}
	}
}