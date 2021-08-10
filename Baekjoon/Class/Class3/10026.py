dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
board = []
for i in range(N):
    inp = list(input())
    board.append(inp)

visit = [[0 for _ in range(N)] for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] != 0:
            continue
        ans1 += 1
        stack = [[i, j, board[i][j]]]
        while stack:
            y, x, c = stack.pop()

            if visit[y][x] == 1:
                continue
        
            visit[y][x] = 1
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]

                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] != c:
                        continue
                    stack.append([ny,nx,c])
                    
visit = [[0 for _ in range(N)] for _ in range(N)]
ans2 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] != 0:
            continue
        ans2 += 1
        stack = [[i, j, board[i][j]]]
        while stack:
            y, x, c = stack.pop()

            if visit[y][x] == 1:
                continue
        
            visit[y][x] = 1
            for k in range(4):
                ny, nx = y+dy[k], x+dx[k]

                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == c:
                        stack.append([ny,nx,c])
                    elif board[ny][nx] == "R" and c == "G":
                        stack.append([ny,nx,board[ny][nx]])
                    elif board[ny][nx] == "G" and c == "R":
                        stack.append([ny,nx,board[ny][nx]])
                    
print(ans1, ans2)