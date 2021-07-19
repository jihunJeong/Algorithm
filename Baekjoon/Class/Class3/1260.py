import sys
from collections import defaultdict, deque

N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())

    graph[n1].append(n2)
    graph[n2].append(n1)

dfs, bfs = [V], deque([V])
visited = [0] * (N+1)
while dfs:
    n = dfs.pop()
    if visited[n] == 1:
        continue

    visited[n] = 1
    print(n, end=" ")

    dfs.extend(sorted(graph[n], reverse=True))
print()

visited = [0] * (N+1)
while bfs:
    n = bfs.popleft()
    if visited[n] == 1:
        continue

    visited[n] = 1
    print(n, end=" ")

    bfs.extend(sorted(graph[n]))