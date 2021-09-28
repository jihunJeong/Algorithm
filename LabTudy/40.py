import heapq
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dikstra = [float('inf') for _ in range(N+1)]
hp = []
heapq.heappush(hp, (0, 1))
dikstra[1] = 0
visited = [False for _ in range(N+1)]

while hp:
    cost, node = heapq.heappop(hp)
    visited[node] = True

    for nnode in graph[node]:
        if visited[nnode] == False and dikstra[nnode] > dikstra[node] + 1:
            dikstra[nnode] = dikstra[node] + 1
            heapq.heappush(hp, (dikstra[nnode], nnode))

max_cost = 0
ans_arr = []
for i in range(2, N+1):
    if dikstra[i] > max_cost:
        max_cost = dikstra[i]
        ans_arr = [i]
    elif dikstra[i] == max_cost:
        ans_arr.append(i)

print(min(ans_arr), max_cost, len(ans_arr))