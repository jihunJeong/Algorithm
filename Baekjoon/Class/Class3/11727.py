import sys

n = int(sys.stdin.readline())
if n == 1:
    print(1)
    exit()

dp = [0] * (n+1)
dp[1], dp[2] = 1, 3

for i in range(3, n+1):
    dp[i] = ((2*dp[i-2])%10007 + dp[i-1]%10007)%10007

print(dp[n])