import sys

num = list(map(int, sys.stdin.readline().rstrip()))
print(num)

dp = [[0 for x in range(len(num))] for y in range(len(num))]
for i in range(len(num)):
	for j in range(len(num)):
		if i == j:
			dp[i][j] = 1