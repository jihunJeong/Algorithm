n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = arr[0][0]
for i in range(1,n):
    for j in range(len(arr[i])):
        if j == 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+arr[i][j])
        elif j == len(arr[i])-1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+arr[i][j])
        else :
            dp[i][j] = max(dp[i][j], dp[i-1][j]+arr[i][j], dp[i-1][j-1]+arr[i][j])
print(max(dp[n-1]))