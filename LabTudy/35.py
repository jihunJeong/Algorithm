N = int(input())

dp = [0]*(N+1)
dp[0] = 1
cnt2, cnt3, cnt5 = 2, 3, 5
idx2, idx3, idx5 = 0, 0, 0
for i in range(1,N+1):
    dp[i] = min(cnt2, cnt3, cnt5)
    if dp[i] == cnt2:
        idx2 += 1
        cnt2 = dp[idx2]*2
    if dp[i] == cnt3:
        idx3 += 1
        cnt3 = dp[idx3]*3
    if dp[i] == cnt5:
        idx5 += 1
        cnt5 = dp[idx5]*5
print(dp[N-1])    