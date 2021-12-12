import sys

N, M = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    arr = list(map(int, sys.stdin.readline().split()))
    temp = 0
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + arr[j-1]
        temp += arr[j-1]
        dp[i][j] = temp + dp[i-1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(answer)