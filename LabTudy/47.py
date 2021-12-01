from collections import defaultdict
import copy
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

def eatFish(sy, sx, nboard, nfish):
    fish = copy.deepcopy(nfish)
    board = copy.deepcopy(nboard)
    fsize, direct = board[sy][sx]
    board[sy][sx] = [-1, direct]
    fish[fsize] = None

    for i in range(1, 17):
        if not fish[i]:
            continue
        fy, fx = fish[i]
        tsize, tdirect = board[fy][fx]
        for j in range(8):
            ny, nx = fy + dy[(tdirect-1+j)%8], fx + dx[(tdirect-1+j)%8]
            if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx][0] >= 0:
                csize, cdirect = board[ny][nx]
                fish[csize] = [fy, fx]
                fish[tsize] = [ny, nx]
                board[fy][fx] = [csize, cdirect]
                board[ny][nx] = [tsize, (tdirect-1+j)%8 + 1]
                break

    sdirect = board[sy][sx][1]
    board[sy][sx] = [0, 0]
    number = 0
    while 0 <= sy < 4 and 0 <= sx < 4:
        ny, nx = sy + dy[(sdirect-1)], sx + dx[(sdirect-1)]
        if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx][0] >= 1:
            number = max(number, eatFish(ny, nx, board, fish))
        sy, sx = ny, nx
    return number + fsize

board = [[[0, 0] for _ in range(4)] for _ in range(4)]
fish = defaultdict(list)
for i in range(4):
    arr = list(map(int, input().split()))
    idx = 0
    while idx < 8:
        board[i][idx // 2][0] = arr[idx]
        fish[arr[idx]] = [i, idx//2] 
        board[i][idx // 2][1] = arr[idx+1]
        idx = idx + 2

sy, sx = 0, 0
answer = eatFish(sy, sx, board, fish)
print(answer)