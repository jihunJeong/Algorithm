from collections import defaultdict
import heapq

graph = defaultdict(dict)

V, E = map(int, input().split())

start = int(input())
for _ in range(E):
    s, e, c = map(int, input().split())
    
    if e not in graph[s].keys():
        graph[s][e] = c
    else :
        graph[s][e] = min(graph[s][e], c)

answer = [float('inf') for _ in range(V+1)]
answer[start] = 0
visited = [False for _ in range(V+1)]
hp = []
heapq.heappush(hp, (0, start))

while hp:
    c, v = heapq.heappop(hp)
    if visited[v]:
        continue
    visited[v] = True
    for key in graph[v].keys():
        if visited[key] or key == 0:
            continue
        e, c = key, graph[v][key]
        answer[e] = min(answer[e], answer[v] + c)
        heapq.heappush(hp, (answer[e], e))

for i in range(1, V+1):
    if visited[i]:
        print(answer[i])
    else :
        print("INF")