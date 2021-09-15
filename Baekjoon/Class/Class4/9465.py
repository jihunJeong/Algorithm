T = int(input())
for _ in range(T):
    n = int(input())
    info = [[0],[0]]
    for i in range(2):
        info[i].extend(list(map(int, input().split())))
    
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    dp[0][1], dp[1][1] = info[0][1], info[1][1]
    for i in range(2, n+1):
        for j in range(2):
            dp[j][i] = max(dp[1-j][i-2], dp[1-j][i-1]) + info[j][i]

    print(max(max(dp[0]), max(dp[1])))