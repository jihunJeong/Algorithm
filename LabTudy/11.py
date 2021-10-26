from collections import deque

N = int(input())

board = [[0 for _ in range(N+2)] for _ in range(N+2)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y][x] = 1

L = int(input())
direct = 0
board[1][1] = 2
pos = deque([[1, 1]])
cy, cx, answer = 1, 1, 0
info = deque([])
for _ in range(L):
    x, c = input().split()
    info.append([x, c])

while True:
    answer += 1
    ny, nx = cy + dy[direct], cx + dx[direct]
    if ny <= 0 or ny > N or nx <= 0 or nx > N or board[ny][nx] == 2:
        print(answer)
        exit()

    if board[ny][nx] != 1:
        py, px = pos.popleft()
        board[py][px] = 0
    board[ny][nx] = 2
    pos.append([ny, nx])
    cy, cx = ny, nx

    if info and answer == int(info[0][0]):
        x, c = info.popleft()
        if c == "L":
            direct = (direct+3) % 4
        else :
            direct = (direct+1) % 4
