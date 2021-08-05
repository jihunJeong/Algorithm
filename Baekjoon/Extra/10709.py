H, W = map(int, input().split())

cloud = []
for i in range(H):
    info = list(input())
    cloud.append(info)

ans = [[-1 for _ in range(W)] for _ in range(H)]
for i in range(H):
    c = -1
    for j in range(W):
        if cloud[i][j] == "c":
            c = 0
        ans[i][j] = c

        if c >= 0:
            c += 1

for i in range(H):
    print(' '.join(str(c) for c in ans[i])) 