from collections import defaultdict

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, K = map(int, input().split())

board = [[[0,0,0] for _ in range(N)] for _ in range(N)]
shark_pos = defaultdict(list)
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] != 0:
            shark_pos[arr[j]] = [i, j]
            board[i][j] = [arr[j], arr[j], K]

shark_direc = list(map(int, input().split()))

shark_priority = [[[] for _ in range(4)] for _ in range(M)]
for i in range(M):
    for j in range(4):
        shark_priority[i][j] = list(map(int, input().split()))

count, time = M, 0
while count > 1 and time <= 1000:
    time += 1
    possible = defaultdict(list)
   
    for key in shark_pos.keys():
        if not shark_pos[key]:
            continue 
        snum = key
        sdirect = shark_direc[key-1]
        y, x = shark_pos[key]
        flag = True
        for k in range(4):
            pridirect = shark_priority[snum-1][sdirect-1][k]
            ny, nx = y + dy[pridirect-1], x + dx[pridirect-1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx][2] == 0:
                possible[ny*N+nx].append([snum, pridirect])
                flag = False
                break
        if flag:
            for k in range(4):
                pridirect = shark_priority[snum-1][sdirect-1][k]
                ny, nx = y + dy[pridirect-1], x + dx[pridirect-1]
                if 0 <= ny < N and 0 <= nx < N and board[ny][nx][1] == snum:
                    possible[ny*N+nx].append([snum, pridirect])
                    break
    
    for key in possible.keys():
        possible[key] = sorted(possible[key], key=lambda x : x[0])
        ny, nx = key // N, key % N
        fshark = possible[key][0]
        board[ny][nx] = [fshark[0], fshark[0], K]
        cy, cx = shark_pos[fshark[0]]
        board[cy][cx][0] = 0
        shark_pos[fshark[0]] = [ny, nx]
        shark_direc[fshark[0]-1] = fshark[1]
        for i in range(1, len(possible[key])):
            count -= 1
            cy, cx = shark_pos[possible[key][i][0]]
            board[cy][cx][0] = 0
            shark_pos[possible[key][i][0]] = None

    for i in range(N):
        for j in range(N):
            if board[i][j][2] > 0 and board[i][j][0] == 0:
                board[i][j][2] -= 1

if time > 1000:
    print(-1)
else :
    print(time)
            
