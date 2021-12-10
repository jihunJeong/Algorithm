from collections import defaultdict
import heapq, sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append([e, c])

ts, te = map(int, sys.stdin.readline().split())

hp = []
distance = [float('inf') for _ in range(N+1)]
heapq.heappush(hp, (0, ts))
distance[ts] = 0
while hp:
    dist, v = heapq.heappop(hp)
    if v == te:
        break
    if distance[v] < dist:
        continue

    for key, val in graph[v]:
        if distance[key] <= dist + val:
            continue
        distance[key] = dist+val
        heapq.heappush(hp, (distance[key], key))
print(distance[te])