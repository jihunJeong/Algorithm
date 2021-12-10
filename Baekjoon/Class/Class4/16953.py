from collections import defaultdict
import heapq

A, B = map(int, input().split())
info = defaultdict(int)

hp = []
heapq.heappush(hp, (A, 0))
while hp:
    num, s = heapq.heappop(hp)
    if num == B:
        print(s+1)
        break
    elif num > B:
        print(-1)
        break

    p1 = num*10+1
    p2 = num*2

    if info[p1] == 0:
        info[p1] = 1
        heapq.heappush(hp, (p1, s+1))

    if info[p2] == 0:
        info[p2] = 1
        heapq.heappush(hp, (p2, s+1))