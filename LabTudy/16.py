from itertools import combinations
from collections import deque
import copy

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def check_safe_area(board, virus, safety_cnt):
    dq = deque(virus)
    col, row = len(board), len(board[0])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < col and 0 <= nx < row:
                if board[ny][nx] == 1 or board[ny][nx] == 2:
                    continue
                board[ny][nx] = 2
                safety_cnt -= 1
                dq.append([ny, nx])
    
    return safety_cnt


N, M = map(int, input().split())

board = []
zero_pos = []
virus = []
safety_cnt = -3
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(M):
        if arr[j] == 0:
            zero_pos.append([i,j])
            safety_cnt += 1
        elif arr[j] == 2:
            virus.append([i, j])
    board.append(arr)

answer = 0
for arr in list(combinations(zero_pos, 3)):
    nboard = copy.deepcopy(board)
    for pos in arr:
        nboard[pos[0]][pos[1]] = 1
    nsafety = check_safe_area(nboard, virus, safety_cnt)
    answer = max(answer, nsafety)
print(answer)