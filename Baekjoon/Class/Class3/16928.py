import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

sadari = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    sadari.append([s,e])

snake = []
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    snake.append([s,e])

hp = []
heapq.heappush(hp, (0, 1))
visited = [0 for _ in range(101)]
while hp:
    t, s = heapq.heappop(hp)
    if s == 100:
        print(t)
        break
    if visited[s] == 1:
        continue
    visited[s] = 1

    flag = False
    for i in range(N):
        if s == sadari[i][0]:
            heapq.heappush(hp, (t, sadari[i][1]))
            flag = True
    for i in range(M):
        if s == snake[i][0]:
            heapq.heappush(hp, (t, snake[i][1]))
            flag = True
    if flag:
        continue
    for i in range(1,7):
        heapq.heappush(hp, (t+1, s+i))