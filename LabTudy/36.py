before = input()
after = input()

alen, blen = len(after), len(before)
dp = [[0 for _ in range(alen+1)] for _ in range(blen+1)]

for i in range(blen):
    for j in range(alen):
        if before[i] == after[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else :
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(alen - dp[blen][alen])