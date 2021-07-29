N = int(input())

ret = 1000 - N
coin = [500, 100, 50, 10, 5, 1]

ans = 0
for i in range(6):
    cnt = ret // coin[i]
    ret -= cnt * coin[i]
    ans += cnt

print(ans)
