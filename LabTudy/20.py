N = int(input())

board = []
teacher, student = [], []
for i in range(N):
    inp = list(input().split())
    for j in range(N):
        if inp[j] == "T":
            teacher.append([i, j])
        if inp[j] == "S":
            student.append([i, j])
    board.append(inp)

for i in range(N*N):
    iy, ix = i // N, i % N
    if board[iy][ix] != "X":
        continue
    for j in range(i, N*N):
        jy, jx = j // N, j % N
        if board[jy][jx] != "X":
            continue
        for k in range(j, N*N):
            ky, kx = k // N, k % N
            if board[ky][kx] != "X":
                continue
            board[iy][ix], board[jy][jx], board[ky][kx] = "O", "O", "O"

            check = 1
            for t in teacher:
                ty, tx = t
                # UP
                for dy in range(1,ty+1):
                    if board[ty-dy][tx] == "O":
                        break
                    if board[ty-dy][tx] == "S":
                        check = 0
                        break
                
                #Down
                for dy in range(1, N-ty):
                    if board[ty+dy][tx] == "O":
                        break
                    if board[ty+dy][tx] == "S":
                        check = 0
                        break
                # Left
                for dx in range(1,tx+1):
                    if board[ty][tx-dx] == "O":
                        break
                    if board[ty][tx-dx] == "S":
                        check = 0
                        break
                
                #Right
                for dx in range(1, N-tx):
                    if board[ty][tx+dx] == "O":
                        break
                    if board[ty][tx+dx] == "S":
                        check = 0
                        break
            
                if check == 0:
                    break

            if check == 1:
                print("YES")
                exit()

            board[iy][ix], board[jy][jx], board[ky][kx] = "X", "X", "X"
print("NO")

