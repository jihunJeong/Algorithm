import sys
import math

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [[0 for x in range(N)] for y in range(N)]

for i in range(N):
	for j in range(N):
		if num[i] == num [j]:
			dp[i][j] = dp[i + 1][j - 1]
		else :
			dp[i][j] = min(dp[i][j - 1] + 1, dp[i + 1][j] + 1)