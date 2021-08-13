from collections import deque
import sys

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())
    visited = [[False for _ in range(I)] for _ in range(I)]
    y, x = map(int, sys.stdin.readline().split())
    ty, tx = map(int, sys.stdin.readline().split())
    visited[y][x] = True
    bfs = deque([[y, x, 0]])
    while bfs:
        y, x, t = bfs.popleft()

        if y == ty and x == tx:
            print(t)
            break

        for i in range(8):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < I and 0 <= nx < I and not visited[ny][nx]:
                bfs.append([ny, nx, t+1])
                visited[ny][nx] = True    