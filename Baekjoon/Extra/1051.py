N, M = map(int, input().split())
arr = []

for i in range(N):
    inp = list(map(int, list(input())))
    arr.append(inp)


ans = 0
for i in range(N):
    for j in range(M):
        hei, wid = N-i, M-j
        for k in range(min(hei,wid)):
            point = arr[i][j]
            if point == arr[i+k][j+k] and point == arr[i+k][j] and point == arr[i][j+k]:
                ans = max(ans, (k+1)**2)
print(ans)