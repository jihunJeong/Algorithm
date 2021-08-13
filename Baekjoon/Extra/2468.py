import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(sys.stdin.readline())

board = []
for i in range(N):
    inp = list(map(int, sys.stdin.readline().split()))
    board.append(inp)

ans = 0
for i in range(101):
    for j in range(N):
        for k in range(N):
            if board[j][k] != 0 and board[j][k] <= i:
                board[j][k] = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if not visited[j][k] and board[j][k] != 0:
                cnt += 1
                dfs = [[j, k]]
                visited[j][k] = True
                while dfs:
                    y, x = dfs.pop()

                    for n in range(4):
                        ny, nx = y+dy[n], x+dx[n]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] > 0:
                            dfs.append([ny, nx])
                            visited[ny][nx] = True
    ans = max(ans, cnt)
print(ans)