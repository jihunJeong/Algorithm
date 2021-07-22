dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())

arr = []
for _ in range(N):
    inp = list(map(int, list(input())))
    arr.append(inp)

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            continue
        
        cnt, s = 0, [[i, j]]
        while s:
            y, x = s.pop()
            if arr[y][x] == 0:
                continue
            cnt += 1
            arr[y][x] = 0
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                if ny < 0 or nx < 0 or ny >= N or nx >= N or arr[ny][nx] == 0:
                    continue
                s.append([ny,nx])
        ans.append(cnt)
ans = sorted(ans)
print(len(ans))
for n in ans:
    print(n)