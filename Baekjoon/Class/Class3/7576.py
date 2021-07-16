from collections import deque
import sys

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

M, N = map(int, sys.stdin.readline().split())

arr = []
apple = deque()
cnt = 0
wall = 0
for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if inp[j] == 1:
            apple.append([i, j, 0])
            cnt += 1
        if inp[j] == -1:
            wall += 1
    arr.append(inp)
if cnt + wall == M*N:
    print(0)
    exit()
    
flag = False
while apple:
    y, x, t = apple.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >=M:
            continue
        if arr[ny][nx] != 0:
            continue

        arr[ny][nx] = 1
        cnt += 1
        apple.append([ny, nx, t+1])

    if cnt + wall == N*M:
        flag = True
        print(t+1)
        break

if not flag:
    print(-1)