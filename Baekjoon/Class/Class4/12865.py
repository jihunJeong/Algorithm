N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

target = []
for i in range(N):
    w, v = map(int, input().split())
    target.append([w, v])

target = sorted(target, key=lambda x : (x[0], x[1]))
for i in range(N):
    w, v = target[i]

    for j in range(K+1):
        if j < w:
            dp[i+1][j] = dp[i][j]
        else :
            dp[i+1][j] = max(dp[i][j], dp[i][j-w] + v)

print(max(map(max, dp)))