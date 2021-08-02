from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

N, K = map(int, input().split())

board = []
virus = deque([deque([]) for _ in range(K+1)])
for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        if inp[j] != 0:
            virus[inp[j]].append([i,j,0])
    board.append(inp)

S, X, Y = map(int, input().split())
t = 0
while t < S:
    for i in range(1,K+1):
        if not virus[i]:
            continue
            
        while virus[i]:
            if virus[i][0][2] != t:
                break
            vx, vy, nt = virus[i].popleft()
            for j in range(4):
                nx, ny = vx+dx[j], vy+dy[j]
                if ny < 0 or nx < 0 or ny >= N or nx >= N or board[nx][ny] != 0:
                    continue

                board[nx][ny] = i
                virus[i].append([nx, ny, nt+1])
    t += 1
print(board[X-1][Y-1])