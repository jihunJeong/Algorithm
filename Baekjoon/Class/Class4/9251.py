str1 = input()
str2 = input()

dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(len(str2)):
    for j in range(len(str1)):
        if str1[j] == str2[i]:
            dp[i+1][j+1] = dp[i][j] + 1
        else :
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(max(map(max, dp)))