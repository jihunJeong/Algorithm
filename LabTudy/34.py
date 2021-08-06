N = int(input())

force = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if force[j] > force[i]:
            dp[i] = max(dp[i], dp[j]+1)
max_num = max(dp)
print(N-max_num)