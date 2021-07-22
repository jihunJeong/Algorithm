board = []

def zip(y, x, size):
    if size == 1:
        print(board[y][x], end="")
        return
    
    start, flag = board[y][x], True
    for p in range(size):
        for q in range(size):
            if start != board[y+p][x+q]:
                flag = False
                break
        if not flag:
            break

    if flag:
        print(start, end="")
        return

    ns = size // 2
    print("(",end="")
    for i in range(2):
        for j in range(2):
            zip(y+ns*i, x+ns*j, ns)
    print(")",end="")

N = int(input())
for i in range(N):
    inp = list(map(int, list(input())))
    board.append(inp)

zip(0, 0, N)