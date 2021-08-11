import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
visited = [[0 for _ in range(M)] for _ in range(N)]

ans = 0
board = []

def dfs(y, x, c, rst):
    global ans

    visited[y][x] = 1
    rst += board[y][x]
    if c == 4:
        ans = max(ans, rst)
        rst -= board[y][x]
        return
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        
        if 0 <= ny < N and 0 <= nx < M:
            if visited[ny][nx] == 1:
                continue
            dfs(ny, nx, c+1, rst)
            visited[ny][nx] = 0
    
    rst -= board[y][x]
    visited[y][x] = 0

def middle(y, x):
    global ans
    ret = 0
    if y >= 1 and x >= 1 and x < M - 1:
        ret = max(ret, board[y][x - 1] + board[y][x] + board[y - 1][x] + board[y][x + 1])
    if y >= 1 and y < N - 1 and x < M - 1:
        ret = max(ret, board[y - 1][x] + board[y][x] + board[y][x + 1] + board[y + 1][x])
    if y >= 0 and y < N - 1 and x < M - 1:
        ret = max(ret, board[y][x - 1] + board[y][x] + board[y + 1][x]+ board[y][x + 1])
    if y >= 1 and y < N - 1 and x >= 1:
        ret = max(ret, board[y - 1][x] + board[y][x] + board[y][x - 1] + board[y + 1][x])
    ans = max(ans, ret)

for _ in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    board.append(inp)

for i in range(N):
    for j in range(M):
        dfs(i, j, 1, 0)
        middle(i, j)
print(ans)