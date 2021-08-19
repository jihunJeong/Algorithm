from sys import stdin
from collections import defaultdict, deque

t = int(stdin.readline())


for case in range(t):

    col, row, target = map(int, stdin.readline().split())

    graph = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
    visted = [[0 for _ in range(row + 1)] for _ in range(col + 1)]
    dq = deque([])
    temp_dq = deque([])

    for i in range(target):
        x, y = list(map(int, stdin.readline().split()))
        graph[x][y] = 1
        dq.append([x, y])

    ck = 0

    while dq:
        temp = dq.popleft()
        x = temp[0]
        y = temp[1]
        if graph[x][y] == 1 and visted[x][y] != 1:
            visted[x][y] = 1
            ck += 1
            if graph[x + 1][y] == 1 and visted[x + 1][y] == 1:
                ck -= 1
                continue
            elif graph[x - 1][y] == 1 and visted[x - 1][y] == 1:
                ck -= 1
                continue
            elif graph[x][y+1] == 1 and visted[x][y+1] == 1:
                ck -= 1
                continue
            elif graph[x][y-1] == 1 and visted[x][y-1] == 1:
                ck -= 1
                continue
    print(ck)
