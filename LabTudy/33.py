N = int(input())

dp = [0]*(N+6)
for i in range(1,N+1):
    t, p = map(int,input().split())
    dp[i+t-1] = max(dp[i+t-1], max(dp[:i])+p)

print(max(dp[:N+1]))
