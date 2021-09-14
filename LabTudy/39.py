import heapq

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in range(T):
    N = int(input())
    board = []
    for j in range(N):
        li = list(map(int, input().split()))
        board.append(li)

    dikstra = [[float('inf') for _ in range(N)] for _ in range(N)]
    dikstra[0][0] = board[0][0]
    hp = []
    heapq.heappush(hp, (board[0][0], [0,0]))
    while hp:
        weight, node = heapq.heappop(hp)
        y, x = node

        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if dikstra[ny][nx] > dikstra[y][x] + board[ny][nx]:
                    dikstra[ny][nx] = dikstra[y][x] + board[ny][nx]
                    heapq.heappush(hp, (dikstra[ny][nx], [ny, nx]))
    print(dikstra[N-1][N-1])

