import math

n = int(input())

ans = [10] * (n+1)
ans[0], ans[1] = 0, 1
for i in range(n+1):
    for j in range(1, math.floor(math.sqrt(i))+1):
        past = i - j**2
        if ans[i] > 1 + ans[past]:
            ans[i] = 1 + ans[past]
print(ans[n])