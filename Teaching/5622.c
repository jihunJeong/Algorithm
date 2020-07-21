#include <stdio.h>
#include <string.h>

int main() {
	char input[16];
	scanf("%s", input);
	
	int ans = 0;
	for (int i = 0; i < strlen(input); i++) {
		if (input[i] == 'A' || input[i] == 'B' || input[i] == 'C') {
			ans += 3;
		} else if (input[i] == 'G' || input[i] == 'H' || input[i] == 'I') {
			ans += 5;
		} else if (input[i] == 'D' || input[i] == 'E' || input[i] == 'F') {
			ans += 4;
		} else if (input[i] == 'J' || input[i] == 'K' || input[i] == 'L') {
			ans += 6;
		} else if (input[i] == 'N' || input[i] == 'M' || input[i] == 'O') {
			ans += 7;
		} else if (input[i] == 'P' || input[i] == 'Q' || input[i] == 'R' || input[i] == 'S') {
			ans += 8;
		} else if (input[i] == 'T' || input[i] == 'U' || input[i] == 'V') {
			ans += 9;
		} else if (input[i] == 'W' || input[i] == 'X' || input[i] == 'Y' || input[i] == 'Z') {
			ans += 10;
		}
	}
	printf("%d\n", ans);
}