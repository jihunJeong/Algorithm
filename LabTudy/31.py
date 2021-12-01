T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    board= [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            board[i][j] = arr[i*m + j]
    
    dp = [[0 for _ in range(m)] for _ in range(n+2)]
    for i in range(1,n+1):
        dp[i][0] = board[i-1][0]
    
    for j in range(1, m):
        for i in range(1,n+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1]) + board[i-1][j]
    print(max(map(max, dp)))