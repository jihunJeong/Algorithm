from collections import deque
import sys, heapq
N = int(sys.stdin.readline())

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
b = []
sizes, eat = 2, 0
for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if inp[j] == 9:
            sy, sx = i, j
    b.append(inp)

isEat, ans = True, 0
shark = deque([[sy, sx, 0]])
while True:
    fish = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    while shark:
        sy, sx, t = shark.popleft()
        visited[sy][sx] = True
        if t == 0:
            fy, fx = sy, sx
        for i in range(4):
            ny, nx = sy+dy[i], sx+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] or 9 > b[ny][nx] > sizes:
                    continue
                if 1 <= b[ny][nx] < sizes:
                    fish.append([ny, nx, t+1])
                shark.append([ny, nx, t+1])
                visited[ny][nx] = True
    if fish:
        fish = sorted(fish, key=lambda x : (x[2], x[0], x[1]))
        sy, sx, t = fish[0]
        eat += 1
        if eat == sizes:
            eat = 0
            sizes += 1
        shark = deque([[sy, sx, 0]])
        b[sy][sx], b[fy][fx] = 9, 0
        ans, isEat = ans+t, True
    else :
        break
print(ans)