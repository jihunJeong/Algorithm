from collections import deque

dh = [1, -1 , 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dx = [0, 0, -1, 1, 0, 0]


M ,N, H = map(int, input().split())

cnt, wall = 0, 0
arr, bfs = [], deque()
for i in range(H):
    new = []
    for j in range(N):
        inp = list(map(int, input().split()))
        for k in range(M):
            if inp[k] == 1:
                bfs.append([i, j, k, 0])
                cnt += 1
            elif inp[k] == -1:
                wall += 1
        new.append(inp)
    arr.append(new)

ans, max_t = -1, 0
while bfs:
    h, y, x, t = bfs.popleft()
    
    if cnt + wall == M*N*H:
        ans = max_t
        break

    for i in range(6):
        nh, ny, nx = h+dh[i], y+dy[i], x+dx[i]
        
        if nh < 0 or nh >= H or ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if arr[nh][ny][nx] != 0:
            continue
        bfs.append([nh,ny,nx, t+1])
        arr[nh][ny][nx] = 1
        cnt += 1
        max_t = max(max_t, t+1)

print(ans)