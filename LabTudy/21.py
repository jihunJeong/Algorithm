from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N, L, R = map(int, input().split())

board = []
for i in range(N):
    li = list(map(int, input().split()))
    board.append(li)

flag, ans = 1, 0
while flag:
    flag = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp = []
                total, cnt = 0, 0
                dq = deque([[i, j]])
                visited[i][j] = 1
                while dq:
                    y, x = dq.popleft()
                    temp.append([y, x])
                    total += board[y][x]
                    cnt += 1
                    for k in range(4):
                        ny, nx = y+dy[k], x+dx[k]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(board[y][x] - board[ny][nx]) <= R:
                            dq.append([ny, nx])
                            visited[ny][nx] = 1
                
                if len(temp) > 1:
                    for y, x in temp:
                        flag = 1
                        board[y][x] = total // cnt
        
    if flag :
        ans += 1
print(ans)
