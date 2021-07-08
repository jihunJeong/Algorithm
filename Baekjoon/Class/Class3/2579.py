N = int(input())

cost = [0]
for i in range(N):
    cost.append(int(input()))

dp = [[0, 0] for _ in range(N+1)]
dp[1][0], dp[1][1] = cost[1], cost[1]
for i in range(2, N+1):
    dp[i][0] = max(dp[i-2]) + cost[i]
    dp[i][1] = dp[i-1][0] + cost[i]

print(max(dp[N]))