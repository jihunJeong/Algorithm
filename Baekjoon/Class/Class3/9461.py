T = int(input())

ans = [0] * 100
ans = [1, 1, 1, 2, 2, 3, 4, 5]
for i in range(8, 100):
    ans.append(ans[i-1] + ans[i-5])

for i in range(T):
    c = int(input())
    print(ans[c-1])